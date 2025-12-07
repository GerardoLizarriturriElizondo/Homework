# ------------------------------------------------------------
# CRUD en Python
# ------------------------------------------------------------
# Name: Gerardo Lizarriturri Elizondo
# Student ID: 2530517
# Group: IM 1-2
# ------------------------------------------------------------
# Problem: In-memory CRUD manager with functions
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------

def create_item(items, item_id, name, price, quantity):
    """Creates a new item if item_id does not already exist."""
    if item_id in items:
        return False
    items[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(items, item_id):
    """Returns the item dictionary if found, otherwise None."""
    return items.get(item_id)


def update_item(items, item_id, new_name, new_price, new_quantity):
    """Updates an existing item. Returns True if successful."""
    if item_id not in items:
        return False
    items[item_id]["name"] = new_name
    items[item_id]["price"] = new_price
    items[item_id]["quantity"] = new_quantity
    return True


def delete_item(items, item_id):
    """Deletes an item by id. Returns True if successful."""
    if item_id not in items:
        return False
    del items[item_id]
    return True


def list_items(items):
    """Prints all items in a readable format."""
    if not items:
        print("No items available.")
        return
    print("Items list:")
    for item_id, data in items.items():
        print(f"- ID: {item_id}, Name: {data['name']}, Price: {data['price']}, Quantity: {data['quantity']}")


def main():
    items = {}

    while True:
        print("\n----- MENU -----")
        print("1) Create item")
        print("2) Read item by ID")
        print("3) Update item by ID")
        print("4) Delete item by ID")
        print("5) List all items")
        print("0) Exit")

        option = input("Choose an option: ").strip()

        if option not in ["0", "1", "2", "3", "4", "5"]:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Exiting program...")
            break

        if option == "1":
            item_id = input("Enter item ID: ").strip()
            if item_id == "":
                print("Error: invalid input")
                continue

            name = input("Enter item name: ").strip()
            if name == "":
                print("Error: invalid input")
                continue

            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                if price < 0 or quantity < 0:
                    print("Error: invalid input")
                    continue
            except:
                print("Error: invalid input")
                continue

            if create_item(items, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: item ID already exists")

        elif option == "2":
            item_id = input("Enter item ID to read: ").strip()
            item = read_item(items, item_id)
            if item:
                print(f"Item found: Name = {item['name']}, Price = {item['price']}, Quantity = {item['quantity']}")
            else:
                print("Item not found")

        elif option == "3":
            item_id = input("Enter item ID to update: ").strip()
            if item_id not in items:
                print("Item not found")
                continue

            new_name = input("Enter new name: ").strip()
            if new_name == "":
                print("Error: invalid input")
                continue

            try:
                new_price = float(input("Enter new price: "))
                new_quantity = int(input("Enter new quantity: "))
                if new_price < 0 or new_quantity < 0:
                    print("Error: invalid input")
                    continue
            except:
                print("Error: invalid input")
                continue

            if update_item(items, item_id, new_name, new_price, new_quantity):
                print("Item updated")
            else:
                print("Item not found")

        elif option == "4":
            item_id = input("Enter item ID to delete: ").strip()
            if delete_item(items, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        elif option == "5":
            list_items(items)


if __name__ == "__main__":
    main()

# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# 1) Python Official Documentation – Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 2) Python Official Documentation – Functions
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#
# 3) Real Python – Dictionaries in Python
#    https://realpython.com/python-dicts/
#
# 4) W3Schools – Python Functions Tutorial
#    https://www.w3schools.com/python/python_functions.asp
#
# 5) Programiz – Python Dictionary (Beginner Guide)
#    https://www.programiz.com/python-programming/dictionary
# ------------------------------------------------------------
# END OF CODE
# ------------------------------------------------------------
