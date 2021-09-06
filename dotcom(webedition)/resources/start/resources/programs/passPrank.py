import os
import random
import random
def clear():
    os.system('clear')
user_pass = input("""Enter your password
==>""")
tries = 0
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z',]
guess = ""
while (guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password[random.randint(0, 25)]
        guess = str(guess_letter) + str(guess)
    print(guess)
    tries += 1
    print()
print("Your password is",guess, "it took me", tries, "tries")


