"""Apartment example."""
import math
from typing import List
from dataclasses import dataclass
from typing_extensions import Self
from cs110 import expect, summarize

@dataclass
class LatLong:
    """A coordinate in the world."""
    latitude: float   #  -90 to  90
    longitude: float  # -180 to 180

    def distance(self, addr: Self) -> float:
        """
        Purpose: Gets the distance between this and another apartment.
        Examples:
            addr_1 = Address("123 Fake St.", 49.0, -123.0)
            addr_2 = Address("456 Fake St.", 50.0, -124.0)
            addr_1.distance(addr_2) -> 1.414...
        """
        dist_lat = self.latitude - addr.latitude
        dist_lon = self.longitude - addr.longitude
        return math.sqrt(dist_lat ** 2 + dist_lon ** 2)


@dataclass
class Location:
    """A class for anything that has a coordinate."""
    coordinates: LatLong


@dataclass
class Address(Location):
    """A class to describe an Address."""
    address: str


@dataclass
class Building:
    """A class to describe a building."""
    address: Address


@dataclass
class Apartment(Building):
    """A class to describe an apartment."""
    price: int


@dataclass
class Grocery(Building):
    """A class to describe a Grocery."""
    name: str


@dataclass
class BusStop(Location):
    """A class to describe a Bus stop."""
    number: int
    connections: List[str]


@dataclass
class BusRoute:
    """A collection of stops for a particular bus route."""
    label: str
    stops: List[BusStop]


@dataclass
class BuildingList:
    """A collection of buildings."""
    buildings: List[Building]


# The database is a list of apartments
# The data is real data from Google Maps
apartments = [
    Apartment(
        price = 2050,
        address = Address(
            address = "1104-1157 Jepson-Young Ln, Vancouver, BC, Canada",
            coordinates = LatLong(
                latitude = 49.28268912323915, 
                longitude = -123.13115296063464
            )
        )
    ),
    Apartment(
        price = 3050,
        address = Address(
            address = "718 Davie St, Vancouver, BC, Canada",
            coordinates = LatLong(
                latitude = 49.27736281422789, 
                longitude = -123.12668440036572
            )
        )
    ),
    Apartment(
        price = 2875,
        address = Address(
            address = "1399 Homer St, Vancouver, BC, Canada",
            coordinates = LatLong(
                latitude = 49.27352901325701, 
                longitude = -123.12602017298748
            )
        )
    )
]

groceries = [
    Grocery(
        name = "IGA",
        address = Address(
            address = "909 Burrard St, Vancouver, BC V6Z 2N2",
            coordinates = LatLong(
                latitude = 49.282612575947034, 
                longitude = -123.12486075671096
            )
        )
    ),
    Grocery(
        name = "Nesters",
        address = Address(
            address = "990 Seymour St, Vancouver, BC V6B 3L9",
            coordinates = LatLong(
                latitude = 49.27970102048647, 
                longitude = -123.12185668280533
            )
        )
    )
]

bus_stop_51916 = BusStop(
    number = 51916,
    connections = [
        "044",
        "084"
    ],
    coordinates = LatLong(
        latitude = 49.273342,
        longitude = -123.239004
    )
)

bus_stop_51917 = BusStop(
    number = 51917,
    connections = [
        "044",
        "084"
    ],
    coordinates = LatLong(
        latitude = 49.273563,
        longitude = -123.246195
    )
)

route_084 = BusRoute(
    label = "084",
    stops=[
        bus_stop_51916,
        bus_stop_51917
    ]
)

route_044 = BusRoute(
    label = "044",
    stops=[
        bus_stop_51916,
        bus_stop_51917
    ]
)

mine = apartments[0]

expect(mine.address.coordinates.distance(apartments[0].address.coordinates),       0, tolerance=0.0001)
expect(mine.address.coordinates.distance(apartments[1].address.coordinates), 0.00695, tolerance=0.0001)
expect(mine.address.coordinates.distance(apartments[2].address.coordinates), 0.01050, tolerance=0.0001)

summarize()