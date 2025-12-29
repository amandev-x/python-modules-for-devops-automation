import os, subprocess

# Execute a system command to list files in the current directory
os.system("ls -l")

# Get a command output using subprocess
result = subprocess.run(["df", "-h"], capture_output=True, text=True)
print(f"Disk space usage:\n{result.stdout}")

# Get file stat
file_stat = os.stat("working-with-system-commands.py")
print(f"File Size: {file_stat.st_size} bytes")
print(f"Last modified time: {file_stat.st_mtime}")
