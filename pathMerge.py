import json
import sys
import datetime

timestamp = datetime.datetime.now().strftime("%H-%M-%S")

# run file with deployer_file, helper_file, and desired routes separated by spaces

def pathMerge(main_paths_file, helper_file, slotId):
    with open(main_paths_file, "r") as mainPathData:
        with open(helper_file, "r") as helperPathData:

            mainPathData = json.load(mainPathData)
            helperPathData = json.load(helperPathData)
            chosenPaths = []

            for i in range(3, len(slotId)):
                try:
                    if int(slotId[i]) < 7:

                        targetHelperPath = helperPathData['routeSelections'][(int(slotId[i]) - 1)]
                        mainPathData['routeSelections'][(int(slotId[i]) - 1)] = targetHelperPath
                        chosenPaths.append(targetHelperPath['label'])

                    else:
                        print(f"{slotId[i]} is not a valid selection.")
                        continue

                except ValueError:
                    print(f"{slotId[i]} was not valid. Please use numbers 1-6 to select routes.")
                    break
                
            else:
                with open(f"combinedPaths-{timestamp}.json", "w") as combinedPaths:
                    json.dump(mainPathData, combinedPaths, indent = 4)
                    print(f"'combinedPaths-{timestamp}.json' has been created, and will contain the changes you specified")
                    print(f"from the following routes:")
                    for i in chosenPaths:
                        print("-> " + i)

    
if __name__ == "__main__":
    pathMerge(sys.argv[1], sys.argv[2], sys.argv)
