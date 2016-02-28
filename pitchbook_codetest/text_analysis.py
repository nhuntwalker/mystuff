# Searching for Companies with Companies
# Author: Nicholas Hunt-Walker
# Date Started: February 26, 2016

"""
Write an algorithm that takes a company name and
returns a list of names of similar companies. For example if I search "Uber", I
would expect to get something like the following list: ["Lyft", "SideCar",
"Curb", ...] where the most similar companies are at the top of the list.
"""

import pandas as pd 
from nltk.corpus import wordnet, stopwords
from nltk.stem.snowball import SnowballStemmer
import re
import numpy as np
import warnings
warnings.filterwarnings("ignore")

infile = "company_descs_5k.csv"
# columns: name, desc, keywords

def split_keywords(keywords):
    """
    Take in a string of keywords/key phrases delimited by spaces and output a 
    list of keywords/key phrases.
    """
    try:
        keywords = keywords.replace(u'\u201c', '"').replace(u'\u201d', '"')\
            .replace("-", " ")
    except AttributeError:
        return []

    if '"' in keywords:
        # for handling key phrases
        final_set = []
        imperfect_set = map(lambda x: x.split(' "'), keywords.split('" '))
        # imperfect_set will contain a list of lists. Must break down

        for sublist in imperfect_set:
            for item in sublist:
                # clear out remaining quotations
                item = item.replace('"', '').lower() 
                # only add if not already there
                if item not in final_set: 
                    final_set.append(item)

                # we may still want individual components of key phrases
                # and permutations of words in those phrases
                if " " in item: 
                    phrase = item.split(" ")
                    if len(phrase) > 2:
                        for ii in range(len(phrase) - 1):
                            for jj in range(ii + 1, len(phrase)):
                                word = " ".join([phrase[ii], phrase[jj]])
                                if word not in final_set:
                                    final_set.append(word)

                    else:
                        for word in phrase: 
                            # again, only if not already there
                            if word not in final_set:
                                final_set.append(word)

    else:
        final_set = keywords.split(" ")

    return final_set     


def get_synonyms(word):
    """
    For a given word, get a set of first-level synonyms
    """
    syns_sets = wordnet.synsets(word)
    if syns_sets:
        desired = syns_sets[0].lemma_names()
        desired = [the_name.replace("_", " ") for the_name in desired]
        return desired

    else:
        return False


def match_keywords_descriptions(input_company):
    """
    For a given input_company, find any company that matches at least 
    one key word.

    If  input_company doesn't have key words, parse the description and make
    those its key words. Then move forward normally.

    Return a dataframe of matches.
    """

    company = input_company["name"]
    key_list = input_company["key_list"]

    if key_list == []:
        stop = stopwords.words("english")
        too_generic = ["developer", "provider", "operator", "owner", 
                       "manufacturer", "manufactures", "company"]

        key_list = [word for word in input_company["desc"].lower().strip()\
                    .split(" ") if (word not in stop) and \
                    (word not in too_generic)]

    syns_list = []

    for word in key_list:
        syns = get_synonyms(word)

        if syns:
            for s in syns:
                syns_list.append(s)

    keyword_matches = company_data[(company_data.key_list.map(lambda x: \
        [word in x for word in key_list] != [False for word in key_list])) \
        & (company_data.name != company)]

    keyword_matches["match_fraction"] = \
        keyword_matches.key_list.map(lambda x: \
        sum([word in x for word in key_list])/float(len(key_list)))

    keyword_matches["syn_match_frac"] = \
        keyword_matches.key_list.map(lambda x: \
        sum([word in x for word in syns_list])/float(len(syns_list)))

    return keyword_matches


def strip_clean_stem_description(text, stemmer):
    """
    Mostly for the description text for each company.

    Take the text, strip of extra white space, kill non-alphanumeric characters,
    strip any resulting whitespace, return cleaned text
    """
    text = text.strip().replace("-"," ")

    kill_nonalpha = re.compile("[\W]+")
    text = kill_nonalpha.sub(" ", text).replace(" s ", " ").strip()

    reduce_whitespace = re.compile("[\s{2,}]+")
    text = reduce_whitespace.sub(" ", text)
    text = " ".join([stemmer.stem(word) for word in text.split(" ")])

    return text


def calculate_cosine_dist(main_text, new_text):
    """
    Calculate and return the cosine distance between two strings
    """
    wordbag = set(" ".join([main_text, new_text]).split(" "))
    dot_prod = 0
    main_text = main_text.split(" ")
    new_text = new_text.split(" ")

    for word in wordbag:
        if word in main_text and word in new_text:
            count_A = sum(np.array(main_text) == word)
            count_B = sum(np.array(new_text) == word)
            dot_prod += count_A * count_B

    return float(dot_prod) / (len(main_text) * len(new_text))


def search_descriptions(companies, main_company, top_count=5):
    """
    For a set of companies matching the initial company, search through each
    description and rank the companies with descriptions that best match the
    description of the main company. Return an ordered list of matches
    """
    stemmer = SnowballStemmer("english")
    main_company_desc = strip_clean_stem_description(main_company.desc, stemmer)
    distances = {"name":[], "distance":[]}

    ## If description is basically nothing
    if ("undisclosed" in main_company.desc) or ("stealth" in main_company.desc):
        ## No keywords either? No search can be done
        if pd.isnull(main_company.keywords):
            return None

        ## No description but had keywords? I can use that
        else:
            return list(companies.sort_values(by="match_fraction", 
                                         ascending=0)[:top_count]["name"])

    else:
        for ii in range(len(companies)):
            company = companies.iloc[ii]
            company_desc = strip_clean_stem_description(company.desc, stemmer)
            dist = calculate_cosine_dist(main_company_desc, company_desc)
            distances["name"].append(company["name"])
            weight = company["match_fraction"] + 0.5 * company["syn_match_frac"]
            distances["distance"].append(dist * weight)

        distances = pd.DataFrame(distances).sort_values(by="distance", 
                                                        ascending=0)
        if len(distances) > top_count:
            return list(distances[:top_count]["name"])

        else:
            return list(distances["name"])


def the_search_function(company_name, top_count=5):
    """
    This function takes in a single company name as a string and returns a list 
    of companies with similar keywords and descriptions. The number of companies
    returned is controlled by the top_count parameter.
    """
    main_company = company_data[company_data.name == company_name].iloc[0]

    if top_count == 1:
        search_str = "\nSearching for the closest company to %s...\n" \
                % (main_company["name"])

    else:
        search_str = "\nSearching for top %g closest companies to %s...\n" \
                % (top_count, main_company["name"])

    print search_str

    matching_companies = match_keywords_descriptions(main_company)    
    search_results = search_descriptions(matching_companies, main_company, 
                                         top_count)

    if search_results:
        print "Results:"

        for result in search_results:
            print "\t" + result

    else:
        print "No results available"

company_data = pd.read_csv(infile, encoding="utf_8")
company_data["key_list"] = company_data.keywords.map(lambda x: \
    split_keywords(x))


if __name__ == "__main__":
    initial_str = "\nWhat company would you like to search for?"
    initial_str += " (Leave empty to test)\n"
    company_name = raw_input(initial_str).strip().lower()

    nulls = ["", "none", "test"]
    if company_name in nulls:
        print "\nAlright, let's do a random search to test out the code"
        indx = np.random.randint(len(company_data))
        the_search_function(company_data.name.iloc[indx])

    elif company_name not in list(company_data.name.map(lambda x: x.lower())):
        print "\nSorry, that name isn't in our database."
        print "Try the searching again with a different name!\n"

    else:
        limit_str = "\nWhat's the maximum number of results would you like?"
        limit_str += " (1 - 5000; Default = 5)\n"
        search_count = raw_input(limit_str)

        try:
            search_count = eval(search_count)

            if search_count <= 0:
                search_count = 1
                counts_str = "\nYou seem to have wanted less than one result."
                counts_str += " We'll just return one for you."
                print counts_str

            elif search_count > len(company_data):
                search_count = len(company_data)
                counts_str = "\nWhoa, you wanted more results, than we have"
                counts_str += " companies! Let's stick to listing at most every"
                counts_str += " company."
                print counts_str

        except NameError:
            search_count = 5
            counts_str = "\nThat wasn't a number. That's alright though, we'll"
            counts_str += " just go with the default of 5 results."
            print counts_str

        the_search_function(company_data[company_data.name.map(lambda x: \
            x.lower()) == company_name].name.iloc[0], search_count)
