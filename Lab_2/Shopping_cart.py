products = [
    {"name": input("Enter product name: "), "price": float(input("Enter product price: ")), "quantity": float(input("Enter quantity: "))},
    {"name": input("Enter product name: "), "price": float(input("Enter product price: ")), "quantity": float(input("Enter quantity: "))},
    {"name": input("Enter product name: "), "price": float(input("Enter product price: ")), "quantity": float(input("Enter quantity: "))},
    {"name": input("Enter product name: "), "price": float(input("Enter product price: ")), "quantity": float(input("Enter quantity: "))}
    ]

total = 0

for product in products:
    quantity = product["quantity"]
    price = product["price"]
    cost = price * quantity
    total += cost


def apply_discount(total):
    if total >= 2000:
        return total - (total * 0.10)
    else:
        return total

final_cost = apply_discount(total)

print("\nTotal cost: ", total)
print("Final cost: ", final_cost)