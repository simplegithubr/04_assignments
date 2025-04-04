# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

# Anton is 3

# Beth is 4

# Chen is 5

# Drew is 6

# Ethan is 7


def main():
    anton : int = 21
    beth : int = 6 + anton
    chen : int = 20 + beth
    drew : int = chen + anton
    ethan : int = chen

    # Print out all of the ages!
    print("Anton is", str(anton), "years old.")
    print("Beth is", str(beth), "years old.")
    print("Chen is", str(chen), "years old.")
    print("Drew is", str(drew), "years old.")
    print("Ethan is", str(ethan), "years old.")

if __name__ == "__main__":
    main()
