#!/usr/bin/env python

user_input = raw_input("Enter number:")

def fizz_buzz(user_input):
  length = int(user_input) + 1
  for i in range(1, length):
    if i % 3 == 0 and i % 5 == 0:
      print("%i FizzBuzz") % (i)
    elif i % 5 == 0:
      print("%i Buzz") % (i)
    elif i % 3 == 0:
      print("%i Fizz") % (i)

fizz_buzz(user_input)
