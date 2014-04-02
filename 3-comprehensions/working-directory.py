import os
import sys

print("before changing wd:")
print(os.getcwd())
os.chdir('../1-your-first-python-program')
print("")

print("after changing wd:")
print(os.getcwd())
print(sys.path)
print("")


print("Trying to open a.txt")
with open("a.txt") as f:
    for line in f:
        print(line)
    print("")

print("Trying to import from_import_test.py:")
import from_import_test



# So changing os.chdir doesn't change the import search path
# but it does change the directory for opening files
