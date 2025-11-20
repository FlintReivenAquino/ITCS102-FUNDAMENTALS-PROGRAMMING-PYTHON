months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug"]


months.append("sept")
print(months)

months.pop()
print(months)

months.remove("jun")
print(months)

months.insert(4, "new")
print(months)

length = len(months)
print("Length of list:", length)

months.sort()
print("Sorted list:", months)

for m in months:
    print(f"{m}, 2025")

fullname = 'aquino flint reiven c'

print(fullname[::-1])