# -*- coding: utf-8 -*-
"""Assignment 3 Ashutosh.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_WSX1BlbOqwexQpdUzMuR8GewN2hHKwf
"""

#1
def is_palindrome(word):

    word = word.lower()
    reversed_word = word[::-1]
    return word == reversed_word

pet_name = input("Enter the name of the pet: ")

if is_palindrome(pet_name):
    print("true")
else:
    print("false")

#2
Secret_Word = "Codeyoung"
odd_indices = Secret_Word[1:9:2]
even_indices = Secret_Word[0:9:2]
print(odd_indices + even_indices)

number = input()
print(number.isnumeric())
print(len(number) == 10)
print(number[0] in ['9', '8', '7'])