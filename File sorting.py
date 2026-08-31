import os
import collections

#find downloads folder
#usually the file path is just user download
downloads_path = os.path.join(
    os.path.expanduser("~"),
    'Downloads'
)
#downloads_path = os.path.normpath(D:/.......) if it's in a different drive

#file to folder depending on file type
file_mappings = collections.defaultdict()
for filename in os.listdir(downloads_path):
    file_type = filename.split(".")[-1] #the file type is the final part of the file name after the last .
    file_mappings.setdefault(file_type, []).append(filename)

#move files into their folders
for folder_name, folder_items in file_mappings.items():
    folder_path = os.path.join(downloads_path, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path) #creates folder if path doesnt exist

    for folder_item in folder_items:
        source = os.path.join(downloads_path, folder_item)
        destination = os.path.join(folder_path, folder_items)
        print(f"Moving {source} to {destination}")
        os.rename(source, destination)