print("Welcome to the bill calculator version 1.00\n");
total_bill=float(input("How much is the total of your bill ?\n"));
print(f"Your bill is {total_bill}\n");
tips=int(input("What is the percentage would you like to pay for tips? 10% 12% or 15%\n"));
print(f"You want to pay {tips} perccent for tips.\n");
num_of_people=int(input("How many people to split the bill?\n"));
print(f"You have {num_of_people} of people.\n");
bill_split=total_bill*(1 + tips / 100) / num_of_people;
bill_split_2decimal=round(bill_split, 2);
# bill_split_in_2decimal=round(bill_split, 2);
print(f"Each person should pay {bill_split_2decimal}.\n");


