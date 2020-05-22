#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "DJJD2150, Janell Huyck, Tiffany McLean"

import sys


def create_word_dict(filename):
    """Returns a word/count dict for the given file."""
    with open(filename, "r") as f:
        word_dict = {}
        line = f.read().split()
        for word in line:
            word = word.lower()
            find_word = word_dict.get(word, 0)
            if find_word == 0:
                word_dict[word] = 1
            elif find_word != 0:
                word_dict[word] += 1
    return word_dict


def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    # Take "word_dict" as it is from the "create_word_dict" function
    # and assign them to a variable
    count_dict = create_word_dict(filename)
    # Sort "count_dict" alphabetically
    count_list = sorted(count_dict.keys())
    # Format each key/ value pair in "count_dict" as "<word> : <count>"
    # Print each key/ value pair in the alphabetically sorted order
    for word in count_list:
        counted_words = print("{}:{}".format(word, count_dict[word]))
    return counted_words


def print_top(filename):
    """Prints the top count listing for the given file."""
    # Take "word_dict" as it is from the "create_word_dict" function
    # and assign them to a variable
    topcount_dict = create_word_dict(filename)
    # Sort "topcount_dict" by value from greatest to least in quantity
    topcount_list = sorted(topcount_dict.items(), key=lambda t: t[-1], reverse=True)
    # Reduce "topcount_list" to the top 20 greatest values
    topcount_list = topcount_list[:20]
    # Format each key/ value tuple in "count_dict" as "<word> : <count>"
    for word in topcount_list:
        topcounted_words = print(word[0] + " : " + str(word[1]))
    return topcounted_words

# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
