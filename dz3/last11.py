import os

def print_files(start_dir):
	for element in os.walk(start_dir):
		for file in element[-1]:
			if file.endswith(".py"):
				print(file)
print_files("/disk2/home/is29")
