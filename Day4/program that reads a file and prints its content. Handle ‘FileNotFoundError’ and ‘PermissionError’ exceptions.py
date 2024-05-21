def read_file(filename):
    """
    Reads and prints the content of a file.
    
    Parameters:
    filename (str): The name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except PermissionError:
        print(f"Error: Permission denied to read {filename}.")

def main():
    filename = 'details.txt'  
    read_file(filename)

if __name__ == '__main__':
    main()
