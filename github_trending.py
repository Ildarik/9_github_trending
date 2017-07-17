import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    period = 7
    datetime_7_days_ago = datetime.now() - timedelta(days=period)
    base_url = 'https://api.github.com/search/repositories?'
    trending_repositories = requests.get(base_url + 'q=created:>' + str(datetime_7_days_ago.date()) + '&sort=stars')
    repos = trending_repositories.json()['items']
    return repos[:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    repo_info = requests.get('https://api.github.com/repos/' + repo_owner + '/' + repo_name)
    return repo_info.json()['open_issues_count']


if __name__ == '__main__':
    trending_repositories = get_trending_repositories(20)
    for repo in trending_repositories:
        repo_owner = repo['owner']['login']
        repo_name = repo['name']
        repo_url = repo['html_url']
        open_issues_amount = get_open_issues_amount(repo_owner, repo_name)
        print('Repo url: {}, open issues amount: {}'.format(repo_url, open_issues_amount))