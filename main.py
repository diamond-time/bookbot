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


def main():
    get_word_count("./books/frankenstein.txt")

main()