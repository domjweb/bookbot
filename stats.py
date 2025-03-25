def wordstring(book_text):
	count = 0
	# Splits the words in the string
	textsplit = book_text.split()
	for word in textsplit:
		count += 1
	
	print(f"{count} words found in the document")