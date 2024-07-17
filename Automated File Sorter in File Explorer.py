import os , shutil
path = r"C:/Users/MOHAMED/Downloads/test/"
file_name = os.listdir(path)
os.path.exists(path + 'csv files')
folder_names = ['csv files' , 'jpg files' , 'pdf files', "jpeg files","docx files", "xlsx files"]
for loop in range(6):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))

for file in file_name:
    if ".jpeg" in file and not  os.path.exists(path + "jpeg files/" + file):
        shutil.move(path + file,path + "jpeg files/" + file)
    elif ".csv" in file and not  os.path.exists(path + "csv files/" + file):
        shutil.move(path + file,path + "csv files/" + file)
    elif ".jpg" in file and not  os.path.exists(path + "jpg files/" + file):
        shutil.move(path + file,path + "jpg files/" + file)
    elif ".docx" in file and not  os.path.exists(path + "docx files/" + file):
        shutil.move(path + file,path + "docx files/" + file)
    elif ".xlsx" in file and not  os.path.exists(path + "xlsx files/" + file):
        shutil.move(path + file,path + "xlsx files/" + file)
    elif ".pdf" in file and not  os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file,path + "pdf files/" + file)

