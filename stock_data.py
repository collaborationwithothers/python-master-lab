from datetime import datetime, timedelta
import itertools

def generate_stock_data():
    """Generate 100,000 days of stock data and write to a CSV file."""
    base_price = 100.0
    start_date = datetime(2020, 1, 1)
    for i in range(100000):
        date = start_date + timedelta(days=i)
        price = base_price + (i * 0.1)  # Simulate a gradual increase in stock price
        volume = 1000 + (i * 5)  # Simulate a gradual increase in volume
        yield f"{date.strftime('%Y-%m-%d')},{price:.2f},{volume}\n"

with open("stock_data.csv", mode="w") as file:
    for line in generate_stock_data():
        file.write(line)

print("Stock data generation complete. Data written to 'stock_data.csv'.")

def days_price_greater_than(threshold):
    """Generator that yields days where the stock price is greater than the given threshold."""
    with open("stock_data.csv", mode="r") as file:
        next(file)  # Skip header if present
        lines = (line.strip() for line in file)
        parsed = (line.split(",") for line in lines)
        high_price = ((date, float(price)) for date, price, volume in parsed if float(price) > threshold)
        yield from high_price

days_above_150 = days_price_greater_than(150.0)
print("Days with stock price greater than $150:")
for date, price in itertools.islice(days_above_150, 10):  # Limit to first 10 results for demonstration
    print(f"Date: {date}, Price: ${price:.2f}")
print(f"Found {sum(1 for _ in days_above_150)} days with stock price greater than $150.")
