import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#getting language from user
print('English or German / Englisch oder Deutsch?')
user_language = input()
print(user_language)



# making a list
DE_dict = {
        "dad": "papa",
        "beer": "bier",
        "love": "liebe",
}

word_key_list = ["dad", "beer", "love"]
key = random.choice(word_key_list)

language_EN = ['English', 'Englisch', 'en', 'yes', 'no']
DE = ['German', 'Deutsch', 'de', 'ja', 'nein']

if user_language in language_EN:
    word_to_guess = key
    print(word_to_guess)
else:
    word_to_guess = DE_dict.get(key)
    print(word_to_guess)

underscorelist = []
for letters in word_to_guess:
    underscorelist.append("_")

print(" ".join(underscorelist))

guess_count = 0
for x in range(0, 999999):
    if user_language in DE:
        print(f'Versuche: {guess_count} von {len(HANGMANPICS)}')
        print('Gib einen Buchstaben an:')
    else:
        print(f'Guesses: {guess_count} of {len(HANGMANPICS)}')
        print('Enter your letter guess:')

    user_guess = input()
    if len(user_guess) != 1:
        continue
    elif user_guess.isnumeric():
        continue


    # check input of the user
    #if user_guess =!
    # no number, no more than 1 letter

    if user_guess in word_to_guess:
        if user_language in DE:
            print(f'Super, {user_guess} ist korrekt!')
        else:
            print(f'yeah, {user_guess} is correct!')
        count = 0
        for letter in word_to_guess:
            if letter == user_guess:
                underscorelist[count] = user_guess
            count += 1
        print(" ".join(underscorelist))
        if "".join(underscorelist) == word_to_guess:
            print("BRAVOOOOOOOOO!")
            break

    else:
        print(HANGMANPICS[guess_count])
        guess_count += 1
        if guess_count == len(HANGMANPICS):
            if user_language in DE:
                print(f'Versuche: {guess_count} von {len(HANGMANPICS)}')
                print('Leider hast du verloren :(')
            else:
                print(f'Guesses: {guess_count} of {len(HANGMANPICS)}')
                print('Sadly you lost :(')
            break
        if user_language in DE:
            print(f'Nö, {user_guess} ist nicht korrekt. Bitte versuche es erneut.')
        else:
            print(f'Nope, {user_guess} is not correct. Please try again.')


#
# mystring = "yolo"
# print(mystring)
# print(len(mystring))
#
# myarray = ["y", "o", "l", "o"]
# print(myarray)
# print(len(myarray))
#
# # temporary variable
# output = ""
# # looping through each letters in myarray
# for letters in myarray:
#     # concatenate letters
#     output += letters
#
# print(output)




