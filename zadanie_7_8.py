import requests
from typing import Optional
import argparse


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: Optional[str],
        street: Optional[str],
        address_2: Optional[str],
        address_3: Optional[str],
        city: Optional[str],
        state: Optional[str],
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state

    def __str__(self):
        return f"Brewery(id={self.id}, name={self.name}, city={self.city}, state={self.state}, type={self.brewery_type})"


def fetch_breweries(where: str):
    url = f"https://api.openbrewerydb.org/v1/breweries?by_city={where}"
    response = requests.get(url)
    data = response.json()
    breweries = []

    for item in data:
        breweries.append(
            Brewery(
                id=item.get("id"),
                name=item.get("name"),
                brewery_type=item.get("brewery_type"),
                street=item.get("street"),
                address_2=item.get("address_2"),
                address_3=item.get("address_3"),
                city=item.get("city"),
                state=item.get("state"),
            )
        )

    return breweries


WhereParse = argparse.ArgumentParser(description="Breweries parser")
WhereParse.add_argument(
    "--city", type=str, default="Berlin", help="Where are the breweries"
)
args = WhereParse.parse_args()
breweries = fetch_breweries(args.city)
for b in breweries:
    print(b)
