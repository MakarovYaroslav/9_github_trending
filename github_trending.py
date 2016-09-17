import datetime
import json
import requests


def get_trending_repositories(top_size):
    now_date = datetime.date.today()
    delta = datetime.timedelta(days=7)
    r = requests.get(
        'https://api.github.com/search/repositories?q=created:>%s&sort=stars'
        % (now_date-delta)
        )
    trending_repositories = {}
    trending_repositories = r.json()['items'][:top_size]
    return trending_repositories


if __name__ == '__main__':
    print ("Ссылка на репозиторий - количество открытых issue:")
    repositories_amount = 20
    repositories = get_trending_repositories(repositories_amount)
    for i in range(repositories_amount):
        print (
            '%s - %s'
            % (repositories[i]['html_url'],
               repositories[i]['open_issues_count'])
        )
