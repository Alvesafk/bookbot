def get_num_words(book_text):
    cont = 0
    word_list = book_text.split()
    for word in word_list:
        cont += 1
    return cont

def count_char(book_text):
    char_dict = {}
    word_list = book_text.lower().split()
    for word in word_list:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_char_dict(char_dict):
    sorted_list = []
    for char in char_dict:
        num = char_dict[char]
        a = {"char": char, "num": num}
        sorted_list.append(a)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
