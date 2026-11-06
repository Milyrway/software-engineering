x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

if x1 > 0 and y1 > 0: q1 = 1
elif x1 < 0 and y1 > 0: q1 = 2
elif x1 < 0 and y1 < 0: q1 = 3
else: q1 = 4

if x2 > 0 and y2 > 0: q2 = 1
elif x2 < 0 and y2 > 0: q2 = 2
elif x2 < 0 and y2 < 0: q2 = 3
else: q2 = 4

if q1 == q2:
    print(f"Yes, {q1}")
else:
    print("No")