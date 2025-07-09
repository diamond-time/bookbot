def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        #print(file_contents)
    return file_contents

def get_word_count(path):
    file = get_book_text(path)
    split_file = file.split()
    words = len(split_file)
    print(f"{words} words found in the document")

def get_char_nums(path):
    file = get_book_text(path)
    file_lowercase = file.lower()
    characters = list(file_lowercase)
    character_nums = {}
    for letter in characters:
        if letter not in character_nums:
            character_nums[letter]=0
        character_nums[letter] +=1
    return character_nums

def fix_dict(path):
    fixed_dict = {}
    char_counts = get_char_nums(path)
    for letter, amount in char_counts.items():
        print(f"Letter is {letter} and amount is {amount}")
        #fixed_dict.add({"char":{letter}, "num":{amount}})
    print(fixed_dict)


def sort_on(char):
    return char[1]

def sort_char_nums(path):
    nums = get_char_nums(path)
    sorted_chars = sorted(nums.values())
    print(sorted_chars)
    return 

def updated_dict(dict):
    return