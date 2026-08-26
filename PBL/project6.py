inventory = {}

while True:
    print("\n1. Add  2. View  3. Update  4. Delete  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        id = input("Product ID: ")
        inventory[id] = {
            "name": input("Product Name: "),
            "price": float(input("Price: ")),
            "qty": int(input("Quantity: "))
        }
        print("Product added!")

    elif choice == "2":
        if not inventory:
            print("Inventory is empty!")
        else:
            for id, p in inventory.items():
                print(id, p)

    elif choice == "3":
        id = input("Product ID: ")
        if id in inventory:
            inventory[id]["name"] = input("New name: ")
            inventory[id]["price"] = float(input("New price: "))
            inventory[id]["qty"] = int(input("New quantity: "))
            print("Product updated!")
        else:
            print("Product not found!")

    elif choice == "4":
        id = input("Product ID: ")
        if id in inventory:
            del inventory[id]
            print("Product deleted!")
        else:
            print("Product not found!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("You have Entered a wrong choice")