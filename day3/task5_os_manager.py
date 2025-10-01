import os

def run_task():
    path = input("Enter a directory path: ")
    if not os.path.isdir(path):
        print("Invalid path. Try again.")
        return run_task()

    backup_path = os.path.join(path, "backup")
    os.makedirs(backup_path, exist_ok=True)

    count = 0
    for file in os.listdir(path):
        if file.endswith(".txt"):
            
            src_file = os.path.join(path, file)
            dst_file = os.path.join(backup_path, file)

            with open(src_file, "rb") as fsrc, open(dst_file, "wb") as fdst:
                fdst.write(fsrc.read())

            count += 1

    print(f"Copied {count} .txt files to backup/")
