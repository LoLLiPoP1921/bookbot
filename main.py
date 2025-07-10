from stats import count_words
from stats import count_characters

def get_book_text():
    """
    returns the contents of the frankenstein.txt in /books as a string
    """
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    

def main():
    text = get_book_text()
    print(f"{count_words(text)} words found in the document")
    print(count_characters(text))


main()