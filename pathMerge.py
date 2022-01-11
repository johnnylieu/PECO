import json
import sys
import datetime

timestamp = datetime.datetime.now().strftime("%H-%M-%S")

# run file with deployer_file, helper_file, and routemainPathData

def pathMerge(main_paths_file, helper_file, slotId):
    with open(main_paths_file, "r") as mainPathData:
        with open(helper_file, "r") as helperPathData:

            mainPathData = json.load(mainPathData)
            helperPathData = json.load(helperPathData)

            targetHelperPath = helperPathData['routeSelections'][(int(slotId) - 1)]

            mainPathData['routeSelections'][(int(slotId) - 1)] = targetHelperPath
            
    with open(f"combinedPaths-{timestamp}.json", "w") as combinedPaths:
        json.dump(mainPathData, combinedPaths, indent = 4)

    print(f"You've selected {mainPathData['routeSelections'][(int(slotId) - 1)]['label']} route!")
    print(f"'combinedPaths-{timestamp}.json' has been created, and should contain the changes you specified")
    
if __name__ == "__main__":
    pathMerge(sys.argv[1], sys.argv[2], sys.argv[3])
