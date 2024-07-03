import requests
from pprint import pprint
import pandas as pd


def fetch_film(n):
    response = requests.get(f'https://swapi.dev/api/films/{n}')
    response_as_dict = response.json()
    return response_as_dict


if __name__ == '__main__':
    # example of fetching a single film
    first_film = fetch_film(1)
    print('first film as dict:')
    pprint(first_film)
    print()


    # now, let's fetch all films and gather relevant info in a dict!
    films_dict = {'release': [], 'title': []}

    for film_number in range(1, 1000):  # how many Star Wars films are there anyway?
        print(f'fetching film number {film_number}...')

        film_dict = fetch_film(film_number)
        if film_dict == {'detail': 'Not found'}:  # this means we have requested a film that doesn't exist,
            break  # so we break the for loop

        films_dict['release'].append(film_dict['release_date'])
        films_dict['title'].append(film_dict['title'])

    films_df = pd.DataFrame(films_dict)
    print('all films, as a dataframe:')
    print(films_df)
