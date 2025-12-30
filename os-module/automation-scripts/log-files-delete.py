# A python script to delete log file older than 7 days. This script will be scheduled to run every day at 12:00 AM.
import os
import datetime
import logging

def cleanup_old_logs(log_dir, days_old=7):
    # Step 1: Check if the given directory exists and is a directory
    print("Checking if the given directory exists or not....")
    os.system("sleep 2")
    try:
        if os.path.exists(log_dir) and os.path.isdir(log_dir):
            # Check if the directory is empty or not
            if not os.listdir(log_dir):
                print("Directory is empty")
                return 0
            print("Given directory exists and is a directory")
        else:
          print("Directory does not exists or maybe it is not a directory but a file")
          return 
    except Exception as e:
        print(f"Error: {e}")
        return 


    # Step 3: Get the current date and time
    print("Getting the current date and time...")
    os.system("sleep 1")
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")

    # Step 4: Iterate over the files in the directory and delete the files older than 7 days
    print("Iterating over the files in the directory and deleting the files older than 7 days...")
    os.system("sleep 1")
    for file in os.listdir(log_dir):
        file_path = os.path.join(log_dir, file)
        if os.path.isfile(file_path):
          try:
            file_mtime = os.path.getmtime(file_path)  # Get the last modified time of the file
            file_modfified_time = datetime.datetime.fromtimestamp(file_mtime)  # Convert the last modified time to a datetime object because the file_mtime is in seconds since the EPOCH
            if (current_date - file_modfified_time).days > days_old:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
                os.system("sleep 0.5")
            else:
                print(f"File is not older than 7 days: {file_path}")
                os.system("sleep 0.5")
                continue 
          except Exception as e:
             print(f"Error: {e}")
             continue
            

cleanup_old_logs("/home/devx/Desktop/python-modules-for-devops-automation/os-module/automation-scripts")