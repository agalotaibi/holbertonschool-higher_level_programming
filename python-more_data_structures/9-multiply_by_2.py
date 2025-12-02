#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    update_dir = a_dictionary.copy()
    product = 2
    for key in update_dir:
        update_dir[key] = update_dir[key] * 2
    return update_dir
