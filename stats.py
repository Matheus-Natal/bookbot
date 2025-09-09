
def get_num_words (book_text):
    words = book_text.split()
    return len(words)


def get_char_count(text):
    """
    Counts the number of times each character appears in a string.

    Args:
        text (str): The string to count characters in.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_chars(char_dict):
    """
    Sorts a dictionary of character counts into a list of dictionaries.

    Args:
        char_dict (dict): A dictionary with characters as keys and counts as values.

    Returns:
        list: A sorted list of dictionaries, where each dictionary has 'char' and 'num' keys.
    """
    # Create a list of dictionaries from the char_dict.
    sorted_list = []
    for char, num in char_dict.items():
        sorted_list.append({"char": char, "num": num})

    # Helper function for sorting by the 'num' key.
    def sort_on(d):
        return d["num"]
    
    # Sort the list in descending order.
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
