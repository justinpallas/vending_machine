class VendingMachine:
    def __init__(self):
        self.items = {
            "snacks": [
                {"name": "chips", "price": 1.50, "weight": "50g", "quantity": 10},
                {"name": "candy", "price": 0.75, "weight": "25g", "quantity": 10},
                {"name": "granola bar", "price": 1.00, "weight": "35g", "quantity": 10},
            ],
            "beverages": [
                {"name": "soda", "price": 2.00, "volume": "350ml", "quantity": 10},
                {"name": "water", "price": 1.00, "volume": "500ml", "quantity": 10},
                {"name": "juice", "price": 1.50, "volume": "250ml", "quantity": 10},
            ],
        }

    def display_items(self):
        print("Available items:")
        for category, items in self.items.items():
            print(f"\n{category.capitalize()}:")
            for item in items:
                print(
                    f"{item['name']} - ${item['price']} - {item.get('weight', item.get('volume'))} - Quantity: {item['quantity']}"
                )

    def add_item(self, category, name, price, attribute):
        if category.lower() == "snacks":
            weight = input("Enter weight: ")
            self.items[category][name] = {"price": price, "weight": weight}
        elif category.lower() == "beverages":
            volume = input("Enter volume: ")
            self.items[category][name] = {"price": price, "volume": volume}
        else:
            print("Invalid category. Please try again.")


    def remove_item(self, category, name):
        for i, item in enumerate(self.items[category]):
            if item["name"] == name:
                del self.items[category][i]
                print(f"{name.capitalize()} removed from {category}!")
                break
        else:
            print(f"{name.capitalize()} not found in {category}.")

    def restock_item(self, category, name):
        for item in self.items[category]:
            if item["name"] == name:
                item["quantity"] = 10
                print(f"{name.capitalize()} restocked!")
                break
        else:
            print(f"{name.capitalize()} not found in {category}.")

    def purchase_item(self, category, name):
        for item in self.items[category]:
            if item["name"] == name:
                if item["quantity"] > 0:
                    item["quantity"] -= 1
                    print(f"{name.capitalize()} purchased!")
                    break
                else:
                    print(f"{name.capitalize()} is out of stock.")
                    break
        else:
            print(f"{name.capitalize()} not found in {category}.")


if __name__ == "__main__":
    vending_machine = VendingMachine()

    while True:
        print("\n\t##########################")
        print("\tVENDING MACHINE SIMULATION")
        print("\t##########################")
        print("\nWhat would you like to do?")
        print("1. Display available items")
        print("2. Add an item")
        print("3. Remove an item")
        print("4. Restock an item")
        print("5. Purchase an item")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            vending_machine.display_items()

        elif choice == "2":
            category = input("Enter category (snacks/beverages): ")
            name = input("Enter name: ")
            price = float(input("Enter price: "))
            attribute = "weight" if category == "snacks" else "volume"
            vending_machine.add_item(category, name, price, attribute)

        elif choice == "3":
            category = input("Enter category (snacks/beverages): ")
            name = input("Enter name: ")
            vending_machine.remove_item(category, name)

        elif choice == "4":
            category = input("Enter category (snacks/beverages): ")
            name = input("Enter name: ")
            vending_machine.restock_item(category, name)

        elif choice == "5":
            category = input("Enter category (snacks/beverages): ")
            name = input("Enter name: ")
            vending_machine.purchase_item(category, name)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

