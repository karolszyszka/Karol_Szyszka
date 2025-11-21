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
        county_province: Optional[str],
        postal_code: Optional[str],
        country: Optional[str],
        longitude: Optional[str],
        latitude: Optional[str],
        phone: Optional[str],
        website_url: Optional[str],
        state_province: Optional[str]
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state_province = state_province

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
                county_province=item.get("county_province"),
                postal_code=item.get("postal_code"),
                country=item.get("country"),
                longitude=item.get("longitude"),
                latitude=item.get("latitude"),
                phone=item.get("phone"),
                website_url=item.get("website_url"),
                state_province=item.get("state_province"),
            )
        )

    return breweries

WhereParse= argparse.ArgumentParser(description="Breweries parser")
WhereParse.add_argument("--city", type=str, default="Berlin", help="Where are the breweries")
args = WhereParse.parse_args()
breweries = fetch_breweries(args.city)
for b in breweries:
        print(b)