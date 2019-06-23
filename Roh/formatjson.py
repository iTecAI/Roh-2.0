import json
with open('data.json','r') as j:
    load = json.load(j)
print('loaded')
for i in load:
    print(i)
with open('data.json','w') as j:
    json.dump(load,j)
    
