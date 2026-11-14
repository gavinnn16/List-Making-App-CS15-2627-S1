items = []
previous_items = []
has_backup = False
while True:
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display the List")
    print("4. Undo The Previous Change")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        previous_items = items.copy()
        has_backup = True
        item = input("Enter Item Name: ")
        items.append(item)
        print(f"Item '{item}' added to the list.")
    elif choice == '2':
        if items:
            index = 0
            for item in items:
                print(index, item)
                index = index + 1

            remove_index = int(input("Enter the index to remove: "))

            if 0 <= remove_index < len(items):
                previous_items = items.copy()
                has_backup = True
                removed_item = items.pop(remove_index)
                print(f"Removed {removed_item} from the list.")
            else:
                print("That index doesn't exist.")
        else:
            print("The list is empty.")
    elif choice == '3':
        if items:
            print("Current List of Items:\n")
            for item in items:
                print(item)
            print()
        else:
            print("The list is empty.")
    elif choice == '4':
        if has_backup:
            items = previous_items.copy()
            has_backup = False
            print("Previous change undone.")
        else:
            print("No previous change to undo.")

    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-5.")