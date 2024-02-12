#fucntion get_numbers()
def get_numbers():
    # Ask the user for input using input() method
    # Save it in the input_string variable
    input_string = input("Type your numbers here:")
    # Convert the input_string to a list of strings by splitting it into separate strings using split()
    # Save it in the list_of_string variable
    list_of_strings = input_string.split()
    # Convert the list of strings to list of numbers by using the int() method
    # Save it in the numbers variable
    numbers = [int(num) for num in list_of_strings]
    # return the numbers variable
    return (numbers)

get_numbers()


