import math

while True:
    user_input : str = input("Enter a number to get the square root, or enter \'quit\' to stop: ")
    # Sets the number to use if the user input is a digit
    number : int = int(user_input) if user_input.isdigit() else None
    if user_input.casefold() == 'quit':
        break
    else:
        print(math.sqrt(number))