file_path = "../task1/sample.log"
keyword = "EMERGENCY"

def generator(file_path, keyword):
    with open(file_path, 'r') as log:
        for line in log:
            if keyword in line:
                yield line


# yield is safer for businesses handling large amounts of data because yield has a limit to the amount of data it loads in at once, while
# f.read() does not. Say a company is handling a log with 10GB of data, but their machine only has 8GB of free space available. If the company
# were to load the data using f.read(), it would load all 10GB at once and crash the program due to a lack of memory. Yield will only load a 
# limited amount of data at a time. This prevents too much memory from being used, allowing the machine to safely process large amounts of data.
