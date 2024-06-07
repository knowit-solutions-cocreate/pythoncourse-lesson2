#!/usr/bin/env python

import argparse
import requests
import json
from enum import Enum


# SWAPI -
SWAPI_BASE_URL = "https://swapi.dev/api/"


# Example of adding a categorical data type
class SWAPIResource(Enum):
    PEOPLE = "people"
    PLANETS = "planets"
    STARSHIPS = "starships"
    VEHICLES = "vehicles"
    SPECIES = "species"
    FILMS = "films"


def fetch_data(endpoint):
    """Fetch data from the SWAPI endpoint."""
    response = requests.get(f"{SWAPI_BASE_URL}{endpoint}")
    if response.status_code == 200:
        return response.json()
    else:
        return None


def display_data(data, output_format):
    """Display fetched data in the specified format."""
    if output_format == "json":
        print(json.dumps(data, indent=2))
    else:
        for key, value in data.items():
            print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser(description="CLI for SWAPI (Star Wars API)")
    parser.add_argument(
        "resource",
        type=str,
        help="The resource to fetch (e.g., people, planets, starships)",
    )
    parser.add_argument("id", type=int, help="The ID of the resource to fetch")
    parser.add_argument(
        "--format",
        choices=["default", "json"],
        default="default",
        help="The output format (default or json)",
    )

    args = parser.parse_args()

    # Examples of error handling
    try:
        resource = SWAPIResource[args.resource.upper()]
    except KeyError:
        print(
            f"Error: '{args.resource}' is not a valid resource. Choose from: {[e.value for e in SWAPIResource]}"
        )
        return

    # Assemble URL for requests
    endpoint = f"{resource.value}/{args.id}/"
    # Make request
    data = fetch_data(endpoint)

    # Another example of error handling
    if data is None:
        print(
            f"Error: Unable to fetch data for {resource.value} with ID {args.id}. Please ensure the endpoint and ID are correct."
        )
        return

    display_data(data, args.format)


if __name__ == "__main__":
    main()
