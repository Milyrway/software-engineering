def draw_rectangle(rows, columns):
    print(f"\nПРЯМОУГОЛЬНИК {rows}x{columns}:")
    for i in range(rows):
        for j in range(columns):
            print("#", end="")
        print()

def draw_right_triangle(n):
    print(f"\nПРАВЫЙ ТРЕУГОЛЬНИК:")
    for i in range(1, n + 1):
        for j in range(i):
            print("#", end="")
        print()

def draw_frame(rows, columns):
    print(f"\nРАМКА {rows}x{columns}:")
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()

n = int(input("Введите высоту (n): "))
m = int(input("Введите ширину (m): "))

draw_rectangle(n, m)
draw_right_triangle(n)
draw_frame(n, m)