from stats import get_num_words, count_char, sort_char_dict, sort_on
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
       
    text = get_book_text(filepath)
    total_words = get_num_words(text)
    word_dict = count_char(text)
    sorted_list_dict = sort_char_dict(word_dict)
    print("============ BookBot ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- WordCount -----------")
    print(f"Found {total_words} total words!")
    print("-------- Character Count --------")
    for char in sorted_list_dict:
        if char["char"].isalpha():
            print(f'{char["char"]}: {char["num"]}')
    print("============= END ===============")
main()

