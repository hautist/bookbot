import sys
from stats import word_count, character_count_dict, sorted_dict_list


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if (len(sys.argv) < 2) or (len(sys.argv) > 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    frankenstein_contents = get_book_text(book)
    frankenstein_wc = word_count(frankenstein_contents)
    frankenstein_char_dict = character_count_dict(frankenstein_contents)
    sorted_frankenstein_char_dict = sorted_dict_list(frankenstein_char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_wc} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_frankenstein_char_dict:
        if char_dict["char"] == "\n":
            continue
        print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")


main()
