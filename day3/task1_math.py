import math
from task7_decorators import log_time

@log_time
def run_task():
    numbers = input("Enter numbers (comma-separated): ").split(',')
    try:
        numbers = [float(n.strip()) for n in numbers]
    except ValueError:
        print("Invalid input. Enter only numbers.")
        return run_task()

    with open("math_report.txt", "w") as f:
        for n in numbers:
            f.write(f"Number: {n}\n")
            f.write(f"Floor: {math.floor(n)}\n")
            f.write(f"Ceil: {math.ceil(n)}\n")
            f.write(f"Square root: {math.sqrt(n)}\n")
            f.write(f"Area of circle: {math.pi * n**2}\n")
            f.write("_"*20 + "\n")

    print("math_report.txt created, and contains : ")
    with open("math_report.txt", "r") as f:
        print(f.read())
