# Working with Paths using OS module

import os 

# Check the current working directory
get_cwd = os.getcwd()
print(f"The current working directory is: {get_cwd}")

# Change the directory to "/tmp"
os.chdir("/tmp")
new_current_directory = os.getcwd()
print(f"The current working directory after changing is: {new_current_directory}")

# Combine the path as a single path. Let's say that we have /etc, app, config.yml then after joining the path will be /etc/app/config.yml
joining_path = os.path.join("/etc", "apache2", "ports.conf")
print(f"The combining path is {joining_path}")

# Getting absolute path
os.chdir("/home/devx/Desktop/python-modules-for-devops-automation/os-module")
abs_path = os.path.abspath("working-with-paths.py")
print(f"The absolute path of working-with-paths.py is {abs_path}")

# Check if the path exists or not
if os.path.exists("/home/devx/Desktop/python-modules-for-devops-automation/os-module"):
    print("Path exists in the system")
else:
    print("Path doesn't exist in the system")

# Check if the given path is file or directory
is_file = os.path.isfile("/home/devx/Desktop/python-modules-for-devops-automation/os-module/working-with-paths.py")
if is_file:
    print(f"The given file is a file: {is_file}")
else:
    print(f"The given file is not an file: {is_file}")

is_dir = os.path.isdir("/home/devx/Desktop/python-modules-for-devops-automation/os-module")
if is_dir:
    print(f"The given dir is a dir: {is_dir}")
else:
    print(f"The given dir is not a dir: {is_dir}")