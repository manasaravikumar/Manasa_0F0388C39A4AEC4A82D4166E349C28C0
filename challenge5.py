
def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ['apple', 'banana', 'orange', 'apple', 'banana', 'orange']
target_product = 'apple'
result = linear_search_product(products, target_product)
print(result)
