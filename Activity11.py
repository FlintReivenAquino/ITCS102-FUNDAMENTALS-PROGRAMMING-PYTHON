temp = eval(input("What's the temperature?: "))

if temp < 1:
    print("temperature is very cold")
elif temp >= 1 and temp <= 20:
    print("temperature is cold")
elif temp >= 21 and temp <= 30:
    print("temperature is kinda warm")
elif temp >= 31 and temp <= 40:
    print("temperature is warm")
elif temp >= 41 and temp <= 50:
    print("temperature hot")
elif temp >= 51:
    print("temperature is above boiling hot")
else:
    print("invalid temperature")