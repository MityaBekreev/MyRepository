import json


def calculate_product_sum_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        product_sum = sum(entry['score'] * entry['weight'] for entry in data)
        return round(product_sum, 3)


file = "input.json"
result = calculate_product_sum_from_json(file)
print(result)
