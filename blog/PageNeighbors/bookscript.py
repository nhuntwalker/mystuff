"""
Created By: Nicholas Hunt-Walker

This script is meant to take data from books 
and help you choose your next book based on 
what you've been reading.

It will have several functions.  I guess that this 
will just be the top-level, and everything else
will flow from here"""

import os

## ===========================================
archive = "master_list.txt"
# This will be where the full list of books read will rest
# In the event that this file does not exist, we will have to make one
files = [f for f in os.listdir('./')]
if archive not in files: # Check if master_list.txt exists
	f = open(archive,'w')
	f.write('\n')
	f.close()

## ===========================================
def add_book():
	yesno = raw_input("Are you sure you want to add a book to the list?\n")

	if yesno.lower() != "yes":
		print "Then you don't need me after all! Bye bye!"

	else:
		verify = "default"
		while verify.lower() != "yes":
			title = raw_input("\nWhat is the book's title?\n").title()
			author = raw_input("\nWho is the book's author?\n").title()
			year = raw_input("\nWhat year was the book published?\n")
			genre = raw_input("\nWhat genre is it?\n").title()
			rating = raw_input("\nOn a scale of 1-10, how would you rate this book?\n")

			print "Just to be sure, your book is...\nTitle: %s\nAuthor: %s\nYear: %s\nGenre: %s\nRating: %s\n" % (title,author,year,genre,rating)
		
			verify = raw_input("Is this correct?\n")

		f = open(archive,'a')
		fmt = "\nTitle: %s\nAuthor: %s\nYear: %s\nGenre: %s\nRating: %s\n"
		f.write(fmt % (title,author,year,genre,rating))
		f.close()

		print "%s added to the master list" % title
		

def show_titles():
	f = open(archive,'r').readlines()
	titles = [line[7:] for line in f if line.startswith('Title:')]
	for t in titles:
		print t[:-1]

def show_authors():
	f = open(archive,'r').readlines()
	authors = [line[8:] for line in f if line.startswith('Author:')]
	for a in authors:
		print a[:-1]

def get_authors_books(auth):
	"""For a given author, retrieve every book they've ever published,
	"""


if __name__ == "__main__":
	# Must add title, author, year, genre, rating
	yesno = raw_input("Are you sure you want to add a book to the list?\n")

	if yesno.lower() != "yes":
		print "Then you don't need me after all! Bye bye!"

	else:
		verify = "default"
		while verify.lower() != "yes":
			title = raw_input("\nWhat is the book's title?\n").title()
			author = raw_input("\nWho is the book's author?\n").title()
			year = raw_input("\nWhat year was the book published?\n")
			genre = raw_input("\nWhat genre is it?\n").title()
			rating = raw_input("\nOn a scale of 1-10, how would you rate this book?\n")

			print "Just to be sure, your book is...\nTitle: %s\nAuthor: %s\nYear: %s\nGenre: %s\nRating: %s\n" % (title,author,year,genre,rating)
		
			verify = raw_input("Is this correct?\n")
		print "Yay, you did it!"

