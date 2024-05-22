# <--------------------------------------
# Coffee Machine App


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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = 0


# <--------------------------------------
# Starting the machine

user_choice = input("What would you like? (espresso/latte/cappuccino): ")
continue_running = True


def report(amounts, money):
    print(f"Water: {amounts['water']}ml")
    print(f"Milk: {amounts['milk']}ml")
    print(f"Coffee: {amounts['coffee']}g")
    print(f"Money: ${money}")


def collect_money():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coins_inserted: float = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return coins_inserted


def enough_resources(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        print("Sorry there is not enough water.")

    if resources['milk'] < MENU[coffee]['ingredients']['milk']:
        print("Sorry there is not enough milk.")

    if resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")

    if (resources['water'] > MENU[coffee]['ingredients']['water']
            and resources['milk'] > MENU[coffee]['ingredients']['milk']
            and resources['coffee'] > MENU[coffee]['ingredients']['coffee']):
        pass
        # ... calcualte here if there is enough money


if user_choice == 'report':
    report(resources, bank)
elif user_choice == 'off':
    continue_running = False    # something with True/False to terminate the code
elif user_choice == 'latte':
    enough_resources(user_choice)
