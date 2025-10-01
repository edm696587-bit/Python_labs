import re
from task7_decorators import log_time

@log_time
def run_task():
    logs = [
        "user1@example.com ",
        "asdfgnhgfds",
        "user2@test.org ",
        "asdfg",
        "user3@domain.com ",
        "test@test.com",
        "bad request",
        "mohamed@eid.com",
        "bad@@email",
        "two.m.com"
    ]
    with open("access.log", "w") as f:
        f.write("\n".join(logs))

    with open("access.log", "r") as f:
        data = f.read()

    emails = set(re.findall(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}", data))

    with open("valid_emails.txt", "w") as f:
        f.write("\n".join(emails))

    print(f"Found {len(emails)} unique and valid emails.")
