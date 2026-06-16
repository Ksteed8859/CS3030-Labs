import re

ip_pattern = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
timestamp_pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]"

with open('./sample.log', 'r') as log:
    data = log.read()

ip_addresses = re.findall(ip_pattern, data)
timestamps = re.findall(timestamp_pattern, data)

print("IP ADDRESSES")
for match in ip_addresses:
    print(match)
print("TIMESTAMPS")
for match in timestamps:
    print(match)

