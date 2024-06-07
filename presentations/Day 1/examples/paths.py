"""
   1. Import the `pathlib module` giving it the nickname `pl`
   7. Use the `file explorer` in vs code to copy the path to one of the files (not a folder) you've made today.
       - Right click on the file, and select `copy path` 
   8. Use the `pathlib` module to make it a `Path` object
       - an example of how to do this is in the `paths.py` file on brightspace.
   9. look up how to print the `parent` of that `Path` object and print it out.
   10. define functions that takes in the path to a file and prints the `parent`, the `name`, or the `suffix` of that file *in all uppercase*.
         - an example of how to do this is in the `paths.py` file on brightspace.
"""

# Step 1
import pathlib as pl

# Step 8
# you can use two different ways of handling windows style path strings in python 
# 1. double backslashes
# I'm going to leave the examples commented out because they'll cause an error if you try to run them
# path = pl.Path('C:\\Users\\username\\Desktop\\path\\to\\file.txt')
# 2. raw strings
# path = pl.Path(r'C:\Users\username\Desktop\path\to\file.txt')
# Note the `r` before the string, this tells python to treat the string as a raw string, which means it will ignore escape characters like `\n` and `\\`
# This is like an `f` string, but for strings that you don't want to format, just use as it literally appears, it gets rid
# of all the special meaning of backslashes in strings.
# This is what I use in my owh because it means I don't have to manually go through a string and add a backslash before every backslash

# For the rest of the examples, I'm going to use a relative path to this file
my_path = pl.Path("./functions.py")

# Step 9
# for the parent of the path object, you can use the .parent attribute
print(my_path.parent)
# for the suffix of the path object, you can use the .suffix attribute
print(my_path.suffix)
# for the name of the path object, you can use the .name attribute
print(my_path.name)

# Step 10
def print_parent(path):
    print(path.parent)

def print_suffix(path):
    print(path.suffix.upper())

def print_name(path):
    print(path.name.upper())