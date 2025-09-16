from stats import get_num_words, count_char, sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    total_words = get_num_words(text)
    word_dict = count_char(text)
    words = sort_char_dict(word_dict)
    print(f'{total_words} words found in the document')
    print(words)

main()

