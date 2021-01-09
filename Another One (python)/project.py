import shutil
import os
path = "C:/Users/Asus/Downloads"
isexists = os.path.exists(path)
print(isexists)
source = "Anything.txt"
destination = "Anithing/anithing1.txt"
dest = shutil.copy(source,destination)
print("done")