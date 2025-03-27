import random

words = ["driver", "bigger", "father", "ninja", "ginger"]
worDex = random.randint(0, 4)
word = words[worDex]

ranDex1 = random.randint(0, len(word))
ranDex2 = random.randint(0, len(word))

if ranDex1 == ranDex2:
    if ranDex1 == 0:
        ranDex2 += 1
    else:
        ranDex1 -= 1

worList = list(word)
worList[ranDex1], worList[ranDex2] = '_', '_'
word2 = "".join(worList)

print("Try to guess what word this is:", word2)
guess = input()
if guess == word:
    print("Congratulations! You've guessed it!")
else:
    print("Incorrect!")