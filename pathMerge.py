# importing built-in packages for:
# Being able to work with json
import json

# and interacting with python environment
# Used to select the file in the command line as an argument
import sys

# f here is just a variable containing the contents of the file
# as a string literal. We could've called f anything, but it seems to be standard.

# sys.argv[1] is what selects the file when we write it in the command line.
# the "r" is the function for reading the file.
f = open(sys.argv[1],"r")

# setting pathData variable to contain the contents of the json
# json.load() method takes the input from "f"(the path file), and
# returns it as a Python dictionary.
pathData = json.load(f)

# Here, using json.dumps to convert the dict back into json string and format it using indent = x
pathjson = json.dumps(pathData, indent = 3)

# prints formatted result to console
print(pathjson)
f.close()

# this takes the formatted json and creates a new file with the contents.
# IF file already exists, will overwrite file completely.
# f = open("pathcopytest.json", "w")
# f.write(pathjson)
# f.close()
