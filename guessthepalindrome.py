import random

name = input("What is your name? ")

print("Good luck ", name, "!")

palindromes = [
    "a", "aa", "aba", "aca", "adda", "aga", "aha", "aka", "ala", "ama", "ana", 
    "anna", "appa", "ava", "awa", "bib", "bob", "boob", "civic", "dad", "deed", 
    "deified", "did", "divid", "dud", "eve", "eye", "gag", "gig", "goog", "haha", 
    "hannah", "huh", "kayak", "kook", "level", "lol", "madam", "malayalam", "mam", 
    "manam", "minim", "mom", "mum", "nan", "noon", "nun", "otto", "pap", "peep", 
    "pip", "pop", "pup", "radar", "redder", "refer", "reifier", "repaper", "reviver", 
    "rotator", "rotor", "sagas", "sees", "sexes", "solos", "stats", "tat", "tenet", 
    "tit", "toot", "tot", "wow", "ada", "ala", "ava", "dad", "eve", "gig", "gog", 
    "huh", "kayak", "mum", "nan", "nun", "peep", "pip", "pop", "pup", "radar", 
    "redder", "refer", "reviver", "rotor", "sagas", "sees", "solos", "stats", 
    "tenet", "toot", "tot", "wow"
]



word = random.choice(palindromes)

print("Guess the characters")

guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in guesses:
        print(char, end=" ")
    else :
        print("_")
        failed += 1

    if failed == 0:
        print("you win!")
        print("The word is: ", word)
        break

    print()
    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have", + turns, "more guesses")

        if turns == 0:
            print("you loose")