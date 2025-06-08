def word_count(text):
    words = text.split()
    return len(words)


def character_count_dict(text):
    character_dict = {}
    for char in text:
        try:
            character_dict[char.lower()] += 1
        except KeyError:
            character_dict[char.lower()] = 1
    return character_dict
