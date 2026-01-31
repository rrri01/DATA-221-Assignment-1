threshold = 100
product = 1
current = 1

while product < threshold:
    product = product * current
    current += 1 # this updates the current number

print(f"The final product is: {product}")
print(f"The integer that caused the product to reach the threshold: {current}")
