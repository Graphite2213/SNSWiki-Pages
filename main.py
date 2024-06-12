from os import walk

filenames = next(walk("./"), (None, None, []))[2]  # [] if no file
print(filenames)