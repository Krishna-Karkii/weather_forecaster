import streamlit as st
import plotly.express as px
from backend import get_data

st.header("Weather forecaster web")

place = st.text_input("Place")
days = st.slider("Choose days to forecast", min_value=1, max_value=5,
                 help="Slide to how many days to forecast")
option = st.selectbox("Select a Format: ", ("Temperature", "Sky"))

if place:
    st.subheader(f"{option} for {days} days at {place}")
    data, dates = get_data(place, days, option)
    figure = px.line(x=dates, y=data, labels={"x": "dates", "y": "Temperature"})
    st.plotly_chart(figure)
