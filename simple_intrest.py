#SI = PRINCIPLE * NUMBER OF YEARS * RATE OF INTREST / 100

principle = int(input("Enter the Amount Borrowed: "))
years = int(input("Enter the  period in Years: "))
rate = int(input("Enter the Rate of Intrest: "))


interest    = principle * years * rate / 100

#print(" simple Interest on the principle amount ₹ "+ str(principle) +" For a period of time "+str(years)+" Years at the rate of "+str(rate)+" % is "+ str(interest))

print(f" simple Interest on the principle amount ₹ {principle}  For a period of time {years} Years at the rate of {rate}  % is {interest}")
