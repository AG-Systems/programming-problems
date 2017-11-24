def convert(hexval):
    import codecs
    return codecs.encode(codecs.decode(hexval, 'hex'), 'base64').decode()

print(convert("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
    
