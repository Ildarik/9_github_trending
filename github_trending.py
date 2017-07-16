import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    base_url = 'https://api.github.com/search/repositories?'
    datetime_7_days_ago = datetime.now() - timedelta(days=7)
    r = requests.get(base_url + 'q=created:>' + str(datetime_7_days_ago.date()) + '&sort=stars')
    repos = r.json()['items']
    return repos[:top_size]

def get_open_issues_amount(repo_owner, repo_name):
    pass

if __name__ == '__main__':
    get_trending_repositories(20)
