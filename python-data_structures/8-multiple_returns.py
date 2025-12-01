#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        result = (length, None)
        return result
    first = sentence[0]
    result = (length, first)
    return result
