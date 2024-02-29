
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to GPA Calculator!


"""



df = pd.DataFrame(
    [
        {"class name": st.text_input, "Letter Grade": "A", "Honors?": False},
    
    ])

#df = load_data()
edited_df = st.data_editor(df, num_rows="dynamic") #creates an editable form

#average_gpa = edited_df.loc[edited_df["Letter Grade"]]
#st.markdown(f"You best class is ** { average_gpa} **")
