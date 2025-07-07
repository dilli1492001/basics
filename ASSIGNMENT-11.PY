
#########   BACKEND      #########



import requests

print("*****RHYMWORD GENERATOR******")
chooice = input("enter your word : ")
endpoint = f"https://api.datamuse.com/words?ml=i%20am%20{chooice}"
response = requests.get(endpoint)
data = response.json()
if response.status_code == 200:
    for items in data:
        tags = items.get("tags")
        print(tags[0])




# import requests
# print("********************")
# chooice = input("enter your word : ")
# endpoint = f"https://api.datamuse.com/words?rel_jjb={chooice}"
# response = requests.get(endpoint)
# data = response.json()
# if response.status_code == 200:
#     for items in data:
#         score = items.get("score")
#         if score > 970:
#             print(score)





    
        
