## WARM-UP QUESTION 1
# THE PARAMETER WEEKDAY IS TRUE IF IT IS A WEEKDAY, AND THE PARAMETER VACATION IS TRUE IF WE ARE ON VACATION.
# WE SLEEP IN IF IT IS NOT A WEEKDAY OR WE'RE ON VACATION. 
# RETURN TRUE IF WE SLEEP IN.

def sleep_in(weekday,vacation):
    if not weekday or vacation:
        return True
    else:
        return False

print(sleep_in(False, False)) # True
print(sleep_in(True, False)) # False
print(sleep_in(False, True)) # True
print(sleep_in(True, True)) # True

## WARM-UP QUESTION 2
# WE HAVE TWO MONKEYS, A AND B, AND THE PARAMETERS A_SMILE AND B_SMILE INDICATE IF EACH IS SMILING. 
# WE ARE IN TROUBLE IF THEY ARE BOTH SMILING OR IF NEITHER OF THEM IS SMILING. 
# RETURN TRUE IF WE ARE IN TROUBLE.

def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False

print(monkey_trouble(True, True)) # True
print(monkey_trouble(False, False)) # True
print(monkey_trouble(True, False)) # False
print(monkey_trouble(False, True)) # False