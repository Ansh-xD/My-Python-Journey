name = "ansh"

print(len(name))
print(name.endswith("sh"))
print(name.startswith("an"))
print(name.capitalize())



def string_functions_demo(s):
    print(f"Original String: '{s}'")
    
    # String Length
    print(f"Length: {len(s)}")
    
    # Convert to Lowercase
    print(f"Lowercase: {s.lower()}")
    
    # Convert to Uppercase
    print(f"Uppercase: {s.upper()}")
    
    # Capitalize First Letter
    print(f"Capitalize: {s.capitalize()}")
    
    # Title Case
    print(f"Title Case: {s.title()}")
    
    # Check if String is Alphanumeric
    print(f"Is Alphanumeric: {s.isalnum()}")
    
    # Check if String is Alphabetic
    print(f"Is Alphabetic: {s.isalpha()}")
    
    # Check if String is Numeric
    print(f"Is Numeric: {s.isdigit()}")
    
    # Check if String is a Valid Identifier
    print(f"Is Identifier: {s.isidentifier()}")
    
    # Strip Whitespace
    print(f"Strip Whitespace: '{s.strip()}'")
    
    # Replace Substring
    print(f"Replace 'test' with 'demo': {s.replace('test', 'demo')}")
    
    # Find Substring
    print(f"Find 'demo': {s.find('demo')}")
    
    # Split String
    print(f"Split by ' ': {s.split()}")
    
    # Join with a Separator
    words = s.split()
    print(f"Join with ', ': {', '.join(words)}")
    
    # Check if String Starts with a Prefix
    print(f"Starts with 'Hello': {s.startswith('Hello')}")
    
    # Check if String Ends with a Suffix
    print(f"Ends with 'World!': {s.endswith('World!')}")
    
    # String Formatting
    name = "Alice"
    age = 30
    formatted_string = f"My name is {name} and I am {age} years old."
    print(f"Formatted String: {formatted_string}")

# Example Usage
example_string = "  Hello, this is a test string for Python string functions. World!  "
string_functions_demo(example_string)




# In this example:

# len(): Returns the length of the string.
# lower(): Converts the string to lowercase.
# upper(): Converts the string to uppercase.
# capitalize(): Capitalizes the first letter of the string.
# title(): Capitalizes the first letter of each word.
# isalnum(): Checks if all characters in the string are alphanumeric.
# isalpha(): Checks if all characters in the string are alphabetic.
# isdigit(): Checks if all characters in the string are digits.
# isidentifier(): Checks if the string is a valid identifier.
# strip(): Removes leading and trailing whitespace.
# replace(): Replaces a substring with another substring.
# find(): Finds the index of the first occurrence of a substring.
# split(): Splits the string into a list of substrings.
# join(): Joins a list of substrings into a single string with a specified separator.
# startswith(): Checks if the string starts with a specified prefix.
# endswith(): Checks if the string ends with a specified suffix.
# f-string: Provides a way to format strings using variables.