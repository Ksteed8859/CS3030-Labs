import re
import csv

error_pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]\s+(ERROR|WARNING|EMERGENCY):\s(.*)"

with open('../task1/sample.log', 'r') as log:
    data = log.read()

errors = re.findall(error_pattern, data)

csv_filename = "error_report.csv"
with open (csv_filename, 'w', newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(errors)