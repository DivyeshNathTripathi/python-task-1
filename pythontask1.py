# -*- coding: utf-8 -*-
"""pythontask1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kzsV4STaxl59oO5iWYgp_oYusaWCUTfE

Q1: Function to Flatten List and Calculate Product

**Answer:**
This function will:

1. Flatten the given list and extract all numeric values.
2. Include numeric keys and values from dictionaries.
3. Calculate the product of all the numeric values.
"""

from functools import reduce

def flatten_and_product(input_list):
    # Helper function to flatten the list
    def flatten(lst):
        flat_list = []
        for item in lst:
            if isinstance(item, (list, set, tuple)):
                flat_list.extend(flatten(item))
            elif isinstance(item, dict):
                flat_list.extend(flatten(item.keys()))  # Flatten keys
                flat_list.extend(flatten(item.values()))  # Flatten values
            elif isinstance(item, (int, float)) and not isinstance(item, bool):  # Include only numbers
                flat_list.append(item)
        return flat_list

    # Flatten the list
    flat_list = flatten(input_list)

    # Calculate product of all numeric values
    if flat_list:
        product = reduce(lambda x, y: x * y, flat_list)
    else:
        product = 0  # Handle case with no numeric values

    return product

# Test case
list1 = [1, 2, 3, 4, [44, 55, 66, True], False, (34, 56, 78, 89, 34),
         {1, 2, 3, 3, 2, 1}, {1: 34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)},
         [56, 'data science'], 'Machine Learning']

result = flatten_and_product(list1)
print("Product of all numeric values:", result)

"""Q2: Encryption Program
**Answer:**
The logic will:

1. Replace each letter with its reverse counterpart (a→z, b→y, etc.).
2. Replace spaces with $.
3. Keep punctuation unchanged.
"""

def encrypt_message(message):
    # Create a mapping for reverse alphabet
    import string
    alphabets = string.ascii_lowercase
    reverse_alphabets = alphabets[::-1]
    encrypt_dict = {alphabets[i]: reverse_alphabets[i] for i in range(len(alphabets))}

    # Encrypt the message
    encrypted_message = ''
    for char in message.lower():
        if char in encrypt_dict:
            encrypted_message += encrypt_dict[char]
        elif char == ' ':
            encrypted_message += '$'
        else:
            encrypted_message += char  # Keep punctuation unchanged

    return encrypted_message

# Input Sentence
input_sentence = "I want to become a Data Scientist."
encrypted_sentence = encrypt_message(input_sentence)
print("Encrypted Sentence:", encrypted_sentence)