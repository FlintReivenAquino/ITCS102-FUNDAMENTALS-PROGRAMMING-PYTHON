import random

print("guessing number")

rndm_num = random.randint(1,3)
tries = 0
turu = True

while turu == True:
    
    num = int(eval(input("input an integer number -> ")))

    tries += 1

    if num == rndm_num:
        print("correct")
        print(f"you took {tries} tries")
        break
    
    else:
        print("wrong")
        print("coninue")
        continue