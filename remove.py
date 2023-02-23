import os
import shutil
os.chdir(r"C:\Users\naresh\Downloads\essentialai\notes")

if os.path.exists("_build"):
    shutil.rmtree("_build")
    print("Deleted _build")

os.system("jb build ../notes/")