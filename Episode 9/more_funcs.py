import os
os.system('cls')

def calc(num1, num2, operator):
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2


INTRO = '''
 __  __           _  ____      _      
 |  \/  | ___   __| |/ ___|__ _| | ___ 
 | |\/| |/ _ \ / _` | |   / _` | |/ __|
 | |  | | (_) | (_| | |__| (_| | | (__ 
 |_|  |_|\___/ \__,_|\____\__,_|_|\___|
                                       
'''

DIVIDER = "-*-"

print(INTRO)
print(DIVIDER * 20)

print("Please enter the first number:")
first_number = input()

print("Now, enter the second number:")
second_number = input()

print("Please enter an operator ( + , - , * , / ):")
operator = input()


print(calc(first_number, second_number, operator))
