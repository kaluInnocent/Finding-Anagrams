# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    word1 = sorted(word1)
    word2 = sorted(word2)
    return word1 == word2

