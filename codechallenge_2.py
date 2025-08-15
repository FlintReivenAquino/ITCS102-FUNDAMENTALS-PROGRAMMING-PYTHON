flint = eval(input("Enter amount to deposit: "))

p = flint // 1000
flint = flint % 1000

o = flint // 500
flint = flint % 500

i = flint // 200
flint = flint % 200

u = flint // 100
flint = flint % 100

y = flint // 50
flint = flint % 50

t = flint // 20
flint = flint % 20

r = flint // 10
flint = flint % 10

e = flint // 5
flint = flint % 5

w = flint // 1
flint = flint % 1

print("Count", p, "= ₱1000")
print("Count", o, "= ₱500")
print("Count", i, "= ₱200")
print("Count", u, "= ₱100")
print("Count", y, "= ₱50")
print("Count", t, "= ₱20")
print("Count", r, "= ₱10")
print("Count", e, "= ₱5")
print("Count", w, "= ₱1")