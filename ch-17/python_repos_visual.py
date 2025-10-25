import requests
import plotly.express as px


# make an api call and check response status

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:starts+stars:>10000"

headers = {
    "Accept": "application/vnd.github.v3+json",}

r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

#convert to dictionary 
response_dict = r.json()
print(response_dict)
repo_dicts = response_dict['items']

repo_name, stars, hover_text = [], [], []
for repos in repo_dicts:
    repo_name.append(repos['name'])
    stars.append(repos['stargazers_count'])
    owner = repos['owner']['login']
    description = repos['description']
    hover_text.append(f"{owner} <br /> {description}")

fig = px.bar(x=repo_name, y=stars, hover_name=hover_text)
title = "Most Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig.update_layout(title=title, xaxis_title="Repository", yaxis_title="Stars")
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()