def get_word_count(path):
    file = get_book_text(path)
    split_file = file.split()
    words = len(split_file)
    print(f"{words} words found in the document")
