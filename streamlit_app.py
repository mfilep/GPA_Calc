
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to GPA Calculator!


"""



df = pd.DataFrame(
    [
        {"class name": st.selectbox, "Letter Grade": "A", "Honors?": False},
    
    ])

df = load.data()
edited_df = st.data_editor(df) #creates an editable form

average_gpa = edited_df.loc[edited_df["Letter Grade"].idmax()]["class name"]
st.markdown("You best class is **", average_gpa, "**")
