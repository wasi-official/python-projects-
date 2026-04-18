# Log Analyzer — Read log file, count and display INFO/ERROR/WARNING
log = []

def read_file(log):
    try:
        with open("log.txt", "r") as file:
            for line in file:
                logs, data = line.strip().split(":", 1)
                log.append((logs, data))
    except FileNotFoundError:
        print("No data found")

def show_messages(log):
    for logs, data in log:
        print(f"[{logs}] {data}")

def summary(log):
    error = 0
    info = 0
    warning = 0
    for logs, data in log:
        if logs == "INFO":
            info += 1
        elif logs == "ERROR":
            error += 1
        elif logs == "WARNING":
            warning += 1
    print(f"Total logs: {error + info + warning}")
    print(f"ERROR logs: {error}")
    print(f"WARNING logs: {warning}")
    print(f"INFO logs: {info}")

read_file(log)
show_messages(log)
summary(log)