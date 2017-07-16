import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    datetime_7_days_ago = datetime.now() - timedelta(days=7)
    r = requests.get('https://api.github.com/search/repositories?' + 'q=created:>' + str(datetime_7_days_ago.date()) + '&sort=stars')
    repos = r.json()['items']
    return repos[:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    r = requests.get('https://api.github.com/repos/' + repo_owner + '/' + repo_name)
    return r.json()['open_issues_count']


if __name__ == '__main__':
    pass