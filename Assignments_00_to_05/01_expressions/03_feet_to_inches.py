# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. 
# There are 12 inches per foot. Foot is the singular, and feet is the plural.

#Solution

"""
An example program with constants
"""
INCHESS_IN_FOOT : int = 12
def main():
    feet: float = float(input("Enter a number of feet: "))
    inches: float = feet * INCHESS_IN_FOOT
    print("That is", inches, "inches!")

if __name__ == "__main__":
    main()