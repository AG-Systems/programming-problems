def is_power_of_four(number):
    while number > 0 and number != 1:
        number = number >> 2
        print(number)
    if number == 1:
        return True
    else:
        return False
