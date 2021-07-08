import os

path = "pictures/"
dirs = os.listdir(path)
for file in dirs:
    os.remove("pictures/"+file)

open("number.txt", "w").write("0")
