import requests
from langchain_core.tools import tool

CITY_COORDINATES = {
    "bangalore": (12.9716, 77.5946),
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "chennai": (13.0827, 80.2707),
}


@tool
def weather(city: str) -> str:
    """
    Returns the current weather for a supported city.
    """

    city = city.lower().strip()

    if city not in CITY_COORDINATES:
        return f"Weather not available for '{city}'."

    latitude, longitude = CITY_COORDINATES[city]

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m"
    )

    try:

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        current = data["current"]

        return (
            f"Weather in {city.title()}\n"
            f"Temperature : {current['temperature_2m']} °C\n"
            f"Wind Speed  : {current['wind_speed_10m']} km/h"
        )

    except Exception as e:
        return f"Weather API Error: {e}"