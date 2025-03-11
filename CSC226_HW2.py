import json
student = "/Users/dylanveliyev/Desktop/student.json"
with open(student, "r") as file:
    jsonStr = file.read()

    jsonObj = json.loads(jsonStr)
    jsonStr = '{"name":"john"}'
    jsonObj["name"] = "Dylan"

with open(student, "w") as file:
    json.dump(jsonObj, file, indent=4)
