import csv
import random

def run_task():
    try:
        count = int(input("How many random numbers? "))
    except ValueError:
        print("Invalid number. Try again.")
        return run_task()

    numbers = [random.randint(1, 100) for _ in range(count)]
    with open("random_numbers.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "value"])
        for i, n in enumerate(numbers, start=1):
            writer.writerow([i, n])

    avg = sum(numbers) / len(numbers)
    print(f"Generated {count} numbers. Average: {avg:.2f}")
