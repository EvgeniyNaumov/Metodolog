import random

GAME_RULES = "What number is missing in the progression?"

def generate_progression():
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = [start * ratio ** i for i in range(length)]
    return progression

def generate_round():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer