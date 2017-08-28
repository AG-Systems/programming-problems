def helper(a_string, tracker, results):
    if tracker >= len(a_string)-1:
        results = ''.join(results)
        return results
    if a_string[tracker] == a_string[tracker+1]:
        if results[tracker] != "*":
            results.insert(tracker+1, "*")
        else:
            results.insert(tracker+2, "*")
    return helper(a_string, tracker + 1, results)

def insert_star_between_pairs(a_string):
    if a_string == None or len(a_string) == 0 or len(a_string) == 1:
        return a_string
    results = list(a_string)
    tracker = 0
    return helper(a_string, tracker, results)
    
    
"""
def insert_star_between_pairs(a_string):
    if a_string is None:
        return None
    elif len(a_string) <= 1:
        return a_string
    elif a_string[0:1] == a_string[1:2]:
        return a_string[0:1] + "*" + insert_star_between_pairs(a_string[1:len(a_string)])

    return a_string[0:1] + insert_star_between_pairs(a_string[1:len(a_string)])

Better solution

"""
