import datetime
import random

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Show app title and description.
st.set_page_config(page_title="Speaker", page_icon="🎫")
st.title(" My Speaker ")
st.write(
    """
   Table from 1 to 10
    """
)
with st.form("add_ticket_form"):
    issue = st.text_area("Number of which you want a table ")
    #priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    submitted = st.form_submit_button("Submit")

if submitted:
        for j in range(1,11):
            st.write(issue ," * " , j ,"= ", issue*j )
        st.write("""--------------------""")
     
