#!/usr/bin/env python
import requests
import pandas as pd


BASE_URL = "https://swapi.dev/api/"

RESOURCES = set(
    [
        "people",
        "films",
        "starships",
        "vehicles",
        "species",
        "planets",
    ]
)


def fetch_resource(resource_name):

    assert (
        resource_name in RESOURCES
    ), f"Resource '{resource_name}' doesn't exist in SWAPI."

    url = BASE_URL + resource_name

    print(f"url: {url}")

    all_data = []
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            all_data.extend(data["results"])
            url = data["next"]
            print(f"Next url:{url}")
        else:
            print(f"Failed to retreive data: {response.status_code}")

    return all_data


def resource_to_csv(resource_name, csv_name):

    data = fetch_resource(resource_name)
    dataframe = pd.DataFrame(data)
    dataframe = dataframe.assign(
        index=lambda x: x.index + 1,
    )
    dataframe.to_csv(csv_name, index=False)


def clean_homeplanet_id(dataframe: pd.DataFrame):
    dataframe = dataframe.assign(
        homeplanet_id=lambda x: x["homeworld"].str.split("/")[-1]
    )


def main():
    resource_to_csv(resource_name="people", csv_name="swapi_people.csv")
    resource_to_csv(resource_name="planets", csv_name="swapi_planets.csv")


if __name__ == "__main__":
    main()
