import re

def count_vowels(input: str):
    return len([i for i in re.findall('[aeiouAEIOU]', input)])


# Test case
print(count_vowels("SOO beautiful"))