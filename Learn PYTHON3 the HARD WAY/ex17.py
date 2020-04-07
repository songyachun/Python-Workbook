from sys import argv
from os.path import exists

script, from_file, to_file = argv
# from_file = "".join(from_file)
# to_file = "".join(to_file)

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file,'r',encoding="utf-8")
indata = in_file.read()

print(f"The input file is{len(indata)} bytes long")

print(f"Dose the output file exist? {exists(to_file)}")
print("Ready, hit enter to continue,CRTLE-C to abort.")
input()

out_file = open(to_file, 'w',encoding="utf-8")
out_file.write(indata)

print("Alright,all done.")

out_file.close()
in_file.close()
