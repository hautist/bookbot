import operator


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


def sorted_dict_list(character_dict):
    new_list = []
    for character in character_dict:
        new_dict = {}
        count = character_dict[character]
        new_dict["char"] = character
        new_dict["num"] = count
        new_list.append(new_dict)
    sort_list = sorted(new_list, key=operator.itemgetter("num"), reverse=True)
    return sort_list
