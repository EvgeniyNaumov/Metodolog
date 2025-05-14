import random
from math import gcd

GAME_RULES = "Find the smallest common multiple of given numbers."

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_three(a, b, c):
    return lcm(lcm(a, b), c)

def generate_round():
    numbers = [random.randint(1, 10) for _ in range(3)]
    question = " ".join(map(str, numbers))
    correct_answer = lcm_three(*numbers)
    return question, correct_answer
