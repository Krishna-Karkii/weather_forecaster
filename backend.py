import plotly.express as ps


def get_temperature(days):
    temperatures = [10, 20, 12]
    date = ["2022-12-21", "2022-12-22", "2022-12-23"]
    temperatures = [days * temperature for temperature in temperatures]
    figure = ps.line(x=date, y=temperatures, labels={"x": "Dates", "y": "Temperature-(C)"})
    return figure