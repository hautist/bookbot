from stats import word_count, character_count_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    frankenstein_contents = get_book_text("books/frankenstein.txt")
    frankenstein_wc = word_count(frankenstein_contents)
    frankenstein_char_dict = character_count_dict(frankenstein_contents)
    print(f"{frankenstein_wc} words found in the document")
    print(frankenstein_char_dict)


main()
