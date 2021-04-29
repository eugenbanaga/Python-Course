from exchange.functions import convert_leu
value = float(input("How many lei?: "))
currency = input("Convert to: ")

value_converted = convert_leu(to=currency, value=value)
if value_converted == -1:
    print("Cannot convert leu to " + currency)
else:
    print(str(value) + " leu = " + str(value_converted) + "" + currency)