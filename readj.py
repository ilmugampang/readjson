import json

# json_string = '{ "channel": "ilmugampang", "author": "wongpinter" }'

f = open("filejson.json", "r")

datajson = json.loads(f.read())
print(datajson["channel"])
print(datajson["author"])

f.close()
