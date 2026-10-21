n = int(input("Секунд с начала суток: "))
n = n % 86400
hours = n // 3600
minutes = (n % 3600) // 60
seconds = n % 60
print(f"{hours}:{minutes:02d}:{seconds:02d}")