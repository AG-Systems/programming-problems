def is_happy_number(number):
    duplicates = []
    
    while number > 0:
        digits = str(number)
        temp = 0
        for digit in range(len(digits)):
            temp += (int(digits[digit]) * int(digits[digit]))
        
        if temp not in duplicates:
            duplicates.append(temp)
        elif temp == 1:
            return True
        else:
            return False
        
        number = temp
