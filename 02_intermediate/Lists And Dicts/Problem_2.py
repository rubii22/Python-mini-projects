# Problem #2  : Index Game

def access_element(lst, index):
    """Returns the element at the given index or an error message if out of range."""
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Error: Index out of range."

def modify_element(lst, index, new_value):
    """Modifies an element at the given index with a new value."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Updated List: {lst}"
    else:
        return "Error: Index out of range."

def slice_list(lst, start, end):
    """Returns a sliced portion of the list, handling out-of-range cases."""
    if 0 <= start < len(lst) and 0 < end <= len(lst) and start < end:
        return f"Sliced List ({start}:{end}): {lst[start:end]}"
    else:
        return "Error: Invalid range for slicing."

def main():
    # Initialize the list
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]

    while True:
        print("\n🔹 Index Game Menu 🔹")
        print("1️⃣ Access an element")
        print("2️⃣ Modify an element")
        print("3️⃣ Slice the list")
        print("4️⃣ Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            index = int(input("Enter the index to access: "))
            print(access_element(my_list, index))
        
        elif choice == "2":
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == "3":
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print(slice_list(my_list, start, end))

        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the game
main()
