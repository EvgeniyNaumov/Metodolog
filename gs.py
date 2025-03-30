import math
import random


def calculate_lcm(a, b, c):

    lcm_ab = a * b // math.gcd(a, b)
    lcm_abc = lcm_ab * c // math.gcd(lcm_ab, c)
    return lcm_abc

def generate_numbers():

    return [random.randint(1, 100) for _ in range(3)]

def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    correct_answers = 0
    total_questions = 3

    for _ in range(total_questions):
        numbers = generate_numbers()
        lcm = calculate_lcm(*numbers)
        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = int(input("Your answer: "))

        if user_answer == lcm:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{lcm}'.")
            print(f"Let's try again, {name}!")
            return

    if correct_answers == total_questions:
        print(f"Congratulations, {name}!")

if __name__ == "__main__":
    play_game()
