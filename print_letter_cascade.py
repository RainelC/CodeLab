import time

letters = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']


user_input = input("Ingrese una palabra: ").lower()
word_without_spaces = user_input.replace(' ', '')  
is_alpha = word_without_spaces.isalpha() 

let = '' 

if is_alpha == True:
    for letter_user_input in user_input:
        for letter_alphabet in letters:
            if letter_user_input == letter_alphabet:
                let = let + letter_user_input
                print(let)
                time.sleep(0.05)
                break
            else:
                print(let+letter_alphabet)
                time.sleep(0.05)