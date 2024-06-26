def count_chars(word):

    word = word.lower()
    character_count = {}
    for character in word:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count
