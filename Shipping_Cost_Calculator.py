# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
while True:
    try:
        weight = float(input("Enter the package weight in kilograms: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value for the package weight.")

while True:
    try:
        rate = float(input("Enter the shipping rate per kilogram: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value for the shipping rate.")
## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} {currency}")
