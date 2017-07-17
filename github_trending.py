import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    period = 7
    datetime_period_ago = datetime.now() - timedelta(days=period)
    base_url = 'https://api.github.com/search/repositories?'
    payload = {'q': 'created:>' + str(datetime_period_ago.date()), 'sort': 'stars'}
    trending_repositories = requests.get(base_url, params=payload)
    repos = trending_repositories.json()['items']
    return repos[:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    repo_info = requests.get('https://api.github.com/repos/' + repo_owner + '/' + repo_name)
    return repo_info.json()['open_issues_count']


if __name__ == '__main__':
    trending_repositories = get_trending_repositories(20)
    for repo in trending_repositories:
        open_issues_amount = get_open_issues_amount(repo['owner']['login'], repo['name'])
        print('Repo url: {}, open issues amount: {}'.format(repo['html_url'], open_issues_amount))