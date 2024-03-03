1.
from functools import reduce

def multiply_all(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

def main():
    number_list = [1, 2, 3, 4, 5]

    if number_list:
        result = multiply_all(number_list)
        print(f"The product of all numbers in the list is: {result}")
    else:
        print("The list is empty. Cannot compute the product.")

if __name__ == "__main__":
    main()

2.
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

def main():
    user_input = input("Enter a string: ")
    
    upper, lower = count_upper_lower(user_input)

    print(f"Number of uppercase letters: {upper}")
    print(f"Number of lowercase letters: {lower}")

if __name__ == "__main__":
    main()

3.
def is_palindrome(s):
    s = s.lower() 
    s = ''.join(char for char in s if char.isalnum())  
    return s == s[::-1]

def main():
    user_input = input("Enter a string to check for palindrome: ")

    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome.")
    else:
        print(f"{user_input} is not a palindrome.")

if __name__ == "__main__":
    main()

4.
import time
import math

def invoke_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result

def main():
    try:
        number = float(input("Enter a number: "))
        milliseconds = int(input("Enter the delay in milliseconds: "))

        if milliseconds < 0:
            raise ValueError("Delay should be a non-negative integer.")

        result = invoke_square_root(number, milliseconds)

        print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

5.
def all_true(elements):
    return all(elements)

def main():
    # Example tuple with boolean values
    bool_tuple = (True, True, True, True)

    result = all_true(bool_tuple)

    if result:
        print("All elements in the tuple are True.")
    else:
        print("Not all elements in the tuple are True.")

if __name__ == "__main__":
    main()