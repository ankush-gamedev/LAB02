n = int(input("Enter a positive integer n: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print(f"The sum of the first {n} natural numbers is: {sum}")
