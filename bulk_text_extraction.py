import requests
import os
import sys
from tkinter import filedialog
from tkinter import *

# To package script as executable change directory in command line to python script and run:
# pyinstaller --console --onefile filename.py

# URL for text extraction
url_text_extraction = 'http://localhost:9998/tika'
# URL for metadata extraction in JSON format
url_metadata_extraction = 'http://localhost:9998/rmeta'

# Determines if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    tika_filepath = os.path.dirname(sys.executable)
elif __file__:
    tika_filepath = os.path.dirname(__file__)

# Running task manager and saving its output
task_manager_output = os.popen('wmic process get description, processid').read()

# Only open command prompt and run tika when not already running
if 'java.exe' not in task_manager_output:
    os.chdir(tika_filepath)
    os.system("start cmd /K java -jar tika-server-standard-2.8.0.jar")

# Opens file explorer and selects target path 
root = Tk()
root.withdraw()
directory = filedialog.askdirectory()

# Creates subfolder to store JSON files
text_files_folder = os.path.join(directory, 'output')
isExist = os.path.exists(text_files_folder)

# Creates output folder if it doesn't exist
if not isExist:
    os.mkdir(text_files_folder)
# Remove leftover files if running in same location
else:
    for file in os.listdir(text_files_folder):
        f = os.path.join(text_files_folder, file)
        if os.path.isfile(f):
            os.remove(f)

file_counter = 1
# Traverses folder with files that need text extraction
for filename in os.listdir(directory):

    f = os.path.join(directory, filename)
    # Checking if a file
    if os.path.isfile(f):

        # Extract text from files
        text_response = requests.request('PUT', url_text_extraction, data=open(f, 'rb'))
        text = str(text_response.text).replace(r"\r"," ").replace(r"\n"," ").replace(r"\r\n", " ").replace(r"\t"," ").replace(r"\s"," ").replace(r"\f", " ").replace('"', '').replace("  "," ").strip()

        filename_no_extension = filename.split('.')[0]
        text_files = os.path.join(text_files_folder, filename_no_extension)
        
        # Writes a text file for each file in folder
        with open(text_files + '.txt', 'w',encoding='utf-8',errors='replace') as write_text_file:
            write_text_file.write(text)
        write_text_file.close()

        printout = str(file_counter) + '. ' + filename
        print(printout)

        file_counter += 1