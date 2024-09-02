
import re
def count_vowels(text):
    vowels = re.findall(r'[aeiou]',text)
    print(len(vowels))

count_vowels('good afternoom')