#print("Learning with Caleb Curry")
import requests 
import json 

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

#peel off the topmost layer 
#each go round of the 'for' loop sees the key be mapped into the data variable
for data in response.json()['items']:
    #If the key mapped into the 'data' variable matches the index 'title' the associated value with the key is printed 
    print(data['title'])

print()

for data in response.json()['items']:
    print(data['content_license'])


