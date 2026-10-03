# Here they are importing the pyjokes module, which is a Python library that provides a collection of programming jokes.

# Using pip-installed external module to get a random joke

import pyjokes

# Built-in module that provides various time-related functions.

import time

""" Here they are using the get_joke() function from the pyjokes module to retrieve a random joke. The joke is then stored in the variable joker."""

joker = pyjokes.get_joke()

print(joker)

time.sleep(2)

print("Thanks for using the joke generator!")
