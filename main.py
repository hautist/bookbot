def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def word_count(text):
    words = text.split()
    return len(words)


def main():
    frankenstein_contents = get_book_text("books/frankenstein.txt")
    frankenstein_wc = word_count(frankenstein_contents)
    print(f"{frankenstein_wc} words found in the document")


main()
