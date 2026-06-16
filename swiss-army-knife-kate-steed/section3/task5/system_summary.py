import subprocess
import re

user_logins = subprocess.run(["last", "-15"], capture_output=True, text=True)

summary_pattern = r"(\d.\d.\d{2}.\d-\w*)\s(\w*\s\w*\s*\d*)\s(\d{2}:\d{2})(?:\s-\s(\d{2}:\d{2})|\s*(still running))"

print(
    f"{'Device Name':<22} {'Date':<10} {'Log On':<8} {'Log Off':<15}"
)
print("-" * 70)

summary_data = re.findall(summary_pattern, user_logins.stdout)

for device, date, start_time, end_time, status in summary_data:
    is_logged_off = end_time if end_time else status
    
    print(
    f"{device:<22} {date:<10} {start_time:<8} {is_logged_off:<15}"
    )