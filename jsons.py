import json
"""people_string='{"people":[{"name":"John","phone":"615-513-123","Emails":["john123@gmail.com","john321@yahoo.com"],"has_license":false},{"name":"Jane","phone":"432-543-123","Emails":null,"has_license":true}]}'
data=json.loads(people_string)
#print(data["people"])
#for person in data["people"]:
#    print(person["name"])

for person in data["people"]:
    del person["phone"]
new_string=json.dumps(data)
new_string=json.dumps(data,sort_keys=True)        #sorts the keys
print(new_string)
"""
'''with open("test.json") as f:
    data=json.load(f)
print(data)

for state in data["states"]:
    #print(state["name"])
    del state["area_codes"]

with open("new_states.json","w") as f:
    #json.dump(data,f)
    json.dump(data,f,indent=2)              #dumps using a good indenting
'''

from urllib.request import urlopen
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source=response.read()
#print(source)

data=json.loads(source)
print(json.dumps(data,indent=2))