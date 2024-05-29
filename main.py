with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

def word_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_counts = {}
    text = text.lower()
    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else: 
            letter_counts[letter] = 1
    return letter_counts

from collections import Counter
def count_characters(filepath):
    with open(filepath, 'r') as file:
        text = file.read().lower()
    return Counter(filter(str.isalpha, text))

letter_counts = count_characters('books/frankenstein.txt')
print(letter_counts)

letter_count_list = [{"letter": char, "num": count} for char, count in letter_counts.items()]
print(letter_count_list)

def sort_on(item):
    return item["num"]

letter_count_list.sort(reverse=True, key=sort_on)
print(letter_count_list)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{sum(letter_counts.values())} words found in the document")
for item in letter_count_list:
    print(f"The '{item['letter']}' character was found {item['num']} times")
print("--- End report ---")
