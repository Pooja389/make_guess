import random
mode = input("do you want to play 'easy' or 'hard' mode :")
random_no = random.randint(1,100)
if mode == "easy":
    print("you have only 8 chances")
    lives = 8
else:
    print("you have only 5 chances")
    lives = 5

while True:
    if lives == 0:
        print(f"you lose,you are out of chances,real number is {random_no}")
        break

    guess = int(input("make a guess between 1 and 100 :"))

    if guess == random_no:
        print("you won")
        break

    elif guess > random_no:
        print(f"real number is less than {guess}")

    else:
        print(f"real number is greater than {guess}")    

    lives -= 1



