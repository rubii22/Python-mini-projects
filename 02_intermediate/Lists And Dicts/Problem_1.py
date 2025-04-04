# Problem #1: List Practice

# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# Solution

def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    print("Fruit List:", fruit_list)

    print("First fruit:", fruit_list[0])
    print("Last fruit:", fruit_list[-1])

    fruit_list.append('mango')
    print("Updated List after adding mango:", fruit_list)

    fruit_list.remove('banana')
    print("Updated List after removing banana:", fruit_list)

    if 'grape' in fruit_list:
        print("Grape is in the list.")

    print("Number of fruits in the list:", len(fruit_list))

main()
