# importing built-in packages for:
# Being able to work with json
import json

# and interacting with python environment
# Used to select the file in the command line as an argument
import sys

# the "r" is the function for reading the file.
def pathMerge(main_paths_file, helper_file, slotId):
    # 'with open' is just an alternate way of writing the whole
    # f = open(), and doesn't require close()
    # this provides the function with the data from the file given as the paths_file argument
    with open(main_paths_file, "r") as mainPathData:
        with open(helper_file, "r") as helperPathData:

    # setting pathData variable to contain the contents of the json
    # json.load() method takes the input paths_file and
    # returns it as a Python dictionary.
            # then narrowing it to JUST the routeSelections data
            mainPathData = json.load(mainPathData)
            # mainPathData = mainPathData['routeSelections']

            helperPathData = json.load(helperPathData)
            # helperPathData = helperPathData['routeSelections']

            # then setting the value of onePath to the routeSelections key
            # chosen by the second argument after the paths_file
            # (same format as the path_replay, except with only the path, and route selection)
            targetMainPath = mainPathData['routeSelections'][(int(slotId) - 1)]
            targetHelperPath = helperPathData['routeSelections'][(int(slotId) - 1)]
            targetMainPath = targetHelperPath
            mainPathData['routeSelections'][(int(slotId) - 1)] = targetMainPath

        # Here, using json.dumps to convert the dict back into json string and format it using indent = x
            targetMainPath = json.dumps(targetMainPath, indent = 3)
            updatedMainPath = json.dumps(mainPathData, indent = 3)
            print(targetMainPath)

    # prints formatted result to console
    print(f"You've selected {mainPathData['routeSelections'][(int(slotId) - 1)]['label']} route!")
    f = open("combinedPaths.json", "w")
    f.write(updatedMainPath)
    f.close()
    

# sys.argv[n] is what selects the file when we write it in the command line.
if __name__ == "__main__":
    # print(f"You've selected route: {int(sys.argv[3])}")
    pathMerge(sys.argv[1], sys.argv[2], sys.argv[3])


# this takes the formatted json and creates a new file with the contents.
# IF file already exists, will overwrite file completely.
