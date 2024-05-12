import plotly.express as ps
import requests

API_KEY = "4a41268fee3b599359e894e530b86d4e"


def get_temperature(place, days=None, weather_format=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    df = response.json()
    return df


if __name__ == "__main__":
    print(get_temperature("Tokyo"))