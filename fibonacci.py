#!/usr/bin/env python

# for positive only
def fibonacci(n):
  if n < 0:
      print "Please enter value greater than zero"
      return
  if n == 0:
      return 0

  prelast, last = 0, 1
  i = 0

  while(i < n):
      last, prelast = prelast, last + prelast
      print last 
      i += 1


fibonacci(10)
