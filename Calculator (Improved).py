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

def add(n1,n2):
    return n1 + n2 

def subtract(n1,n2):
    return n1 - n2  

def multiply(n1,n2):
    return n1 * n2  

def divide(n1,n2):
    return n1 / n2  

operations = {
    "+" : add,
    "-" : subtract,
    "x" : multiply,
    "/" : divide
}

def calculator():
    
    print(logo)
    print(text)
    num1 = float(input("What's the first number? : "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the above: ")
        num2 = float(input("What's the next number? : "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == "y":
            num1 = answer 
        elif input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == "n":
            should_continue = False
            calculator() 
        else:
            break

calculator()