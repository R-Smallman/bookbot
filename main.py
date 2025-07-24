from stats import get_book_text, get_book_length, get_book_characters, get_book_sorted_characters, report

import sys

def main():
    # require filepath on run
    if len(sys.argv) != 2:
        # custom error message
        print("Usage: python3 main.py <path_to_book>")
        # exit program
        sys.exit(1)
    
    # get filepath on run
    filepath = sys.argv[1]
    
    # output
    report(filepath)

main()