import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import (get_book_text, get_char_count, sort_on)


filepath = sys.argv[1]
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    get_book_text(filepath) 
    print("--------- Character Count -------")
    get_char_count(filepath)
    #print(get_char_count(filepath))
    sorted_list = (sort_on(get_char_count(filepath)))
    for i in sorted_list:
        alpha_check = i["char"]
        if alpha_check.isalpha() == True:
            print(f"{i["char"]}: {i["num"]}")
        

main()


