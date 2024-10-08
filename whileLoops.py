#Compound Interest Calculator

principle = 0
time = 0 #In years
rate = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))

    if principle <= 0:
        print("Principle can not be less than or equal to 0. ")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))

    if rate <= 0:
        print("Interest rate can not be less than or equal to 0. ")

while time <= 0:
    time = int(input("Enter the time in years: "))

    if time <= 0:
        print("Time can not be less than or equal to 0. ")


print(principle)
print(rate)
print(time)


total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} years is ${total:.2f}")
