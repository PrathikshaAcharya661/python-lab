principle=int(input("Enter the principle amount:"))
interest_rate=int(input("Enter the interest rate:"))
time=int(input("Enter the time in year:"))
simple_interest=(principle*interest_rate*time)/100
total_amount= principle + simple_interest
print("simple interest:", simple_interest)
print("total amount:", total_amount)