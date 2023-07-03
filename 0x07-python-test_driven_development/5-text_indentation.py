#!/usr/bin/python3
"""Module: Text indentation"""
def text_indentation(text):
    """  prints a text 
    with 2 new lines after 
    each of these characters: ., ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    
    processed_text = text.replace(".", ".\n\n")
    processed_text = processed_text.replace("?", "?\n\n")
    processed_text = processed_text.replace(":", ":\n\n")
    processed_text = processed_text.replace(" \n", "\n")
    processed_text = processed_text.replace("\n ", "\n")


    processed_text = processed_text.strip(" ")


    print(processed_text, end="")
