
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to GPA Calculator!


"""
standard = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
honors = {"A": 5, "B": 4, "C": 3, "D": 2, "F": 1}


df = pd.DataFrame(
    [
        {"Grade": "grade",
         "Semester": "semester",
         "Class Name": "Enter Class Name",
         "Letter Grade": "A",
         "Converted": "number",
         "Honors?": False},
         "AP?": False
    
    ])

#df = load_data()

edited_df = st.data_editor(df, num_rows="dynamic") #creates an editable form


df[0]["Converted"] = standard["Letter Grade"] #= edited_df.loc[edited_df["Letter Grade"]]
#st.markdown(f"You best class is ** { average_gpa} **")
