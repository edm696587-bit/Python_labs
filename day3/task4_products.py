import json

def run_task():
    products = input("Enter product names (comma-separated) as dryfood , mouse , notbook : ").split(',')
    prices = input("Enter product prices (comma-separated): 50 , 120 , 5 ").split(',')

    try:
        prices = [float(p.strip()) for p in prices]
    except ValueError:
        print("Invalid prices entered")
        return run_task()

    if len(products) != len(prices):
        print("Invalid number of prices entered.")
        
        return run_task()

    paired = zip(products, prices)
    filtered = filter(lambda x: x[1] > 0, paired)
    
    transformed = map(lambda x: {"product": x[0].strip(), "price": x[1], "discounted": x[1]*0.9}, filtered)

    result = list(transformed)
    
    with open("products.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Products saved to products.json. Preview:")
    print(result[:5])
