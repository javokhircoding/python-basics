
import json

bemor = {
    "ism": 'Alijon valiyev', 
    'yosh': 30,
    'oila': True,
    'farzandlar': ['Ahmad', 'Bonu'],
    'allergiya': None,
    'dorilar': [
        {'nomi': 'Analgin', 'miqdori': 0.5},
        {'nomi': 'Panadol', 'miqdori': 1.2}
    ]
}
bemor_j = json.dumps(bemor, indent = 4)

with open('bemor_j', 'w') as f:
    json.dump(bemor, f)
    

with open('bemor_j') as f:
    a = f.read()
    print(a)

with open('bemor_j') as f:
    bemor3 = json.load(f)
    #b = bemor3.read()
    print(bemor3)
    print(type(bemor3))



bemor2 = json.loads(bemor_j)
print(type(bemor2))