
def calculateVegetablesGST(vegetables):
    return vegetables + (vegetables * 5 / 100)


def calculateFruitsGST(fruits):
    return fruits + (fruits * 5 / 100)


def calculateGroceriesGST(groceries):
    return groceries + (groceries * 5 / 100)


def totalBill(vegetables, fruits, groceries):
    return (
        calculateVegetablesGST(vegetables)
        + calculateFruitsGST(fruits)
        + calculateGroceriesGST(groceries)
    )


def calculateDiscountedBill(vegetables, fruits, groceries):
    total = totalBill(vegetables, fruits, groceries)
    discount = total * 10 / 100
    return total - discount


# Predefined amounts
vegetables = 500
fruits = 300
groceries = 1200

vegetables_total = calculateVegetablesGST(vegetables)
fruits_total = calculateFruitsGST(fruits)
groceries_total = calculateGroceriesGST(groceries)
total = totalBill(vegetables, fruits, groceries)
discount = total * 10 / 100
final_amount = calculateDiscountedBill(
    vegetables, fruits, groceries
)

print(f"Vegetables after GST: ₹{vegetables_total:.2f}")
print(f"Fruits after GST: ₹{fruits_total:.2f}")
print(f"Groceries after GST: ₹{groceries_total:.2f}")
print(f"Total after GST: ₹{total:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final payable amount: ₹{final_amount:.2f}")
