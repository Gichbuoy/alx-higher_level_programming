#!/usr/bin/python3
"""program that defines a text-indentation function."""


def text_indentation(text):
    """define function that indents text"""

    # Check that the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Skip over any leading whitespace
    y = 0
    while y < len(text) and text[y] == ' ':
        y += 1

    # Loop over the characters in the input string
    while y < len(text):
        # Print the current character without a newline
        print(text[y], end="")

        # Check if we need to add newlines
        if text[y] == "\n" or text[y] in ".?:":
            # If the character is one of '.', '?', or ':', add two newlines
            if text[y] in ".?:":
                print("\n")
            print("\n")

            # Skip over any leading whitespace in the next line
            y += 1
            while y < len(text) and text[y] == ' ':
                y += 1

            # Continue to the next character
            continue

        # Increment the character index
        y += 1
