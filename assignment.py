#1. Question 1;

def calculate_discount(price, discount_percent):
    #Calculates the final price after applying a discount if it's 20% or higher.
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price  # No discount applied if less than 20%

print(calculate_discount(100, 25))

#2. Question 2;
def calculate_discount(price, discount_percent):
    #Calculates the final price after applying a discount if it's 20% or higher.
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price  # No discount applied if less than 20%

# Get user input
price = float(input("Enter the original price:"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Display the result
print(f"Final price: {final_price:.2f}")