from os import walk

filenames = next(walk("./en/"), (None, None, []))[2]  # [] if no file
print(filenames)