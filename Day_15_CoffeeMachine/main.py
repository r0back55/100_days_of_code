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


# <----------------------------------------------------------------------------
# Functions section
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


def resources_check(coffee):
    if coffee != 'espresso':
        if resources['water'] < MENU[coffee]['ingredients']['water']:
            print("Sorry there is not enough water.")
            return False

        if resources['milk'] < MENU[coffee]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            return False

        if resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            return False

        # if (resources['water'] > MENU[coffee]['ingredients']['water']
        #         and resources['milk'] > MENU[coffee]['ingredients']['milk']
        #         and resources['coffee'] > MENU[coffee]['ingredients']['coffee']):
        #     print("Ingredients ok")

        # If all checks pass, return True
        return True

    elif coffee == 'espresso':
        if resources['water'] < MENU[coffee]['ingredients']['water']:
            print("Sorry there is not enough water.")
            return False

        if resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            return False

        # if (resources['water'] > MENU[coffee]['ingredients']['water']
        #         and resources['coffee'] > MENU[coffee]['ingredients']['coffee']):
        #     print("Ingredients ok")

        # If all checks pass, return True
        return True


def money_check(coffee, inserted):
    if inserted >= MENU[coffee]['cost']:
        change = round(inserted - MENU[coffee]['cost'], 2)
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry that's not enough. Money refunded.")
        return False


def resources_update(coffee):
    if coffee != 'espresso':
        resources['water'] -= MENU[coffee]['ingredients']['water']
        resources['milk'] -= MENU[coffee]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[coffee]['ingredients']['water']
        resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    return resources


# <----------------------------------------------------------------------------
# Starting the machine
continue_running = True
bank = 0

# <----------------------------------------------------------------------------
# Main program
while continue_running:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'report':
        report(resources, bank)
    elif user_choice == 'off':
        continue_running = False
    else:
        if resources_check(user_choice):
            print(resources_check(user_choice))
            inserted_coins = collect_money()
            if money_check(user_choice, inserted_coins):
                resources_update(user_choice)
                print(f"Here is your {user_choice} ☕. Enjoy!")
                bank += MENU[user_choice]['cost']
        else:
            continue_running = False
        report(resources, bank)
