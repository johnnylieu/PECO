# importing built-in packages for:
# Being able to work with json
import json

# and interacting with python environment
# Used to select the file in the command line as an argument
import sys

# the "r" is the function for reading the file.
def pathMerge(paths_file, slot):
    # 'with open' is just an alternate way of writing the whole
    # f = open(), and doesn't require close()
    # this provides the function with the data from the file given as the paths_file argument
    with open(paths_file, "r") as pathData:

    # setting pathData variable to contain the contents of the json
    # json.load() method takes the input paths_file and
    # returns it as a Python dictionary.
        pathData = json.load(pathData)
        # then narrowing it to JUST the routeSelections data
        pathData = pathData['routeSelections']

        # then setting the value of onePath to the routeSelections key
        # chosen by the second argument after the paths_file
        # (same format as the path_replay, except with only the path, and route selection)
        onePath = pathData[(int(slot) - 1)]['path']

    # Here, using json.dumps to convert the dict back into json string and format it using indent = x
        fullPathData = json.dumps(pathData, indent = 3)
        onePath = json.dumps(onePath, indent = 3)

    # prints formatted result to console
    print(onePath)
    print(f"You've selected {pathData[(int(slot) - 1)]['label']} route!")
    

# sys.argv[n] is what selects the file when we write it in the command line.
if __name__ == "__main__":
    print(f"You've selected route: {int(sys.argv[2])}")
    pathMerge(sys.argv[1], sys.argv[2])


# this takes the formatted json and creates a new file with the contents.
# IF file already exists, will overwrite file completely.
# f = open("pathcopytest.json", "w")
# f.write(fullPathData)
# f.close()
