
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# Solution

def main():
    numbers: list[int] = [1, 2, 3, 4] # Make a list of numbers
    for i  in range(len(numbers)):
       element = numbers[i] # Get the element at index i
       numbers[i] = element * 2 # Double the element and assign it back to the list
    print(numbers) # Print out the list of numbers

if __name__ == "__main__":
    main()