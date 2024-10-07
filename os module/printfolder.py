import os
folders=os.listdir("man")# Displays all folder in list
# print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f"man/{folder}"))#displa all files inside folders
