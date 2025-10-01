from datetime import datetime

def run_task():
    date_str = input("Enter a date like 2025-5-19 : in the future ")
    try:
        target = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date it must be like 2002-11-28. Try again.")
        return run_task()

    today = datetime.today().date()
    delta = (target - today).days

    if delta < 0:
        print("This date has already passed.")
    else:
        with open("reminders.txt", "a") as f:
            f.write(f"{date_str} -> {delta} days left\n")
        print(f"Reminder saved: {date_str} -> {delta} days left")
