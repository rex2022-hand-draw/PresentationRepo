import json

def readJSON (filePath):
    with open(filePath, 'r') as file:
        fileContent = file.read()
        readJsonArray = json.loads(fileContent)

    return readJsonArray["coordinates"]