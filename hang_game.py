import random

# making a list
word_list = ["yolo", "microsoft", "baby", "plastic"]
word_to_guess = random.choice(word_list)
print(word_to_guess)

underscorelist = []
for letters in word_to_guess:
    underscorelist.append("_")

print(" ".join(underscorelist))

for x in range(0, 999999):
    print('Enter your letter guess:')
    user_guess = input()

    if user_guess in word_to_guess:
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
        print(f'Nope, {user_guess} is not correct. Pleass try again.')


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




