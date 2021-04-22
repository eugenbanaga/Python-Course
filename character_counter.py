alpha_numeric = "qwertyuiopasdfghjklzxcvbnm1234567890"

phrase = input("Enter your phrase: ")

for x in alpha_numeric:
    counter = 0
    for y in phrase:
        if x == y.casefold():
            counter += 1
    if counter > 1:
        print("Character " + x + " is encountered " + str(counter) + " times")



