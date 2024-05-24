class FileProcessor:
    @staticmethod
    def read_data(filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return f"An error occurred: {e}"

    @staticmethod
    def write_data(filename, data):
        try:
            with open(filename, 'w') as file:
                file.write(data)
                return "Data written successfully."
        except Exception as e:
            return f"An error occurred: {e}"

    @staticmethod
    def append_data(filename, data):
        try:
            with open(filename, 'a') as file:
                file.write(data)
                return "Data appended successfully."
        except Exception as e:
            return f"An error occurred: {e}"

# Read data from a file
print(FileProcessor.read_data("example.txt"))

# Write data to a file
print(FileProcessor.write_data("example.txt", "Hello, World!\n"))

# Append data to a file
print(FileProcessor.append_data("example.txt", "This is a new line."))
