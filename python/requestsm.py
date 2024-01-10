#import requests 
from pprint import pprint 
'''
# Making a GET request 
r = requests.get('https://api.github.com/users/naveenkrnl') 

# check status code for response received 
# success code - 200 
pprint(r) 

# print content of request 
pprint(r.content) 
'''

# import requests module 
import requests 
# Making a get request 
response = requests.get('https://api.github.com/') 
# print request object 
print(response.url) 
# print status code 
print(response.status_code)
