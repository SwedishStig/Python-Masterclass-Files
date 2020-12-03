def find_consonant(text: str = " ") -> set:
    """
    returns a list of consonants used in a statement
    :param text: a string of any length
    :return: returns
    """
    vowels = {"a", "e", "i", "o", "u"}
    cons = set()
    for letter in text.casefold():
        if letter.isalpha() and letter not in vowels:
            cons.add(letter)
    return cons


sentence = input("What's your damage? ")
sentence = find_consonant(sentence)

print(", ".join(sentence))
