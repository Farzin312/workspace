def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    x = text.split()
    total_words = len(x)
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words} words were found in the document")
    word_counter(text)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    letter_count = {}
    for word in text.split():  
        for letter in word:
            letter_count[letter.lower()] = letter_count.get(letter.lower(), 0) + 1

    y = list(letter_count.keys())
    key_names = []
    for name in y:
        if name.isalpha():
            key_names.append(name)
    key_names.sort()
    for i in range(len(key_names)):
        print(f"The {key_names[i]} character was found {letter_count[key_names[i]]} times")

main()
