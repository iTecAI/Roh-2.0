import json, random, threading

class Roh:
    def __init__(self,data='output.json'):
        with open(data,'r') as f:
            self.data = json.load(f)
        self.datapath = data
        self.last = ''
    def save(self):
        with open(self.datapath,'w') as f:
            json.dump(self.data, f, indent=2)
    def respond(self, text):
        if self.last != '':
            words = []
            jnr = ''
            for l in self.last:
                if l == ' ':
                    if len(jnr) >= 3:
                        words.append(jnr)
                    jnr = ''
                elif l in "qwertyuiopasdfghjklzxcvbnm1234567890'":
                    jnr += l
                else:
                    pass

            for i in words:
                if i in self.data.keys():
                    self.data[i][str(set(words))] = text
                else:
                    self.data[i] = {str(set(words)):text}

        words = []
        jnr = ''
        for l in text:
            if l == ' ':
                if len(jnr) >= 3:
                    words.append(jnr)
                jnr = ''
            elif l in "qwertyuiopasdfghjklzxcvbnm1234567890'":
                jnr += l
            else:
                pass
        possible = []
        for word in words:
            if word in self.data.keys():
                for i in list(self.data[word].keys()):
                    s = eval(i)
                    if set(words).issubset(s) or s.issubset(set(words)):
                        possible.append(self.data[word][i])
        if len(possible) == 0:
            key = random.choice(list(self.data.keys()))
            r = self.data[key][random.choice(list(self.data[key].keys()))]
            self.last = r
            if 'bye' in text:
                raise SystemExit
            return r
        r = random.choice(possible)
        self.last = r
        if 'bye' in text:
            raise SystemExit
        return r

roh = Roh()
try:
    while True:
        print(roh.respond(input('>>> ')))
except SystemExit:
    roh.save()



        