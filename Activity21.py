clean = True

while clean == True:
    choice = input("do you wish to continue cleaning? (yes/no): ").lower()

    if choice  == 'yes':
        print("continue looping")
        continue
    elif choice == 'no':
        print("loop stops")
        break
    else:
        print("invalid choice")
        continue