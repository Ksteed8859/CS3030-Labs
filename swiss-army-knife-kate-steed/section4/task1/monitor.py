import psutil
import time # for task 5

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

while True:

    cpu_usage = psutil.cpu_percent(interval=1)
    available_ram = psutil.virtual_memory().available / (1024 ** 3)
    disk_usage = psutil.disk_usage('/').percent

    if cpu_usage > 80 or available_ram < 1:
        print(f"{RED}WARNING{RESET}")
    else:
        print(f"{GREEN}System Normal{RESET}")

    time.sleep(60)