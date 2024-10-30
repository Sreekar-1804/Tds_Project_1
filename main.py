import requests
import pandas as pd

# Replace with your own GitHub personal access token
token = 'TOKEN'
headers = {"Authorization": f"token {token}"}

def clean_company_name(company):
    if company:
        company = company.strip()
        if company.startswith('@'):
            company = company[1:]
        return company.upper()
    return ""

def fetch_users():
    users_data = []
    url = "https://api.github.com/search/users?q=location:sydney+followers:>100"
    
    # Handle pagination
    page = 1
    while True:
        response = requests.get(url + f"&page={page}", headers=headers).json()
        
        # Break the loop if there are no more users
        if 'items' not in response or not response['items']:
            break
        
        for user in response.get('items', []):
            user_details = requests.get(user['url'], headers=headers).json()
            users_data.append({
                'login': user_details.get('login', ''),
                'name': user_details.get('name', ''),
                'company': clean_company_name(user_details.get('company', '')),
                'location': user_details.get('location', ''),
                'email': user_details.get('email', ''),
                'hireable': user_details.get('hireable', ''),
                'bio': user_details.get('bio', ''),
                'public_repos': user_details.get('public_repos', 0),
                'followers': user_details.get('followers', 0),
                'following': user_details.get('following', 0),
                'created_at': user_details.get('created_at', '')
            })
        
        page += 1  # Increment the page number for the next request

    return users_data

def fetch_repositories(login):
    repos_data = []
    url = f"https://api.github.com/users/{login}/repos?per_page=500"
    response = requests.get(url, headers=headers).json()
    
    for repo in response:
        license_name = repo.get('license').get('key') if repo.get('license') else ''

        repos_data.append({
            'login': login,
            'full_name': repo.get('full_name', ''),
            'created_at': repo.get('created_at', ''),
            'stargazers_count': repo.get('stargazers_count', 0),
            'watchers_count': repo.get('watchers_count', 0),
            'language': repo.get('language', ''),
            'has_projects': repo.get('has_projects', False),
            'has_wiki': repo.get('has_wiki', False),
            'license_name': license_name
        })
    return repos_data

# Fetch user data
users = fetch_users()
user_logins = [user['login'] for user in users]

# Fetch repository data for each user
all_repositories = []
for login in user_logins:
    all_repositories.extend(fetch_repositories(login))

# Save to CSV
pd.DataFrame(users).to_csv("users.csv", index=False)
pd.DataFrame(all_repositories).to_csv("repositories.csv", index=False)
