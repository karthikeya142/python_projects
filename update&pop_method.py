prices = {"iphone": 760, "vivo": 1000, "samsng": 2000}
new_prices = {"iphone": 15000, "redmi": 1200, "imac": 16000}
prices.update(new_prices)
print(prices)
a = prices.pop("vivo")
print(f" using pop method {a}")

print(f"using values method {prices.values()}")
print(f'using key method {prices.keys()}')
print(f"using items method {prices.items()}")
