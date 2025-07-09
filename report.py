from stats import get_word_count
from stats import fix_dict

def report(path):
    words = get_word_count(path)
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")   
    for entry in fix_dict(path):
        if entry{1}.isalpha():
            print(f"{entry{1}}: {entry{2}}")
    
    print("============= END ===============")