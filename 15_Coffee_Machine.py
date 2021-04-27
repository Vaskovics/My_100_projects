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


def check_resources(drink):
    water = MENU[drink]['ingredients']['water']
    milk = MENU.get(drink, {}).get("ingredients").get("milk", 0)
    coffee = MENU[drink]['ingredients']['coffee']
    if resources['water'] - water >= 0:
        if resources['milk'] - milk >= 0:
            if resources['coffee'] - coffee >= 0:
                return True
            else:
                print(print("There is not enough coffee."))
                return False
        else:
            print("There is not enough milk.")
            return False
    else:
        print("There is not enough water.")
        return False


def reducing_resources(drink):
    water = MENU[drink]['ingredients']['water']
    milk = MENU.get(drink, {}).get("ingredients").get("milk", 0)
    coffee = MENU[drink]['ingredients']['coffee']
    if resources['water'] - water > 0:
        resources['water'] -= water
    if resources['milk'] - milk > 0:
        resources['milk'] -= milk
    if resources['coffee'] - coffee:
        resources['coffee'] -= coffee


def check_price(drink):
    if drink == "espresso":
        cost = espresso
    elif drink == "latte":
        cost = latte
    elif drink == "cappuccino":
        cost = cappuccino
    return cost


def check_enough_money(price, value):
    if price > value:
        return False
    elif price < value:
        return True


espresso = MENU['espresso']["cost"]
latte = MENU['latte']["cost"]
cappuccino = MENU['cappuccino']["cost"]

money = 0
is_available = None
while True:
    user_order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_order == 'off':
        break
    elif user_order == "report":
        for item, contain in resources.items():
            print(f"{item} : {contain}")
        print(f'Money: ${money:.2f}')
    else:
        if check_resources(user_order):
            price = check_price(user_order)
            reducing_resources(user_order)
            print(f"The price for {user_order} is ${price}")
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            value = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
            if check_enough_money(price, value):
                change = value - price
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {user_order}, Enjoy!")
                money += price
            else:
                print("There is not enough monet")
        else:
            print("Please choice something else.")
    change = 0

























