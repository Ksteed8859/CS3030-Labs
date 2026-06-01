import pathlib

target_directory = '.'
for file_path in pathlib.Path(target_directory).rglob("*.tmp"):
    print("Found junk: ", file_path)
