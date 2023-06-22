MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


coin_values = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickels" : 0.05,
    "pennies" : 0.01
}

current_resource_values = {
    "water" : 500,
    "milk" : 400,
    "coffee" : 300,
    "money" : 0
}


def check_resources(user_choice):
    ingredients = MENU[user_choice]["ingredients"]
    insufficient_ingredients = []
    
    if current_resource_values["water"] < ingredients.get("water", 0):
        insufficient_ingredients.append("water")

    if current_resource_values["coffee"] < ingredients.get("coffee", 0):
        insufficient_ingredients.append("coffee")

    if current_resource_values.get("milk", 0) < ingredients.get("milk", 0):
        insufficient_ingredients.append("milk")

    if len(insufficient_ingredients) > 0:
        return "insufficient", insufficient_ingredients
    else:
        return "sufficient", None


def deduct_resources(user_choice):
    for resource, amount in MENU[user_choice]["ingredients"].items():
        current_resource_values[resource] -= amount

def increment_resources(user_choice):
    for resource, amount in MENU[user_choice]["ingredients"].items():
        current_resource_values[resource] += amount 


def add_money(coffee):
    current_resource_values["money"] += MENU[coffee]["cost"]


def insert_and_calculate_total_coins():

    quarters = float(input("How many quarters? : "))
    dimes = float(input("How many dimes? : "))
    nickels = float(input("How many nickels? : "))
    pennies = float(input("How many pennies? : "))

    total_value = ((quarters * coin_values["quarters"]) + 
                   (dimes * coin_values["dimes"]) + 
                   (nickels * coin_values["nickels"]) + 
                   (pennies * coin_values["pennies"] )) 
    
    return total_value 


def calculate_change(coffee, coins_inserted):
     
    price = MENU[coffee]["cost"]
    change = coins_inserted - price
    return change


def display():

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        return 
    elif user_choice == "report":
        for resource in current_resource_values:
            if resource == "water" or resource == "milk":
                print(f"{resource} : {current_resource_values[resource]}ml ")
            elif resource == "coffee":
                print(f"Coffee : {current_resource_values[resource]}g ")
            elif resource == "money":
                print(f"Money: ${current_resource_values[resource]} ") 
        display()
    else:

        state_of_resources, insufficient_ingredients = check_resources(user_choice)
        if state_of_resources == "insufficient":
            print(f"Sorry, there is not enough {', '.join(insufficient_ingredients)}.")
            return

        else:           

            deduct_resources(user_choice)
            print(f"That would be ${MENU[user_choice]['cost']}. ")
            coins_inserted = insert_and_calculate_total_coins()
            if coins_inserted > MENU[user_choice]["cost"]:
                add_money(user_choice)
                print(f"Here is ${calculate_change(user_choice, coins_inserted)} in change. Enjoy!")
                display()

            elif coins_inserted == MENU[user_choice]["cost"]:
                add_money(user_choice)
                print("There's no change. Enjoy!")    
                display()
            
            else:
                print("Not enough money. Money refunded.")
                increment_resources(user_choice)
                display()

display()