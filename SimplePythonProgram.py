# This is a sample Python script.
""""
#Celcius --> Farenheit
cel = input("celcuius : ")
cel = float(cel)

far = (cel * 9/5) + 32
print("Farenheit : " , far)


#Farenheit --> Celcius
far = input("Farenheit : ")
far = float(far)

cel = (far - 32) * 5/9
print("Celcius : " , cel)


# Simple Interest Formula Calculation
# Formula = Simple Interest = ( Principal * No of Months * Interest Rate(%) ) / 100
PrincipalAmt = input("Enter the Principal Amount for the Loan: ")
PrincipalAmt = int(PrincipalAmt)
NoOfMonths = input("Enter the Time period in years: ")
NoOfMonths = int(NoOfMonths)
InterestRate = input("Enter the interest rate in %: ")
InterestRate = int(InterestRate)

SimpleInterest = (PrincipalAmt * NoOfMonths * InterestRate) / 100
print(SimpleInterest)
"""

print(max(1,2,3,4,5))
print(min(10,20,44,1,43))
print(abs(-44322))
print(pow(2,4))
