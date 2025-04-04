# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

#solution
def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if low <= n <= high:
        return True
    return False

print(in_range(5, 1, 10))  # True
print(in_range(15, 1, 10))  
print(in_range(10, 1, 10))  


   