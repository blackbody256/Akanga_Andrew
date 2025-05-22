import csv

inventory = {}

def load_inventory():
    global inventory
    try:
        #I am using try since the file may not exist first
        #opening it in read mode
        with open('inventory.csv', 'r', newline='') as csvfile:
            #to read each line as a dictionary 
            reader = csv.DictReader(csvfile)
            for row in reader:
                item_name = row['item_name']
                #Building the nested dict
                inventory[item_name] = {
                    #since they are strings i need to type cast
                    'quantity': float(row['quantity']),
                    'price': int(row['price']),
                    'location': row['location']
                }
        print("Inventory loaded successfully")
    except FileNotFoundError:
        print("No existing inventory file found. Starting with empty inventory.")




def save_inventory():
    #since in the function calling this function the global inventory is already accessible then there is no need
    #this is to create the file if it doesn't exist and it's in write mode
    with open('inventory.csv', 'w', newline='') as csvfile:
        #newline is to prevent empty rows in the csv
        #Header titles
        fieldnames = ['item_name', 'quantity', 'price', 'location']
        #DictWriter is used to write dictionaries as rows of a csv
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        #writing the headers on the first row
        writer.writeheader()
        #looping throught all items in the dic
        for item_name, details in inventory.items():
            #writing the dic in one row
            writer.writerow({
                'item_name': item_name,
                'quantity': details['quantity'],
                'price': details['price'],
                'location': details['location']
            })
    print("Inventory saved successfully")


    

def add_item():
    item_name = input("Enter the name of the item\n:")
    item_quantity = float(input("Enter the quantity of the item\n:"))
    item_price = int(input("Enter the price of the item\n:"))
    item_location = input("Enter the location the item is kept\n:")
    
    global inventory
    inventory[item_name]={
        "quantity" : item_quantity,
        "price" :item_price,
        "location" : item_location
    }

    save_inventory()
    print(f"{item_name} is successfully added to the inventory")




def remove_item():
    global inventory
    item_name = input("Enter the item name to remove from the inventory")

    if item_name in inventory:
        inventory.pop(item_name)
        save_inventory()
    else:
        print("The item is not in the inventory\nplease confirm the spelling please")

        

def update_item():
    global inventory
    item_name = input("Enter the name of the item to update: ")
    
    if item_name in inventory:
        print(f"Current details for {item_name}:")
        print(f"Quantity: {inventory[item_name]['quantity']}")
        print(f"Price: {inventory[item_name]['price']}")
        print(f"Location: {inventory[item_name]['location']}")
        
        what_to_update = input("What do you want to update? (quantity/price/location/all): ").lower()
        
        if what_to_update == "quantity":
            new_quantity = float(input("Enter the new quantity: "))
            inventory[item_name]['quantity'] = new_quantity
        elif what_to_update == "price":
            new_price = int(input("Enter the new price: "))
            inventory[item_name]['price'] = new_price
        elif what_to_update == "location":
            new_location = input("Enter the new location: ")
            inventory[item_name]['location'] = new_location
        elif what_to_update == "all":
            new_quantity = float(input("Enter the new quantity: "))
            new_price = int(input("Enter the new price: "))
            new_location = input("Enter the new location: ")
            
            inventory[item_name]['quantity'] = new_quantity
            inventory[item_name]['price'] = new_price
            inventory[item_name]['location'] = new_location
        else:
            print("Invalid option. No changes made.")
            return
        
        save_inventory()
        print(f"{item_name} has been updated successfully.")
    else:
        print(f"Item '{item_name}' not found in inventory.")



def view_inventory():
    global inventory
    
    if not inventory:
        print("Inventory is empty.")
        return
    
    print("\n" + "="*60)
    print(f"{'Item':<15} {'Quantity':<10} {'Price':<10} {'Location':<20}")
    print("-"*60)
    
    for item_name, details in inventory.items():
        print(f"{item_name:<15} {details['quantity']:<10} ${details['price']:<9} {details['location']:<20}")
    
    print("="*60)
    print(f"Total Items: {len(inventory)}")
    print()

def main():
    load_inventory()
    #The Display menu
    while True:
        operation = int(input("Select the desired operations:\n1: View inventory\n2: Add an item\n3: Remove an item\n4: Update an item\n0: Exit\n(NOTE:Enter 1,2,3 or 4)\n:"))
        
        if operation == 1:
            view_inventory()

        elif operation == 2:
            add_item()

        elif operation == 3:
            remove_item()

        elif operation == 4:
            update_item()

        elif operation == 0:
            break

        else:
            print("Wrong input\nTry again\n\n")




if __name__ == "__main__":
    main()