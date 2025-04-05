from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) >= 2:
        path_to_file = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    print("============ BOOKBOT ============")
    book_contents = get_book_text(path_to_file)
    print(f"Analyzing book found at {path_to_file}...")

    print("----------- Word Count ----------")
    num_words = get_num_words(book_contents)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    num_chars = get_num_chars(book_contents)
    char_and_count = sort_chars(num_chars)
    for i in range(0, len(char_and_count)):
        if char_and_count[i]["char"].isalpha():
            print(f"{char_and_count[i]["char"]}: {char_and_count[i]["count"]}")
    print("============= END ===============")


main()