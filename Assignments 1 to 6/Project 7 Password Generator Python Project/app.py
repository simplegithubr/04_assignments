import random
import string

def main():
    num_passwords  =  int(input("How many passwords do you need?"))
    password_length = int(input("What should be the length of each password?"))

    characters = string.ascii_letters + string.digits + string.punctuation

    print("\nGenrate Passwored")
    for _ in  range(num_passwords):
        password = ''.join(random.choices(characters, k=password_length))
        print(password)

if __name__ == "__main__":
    main()