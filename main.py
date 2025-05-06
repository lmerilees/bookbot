from stats import count_characters, get_num_words, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
  
def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    letters = count_characters(book_text)
    sorted_list = sort_dict(letters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char in sorted_list:
        if (char["char"].isalpha()):
            print(f"{char["char"]}: {char["num"]}")


main()