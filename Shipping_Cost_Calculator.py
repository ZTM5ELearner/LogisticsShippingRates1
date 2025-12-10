# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
currency = input("Enter the currency (e.g., USD, EUR, GBP): ").strip().upper()
rate = float(input(f"Enter the shipping rate per kilogram in {currency}: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} {currency}")
