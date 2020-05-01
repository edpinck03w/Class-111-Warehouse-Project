import os


def menu():
    print("\n\n")
    print("-" * 30)
    print("    Warehouse Control")
    print("-" * 30)

    print('[1] Register Items')
    print('[2] Display Catalog')
    print('[3] Out of Stock Items')
    print('[4] Update Item Stock Quantity')
    print('[5] Calculate Stock Value')
    print('[6] Remove an Item Completely')

    print(" [x] Exit")


def header(title):
    clear()
    print("-" * 70)
    print(" " + title)
    print("-" * 70)



def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')