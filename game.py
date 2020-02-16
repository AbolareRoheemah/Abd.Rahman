#"Guess the secret number" game
import random
secret_num = random.randint(1,21)
for guess in range(1,7):
    print("I am thinking of a number, can you guess what number it is?:\n")
    player_num = int(input())
    if player_num == secret_num:
        print("Hurrah! you guessed the secret number correctly in "+str(guess)+" guesses")
        break                  
    elif player_num < secret_num:
        print("Your guess is too low")
    elif player_num > secret_num:
        print("You guessed too high")
if player_num != secret_num:
    print("You couldn't guess the secret number😢")
    print("The secret number is "+ str(secret_num))     