import random
import sys
import os

# I'm a single line commentary

'''
I'm a multi line commentary
 see :)
'''

class Groceries:
    __groceries = None

    def __init__(self, groceries):
        self.__groceries = groceries

    def to_string(self):
        g_string = ""
        for g in self.__groceries:
            g_string += g + ' '
        return g_string

    def print_string(self):
        for gr in self.__groceries:
            print(gr, end=" ")

    def add_groceries(self, groceries):
        self.__groceries = groceries

    def get_groceries(self):
        return self.__groceries

groceries = Groceries(['Tomatoes', 'Apples', 'Bananas', 'Cherries'])
print(groceries.to_string())
groceries.print_string()
groceries.add_groceries(["Tobacco", "Plants", "Sweets"])
groceries.print_string()
