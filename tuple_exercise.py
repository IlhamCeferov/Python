import random

def cast():
    first,second = random.randint(1,6),random.randint(1,6)
    return first,second

dice1 , dice2 = cast()
print(f"The dice show {dice1} and {dice2}.")