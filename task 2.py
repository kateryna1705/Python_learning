hen = int(input("Enter the number of hens: "))
cow = int(input("Enter the number of cows: "))
pig = int(input("Enter the number of pigs: "))

hen_legs = hen * 2
cow_legs = cow * 4
pig_legs = pig * 4
total_n_of_legs = hen_legs + cow_legs + pig_legs

print("The total number of legs in the farm is ", total_n_of_legs)