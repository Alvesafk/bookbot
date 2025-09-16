from stats import get_num_words
from stats import count_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    num = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f'{num} words found in the document')
    print(count_char(get_book_text("books/frankenstein.txt")))

main()

