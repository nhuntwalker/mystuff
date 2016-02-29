# Download all american TV series from wikipedia
# parse file to get show names, years, and categories
# -- only take shows that have at least a name and year
# -- if two shows have same name, second instance has year appended as a modified name
# -- save original name, my modified name, year, category
# For each show get IMDB page

import os
import re
from bs4 import BeautifulSoup
import urllib
# get the wikipedia page for list of american TV series
# os.system('curl https://en.wikipedia.org/wiki/List_of_American_television_series > tv_series_list.html')

all_tv = "tv_series_list.html"

def parse_wiki_tvlist(the_page):
    """
    Crawl through the TV list from Wikipedia and produce a JSON object 
    containing...
    Title, Year, Category, Alt Title, Wikipedia URL (for getting IMDB url)
    """
    # shows = {"titles":[], "years":[], "categories":[], 
    #         "alt_titles":[], "urls":[]}
    shows = []
    html_doc = open(the_page).read()
    soup = BeautifulSoup(html_doc, "html.parser")
    show_sections = soup.find(id="mw-content-text").findAll("ul")[1:]
    link_base = "https://en.wikipedia.org"

    for section in show_sections[:-10]:
        list_items = section.findAll("li")

        for item in list_items:
            show_item = {}

            title_yr_cat = item.text.replace(u"\u2013", "-")\
                            .replace(u"\u2014", "-").replace(" ","")

            if item.a == None:
                title = item.i.text
                link = ""

            else:            
                title = item.a.text
                link = link_base + item.a.attrs["href"]
                if "redlink=1" not in link:
                    kill_non_alphanum = re.compile("[\(\)\/:]+")
                    show_item["page_file"] = "wiki_pages/%s.html" % kill_non_alphanum.sub("", item.a.attrs["href"].split("/wiki/")[-1])

            # shows["titles"].append(title)
            # shows["urls"].append(link)
            show_item["title"] = title
            show_item["url"] = link

            cut_on_yr = re.compile("[\(\)]+")
            show_arr = cut_on_yr.split(title_yr_cat)

            if len(show_arr) > 1:
                numeric_only = re.compile("\D+")
                yr = show_arr[1].split("-")[0].split(",")[-1]
                yr = numeric_only.sub("", yr)
                if len(yr) < 4:
                    yr = ""
                else:
                    yr = yr[-4:]

                category = show_arr[-1]

            else:
                yr = ""
                category = ""

            # shows["years"].append(yr)
            # shows["categories"].append(category)
            show_item["year"] = yr
            show_item["category"] = category

            alt_title = title + " " + str(yr)

            # shows["alt_titles"].append(alt_title)
            show_item["alt_title"] = alt_title.strip()
            shows.append(show_item)

    return shows

def download_show_wiki_page(show):
    if "page_file" in show.keys():
        sock = urllib.urlopen(show['url'])
        htmlSource = sock.read()
        outfile = open(show["page_file"], "w")
        outfile.write(htmlSource)
        outfile.close()
        # os.system('curl %s > %s' % (show['url'], show['page_file']))


def add_imdb_link(show):
    html_doc = open(show["page_file"]).read()
    soup = BeautifulSoup(html_doc, "html.parser")
    links = soup.findAll("a")
    target = []
    for ii in range(len(links)):
        if links[ii].has_attr("title") and links[ii].attrs["title"] == "Internet Movie Database":
            target.append(links[ii])

    if target != []:
        show["imdb_link"] = target[0].parent.findAll("a")[0].attrs["href"]

    return show

shows = parse_wiki_tvlist(all_tv)
for show in shows:
    download_show_wiki_page(show)
    if "page_file" in show.keys():
        show = add_imdb_link(show)

# Next step: explore IMDB
