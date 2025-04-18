import streamlit as st

def convert_units(category, value, from_unit, to_unit):
    conversions = {
        "Length": {
            "Meter": 1,
            "Kilometer": 0.001
        },
        "Weight": {
            "Kilogram": 1,
            "Gram": 1000
        },
        "Time": {
            "Second": 1,
            "Minute": 1/60,
            "Hour": 1/3600,
        },
        "Temperature": {
            "Celsius": lambda x: x,
            "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Kelvin": lambda x: x + 273.15
        }
    }
    
    if category == "Temperature":
        if from_unit == "Fahrenheit":
            value = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            value = value - 273.15
        
        return conversions[category][to_unit](value)
    
    base_value = value / conversions[category][from_unit]
    return base_value * conversions[category][to_unit]

# Streamlit UI
st.title("Unit Converter App")
st.markdown("**Converts Length, Weight, Time, and Temperature Instantly**")

category = st.selectbox("Select a category:", ["Length", "Weight", "Time", "Temperature"])

conversions = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001
    },
    "Weight": {
        "Kilogram": 1, "Gram": 1000
    },
    "Time": {
        "Second": 1, "Minute": 1/60, "Hour": 1/3600
    },
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

units = list(conversions[category].keys()) if category != "Temperature" else conversions["Temperature"]

from_unit = st.selectbox("From:", units)
to_unit = st.selectbox("To:", units)

value = st.number_input("Enter value:", value=0.0, format="%.4f")

if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    st.success(f"Converted Value: {result:.4f} {to_unit}")

