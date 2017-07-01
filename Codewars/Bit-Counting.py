def countBits(n):
    return len([i for i in str(bin(n)) if i == '1'])
