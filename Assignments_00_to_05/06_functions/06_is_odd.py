# Problem Statement
# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

#solution
def main():
    for i in range(10, 20):
        if is_odd(i):
            print(i,'odd')
        else:
            print(i,'even')
def is_odd(value: int):
     """
    Checks to see if a value is odd. If it is, returns true.
    """
     return value % 2 != 0
if __name__ == "__main__":
    main()

