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

def sort_dic(chars):
    sorted_chars_final = []
    sorted_by_value = dict(sorted(chars.items(), key=lambda x: x[1], reverse=True))
    for key in sorted_by_value:
        dic_entry = {"char": "", "num": 0}
        dic_entry["char"] = key
        dic_entry["num"] = sorted_by_value[f"{key}"]
        sorted_chars_final.append(dic_entry)

    return sorted_chars_final