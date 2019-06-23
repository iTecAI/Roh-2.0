import json

with open('data.json','r') as f:
    raw = json.load(f)

'''[{"dialog": [{"id": 0, "sender": "participant2", "text": "I love iphone! i just bought new iphone!", "evaluation_score": null, "sender_class": "Bot"}, {"id": 1, "sender": "participant1", "text": "Thats good for you, i'm not very into new tech", "evaluation_score": null, "sender_class": "Human"}, {"id": 2, "sender": "participant2", "text": "I am a college student and i am a college student", "evaluation_score": null, "sender_class": "Bot"}, {"id": 3, "sender": "participant1", "text": "I am go to gym and live on donations", "evaluation_score": null, "sender_class": "Human"}, {"id": 4, "sender": "participant2", "text": "I am a vegan and i am in the midwest", "evaluation_score": null, "sender_class": "Bot"}, {"id": 5, "sender": "participant1", "text": "So vegan... i have dogs maybe i should told then that they may eat cheap salads insted of meat", "evaluation_score": null, "sender_class": "Human"}, {"id": 6, "sender": "participant2", "text": "I would not mind having them in the office that would be hard for me", "evaluation_score": null, "sender_class": "Bot"}, {"id": 7, "sender": "participant1", "text": "Dogs or vegan in office?", "evaluation_score": null, "sender_class": "Human"}, {"id": 8, "sender": "participant2", "text": "I am a vegetarian so i am vegan", "evaluation_score": null, "sender_class": "Bot"}, {"id": 9, "sender": "participant1", "text": "Strange answer", "evaluation_score": null, "sender_class": "Human"}, {"id": 10, "sender": "participant2", "text": "I guess i just do not know what to ps4 experience with.", "evaluation_score": null, "sender_class": "Bot"}]'''

convos = []
for i in raw:
    convo = []
    dialog = i['dialog']
    for i in dialog:
        convo.append(i['text'])
    convos.append(convo)
    
processed = {}
for convo in convos:
    proc = []
    for turn in convo:
        jnr = ''
        for l in turn.lower():
            if l in "qwertyuiopasdfghjklzxcvbnm1234567890 '":
                jnr += l
        proc.append(jnr)
    for p in range(len(proc)):
        if p == len(proc) - 1:
            pass
        else:
            sp = proc[p].split()
            procsp = []
            for i in sp:
                if len(i) >= 3:
                    procsp.append(i)
            sp = procsp
            for i in sp:
                if i in processed.keys():
                    processed[i][str(set(sp))] = proc[p+1]
                else:
                    processed[i] = {str(set(sp)):proc[p+1]}

with open('output.json','w') as out:
    json.dump(processed, out, indent=2)
    
