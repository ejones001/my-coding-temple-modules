# main.py

import text_utils as tu

# Example usage of functions from text_utils.py
input_string = input("Enter a string: ")

reversed_string = tu.reverse_string(input_string)
capitalized_string = tu.capitalize_string(input_string)

print("Reversed string:", reversed_string)
print("Capitalized string:", capitalized_string)
