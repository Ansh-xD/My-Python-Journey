# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 




import os

def print_directory_contents(directory):
    try:
        # Get the list of entries in the directory
        entries = os.listdir(directory)
        
        # Print each entry
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
    except PermissionError:
        print(f"You do not have permission to access the directory {directory}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = '/'  # Change / to the directory you want to list
print_directory_contents(directory_path)
