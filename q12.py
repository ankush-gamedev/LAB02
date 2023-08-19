coins_10 = int(input("Enter the number of 10-rupee coins: "))
coins_5 = int(input("Enter the number of 5-rupee coins: "))
coins_2 = int(input("Enter the number of 2-rupee coins: "))
coins_1 = int(input("Enter the number of 1-rupee coins: "))

total_amount = (coins_10 * 10) + (coins_5 * 5) + (coins_2 * 2) + coins_1

print(f"The total amount in the piggy bank is: {total_amount} rupees")
