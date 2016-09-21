# coding: utf8

import datetime
import json
import requests


def get_trending_repositories(top_size):
    now_date = datetime.date.today()
    period_of_time = 7  # репозитории, созданные за последнюю неделю
    delta = datetime.timedelta(days=period_of_time)
    parameters = {"q": "created:>%s" % (now_date-delta), "sort": "stars"}
    r = requests.get(
        'https://api.github.com/search/repositories',
        params=parameters
        )
    trending_repositories = {}
    trending_repositories = r.json()['items'][:top_size]
    return trending_repositories


if __name__ == '__main__':
    print ("Ссылка на репозиторий - количество открытых issue:")
    repositories_amount = 20  # количество репозиториев для анализа
    repositories = get_trending_repositories(repositories_amount)
    for i in range(repositories_amount):
        print (
            '%s - %s'
            % (repositories[i]['html_url'],
               repositories[i]['open_issues_count'])
        )
