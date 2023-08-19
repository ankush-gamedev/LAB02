quantity_sold = int(input("Enter the quantity sold: "))
item_value = float(input("Enter the value of the item per unit: "))
discount_percentage = float(input("Enter the discount percentage: "))
tax_percentage = float(input("Enter the tax percentage: "))

total_value_before_discount = quantity_sold * item_value

discount_amount = (discount_percentage / 100) * total_value_before_discount

total_value_after_discount = total_value_before_discount - discount_amount

tax_amount = (tax_percentage / 100) * total_value_after_discount

bill_amount = total_value_after_discount + tax_amount

print(f"Bill Amount: {bill_amount} rupees")
