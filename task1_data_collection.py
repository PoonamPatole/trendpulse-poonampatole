import requests

url="https://hacker-news.firebaseio.com/v0/topstories.json"
response=requests.get(url)
if response.status_code==200:
  data=response.json() # convert JSON response to python dict
  print(data)
else:
  print("Error", response.status_code)
data = data[:10]  # take first 10 IDs
stories = []

#Check if request was successful

for story_id in data:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    item_response = requests.get(item_url)
    if item_response.status_code == 200:
        stories.append(item_response.json())

print(stories)
