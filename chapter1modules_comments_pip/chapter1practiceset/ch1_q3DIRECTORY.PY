#  wap to print content of a directory using os module . search online for function which does that 
import os

def print_directory_contents(directory):
    try:
        # Get the list of files and directories
        contents = os.listdir(directory)
        
        # Print the contents
        print(f"Contents of the directory '{directory}':")
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory}'.")

# Example usage:
directory_path = '/New folder'  # Current directory
print_directory_contents(directory_path)
#Q5 is also done 