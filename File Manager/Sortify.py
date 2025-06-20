import os
import shutil
from datetime import datetime

file_types={
    'Image':['.jpg','.jpeg','.png','.gif'],
    'Videos':['.mp4','.mkv','.flv'],
    'Documents':['.txt','.pdf','.txt','.docx'],
    'Audios':['.mp3','.wav'],
    'Spreadsheets':['.xlsx','.xls','.csv'],
    'Archives':['.zip','.tar','.rar'],
    'Codes':['.py','.html','.css','.cpp','.c','.js','.jsx']
}

source_folder=input("Enter the full path of the folder to organize: ").strip()
log_file_path=os.path.join(source_folder,"organizer_log.txt")

def create_folders():
    for folder in file_types:
        folder_path=os.path.join(source_folder,folder)
        if not  os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    others_path=os.path.join(source_folder,"Others")
    if not os.path.exists(others_path):
        os.makedirs(others_path)

def log_action(action):
    with open(log_file_path,"a") as log_file:
        log_file.write(f"{datetime.now()}-{action}\n")

def organizing_folders():
    for filename in os.listdir(source_folder):
        if filename=="organizer_log.txt":
            continue
        file_path=os.path.join(source_folder,filename)

        if os.path.isdir(file_path):
            continue

        file_ext=os.path.splitext(filename)[1].lower()

        moved=False
        for folder,extensions in file_types.items():
            if file_ext in extensions:
                target_folder=os.path.join(source_folder,folder)
                shutil.move(file_path,target_folder)
                log_action(f"Moved {filename} to {folder}")
                print(f"Moved {filename} to {folder}")
                moved=True
                break

        if not moved:
            print(f"Moved'{filename} to 'Others'(unknown extension)")
            log_action(f"Moved'{filename} to 'Others'(unknown extension)")
            
            
create_folders()
organizing_folders()
print(f"\n✅Organizing complete.\nLog saved to:{log_file_path}")  