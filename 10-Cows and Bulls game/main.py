import random

def get_digits(num_digits):
    return [int(i) for i in str(num_digits)]

def no_duplicates(num_duplicates):
    num_li = get_digits(num_duplicates)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False

def generate_num():
    while True:
        generate_nums = random.randint(1000, 9999)
        if no_duplicates(generate_nums):
            return generate_nums

def num_of_bulls_cows(nums, guesses):
    bulls_and_cows = [0, 0]
    num_li = get_digits(nums)
    guess_li = get_digits(guesses)

    for i, j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bulls_and_cows[0] += 1
            else:
                bulls_and_cows[1] += 1
    return bulls_and_cows

num = generate_num()
tries = int(input('Enter number of tries: '))

while tries > 0:
    guess = int(input("Enter your guess: "))
    if not no_duplicates(guess):
        print("Number should not have repeated digits. Try again.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again.")
        continue
    bulls_and_cows = num_of_bulls_cows(num, guess)
    print(f"{bulls_and_cows[0]} bulls, {bulls_and_cows[1]} cows")
    tries -= 1
    if bulls_and_cows[0] == 4:
        print("You guessed right!")
        break
else:
    print(f"You ran out of tries. Number was {num}")
