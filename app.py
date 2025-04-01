
import streamlit as st

# Page setup
st.set_page_config(page_title="RYA Yachtmaster Offshore", layout="wide")
st.title("RYA Yachtmaster Offshore Practice App")

# Intro section
st.markdown("""
Welcome to the **RYA Yachtmaster Offshore** practice tool!  
Use this app to work on:
- Tidal height calculations
- Navigation theory
- Course plotting tools
- Practice questions

This version is iPad-friendly and under active development.
""")

# Section: Tidal Height Calculator
st.header("Tidal Height Calculator (Rule of Twelfths)")
high = st.number_input("High Water Height (m)", min_value=0.0, format="%.2f")
low = st.number_input("Low Water Height (m)", min_value=0.0, format="%.2f")
hours = st.slider("Hours after High Water", 0, 6, 3)

if high > low:
    range_ = high - low
    twelfths = [1, 2, 3, 3, 2, 1]
    rise = sum(twelfths[:hours]) / 12 * range_
    height = low + rise
    st.success(f"Estimated tidal height: {height:.2f} m")
else:
    st.info("Enter high and low water heights above.")

# Section: Sample Question
st.header("Sample Navigation Question")
question = st.radio("What is the first action when you see a vessel displaying red over white lights at night?",
                    ["Alter course to port", "Maintain speed and course", "Keep clear - it's a fishing vessel", "Sound five short blasts"])

if question:
    if question == "Keep clear - it's a fishing vessel":
        st.success("Correct! That light pattern means a fishing vessel with gear extending more than 150m.")
    else:
        st.error("Not quite. Red over white indicates a fishing vessel – the correct action is to keep clear.")
