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

        - Saving / retrieving data to / from file

        - Update the stock of an item
            - show the list items
            - ask the user to choose and id
            - ask the user for thenew stock value
            - find the item with selected id
            - update the stock
            - save changes

        - Print the Total value of the stock (sum (price* stock))

        -Remove an Item from the catalog

        -Register a Sale
            -show the list of items
            -ask the user to choose an id
            -ask the user to provide the quantity
            -update the stock

        -Have a log of events
            -file name for the logs
            -a list for the log entries(list of string)
            -add_log_event function that recieves an string
            -save_log
            -read_log
            -update existing functions to register log entries

        -Display the log of events

        -Display list of categores (unique categories)
"""


from menu import menu, clear, header
# from (the file name) import (what function - this can be multiply functions if needed)

from item import Item
import datetime
import pickle

# global variables
catalog = []
log = []
last_id = 0
data_file = 'warehouse.data'
log_file = 'log.data'

def save_catalog():
    global data_file
    writer = open(data_file, "wb") #create file (overwrite)
    pickle.dump(catalog, writer)
    writer.close()
    print("Data Saved!!")

def save_log():
    global log_file
    writer = open(log_file, "wb")
    pickle.dump(log, writer)
    writer.close()
    print("Log Saved!!")

def read_log():
    try:
        global log_file
        reader = open(log_file, "rb")
        temp_list = pickle.load(reader)

        for entry in temp_list:
            log.append(entry)
        
        how_many = len(log)
        print("Loaded " + str(how_many) + " Log enteries")

    except:
        print("Error loading log entries")


def read_catalog():
    try:
        global data_file
        global last_id
        reader = open(data_file, "rb")
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[-1]
        last_id = last.id

        how_many = len(catalog)
        print("Loaded  " + str(how_many) + " items")
    except:
        print("No data file found, db is empty")



# functions
def register_item():
    global last_id
    header("Register new Item:")
    
    title = input("New Item Title: ")
    category = input("New Item Category: ")
    price = float (input("New Item Price: "))
    stock = int(input("New Item Quantity:"))

    new_item = Item() # <- create instances of a class (objects)
    last_id += 1  # No last_id++
    new_item.id = last_id
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock

    catalog.append(new_item)
    add_log_event("NewItem", "Added Item: "+ str(last_id))
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

def out_ofstock():
    size = len(catalog)
    header("Out of Stock(" + str(size) + "  items) ")

    #print(" " * 60)    
    print("|" + 'ID'.rjust(2) 
        + "|" + 'Title'.ljust(24) 
        + "|" + 'Category'.ljust(15) 
        + "|" + 'Price'.rjust(10) 
        + "|" + 'Stock'.rjust(5) + "|")
    print("-" * 70)

    for item in catalog:
        if(item.stock == 0):
            print("|" + str(item.id).rjust(2) 
            + "|" + item.title.ljust(24) 
            + "|" + item.category.ljust(15) 
            + "|" + str(item.price).rjust(10) 
            + "|" + str(item.stock).rjust(5) + "|" )
    
    print("-" * 70)



def update_stock(opc):
    display_catalog()
    id = int(input("Please select an ID from the list to continue:"))

   
    # find the item with id = id
    found = False
    for item in catalog:
        if(item.id == id):
            found = True

            if(opc == 1):
                stock = int(input("New Stock Value: "))
                item.stock = stock
                print('Stock updated!')
                add_log_event("SetStock", "Updated stock for item:  " + str(item.id))
            else:
                sold = int(input("Number of items for sale:"))
                item.stock -= sold # decrease the stock value
                print('Sale registered!')
                add_log_event("Sale", "Sold  " + str(sold) + "items of item:  " + str(item.id))
            
            
                
    if(not found):
        print("Error: Selected ID does not exist - Try Again!")


def calculate_stock_value():
    total = 0.0
    for item in catalog:
        total += (item.price * item.stock)

    print("Total stock Value: $" + str(total))

def remove_item():
    display_catalog()
    id = int(input("Select the id of the item to remove:  "))
    found = False
    for item in catalog:
        if(item.id == id):
            catalog.remove(item)
            found = True
            add_log_event("Remove", "Removed item:  " + str(item.id))
            break
    if(found):
        print("Item remove from catalog")
    else:
        print("Error: selected id is incorrect - Try again!")
    

# instructions


def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%b/%d/%Y %T")

def add_log_event(event_type, event_description):
    entry = get_current_time() + "|" + event_type.ljust(10) + "|" + event_description
    log.append(entry)
    save_log()

def print_log():
    header("Log of events")
    for entry in log:
        print(entry)

    
read_catalog()
read_log()
input("Press enter to continue")


# Start menu
opc = ''
while(opc != 'x'):
    clear()
    menu()
    print("\n")
    opc = input('Please select an option: ')
         
    if(opc == '1'):
        register_item()
        save_catalog()
    elif (opc == '2'):
        display_catalog()
    elif (opc =='3'):
        out_ofstock()
    elif (opc == '4'):
        update_stock(1) #update stock
        save_catalog()
    elif(opc == '5'):
        calculate_stock_value()
    elif( opc == '6'):
        remove_item()
        save_catalog()
    elif (opc == '7'):
        update_stock(2) #register a sale
        save_catalog()
    elif (opc == '8'):
        print_log()


    input("Press Enter to continue...")

