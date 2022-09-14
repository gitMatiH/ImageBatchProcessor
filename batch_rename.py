# Python 3 code to rename multiple
# files in a directory or folder
#https://www.geeksforgeeks.org/rename-multiple-files-using-python/
#https://pynative.com/python-rename-file/

# importing os module
import os

# Function to rename multiple files
def main():

	folder = "batch"
	for count, filename in enumerate(os.listdir(folder)):
		dst = f"How do CRCs work {str(count)}.jpg"
		src =f"{folder}/{filename}" # foldername/filename, .py file should be outside the folder
		dst =f"{folder}/{dst}"
		
		# rename() function will
		# rename all the files
		os.rename(src, dst)

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()
