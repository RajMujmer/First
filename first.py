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
tab2, tab1 = st.tabs(["Calculator", "Table Generator"])
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
        num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
        num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")
        Option = st.selectbox("Option", ["Addition", "Subtration", "Multiplication", "Division"])
        submitted = st.form_submit_button("Calculate")

    if submitted:
        result = None
        if operation == "Add":
            result = num1 + num2
            st.write(f"The result of addition is: {result}")
        elif operation == "Subtract":
            result = num1 - num2
            st.write(f"The result of subtraction is: {result}")
        elif operation == "Multiply":
            result = num1 * num2
            st.write(f"The result of multiplication is: {result}")
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
                st.write(f"The result of division is: {result}")
            else:
                st.write("Error: Division by zero is undefined.")
