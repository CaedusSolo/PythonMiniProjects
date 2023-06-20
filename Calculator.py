logo = """ 

 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""
text = """  

                888                888        888                   
                888                888        888                   
                888                888        888                   
 .d8888b 8888b. 888 .d8888b888  888888 8888b. 888888 .d88b. 888d888 
d88P"       "88b888d88P"   888  888888    "88b888   d88""88b888P"   
888     .d888888888888     888  888888.d888888888   888  888888     
Y88b.   888  888888Y88b.   Y88b 888888888  888Y88b. Y88..88P888     
 "Y8888P"Y888888888 "Y8888P "Y88888888"Y888888 "Y888 "Y88P" 888 


"""

print(text)
print(logo)
print("Welcome to C's Calculator Program!")


def add(num1, num2):
    result = num1 + num2
    return result 


def subtract(num1, num2):
    result = num1 - num2 
    return result


def multiply(num1, num2):
    result = num1 * num2
    return result  


def divide(num1, num2):
    result = num1 / num2 
    return result   


def first_number():
    number = float(input("What's the first number?: "))
    return number


def second_number():
    number = float(input("What's the next number?: "))
    return number


def operation():
    operation = input("Choose an operation ( + - x / ): ")
    return operation


def evaluate(firstNum,secondNum,operation):
    if operation == "+":
        result = add(firstNum,secondNum)
        print(f"{firstNum} {operation} {secondNum} = {round(result,2)}")
        return round(result,2)

    elif operation == "-":
        result = subtract(firstNum,secondNum)
        print(f"{firstNum} {operation} {secondNum} = {round(result,2)}")
        return round(result,2)

    elif operation == "x":
        result = multiply(firstNum,secondNum)
        print(f"{firstNum} {operation} {secondNum} = {round(result,2)}")
        return round(result,2)

    elif operation == "/":
        result = divide(firstNum,secondNum)
        print(f"{firstNum} {operation} {secondNum} = {round(result,2)}")
        return round(result,2)


def resume(firstNum):
    operand = operation() 
    secondNum = second_number()
    result = evaluate(firstNum,secondNum,operand)
    
    return result


def go(result):
    wants_to_continue = True
    while wants_to_continue:

        replay = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, type any other character to exit: ").lower()
        if replay == "y":
            result = resume(result)

        elif replay == "n":
            display()

        else:
            print("Thank you for using this calculator. Have a nice day!")
            wants_to_continue = False
            exit

def display():
    first_num = first_number()
    operand = operation()
    second_num = second_number()

    result = evaluate(first_num,second_num,operand)
    go(result)

    return result
            

display()