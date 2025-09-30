import os

cwd = os.getcwd()
def getfolder(path):
    return os.path.join(cwd, path)

def getAllFiles(folder):
    files_list = []
    for entry in os.listdir(folder):
        full_path = os.path.join(folder, entry)
        if os.path.isfile(full_path):
            files_list.append(full_path)
        elif os.path.isdir(full_path):
            files_list.extend(getAllFiles(full_path))
    return files_list



def generateSessionID():
    subset = "123456789qwertyuiopasdfghjklzxcvbnm"
    length = 5
    id = ""
    for i in range(length):
        id += subset[os.urandom(1)[0] % len(subset)]
    return str(id)

