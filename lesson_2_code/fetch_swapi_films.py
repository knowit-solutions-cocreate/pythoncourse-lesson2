import requests
from pprint import pprint


def fetch_film(n):
    response = requests.get(f'https://swapi.dev/api/films/{n}')
    response_as_dict = response.json()
    return response_as_dict


if __name__ == '__main__':
    first_film = fetch_film(1)
    print('first film as dict:')
    pprint(first_film)
    print()

    response_to_film_that_doesnt_exist = fetch_film(1000)  # how many Star Wars films are there anyway?
    print('response to film that doesnt exist:')
    pprint(response_to_film_that_doesnt_exist)
