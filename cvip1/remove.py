import os
import shutil
os.chdir(r"C:\Users\nares\Downloads\Fall-2022\cvip-doc\cvip")

if os.path.exists("_build"):
    shutil.rmtree("_build")
    print("Deleted _build")

os.system("jb build ../cvip/")