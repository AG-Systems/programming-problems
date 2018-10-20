#
# Complete the 'usernamesSystem' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY u as parameter.
#

def usernamesSystem(u):
    # Write your code here
    if u == None:
        return None
    if len(u) == 0:
        return []
    hashtable = {}
    unique_usernames = []
    for username in u:
        if username.isalpha(): 
            if username in hashtable:
                hashtable[username] += 1
                unique_usernames.append( (username + str(hashtable[username])))
            else:
                unique_usernames.append(username)
                hashtable[username] = 0 
    return unique_usernames
        
        
