# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    if sorted(word1) == sorted(word2):
        print(True)
    else:
        return False


word1 = "flow"
word2 = "wolf"
find_anagrams(word1, word2)

# [assignment] Add your code here
