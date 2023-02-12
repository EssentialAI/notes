import os
import shutil
os.chdir(r"C:\Users\kumar\Downloads\UB\essentialai\cvip")

if os.path.exists("_build"):
    shutil.rmtree("_build")
    print("Deleted _build")

os.system("jb build ../cvip/")