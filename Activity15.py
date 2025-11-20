    # q = 'flint'
    # w = 'reiven'
    # e = 'aquino'

    # print("my name is", q, " ", w, "", e)
    # print(f"my name is {q}  {w}  {e}")


odd_sum = 0
for r in range(1, 11, 1):
    num = eval(input(f"{r}. Enter a number --> "))
    if num % 2 == 1:
        odd_sum += num
print(f"The sum of all the ODD numbers given is:", {odd_sum})