# # Create a function isAlt() that accepts a string as an argument and validates 
# # whether the vowels (a, e, i, o, u) and consonants are in alternate order.

def isAlt(word: str):
    word = word.lower()
    for i in range(len(word)-1):
        letter = word[i]
        if letter in vowels:
            next_letter = word[i+1]
            if next_letter not in consonants:
                return False      
        elif letter in consonants:
            next_letter = word[i+1]
            if next_letter not in vowels:
                return False      
    return True

vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"
print(isAlt("amazon"))
print(isAlt("apple"))
print(isAlt("banana"))