eggs_count = input("Enter eggs count:")
eggs_count = int(eggs_count)

flour_in_grams = eggs_count * 200

print(f"You need {eggs_count * 200}g of flour")
print(f"You need {flour_in_grams * 2}ml of water")
print(f"You need {int(flour_in_grams / 400)} g of vanilla")
print(f"You need {int(flour_in_grams / 300)} apples")