original_price = float(input())
discount_price = float(input())

discount_price_result = original_price - discount_price

print(original_price)
print(discount_price_result)

factor = 10 ** 2
original_price_rounded = int(original_price * factor + 0.5) / factor
discount_price_rounded = int((discount_price_result) * factor + 0.5) / factor

print(f"Price(dollar): {original_price_rounded:.2f}, Discounted(dollar): {discount_price_rounded:.2f}")

exchange_rate = 1325.82
price_in_won = original_price * exchange_rate
discounted_in_won = discount_price_result * exchange_rate

factor = 1
original_price_in_won = int(price_in_won * factor + 0.5) / factor
discount_price_in_won = int((discounted_in_won) * factor + 0.5) / factor

print(f"Price(won): {int(original_price_in_won)}, Discounted(won): {int(discount_price_in_won)}")
