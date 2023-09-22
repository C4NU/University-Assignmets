price_usd = float(input())
discount_percent = float(input())

usdkrw= 1325.82

print(f"Price(dollar): {price_usd}, Discounted(dollar): {price_usd - discount_percent}")
print(f"Price(won): {price_usd * usdkrw}, Discounted(won): {((price_usd - discount_percent)* usdkrw)}")