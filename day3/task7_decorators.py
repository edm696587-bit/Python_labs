import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)
        end = time.time()
        
        with open("execution_log.txt", "a") as f:
            f.write(f"{func.__name__} executed in {end - start:.4f} seconds\n")
        return result
    return wrapper


@log_time
def math_task():
    total = sum(i * i for i in range(1, 1000000))
    return total


@log_time
def regex_task():
    import re
    data = "test@example.com some text hello@world.org"
    return re.findall(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}", data)

def run_task():
    print("Running math_task...")
    print("Result:", math_task())

    print("Running regex_task...")
    print("Result:", regex_task())

    print("\nCheck 'execution_log.txt' for execution logs.")


if __name__ == "__main__":
    run_task()