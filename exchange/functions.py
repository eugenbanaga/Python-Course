from exchange.constants import CURRENCIES_LEU

def convert_leu(to, value):
    currency = CURRENCIES_LEU.get(to, None)
    if currency is None:
        return -1
    return float("%.2f" % (value * currency["rate"]))
