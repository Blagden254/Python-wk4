def read_and_modify_file():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename to read: ")
        
        # Open the file and read its content
        with open(filename, "r") as file:
            content = file.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content written to {new_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
