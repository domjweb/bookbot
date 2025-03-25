from stats import wordstring, characters, listdict, sort

def get_book_text(path_to_file):
	# Open the file within the 'with' statement
	with open(path_to_file) as f:
	# Read file contents
		content = f.read()
	# Return the contents (the file automatically closes here)
	return content


def main():
	booktext = get_book_text("books/frankenstein.txt")
	# print(booktext)
	wordcount = wordstring(booktext)
	charcount = characters(booktext)
	list_of_dicts = listdict(charcount)
	sorted_list_of_dicts = sort(list_of_dicts)

	character_counts = ""
	for pair in sorted_list_of_dicts:
		if pair['char'].isalpha():
			character_counts += f"{pair['char']}: {pair['count']}\n"

	
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {wordcount} total words")
	print("--------- Character Count -------")
	print(character_counts.strip())
	print("============= END ===============")
	


	

main()

