""" 
    Program: Warehouse management system
    Functionality:
        -Repeated menu
        - Register items to the catalog
        id (auto genterated)
        title
        category
        price
        stock
        - Display Catalog
        - Display items with no stock (out of stock)
"""


from menu import menu, clear, header
# from (the file name) import (what function - this can be multiply functions if needed)

from item import Item
# global variables
catalog = []





# functions
def register_item():
    header("Register new Item:")
    
    title = input("New Item Title: ")
    category = input("New Item Category: ")
    price = float (input("New Item Price: "))
    stock = int(input("New Item Quantity:"))

    new_item = Item() # <- create instances of a class (objects)
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock

    catalog.append(new_item)
    print("Item created!")


def display_catalog():
    size = len(catalog)
    header("Current Catalog(" + str(size) + "  items) ")

    #print(" " * 60)    
    print("|" + 'ID'.rjust(2) 
        + "|" + 'Title'.ljust(24) 
        + "|" + 'Category'.ljust(15) 
        + "|" + 'Price'.rjust(10) 
        + "|" + 'Stock'.rjust(5) + "|")
    print("-" * 70)

    for item in catalog:
        print("|" + str(item.id).rjust(2) 
        + "|" + item.title.ljust(24) 
        + "|" + item.category.ljust(15) 
        + "|" + str(item.price).rjust(10) 
        + "|" + str(item.stock).rjust(5) + "|" )
    
    print("-" * 70)
# instructions


# Start menu
opc = ''
while(opc != 'x'):
    clear()
    menu()
    print("\n")
    opc = input('Please select an option: ')
         
    if(opc == '1'):
        register_item()
    elif (opc == '2'):
        display_catalog()


    input("Press Enter to continue...")

