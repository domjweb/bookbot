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








