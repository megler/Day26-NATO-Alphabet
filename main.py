# natoAlphabet.py
#
# Python Bootcamp Day 26 - NATO Alphabet Converter
# Usage:
#   At the input, enter your name. You will receive an output of
#   how your name is spelled phonetically using the NATO alphabet.
#
# Marceia Egler November 23, 2021

import pandas as pd


# Keyword Method with iterrows()
df = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:

nato = {row.letter: row.code for (index, row) in df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


while True:
    name = input("What's your name? ").upper()
    try:
        output = [nato[letter] for letter in name]
    except KeyError:
        print("Sorry, only alphabet characters, please.")
    else:
        print(output)
        break


# How I orignally did this
# name_chars = [char for char in name]
# output = [nato.get(char) for char in name_chars if char in nato]
