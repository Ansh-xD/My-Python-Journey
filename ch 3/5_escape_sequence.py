a = "Ansh is good boy\nbut not a bad boy"
# a = "Ansh is good boy    { \n }   but not a bad boy"
#                           \n work as enter

print(a)




def escape_sequences_demo():
    # Newline
    newline_example = "Hello, world!\nWelcome to Python."
    print("Newline Example:")
    print(newline_example)
    
    # Tab
    tab_example = "Hello,\tworld!\tWelcome to Python."
    print("\nTab Example:")
    print(tab_example)
    
    # Carriage Return
    carriage_return_example = "Hello, world!\rPython"
    print("\nCarriage Return Example:")
    print(carriage_return_example)
    
    # Backslash
    backslash_example = "Path to file: C:\\Program Files\\Python"
    print("\nBackslash Example:")
    print(backslash_example)
    
    # Single Quote
    single_quote_example = 'She said, \'Hello, world!\''
    print("\nSingle Quote Example:")
    print(single_quote_example)
    
    # Double Quote
    double_quote_example = "He said, \"Welcome to Python!\""
    print("\nDouble Quote Example:")
    print(double_quote_example)
    
    # Backspace
    backspace_example = "Hello, wo\borld!"
    print("\nBackspace Example:")
    print(backspace_example)
    
    # Form Feed
    form_feed_example = "Hello, world!\fPage Break"
    print("\nForm Feed Example:")
    print(form_feed_example)
    
    # Unicode Character
    unicode_example = "Unicode Character: \u03A9 (Omega)"
    print("\nUnicode Example:")
    print(unicode_example)
    
    # Hexadecimal Unicode Character
    hex_unicode_example = "Hexadecimal Unicode Character: \u00A9 (Copyright)"
    print("\nHexadecimal Unicode Example:")
    print(hex_unicode_example)
    
    # Octal Unicode Character
    octal_unicode_example = "Octal Unicode Character: \u265E (Knight)"
    print("\nOctal Unicode Example:")
    print(octal_unicode_example)

# Run the demo
escape_sequences_demo()





# \n: Newline - Moves the cursor to the next line.
# \t: Tab - Inserts a tab space.
# \r: Carriage Return - Moves the cursor to the beginning of the line.
# \\: Backslash - Inserts a literal backslash.
# \': Single Quote - Inserts a literal single quote within single-quoted strings.
# \": Double Quote - Inserts a literal double quote within double-quoted strings.
# \b: Backspace - Moves the cursor one character back (deletes the previous character).
# \f: Form Feed - Moves the cursor to the next page.
# \u: Unicode Character - Inserts a Unicode character using its hexadecimal code.
# \u00A9: Hexadecimal Unicode Character - Example for the copyright symbol.
# \u265E: Unicode character for a chess knight (example of how to use a hexadecimal Unicode code).