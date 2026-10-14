
def calculatePhoneGST(phone):
    return phone + (phone * 18 / 100)


def calculateAccessoriesGST(accessories):
    return accessories + (accessories * 12 / 100)


def totalBill(phone, accessories):
    return calculatePhoneGST(phone) + calculateAccessoriesGST(accessories)


def calculateDiscountedBill(phone, accessories):
    total = totalBill(phone, accessories)
    discount = total * 10 / 100
    return total - discount


# Predefined amounts
phone = 20000
accessories = 2000

phone_total = calculatePhoneGST(phone)
accessories_total = calculateAccessoriesGST(accessories)
total = totalBill(phone, accessories)
discount = total * 10 / 100
final_amount = calculateDiscountedBill(phone, accessories)

print(f"Phone after GST: ₹{phone_total:.2f}")
print(f"Accessories after GST: ₹{accessories_total:.2f}")
print(f"Total after GST: ₹{total:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final payable amount: ₹{final_amount:.2f}")
