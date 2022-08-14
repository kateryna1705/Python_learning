minute = int(input("Enter value from 0 to 59: "))
if minute <= 14:
    print("This minute is in the first quarter")
if minute > 14 and minute <= 29:
    print("This minute is in the second quarter")
if minute > 29 and minute <= 44:
    print("This minute is in the third quarter")
if minute > 44 and minute <= 59:
    print("This minute is in the fourth quarter")
else:
    print("Invalid value")
