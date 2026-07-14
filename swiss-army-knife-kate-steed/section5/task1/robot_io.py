missing_file = './missing_file.txt'

try:

# Read the File
    with open(missing_file, "r", encoding="utf-8") as file:
        content = file.read()
# Modify file
    new_content = content + "Hello World!"
# Write new content to file
    with open(missing_file, "w", encoding="utf-8") as file:
        file.write(new_content)

except FileNotFoundError:
    print(f"ERROR: The file {missing_file} does not exist or has been moved.")

except PermissionError:
    print(f"ERROR: The current OS user does not have permission to access {missing_file}.")

except Exception:
    print("ERROR: Something went wrong :(")

finally:
    print("Operation Attempted")