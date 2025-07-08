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

def get_characters(path):
    file = get_book_text(path)
    file_lowercase = file.lower()
    characters = list(file_lowercase)
    character_numbers = {}
    for letter in characters:
        if letter not in character_numbers:
            character_numbers[letter]=0
        character_numbers[letter] +=1
    print (character_numbers)
    return