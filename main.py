from stats import count_words
from stats import count_characters
from stats import sort_dic
import sys

def get_book_text(file):
    """
    returns the contents of .txt files in /books as a string
    """
    with open(file) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    try:
        file = sys.argv[1]
        text = get_book_text(file)
        sorted_char = sort_dic(count_characters(text))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file}")
        print("----------- Word Count ----------")
        print(f"Found {count_words(text)} total words")
        print("--------- Character Count -------")
        
        for i in range(0, len(sorted_char)):
            entry = sorted_char[i]
            char, num = entry["char"], entry["num"]
            print(f"{char}: {num}")
        
        print("============= END ===============")
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
main()