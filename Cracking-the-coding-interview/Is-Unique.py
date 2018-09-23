def is_unique(string):
  hashtable = {}
  for character in string:
    if character in hashtable:
      return False
    else:
      hashtable[character] = True
  
  return True

print(is_unique("asdfasdf"))
print(is_unique(""))
print(is_unique("cx"))
