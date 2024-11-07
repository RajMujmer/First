import datetime
import random
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Page configuration must be the first command
st.set_page_config(
    page_title="Custom Background",
    page_icon=":art:",
    layout="centered"
)

# CSS to set background color
page_bg = """
<style>
.stApp {
    background-color:#00BFFF; /* Light grey background */
}
</style>
"""

# Apply the background color using markdown
st.markdown(page_bg, unsafe_allow_html=True)
st.title(" My Speaker ")
tab2, tab1, tab3 = st.tabs(["Calculator", "Table Generator", "Measures"])
# Show app title and description

with tab1:
    st.header("Table")
    with st.form("Table of N"):
        issue = st.text_area("Number of which you want a table ")
        submitted = st.form_submit_button("Submit")

    if submitted:
        for j in range(1, 11):
            st.write(issue, " * ", j, "= ", int(issue) * j)
        st.write("-=-=-=-=-=-=-=-=-==--=-=-=-=-==-=-=-=-===-=-=-===-=")


with tab2:
    st.header("Calculator")
    with st.form("Calculation"):
        num1 = st.number_input("Enter the first number", value=0.0, format="%f")
        num2 = st.number_input("Enter the second number", value=0.0, format="%f")
        Option = st.selectbox("Option", ["Addition", "Subtraction", "Multiplication", "Division"])
        submitted = st.form_submit_button("Calculate")

    if submitted:
        result = None
        if Option == "Addition":
            result = num1 + num2
            st.write(f"The result of addition is: {result}")
        elif Option == "Subtraction":
            result = num1 - num2
            st.write(f"The result of subtraction is: {result}")
        elif Option == "Multiplication":
            result = num1 * num2
            st.write(f"The result of multiplication is: {result}")
        elif Option == "Division":
            if num2 != 0:
                result = num1 / num2
                st.write(f"The result of division is: {result}")
            else:
                st.write("Error: Division by zero is undefined.")
    with tab3:
        st.header("Measures")
        with st.form("!!Measurement!!"):
            ms = st.selectbox("Measures", ["Area", "BMI", "Length", "Speed", "Time", "GST"])
            if ms == "Area":
                ar = st.selectbox("area", ["Acre to Hectare", "Sq ft to Sq m", "Sq km to Sq m"])
                submitted = st.form_submit_button("Calculate")
                if submitted:
                    res = None
                    if ms == "Area" and ar == "Acre to Hectare":
                        n1 = st.number_input("Acre", value=0.0, format="%f")
                        res = (n1/10 )* 4
                        st.write(f"{n1} Acre is equal to {res} Hectare")
                    if ms == "Area" and ar == "Sq ft to Sq m":
                        n1 = st.number_input("Square Foot", value = 0.0, format= "%f")
                        res = n1/10.76
                        st.write(f"{n1} Square Foot is Equal to {res} Square meter")
                    if ms == "Area" and ar == "Sq km to Sq m":
                        n1 = st.number_input("Square Kilometer", value = 0.0, format = "%f")
                        res = n1*1000000
                        st.write(f"{n1} Square kilometer is = {res} meter")
          if ms == "BMI":
               weight = st.number_input("Enter your Weight (kg) ", value = 0.0, format = "%f")
               height = st.number_input("Enter your Height (cm)", value = 0.0, format = "%f")
               BMI = weight/((height/100)**2)
               st.write(f"Your BMI is : {BMI}")
