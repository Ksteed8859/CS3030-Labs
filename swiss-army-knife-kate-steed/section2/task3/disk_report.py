import subprocess

disk_results = subprocess.run(["df", "-h"], capture_output=True, text=True)

for line in disk_results.stdout.splitlines():
    if " / " in line or " /mnt/c" in line:
        print(line)
