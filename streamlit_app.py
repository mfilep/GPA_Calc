
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
        {"Year": ['9', '10', '11', '12'],
         "Semester": ['1', '2'],
         "Class Name": "Enter Class Name",
         "Grade": ['A', 'B', 'C', 'D', 'F'],
         "Converted": "number",
         "Honors?": False,
         "AP?": False}        
     ], dtype = "category")

#df = load_data()

edited_df = st.data_editor(df,
                           column_order = ["Year", "Semester", "Class Name", "Honors?", "AP?", "Letter Grade", "Converted"],
                           column_config = {"Year": st.column_config.SelectboxColumn("Year", options = ['9', '10', '11', '12']),
                                            "Semester": st.column_config.SelectboxColumn("Semester", options= ['1', '2']),
                                            "Letter Grade": st.column_config.SelectboxColumn("Grade", options= ['A', 'B', 'C', 'D', 'F'])
                                           }                                                                         
                           num_rows="dynamic") #creates an editable form


#df[0]["Converted"] = standard["Letter Grade"] #= edited_df.loc[edited_df["Letter Grade"]]
#st.markdown(f"You best class is ** { average_gpa} **")
