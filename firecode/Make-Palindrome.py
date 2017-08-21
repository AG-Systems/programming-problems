def make_palindrome(input):
    s = input
    if s == s[::-1]:
        return s
    else:
        if len(s) % 2 == 0:
            t = s[0:3]
        else:
            t = s[0:2]
        s += t[::-1]
        return s
        
        
        
     # I do not like this solution at all
     # I want to find a better one maybe using dp
