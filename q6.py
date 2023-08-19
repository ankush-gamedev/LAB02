principal = float(input("Enter Principle "))
annual_interest_rate = float(input("Enter annual ROI % "))
compounding_frequency = int(input("Enter the number of times interest is compounded per year: "))
years = float(input("Enter the number of years: "))

rate = annual_interest_rate / 100

compound_interest = principal * (1 + rate/compounding_frequency)**(compounding_frequency*years) - principal

print(f"The compound interest is: {compound_interest}")
