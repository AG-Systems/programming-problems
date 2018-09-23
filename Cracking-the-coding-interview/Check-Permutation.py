def check_permutation(str1, str2):
  hashtable = {}
  
  substring = None
  mainstring = None
  if len(str1) >= len(str2):
    mainstring = str1
    substring = str2
  else:
    mainstring = str2
    substring = str1
  
  for character in substring:
    if character in hashtable:
      hashtable[character] += 1
    else:
      hashtable[character] = 1
  
  for character in mainstring:
    if character in hashtable:
      if hashtable[character] > 0:
        hashtable[character] -= 1
  
  for key,val in hashtable.items():
    if val > 0:
      return False
  return True


print(check_permutation("", ""))
print(check_permutation("max", "maxy"))
print(check_permutation("maxy", "max"))
print(check_permutation("maxy", "m"))
print(check_permutation("maxy", "mz"))
