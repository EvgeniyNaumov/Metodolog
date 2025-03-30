import random


def generate_progression(start, step, length):
    return [start * (step ** i) for i in range(length)]


def hide_element(progression, position):
    hidden_value = progression[position]
    progression[position] = '..'
    return ' '.join(map(str, progression)), hidden_value


def play_progression_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    rounds = 3
    correct_answers = 0

    for _ in range(rounds):
        start = random.randint(1, 5)
        step = random.randint(2, 5)
        length = random.randint(5, 10)
        progression = generate_progression(start, step, length)
        hidden_position = random.randint(0, len(progression) - 1)

        question, correct_answer = hide_element(progression, hidden_position)
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    if correct_answers == rounds:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_progression_game()
