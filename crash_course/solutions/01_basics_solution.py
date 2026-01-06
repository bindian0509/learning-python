"""
=============================================================================
SOLUTIONS - Module 01: Basics
=============================================================================
"""

print("=" * 50)
print("SOLUTIONS - Module 01: Basics")
print("=" * 50)

# Exercise 1: User Profile
print("\n--- Exercise 1: User Profile ---")
first_name = "John"
last_name = "Doe"
email = "john.doe@example.com"
age = 28
is_premium_user = True

print(f"""
User Profile:
  Name: {first_name} {last_name}
  Email: {email}
  Age: {age}
  Premium: {'Yes' if is_premium_user else 'No'}
""")


# Exercise 2: Temperature Converter
print("--- Exercise 2: Temperature Converter ---")
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")


# Exercise 3: String Manipulation
print("\n--- Exercise 3: String Manipulation ---")
messy_string = "  PyTHon ProGRAMming  "
clean_string = messy_string.strip().title()
print(f"Original: '{messy_string}'")
print(f"Cleaned: '{clean_string}'")


# Exercise 4: Calculate Discount
print("\n--- Exercise 4: Calculate Discount ---")
price = 99.99
discount_percent = 15
discount_amount = price * discount_percent / 100
final_price = price - discount_amount
print(f"Original: ${price:.2f}, Discount: {discount_percent}%, Final: ${final_price:.2f}")


# Exercise 5: Range Check
print("\n--- Exercise 5: Range Check ---")
number = 42
in_range = 1 <= number <= 100
print(f"Is {number} between 1 and 100? {in_range}")

# Test with other numbers
test_numbers = [0, 1, 50, 100, 101]
for num in test_numbers:
    print(f"  Is {num} in range? {1 <= num <= 100}")

