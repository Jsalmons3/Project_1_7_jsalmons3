"""
Shop and Inventory
Jeffrey Salmons
A fantasy shop and inventory system for a game that uses a bunch of basic programming concepts.
6/20/2026
"""

player_name = input("What is your name, adventurer? ")
print(f"Welcome to the Dragon's Hoard shop, {player_name}!")

gold = 100

player_inventory = ["Squire Sword", "Cloth Armour", "Wooden Shield"]

shop = {
    "Health Potion": 10,
    "Master Sword": 200,
    "Knight Armour": 75,
    "Square Shield": 25,
    "Ring of Strength": 50
}

starter_items = ("Squire Sword", "Cloth Armour", "Wooden Shield")

while True:

    print("Menu")
    print("----------")
    print("1. View Inventory")
    print("2. View Shop")
    print("3. Buy Item")
    print("4. Sell Item")
    print("5. View Gold")
    print("6. Leave")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your Inventory:")
        if len(player_inventory) == 0:
            print("Inventory is empty.")
        
        else:
            for item in player_inventory:
                print("-", item)

        input("Press Enter to continue...")