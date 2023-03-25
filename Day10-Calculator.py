from art import logo
import os
def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide
        }

def do_op(numX, input_operation, numY):
    calc = operations[input_operation]
    return calc(numX, numY)



def calculator():
    os.system('clear')
    print(logo)
    num1 = float( input("Enter the first number : "))
    for keys in operations:
        print(keys)

    repeat = 0
    answer = 0
    x = True 
    while x:
        users_operation = input("Pick an operation: ")
        num2 = float( input("Enter the next number : "))
        
        if repeat == 0:
            answer = do_op(num1, users_operation, num2)
            print(f"{num1} {users_operation} {num2} = {answer}")
        else:
            new_answer = do_op(answer, users_operation, num2)
            print(f"{answer} {users_operation} {num2} = {new_answer}")
        repeat += 1

        retry = input(f"Type 'y' to continue calculating with previous {answer} , 'r' to restart and 'e' to exit : " )
        
        if retry == "e":
            x = False
            break
        elif retry == "r":
            calculator()

calculator()

