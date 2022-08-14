minute = int(input("Enter value from 1 to 60: "))
if minute <= 15:
    print("This minute is in the first quarter")
if minute > 15 and minute <= 30:
    print("This minute is in the second quarter")
if minute > 30 and minute <= 45:
    print("This minute is in the third quarter")
if minute > 45 and minute <= 60:
    print("This minute is in the fourth quarter")
else:
    print("Invalid value")