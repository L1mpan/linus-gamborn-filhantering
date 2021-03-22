#imports
import random as rnd

#listor
rolls = []

#terminal meddelande
print("Kolla diceroll.txt")

#koden
with open("diceroll.txt", "w") as f1:
    for i in range(10):
        dice = (rnd.randint(1,6))
        rolls.append(dice)
        roll_counter = rolls.count(5)
    f1.write(f"Simulera 10 tarningskast: {rolls}" + "\n")
    rolls.sort()
    f1.write(f"Kastet sortera: {rolls}" + "\n")
    f1.write(f"Antal femmor: {roll_counter}")