import streamlit as st 
from PIL import Image


st.title("This is My Temp Convertor")

img = Image.open("temp.jpg")
st.image(img)

# Introduction

st.subheader("Introduction")

st.text("""
Quick Celsius (°C) / Fahrenheit (°F) Conversion:

There are two main temperature scales:

°C, the Celsius Scale (part of the Metric System, used in most countries)
°F, the Fahrenheit Scale (used in the US)
They both measure the same thing (temperature!), but use different numbers:

Boiling water (at normal pressure) measures 100° in Celsius, but 212° in Fahrenheit
And as water freezes it measures 0° in Celsius, but 32° in Fahrenheit
        
	""")

# Input

tc = st.number_input("Enter Temp in °C")


tf = (tc/5*9)+32

st.success(f"The Fahrenheit (°F) is {tf}")
