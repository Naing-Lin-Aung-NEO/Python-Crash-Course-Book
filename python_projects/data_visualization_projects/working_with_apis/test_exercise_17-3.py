# 17.3 Testing python_repos.py

# 1. for status code

# import requests

# def test_api_1():
#     """Testing python api status code!"""
#     url = "https://api.github.com/search/repositories?q=language:python+stars:>10000&sort=stars"
#     r = requests.get(url)
#     status_code = r.status_code
#     assert status_code == 200


# 2. for item returns amount 

# import requests

# def test_api_2():
#     """Testing the numbers of itmes."""
#     url = "https://api.github.com/search/repositories?q=language:python+stars:>10000&sort=stars"

#     headers = {"Accept": "application/vnd.github.v3+json"}
#     r = requests.get(url, headers=headers)

#     response_dict = r.json()
#     repo_dict = response_dict['items']
#     assert len(repo_dict) < 100

# -----------------------------------------------------------------------------