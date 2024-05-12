import plotly.express as ps
import requests

API_KEY = "4a41268fee3b599359e894e530b86d4e"


def get_data(place, days=None, weather_format=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    df = response.json()
    nr_days = 8 * days
    filtered_data = df['list'][:nr_days]

    if weather_format == "Temperature":
        filtered_data = [data['main']['temp'] for data in filtered_data]
    else:
        filtered_data = [data['weather'][0]['main'] for data in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data("Tokyo", days=5, weather_format="Temperature"))