def make_shirt(message : str = 'I love programming', size : str = 'large'):
    """Prints a summary of a shirt given its size and the text that will be on the shirt"""
    valid_sizes : list = ['small', 'medium', 'large', 'x-large']
    valid_input : bool = False
    for valid_size in valid_sizes:
        if valid_size == size:
            valid_input = True
    if not valid_input:
        print("Invalid size.")
        return
    print(f"You ordered a {size} sized shirt that says {message}.")

# make_shirt(size = 'medium')
# make_shirt()

message : str = ''
while(message.casefold() != 'quit'):
    message = input("Please enter a message for your t-shirt or enter \'quit\' to exit: ")
    if message == 'quit':
        break
    size = input("Please enter a size for your t-shirt: ")
    make_shirt(message, size)

