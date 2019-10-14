## There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the 
## poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new, 
## random IDs based on her Completely Foolproof Scheme. She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113".
## Help the Commander assign these IDs by writing a function answer(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

""" Languages
=========
Inputs:
    (int) n = 0
Output:
    (string) "23571"
Inputs:
    (int) n = 3
Output:
    (string) "71113" """


def generate_prime(max_range):
    seed = list(range(2, max_range))
    while not len(seed) == 0:
        top = seed.pop(0)
        yield top
        seed = [i for i in seed if not i % top == 0]

def answer(n):
    prime = list(generate_prime(21000))

    primes=  ''.join(map(str, prime))
    print primes

    for idx, val in enumerate(primes):
        print idx,val
        if idx == n:
            final=primes[idx:idx+5]
            return ''.join(map(str, final))


    return -1

#n = 10000
#print(answer(n))
