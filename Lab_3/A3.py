prev = int(input("Предыдущее показание: "))
curr = int(input("Текущее показание: "))

if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

if used <= 300:
    total = 21.0
elif used <= 600:
    total = 21.0 + (used - 300) * 0.06
elif used <= 800:
    total = 21.0 + 300 * 0.06 + (used - 600) * 0.04
else:
    total = 21.0 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

avg_price = total / used if used > 0 else 0

print("Предыдущее Текущее Использовано К оплате Ср. цена m^3")
print(f"{prev:<10} {curr:<7} {used:<12} {total:.2f}     {avg_price:.2f}")