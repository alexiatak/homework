#combining files
import glob
import os

myadress=os.getcwd()
read_files = glob.glob("*.txt")

with open("resultof33.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(f"from {f} : ")
            outfile.write(infile.read())
