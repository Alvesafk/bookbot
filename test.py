string = 'adjaihdoiadojaodhacxhaihdahoahd miguel'

char_dict = {}
word_list = string.split()
for word in word_list:
    for char in word:
        print(char)
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
print(char_dict)
