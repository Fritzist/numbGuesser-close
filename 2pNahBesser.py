import random


def get_score(a, b):
    return abs(a - b)


def get_num_input(text):
    some = ""
    while not some.isnumeric():
        some = input(text)
    return int(some)


tries = 0
result = random.randint(0, 99)

print("Um anzufangen brauche ich eure Namen")
print(result)
name1 = (input('Dein Name : '))
name2 = (input('Dein Name: '))

print(f"Hallo {name1} und {name2} ihr werdet gleich beide eine Zahl sagen und die Person, die näher an der "
      f"Zuffalszahl ist, hat gewonnen. Die Zahlen gehen von 0-99")

print(f"{name1} Deine Zahl bitte")

number_p1 = get_num_input(">")

if number_p1 < 0 or number_p1 > 99:
    print(f"Bis du Dumm {name1}")

print(f"{name2} Deine Zahl bitte")

number_p2 = get_num_input(">")

if number_p2 < 0 or number_p2 > 99:
    print(f"Bis du Dumm {name2}")

score1 = get_score(number_p1, result)
score2 = get_score(number_p2, result)

if number_p1 == result:
    print(f"Wow! {name1} du hast genau die Zahl erraten")
    
if number_p2 == result:
    print(f"Wow! {name2} du hast genau die Zahl erraten")


if score1 == score2:
    print("Unentschieden")
elif score1 < score2:
    print(f"{name1} hat gewonnen")
else:
    print(f"{name2} hat gewonnen")
print(f"Die Zahl ist {result}")
