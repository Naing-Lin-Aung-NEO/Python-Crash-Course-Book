# 17.1 Other Languages 

# import requests
# import plotly.express as px 

# url = "https://api.github.com/search/repositories"
# url += "?q=language:java+stars:>10000&sort=stars"

# headers = {"Accept": "application/vnd.github.v3+json"}
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# # Convert response format to python object.
# response_dicts = r.json()
# print(f"Complete Results: {not response_dicts['incomplete_results']}")

# # Process Repo information.
# repo_dicts = response_dicts['items']
# links, stars, hover_texts = [], [], []
# for repo_dict in repo_dicts:
#     name = repo_dict['name']
#     url = repo_dict['html_url']
#     link = f"<a href='{url}'>{name}</a>"
#     links.append(link)

#     star = repo_dict['stargazers_count']
#     stars.append(star)

#     owner = repo_dict['owner']['login']
#     description = repo_dict['description']
#     hover_text = f"{owner}<br />{description}"
#     hover_texts.append(hover_text)

# # Visualize the Chart 
# title = "Most Starred Java Projects on GitHub"
# labels = {'x': 'Repository', 'y': 'Stars'}
# fig = px.bar(x=links, y=stars, title=title, labels=labels, hover_name=hover_texts)

# fig.update_layout(title_font_size=26, xaxis_title_font_size=16,
#                   yaxis_title_font_size=16)

# fig.update_traces(marker_color='yellow', marker_opacity=0.9)

# fig.show()

# -----------------------------------------------------------------------------

# 17.2 Active Discussions

# -----------------------------------------------------------------------------

# 17.3 Testing python_repos.py

# -----------------------------------------------------------------------------

# 17.4 Further Exploration

# -----------------------------------------------------------------------------