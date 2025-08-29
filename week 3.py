def calculate_discount(price, discount_percent):
    """Calculate final price after discount if >= 20%"""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price   # no discount applied

# Prompt user
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Print results
if discount_percent >= 20:
    print(f"Original Price: {price}")
    print(f"Discount: {discount_percent}%")
    print(f"Final Price after discount: {final_price}")
else:
    print(f"No discount applied. The price remains: {price}")