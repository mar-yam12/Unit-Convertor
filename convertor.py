# Project 01: Unit Convertor
# Build a Google Unit Convertor using Python and Streamlit

import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #a4d2e0;
        font-family: 'Arial', sans-serif;
        color: #333;
        margin: 0;
        padding: 0;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        padding: 30px;
        text-align: center;
    }
    h1 {
        text-align: center;
        color: #2c3e50;
        font-size: 36px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #fff;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 25px rgba(0, 201, 255, 0.5);
        background: linear-gradient(135deg, ##fcc39a 0%, #2e7d32 100%);
    }
    .result-box {
        font-size: 32px;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 50px;
        text-align: center;
        background: rgba(200, 255, 255, 0.9);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 10, 0, 0.1);
    }
    .footer {
        text-align: center;
        margin-top: 60px;
        color: #666;
        font-size: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("Unit Convertor")

st.write("This is a simple unit convertor. It converts units from one unit to another.")

# sidebar 
conversion_type = st.sidebar.selectbox('Select Conversion Type', ['Length', 'Weight', 'Temperature', 'Area', 'Volume'])
value = st.number_input("Enter the value to convert:", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)


if conversion_type == 'Length':
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles", "Feet", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles", "Feet", "Yards", "Inches"])
elif conversion_type == 'Weight':
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])

elif conversion_type == 'Temperature':
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

elif conversion_type == 'Area':
    with col1:
        from_unit = st.selectbox("From", ["Square Meters", "Square Kilometers", "Square Miles", "Acres", "Hectares"])
    with col2:
        to_unit = st.selectbox("To", ["Square Meters", "Square Kilometers", "Square Miles", "Acres", "Hectares"])

elif conversion_type == 'Volume':
    with col1:
        from_unit = st.selectbox("From", ["Liters", "Cubic Meters", "Cubic Feet", "Gallons", "Pints"])
    with col2:
        to_unit = st.selectbox("To", ["Liters", "Cubic Meters", "Cubic Feet", "Gallons", "Pints"])

# Conversion function
def convert_length(value, from_unit, to_unit):
    length_units = {
        'Meters': 1.0,
        'Kilometers': 1000.0,
        'Miles': 1609.34,
        'Feet': 0.3048,
        'Yards': 0.9144,
        'Inches': 0.0254
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1.0,
        'Grams': 0.001,
        'Miligrams': 0.000001,
        'Pounds': 0.453592,
        'Ounces': 0.0283495
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]          
        
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value + 459.67) * 5/9
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value * 9/5) - 459.67   
        
def convert_area(value, from_unit, to_unit):
    area_units = {
        'Square Meters': 1.0,
        'Square Kilometers': 1000000.0,
        'Square Miles': 2589988.1103,
        'Acres': 4046.86,
        'Hectares': 10000.0
    }
    return (value / area_units[from_unit]) * area_units[to_unit]

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'Liters': 1.0,
        'Cubic Meters': 1000.0,
        'Cubic Feet': 28.3168,
        'Gallons': 3.78541,
        'Pints': 0.473176
    }
    return (value / volume_units[from_unit]) * volume_units[to_unit]

# Conversion Button
if st.button("🦋Convert"):
    if conversion_type == 'Length':
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == 'Weight':
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == 'Temperature':
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_type == 'Area':
        result = convert_area(value, from_unit, to_unit)
    elif conversion_type == 'Volume':
        result = convert_volume(value, from_unit, to_unit)  

    st.markdown(f"<div class-'result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>",unsafe_allow_html=True)

    st.markdown(f"<div class-'footer'>Developed by <a href='https://www.linkedin.com/in/maryam-shahid-b2765529a/'> Maryam Shahid </a></div>",unsafe_allow_html=True)
