def get_book_text(path_to_file):
	# Open the file within the 'with' statement
	with open(path_to_file) as f:
	# Read file contents
		content = f.read()
	# Return the contents (the file automatically closes here)
	return content

def main():
	booktext = get_book_text("books/frankenstein.txt")
	print(booktext)

main()
