def wordstring(book_text):
	count = 0
	# Splits the words in the string
	textsplit = book_text.split()
	for word in textsplit:
		count += 1
	return count
	
	# print(f"{count} words found in the document")
	
def characters(book_text):
	count = {}
	
	# Empty dictionary iterates through and sets up new keys and attributes counts 
	'''
	
    Dictionaries are great for solving counting problems like this where
	there are many variables to keep track of and also keep the counts for.
	
    '''
	for character in book_text:
		character = character.lower() # Reassigning is necessary when using a method
		if character not in count:
			count[character] = 1
		else:
			count[character] += 1
	# print(count)
	return count

def listdict(dict):
	list_of_dicts = []
	
	# This method creates a new dictionary in the empty list for each character and count from an existing dictionary
	for char, count in dict.items():
		list_of_dicts.append({"char": char, "count": count})
	
	return list_of_dicts

def sort(list):
	# This function sorts the new list of dictionaries based on a key value in the .sort method
	list.sort(reverse=True, key=lambda d: d["count"])
	return list



    
	
    