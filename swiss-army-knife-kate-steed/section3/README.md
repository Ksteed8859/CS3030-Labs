# Section 3 Regex Patterns

## Task 1

- r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

This pattern was used in task 1 to find IP addresses within a sample log file. This pattern will only pull out valid IP addresses, with the max value it looks for being 255.255.255.255.

- r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]"

This pattern was used to find the timestamps of each message in the sample log. It looks for dates formatted YYYY-MM-DD HR-MI, and only looks for numerical values. Another thing to note is that it is specifically looking for these values inside brackets; if the timestamp is not within the brackets, it goes ignored.

## Task 2

- \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]\s+(ERROR|WARNING|EMERGENCY):\s(.*)

This pattern is used to isolate the ERROR messages in the log file and then capture the timestamp, ERROR type, and message. This looks for three warning types: ERROR, WARNING, or EMERGENCY.

## Task 5

- (\d.\d.\d{2}.\d-\w*)\s(\w*\s\w*\s*\d*)\s(\d{2}:\d{2})(?:\s-\s(\d{2}:\d{2})|\s*(still running))

This pattern is used to isolate specific data from the last system command and the people who logged on. Since the command gives quite a bit of data, this regex only pulls the device name, date, time of log on, and time of log off OR returns "still running" if the user hasn't logged off yet.