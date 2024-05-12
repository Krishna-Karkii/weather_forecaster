import plotly.express as ps
import requests

API_KEY = "4a41268fee3b599359e894e530b86d4e"


def get_data(place, days, weather_format):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    df = response.json()
    nr_days = 8 * days
    filtered_data = df['list'][:nr_days]
    dates = [data['dt_txt'].split(" ") for data in filtered_data]
    filtered_times = [data[1] for data in dates]

    index = 0
    filtered_dates = []
    while index < days:
        num = index * 8
        if num > 0:
            num = num - 1
        filtered_dates.append(dates[num][0])
        index = index + 1

    for index in range(0, days):
        if index <= days:
            num = index * 8
            if num > 0:
                num = num - 1
            filtered_times[num] = filtered_dates[index] + " " + filtered_times[num]
            index = index + 1

    if weather_format == "Temperature":
        filtered_data = [data['main']['temp'] for data in filtered_data]
    else:
        filtered_data = [data['weather'][0]['main'] for data in filtered_data]

    return filtered_data, filtered_times


if __name__ == "__main__":
    print(get_data("Tokyo", days=5, weather_format="Temperature"))