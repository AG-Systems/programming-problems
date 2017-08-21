def unique_chars_in_string(input_string):
    container = {}
    for x in input_string:
        if x in container:
            return False
        else:
            container[x] = 1
    return True
