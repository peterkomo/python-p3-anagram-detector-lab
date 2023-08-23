# your code goes here!
class Anagram:
    def __init__(self, word):
        self.letters = sorted(letter for letter in word)

    def match(self, words):
        matched_words = []

        for word in words:
            if sorted(letter for letter in word) == self.letters:
                matched_words.append(word)

        return matched_words


        pass
            