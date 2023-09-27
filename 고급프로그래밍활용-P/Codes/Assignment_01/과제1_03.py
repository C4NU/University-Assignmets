price_dollar = float(input())
discount_price_dollar = float(input())

discounted_price_dollar = price_dollar - (price_dollar * discount_price_dollar / 100)

factor = 10 ** 2
original_price_rounded = int(price_dollar * factor + 0.5) / factor
discount_price_rounded = int((discounted_price_dollar) * factor + 0.5) / factor

print(f"Price(dollar): {original_price_rounded:.2f}, Discounted(dollar): {discount_price_rounded:.2f}")

usdkrw = 1325.82

price_won = price_dollar * usdkrw
discounted_price_won = discounted_price_dollar * usdkrw

factor = 1
original_price_in_won = int(price_won * factor + 0.5) / factor
discount_price_in_won = int((discounted_price_won) * factor + 0.5) / factor

print(f"Price(won): {int(original_price_in_won)}, Discounted(won): {int(discount_price_in_won)}")
