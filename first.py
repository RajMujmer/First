import datetime
import random

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Show app title and description.
st.set_page_config(page_title="Customer preferences", page_icon="🎫")
st.title("🎫 Customer Preferences")
st.write(
    """
    This app shows how you can build an internal tool in Streamlit. Here, we are 
    implementing a support ticket workflow. The user can create a ticket, edit 
    existing tickets, and view some statistics.
    """
)
