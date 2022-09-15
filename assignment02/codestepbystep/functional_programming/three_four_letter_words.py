
# Suppose you have a list of strings declared as follows. Write functional code
# to produce a new list named words2 containing all of the three- or
# four-letter words in the list.

words = ["four", "score", "and", "seven", "years", "ago"]

words2 = [word for word in words if len(word) == 3  or len(word) == 4]

print(words2)


					