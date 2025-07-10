def count_words(text):
    """
    Counts the words in a string
    """
    return len(text.split())

def count_characters(text):
    """
    Counts how many of each character are in a text
    """
    characters = list(text.lower())
    character_set = set(characters)
    char_count_dic = {}

    for character in character_set:
        count = characters.count(character)
        char_count_dic[character] = count
    return char_count_dic