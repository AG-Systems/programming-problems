# given an integer n, return a string of balanced parentheses of length n

"""
n = 2, return "()"
n = 4, return "()()", "(())"
n = 6 return "()()()", "((()))", "(()())", "(())()"
"""


def f(n):
  if n % 2 != 0:
    return None
  
  import random

  balanced = ""
  many_opens = 0 
  many_closing = 0
  counter = 0

  while counter < n:
    if many_opens < n / 2:
      bracket = random.choice(["(", ")"])
    else:
      bracket = ")"
    if counter == 0:
      balanced += "("
      many_opens += 1
    elif counter == n-1:
      balanced += ")"
      many_closing += 1
    elif bracket == "(" and many_opens < n / 2:
      balanced += "("
      many_opens += 1
    elif bracket == ")" and many_closing < many_opens:
      balanced += ")"
      many_closing += 1
    else:
      balanced += "()"
      counter += 1
    counter += 1
  return balanced
  
print(f(8))
