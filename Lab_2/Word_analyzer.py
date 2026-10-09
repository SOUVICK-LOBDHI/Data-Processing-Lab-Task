word = input("Enter a word or short sentence: ")

characters = len(word)
spaces = 0
vowels = 0

for ch in word:
    if ch  in 'aeiou':
        vowels += 1
    elif ch in 'AEIOU':
        vowels += 1
    elif ch in ' ':
        spaces += 1

print("Number of characters: ", characters)
print("Number of spaces: ",spaces)
print("Number of vowels: ", vowels)

