from stats import get_book_text, get_book_length, get_book_characters, get_book_sorted_characters, prepare_report

import sys

def main():
    #
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #
    filepath = sys.argv[1]
    prepare_report(filepath)

main()