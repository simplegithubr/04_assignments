# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

# Solution
def main():
    # Get the 3 side lengths of the triangle
    side1 = float(input("What is The Lenght of side 1? "))
    side2  = float(input("What is The Lenght of side 2? "))
    side3  = float(input("What is The Lenght of side 3? "))
    # Calculate the perimeter of the triangle
    premater = side1 + side2 + side3
     # Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating!
    print(f"The perimeter of the triangle is {premater:.1f}")

if __name__ == "__main__":
    main()
