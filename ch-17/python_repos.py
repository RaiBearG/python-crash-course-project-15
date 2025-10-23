import requests

# make an api call and check response status

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:starts+stars:>10000"

headers = {
    "Accept": "application/vnd.github.v3+json",}

r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

#convert to dictionary 
response_dict = r.json()

print(f"Returned keys : {response_dict.keys()}")

print(f"Total repositories: {response_dict['total_count']}")

print(f"Complete Results: {not response_dict['incomplete_results']}")

#explorer repository 

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#print the first repo 

repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)
for repos in repo_dicts:
    print(f"\nName: {repos['name']}")
    print(f"Owner: {repos['owner']['login']}")
    print(f"Stars: {repos['stargazers_count']}")
    print(f"Repository: {repos['html_url']}")
    print(f"Description: {repos['description']}")
# print("\nSelected information about first repository:")
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")