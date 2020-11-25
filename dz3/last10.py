import os

def print_files(start_dir):
	for element in os.walk(start_dir):
		for file in element[-1]:
			print(file)
print_files("/disk2/home/is29/is29_licov/Desktop/123")
