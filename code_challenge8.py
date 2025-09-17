print("MULTIPLICATION TABLE MAKER")

num = eval(input("Enter a number: "))

print("The Multiplication Table For", number, ":")

for i in range(1, 11):
    result = num * i
    print(num, "x" , i , "=" , result ,)