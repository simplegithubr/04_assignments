# Write a Python program that takes two integer
#  inputs from the user and calculates their sum.
#  The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working 
# implementation of this problem, where the main() function guides the user
#  through the process of entering two numbers and displays their sum.




def main():
    print("This program adds two numbers:")
    num1: str = input("Enter the first number: ")
    num1 : int= int(num1)
    num2: str = input("Enter the second number: ")
    num2 : int= int(num2)
    total: int = num1 + num2
    print("The total sum is: " + str(total) + ".")


#call the main function to run the program
if __name__ == "__main__":
    main()


