import json
import sys

f = open(sys.argv[1],"r")
pathData = json.loads(f.read())
for i in pathData['routeSelections']:
  print(i)
f.close()
