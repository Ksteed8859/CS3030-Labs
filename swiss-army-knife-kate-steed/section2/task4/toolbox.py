import pathlib
import argparse



parser = argparse.ArgumentParser(
        prog="Toolbox",
        description="An upgraded version of Task 1 using argparse to accept arguments directly from the command line using flags."
)

parser.add_argument(
        '--path',
        type=str,
        help="The directory path you want to scan.",
        required=True
        )
    
parser.add_argument(
        '--ext',
        type=str,
        help="The file extension you want to search for, eg., .txt, .py, .tmp",
        required=True
    )

args = parser.parse_args()

target_directory = args.path
file_ext = args.ext

for file_path in pathlib.Path(target_directory).rglob(f"*{file_ext}"):
    print("File Found: ", file_path)
