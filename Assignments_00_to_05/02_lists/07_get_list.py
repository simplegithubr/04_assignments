

# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

#Solution:
def main():
    lst = []
    value = input("Enter a value: ")
    while value :
        lst.append(value)
        value = input("Enter a value: ")
    print("Here's the list:", lst)
if __name__ == "__main__":
    main()
