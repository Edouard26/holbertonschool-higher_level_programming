#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or not a_dictionary:
        return None
    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key
