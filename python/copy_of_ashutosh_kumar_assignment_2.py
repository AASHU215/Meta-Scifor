# -*- coding: utf-8 -*-
"""Copy of Ashutosh Kumar Assignment 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mXuQneZg3sinwINfSRCRwIJTnYq9Nvgb
"""

#1
# Number of chocolates with the teacher
chocolates = 327

# Number of kids in the class
kids = 78

# Chocolates left after distribution
chocolates_left = chocolates % kids

# Print the number of chocolates left
print(chocolates_left)

#2
customerName = input("Please enter your name: ")
age = input("Please enter your age: ")
M_no = input("Please enter your mobile number: ")
email = input("Please enter your email address: ")
print("Hi, " + customerName + "!! Thanks for visiting our restaurant and registering for our lucky draw competition on our 25th Anniversary. Once the lucky draw results are \n announced, you will receive a message on your mobile number: " + M_no + ". A detailed description of your gift will be sent to your email address: \n " + email + ". Thank you for being a valued customer, " + customerName + "!! - Domino's")

#4
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)

print(f"{fahrenheit}°F is equal to {celsius}°C")

#3
def calculate_teams(total_students, students_per_team):
    total_teams = total_students // students_per_team
    return total_teams

total_students = 60
students_per_team = 4

total_teams = calculate_teams(total_students, students_per_team)

print(f"Total number of teams that can be created: {total_teams}")