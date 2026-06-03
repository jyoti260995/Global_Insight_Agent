import os
import requests
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()


@tool
def get_weather(place: str) -> str:
    """Get current temperature and weather condition for a city or country."""

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return "OPENWEATHER_API_KEY not found in .env"

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": place,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Error: {response.text}"

    data = response.json()

    temp = data["main"]["temp"]
    condition = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    return (
        f"Weather in {place}: "
        f"{temp}°C, "
        f"{condition}, "
        f"humidity {humidity}%"
    )


# if __name__ == "__main__":
#     result = get_weather.invoke({"place": "Delhi"})
#     print(result)