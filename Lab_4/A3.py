packets = input("Введите строку из 0 и 1: ")

if len(packets) < 5:
    print("Ошибка: длина строки должна быть не меньше 5.")
elif not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    total_packets = len(packets)
    lost_packets = packets.count('0')
    
    max_lost_seq = 0
    current_seq = 0
    for char in packets:
        if char == '0':
            current_seq += 1
            if current_seq > max_lost_seq:
                max_lost_seq = current_seq
        else:
            current_seq = 0
            
    loss_percent = (lost_packets / total_packets) * 100 if total_packets > 0 else 0
    
    if loss_percent <= 1:
        quality = "отличное"
    elif loss_percent <= 5:
        quality = "хорошее качество"
    elif loss_percent <= 10:
        quality = "удовлетворительное качество"
    elif loss_percent <= 20:
        quality = "плохое качество"
    else:
        quality = "критическое состояние сети"

    print(f"Общее количество пакетов: {total_packets}")
    print(f"Количество потерянных пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_lost_seq}")
    print(f"Процент потерь: {loss_percent:.1f}%")
    print(f"Качество связи: {quality}")