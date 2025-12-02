#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    product = 2
    for itm in a_dictionary.values():
         product *= itm
    return a_dictionary
