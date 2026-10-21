x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
    if (x1 + y1) % 2 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")