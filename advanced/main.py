items = []
completed_items = []
previous_items = []
previous_completed_items = []
has_backup = False

while True:
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display the List")
    print("4. Undo The Previous Change")
    print("5. View Completed Items")
    print("6. Replace an Item")
    print("7. Complete an Item")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        previous_items = items.copy()
        previous_completed_items = completed_items.copy()
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

            remove_index = input("Enter the index to remove: ")

            if remove_index.isnumeric():
                remove_index = int(remove_index)

                if 0 <= remove_index < len(items):
                    previous_items = items.copy()
                    previous_completed_items = completed_items.copy()
                    has_backup = True
                    removed_item = items.pop(remove_index)
                    print(f"Removed {removed_item} from the list.")
                else:
                    print("That index doesn't exist.")
            else:
                print("Please enter a number.")
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
            completed_items = previous_completed_items.copy()
            has_backup = False
            print("Previous change undone.")
        else:
            print("No previous change to undo.")

    elif choice == '5':
        if completed_items:
            print("Completed Items:\n")
            for item in completed_items:
                print(item)

        else:
            print("The list is empty.")

    elif choice == '6':
        if items:
            index = 0
            for item in items:
                print(index, item)
                index = index + 1

            replace_index = input("Enter the index to replace: ")

            if replace_index.isnumeric():
                replace_index = int(replace_index)

                if 0 <= replace_index < len(items):
                    previous_items = items.copy()
                    previous_completed_items = completed_items.copy()
                    has_backup = True

                    new_item = input("Enter the new item: ")
                    items[replace_index] = new_item
                    print(f"Item replaced with '{new_item}'.")
                else:
                    print("That index doesn't exist.")
            else:
                print("Please enter a number.")
        else:
            print("The list is empty.")

    elif choice == '7':
        if items:
            index = 0
            for item in items:
                print(index, item)
                index = index + 1

            complete_index = input("Enter the index to complete: ")

            if complete_index.isnumeric():
                complete_index = int(complete_index)

                if 0 <= complete_index < len(items):
                    previous_items = items.copy()
                    previous_completed_items = completed_items.copy()
                    has_backup = True

                    completed_item = items.pop(complete_index)
                    completed_items.append(completed_item)
                    print(f"Completed {completed_item} from the list.")
                else:
                    print("That index doesn't exist.")
            else:
                print("Please enter a number.")
        else:
            print("The list is empty.")
    elif choice == '8':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-8.")