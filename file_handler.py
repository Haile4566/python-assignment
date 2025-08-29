def read_and_write_file():
    try:
        # Ask user for input file name
        input_file = input("Enter the filename to read: ")
        
        # Open and read the file
        with open(input_file, "r") as file:
            content = file.read()
        
        # Modify the content (example: convert text to uppercase)
        modified_content = content.upper()
        
        # Write modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to {output_file}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename.")
    except PermissionError:
        print("Error: Permission denied. Cannot read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
