print("Welcome to the tip calculator")
total_bil = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill"))

result = (total_bil * (tip / 100 + 1)) / people
print(f"Each person should pay: ${round(result, 2)}")
