from stats import count_words
from stats import count_characters
from stats import sort_dic

def get_book_text(file):
    """
    returns the contents of the frankenstein.txt in /books as a string
    """
    with open(file) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    file = "books/frankenstein.txt"
    text = get_book_text(file)
    sorted_char = sort_dic(count_characters(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    print(sort_dic)


main()