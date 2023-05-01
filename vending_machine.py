"""A simple command line simulation of a vending machine"""

class VendingMachine:
    def __init__(self):
        # initializing self.items and adding sample items
        self.items = {
            "snacks": [
                {"name": "chips", "price": 1.50, "weight": 50, "quantity": 10},
                {"name": "candy", "price": 0.75, "weight": 25, "quantity": 10},
                {"name": "granola bar", "price": 1.00, "weight": 35, "quantity": 10},
            ],
            "beverages": [
                {"name": "soda", "price": 2.00, "volume": 350, "quantity": 10},
                {"name": "water", "price": 1.00, "volume": 500, "quantity": 10},
                {"name": "juice", "price": 1.50, "volume": 250, "quantity": 10},
            ],
        }

    def display_items(self):
        """display all available items"""
        print("\n\tAvailable items:")
        # iterating over all categories and items in self.items and printing each item
        for category, items in self.items.items():
            print(f"\n\t{category.capitalize()}:")
            # putting the unit grams (g) after every weight and the unit milliliters (ml) after every volume
            attribute_suffix = "g" if category == "snacks" else "ml"
            for item in items:
                print(
                    f"\t{item['name']} - ${item['price']} - {item.get('weight', item.get('volume'))}{attribute_suffix} - Quantity: {item['quantity']}"
                )

    def add_item(self, category, name, price, attribute, attribute_value):
        """add an item to the vending machine"""
        # append the given item to the corresponding category list with a default quantity of 10
        self.items[category].append({"name": name,"price": price, f"{attribute}": attribute_value, "quantity": 10})
        print(f"\n\t{name.capitalize()} added to {category}!")


    def remove_item(self, category, name):
        """remove an item from the vending machine"""
        # searching the category's list for the given item name and remove it if found
        for i, item in enumerate(self.items[category]):
            if item["name"] == name:
                del self.items[category][i]
                print(f"\n\t{name.capitalize()} removed from {category}!")
                break
        else:
            print(f"\n\t{name.capitalize()} not found in {category}.")

    def restock_item(self, category, name):
        """restock a certain item in the vending machine"""
        # seaching the category's list for the given item name and if found, setting it's quantity to 10
        for item in self.items[category]:
            if item["name"] == name:
                item["quantity"] = 10
                print(f"\n\t{name.capitalize()} restocked!")
                break
        else:
            print(f"{name.capitalize()} not found in {category}.")

    def purchase_item(self, category, name):
        """purchase an item from the vending machine"""
        # searching the category's list for the given item name and if found, decreasing its quantity by 1
        for item in self.items[category]:
            if item["name"] == name:
                if item["quantity"] > 0:
                    item["quantity"] -= 1
                    print(f"\n\t{name.capitalize()} purchased!")
                    break
                else:
                    print(f"\n\t{name.capitalize()} is out of stock.")
                    break
        else:
            print(f"{name.capitalize()} not found in {category}.")
        
    def is_full(self):
        """check if the vending machine is full (returns bool)"""
        total_items = len(self.items["snacks"]) + len(self.items["beverages"])
        if total_items < 10:
            return False
        else:
            return True
        
    def is_empty(self):
        """check if the vending machine is empty (returns bool)"""
        total_items = len(self.items["snacks"]) + len(self.items["beverages"])
        if total_items > 0:
            return False
        else:
            return True

def get_category():
    """prompt the user for a category and check if it is valid"""
    category = input("Enter category (snacks/beverages): ").lower() 
    while category != "snacks" and category != "beverages":
        print("\n\tInvalid category. Please try again.")
        category = input("\nEnter category (snacks/beverages): ").lower()
    return category

if __name__ == "__main__":
    vending_machine = VendingMachine()

    print("\n\t##########################")
    print("\tVENDING MACHINE SIMULATION")
    print("\t##########################")

    while True:
        print("\nWhat would you like to do?")
        print("1. Display available items")
        print("2. Add an item")
        print("3. Remove an item")
        print("4. Restock an item")
        print("5. Purchase an item")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        # choice 1: Display available items
        if choice == "1":
            if vending_machine.is_empty() == False:
                vending_machine.display_items()
            else:
                print("\n\tThe vending machine is currently empty.")

        # choice 2: Add an item
        elif choice == "2":
            if vending_machine.is_full() == False:
                category = get_category()
                attribute = "weight" if category == "snacks" else "volume"
                name = input("Enter name: ")
                while True:
                    try:
                        price = float(input("Enter price: "))
                        break
                    except ValueError:
                        print("\n\tInvalid price. Please enter a number!")
                while True:
                    try:
                        attribute_value = int(input(f"Enter {attribute}: "))
                        break
                    except ValueError:
                        print(f"\n\tInvalid {attribute}. Please enter a whole number!")
                vending_machine.add_item(category, name, price, attribute, attribute_value)
            else:
                print("\n\tThe vending machine is already full. Please remove an item before adding another one!")

        # choice 3: Remove an item
        elif choice == "3":
            if vending_machine.is_empty() == False:
                category = get_category()
                name = input("Enter name: ")
                vending_machine.remove_item(category, name)
            else:
                print("\n\tThe vending machine is already empty. Please add an item first!")

        # choice 4: Restock an item
        elif choice == "4":
            if vending_machine.is_empty() == False:
                category = get_category()
                name = input("Enter name: ")
                vending_machine.restock_item(category, name)
            else:
                print("\n\tThere are no items in the vending machine. Please add an item first!")

        # choice 5: Purchase an item
        elif choice == "5":
            if vending_machine.is_empty() == False:
                category = get_category()
                name = input("Enter name: ")
                vending_machine.purchase_item(category, name)
            else: 
                print("\n\tThere are no items in the vending machine. Please add an item first!")

        # choice 6: Exit the program
        elif choice == "6":
            print("\n\tExiting program.")
            break

        else:
            print("\n\tInvalid choice. Please try again.")