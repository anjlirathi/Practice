##Automatic File Shorter in File Explorer

import os, shutil

path = r"C:/Users/Anjli Rathi/Downloads/Softwares/Website Portfolio/Practice/Python/"
file_name = os.listdir(path)
folder_names = ['csv files', 'text files', 'image files']
for i in range(0,3):
    if not os.path.exists(path + folder_names[i]):
        #print(path + folder_names[i])
        os.makedirs(path + folder_names[i])

for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    
   
