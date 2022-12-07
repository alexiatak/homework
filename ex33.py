#combining files
import glob
import os

myadress=os.getcwd()
read_files = glob.glob("*.txt")

with open("resultof33.txt", "w") as outfile:
    for f in read_files:
       with open(f, "r") as infile:
            outfile.write(f"from {f} : \n")
            outfile.write(infile.read() + "\n")
