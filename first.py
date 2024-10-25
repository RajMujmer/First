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
   This is that
    """
)
for i in range(1, 11):
    for j in range(1,11):
        st.write(i ," * " , j ,"= ", i*j )
     
