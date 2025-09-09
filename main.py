import sys

from stats import get_num_words
from stats import get_char_count
from stats import sort_chars

# This script reads the contents of a text file and prints it to the console.

def get_book_text(filepath):
    """
    Reads the contents of a file at the given filepath and returns it as a string.

    Args:
        filepath (str): The relative path to the text file.

    Returns:
        str: The entire content of the file.
    """
    try:
        # The 'with' statement ensures the file is automatically closed.
        with open(filepath, 'r', encoding='utf-8') as file:
            # Read the entire file content into a single string.
            text_content = file.read()
        return text_content
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return ""

def main():
    """
    Main function to get the text of the book and print it.
    """
    """
    Main function to get the text of the book, count words and characters, and print the report.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Call the function to get the text.
    book_text = get_book_text(file_path)
    
    # Check if the file was read successfully.
    if book_text:
        # Get the word count.
        words_quantity = get_num_words(book_text)

        # Get the character count dictionary and then sort it.
        char_count_dict = get_char_count(book_text)
        sorted_char_list = sort_chars(char_count_dict)

        # Print the report.
    # Define the relative path to the frankenstein.txt file.
    # The script assumes this file is in the same directory.
    #file_path = "books/frankenstein.txt"
    
    # Call the function to get the text.
    #book_text = get_book_text(file_path)
    #book_words = get_char_count(book_text)
    #word_sorted = sort_chars(book_words)
    
    # Print the text if the file was read successfully.
    """if book_text:
        print("--- Book Contents ---")
        print(book_text)
        print("--- End of Contents ---")
    else:
        print("Could not read the book file.") """

    """words = book_text.split()
    words_quantity = len(words)
    print(f'{words_quantity} words found in the document')"""
    #print(f'{get_num_words(book_text)} words found in the document')
    #print(book_words)

    # Imprime o relatório.
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")

            # Itera sobre a lista ordenada e imprime cada caractere e sua contagem.
    for item in sorted_char_list:
         if item ["char"].isalpha():
             print(f"{item['char']}: {item['num']}")
            
    print("============= END ===============")
    
    

# This is the main entry point of the program.
# It ensures that main() is called only when the script is executed directly.
if __name__ == "__main__":
    main()