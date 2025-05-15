#!/usr/bin/env python

# Importing
from hashlib import new
import sys 	# system functions and parameters
from datetime import datetime
from datetime import datetime as dt 	# importing with an alias

print("Importing ios important:")

print(datetime.now())
print(dt.now())

def new_line():
    print('\n')

new_line()

# Advanced Strings
print("Advance strings:")
my_name = "James"
print(my_name[0])	# first initial
print(my_name[-1])	# last object

sentence = "This is a sentence."
print(sentence[:4])  # first word
print(sentence[-9:-1])  # last word

print(sentence.split())  # split sentence by delimiter (space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

quoteception = "I said, 'give me all the money'"
print(quoteception)

quoteception = "I said, \"give me all the money\""
print(quoteception)

print("A" in "Apple")
letter = "A"
word = "Apple"
print(letter.lower() in word.lower())  # Improved -- case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower() and not (letter.lower() in word_two.lower())))

too_much_space = "       hello       "
print(too_much_space.strip())

full_name = "ames Adams"
print(full_name.replace("ames", "James"))
print(full_name.find("Adams"))

# Place Holder -- {}.format()
movie = "The Hangover"
print("My favorite movie is {}.".format(movie))

def favorite_book(title, author):
    fav = "my favorite book is \"{}\", which is written by {}.".format(
        title, author)
    return fav

print(favorite_book("The Great Gatsby", "F. Scott Fitzgerald"))

new_line()

# Dictionaries
print("Dictionaries are keys and values:")
drinks = {"White Russian": 7, "Old Fashion": 10, "Lemon Drop": 8,
          "Buttery Nipple": 6}  # drink is key, price is value
print(drinks)
print(drinks['Lemon Drop'])

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": [
    "Gene", "Louse", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)
employees['Legal'] = ["Mr Frond"]  # add new key: value pair
print(employees)

employees.update({"Sales": ["Andi", "Ollie"]})
print(employees)

# List and dictionaries
movies = ["Wheh Harry Met Sally", "The Hangover",
          "The Perks of Being a Wallflower", " The Exorcist"]
person = ["Jake", "James", "Leah", "Jeff"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}
print(movie_dictionary)
