principal = float(input("Enter Principle "))
roi = float(input("Enter ROI %: "))
time = float(input("Enter time period "))

simple_interest = (principal * roi * time) / 100

print(f"The simple interest is: {simple_interest}")
