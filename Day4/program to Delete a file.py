import os

def check_file_existence(file_path):
	if os.path.exists(file_path):
		print(f'The file "{file_path}" exists.')
	else:
		print(f'The file "{file_path}" does not exist.')

# Example usage:
file_path = 'path/to/your/file.txt'
check_file_existence(file_path)
