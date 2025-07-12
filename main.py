import sys
from stats import get_book_text
from stats import get_word_count
from stats import get_char_nums
from stats import sort_char_nums
from stats import sort_on
from stats import fix_dict
from report import report

def main():
    print("Usage: python3 main.py <path_to_book>")
    #print(sys.argv[1])
    if len(sys.argv) !=2:
        sys.exit(1)
    report(sys.argv[1])

main()