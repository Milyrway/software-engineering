def isValidNumber(string):
    return string.isdigit() and len(string) in [13, 15, 16]

def getCheckSum(string):
    checkSum = 0
    for i in reversed(range(0, len(string) - 1, 2)):
        doubled = int(string[i]) * 2
        if doubled > 9:
            checkSum += doubled - 9
        else:
            checkSum += doubled
    for i in reversed(range(1, len(string) + 1, 2)):
        checkSum += int(string[i])
    return checkSum

def getCardType(string):
    if len(string) in [13, 16] and string.startswith("4"):
        return "Visa"
    if len(string) == 15 and (string.startswith("34") or string.startswith("37")):
        return "American Express"
    if len(string) == 16 and string[0] == '5' and string[1] in '12345':
        return "Master Card"
    return "Invalid"

cardNumber = input("Введите номер банковской карты: ")
cardNumber = cardNumber.replace(" ", "")

if isValidNumber(cardNumber):
    if getCheckSum(cardNumber) % 10 == 0:
        print(getCardType(cardNumber))
    else:
        print("Invalid")
else:
    print("Invalid")
