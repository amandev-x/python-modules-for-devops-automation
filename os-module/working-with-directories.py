import os 

# Create a directory name 'logs' in current working directory
# os.mkdir('/home/devx/Desktop/python-modules-for-devops-automation/os-module/logs')

# Create a nested directories: eg. mkdir -p /home/app/logs
# os.makedirs("logs/app/frontend", exist_ok=True)

# List file in a directories
file_list = os.listdir("/home/devx/Desktop")
print(file_list)

# Remove a file 
# os.remove("log.txt")

# Remove a dir 
# os.rmdir("logs")

# Rename a file
os.rename('log.txt', 'app-log.txt')