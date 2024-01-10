
import json

'''
x = 10
x_json = json.dumps(x) #json.dumps() funksiyasi orqali json formatga o'tkazamiz
print(x_json)
'''


bemor = {
    'ism': 'Alijon valiyev', 
    'yosh': 30,
    'oila': True,
    'farzandlar': ['Ahmad', 'Bonu'],
    'allergiya': None,
    'dorilar': [
        {'nomi': 'Analgin', 'miqdori': 0.5},
        {'nomi': 'Panadol', 'miqdori': 1.2}
    ]
}

'''
print(type(bemor))
'''
bemor_j = json.dumps(bemor, indent = 4)
print(bemor_j)





