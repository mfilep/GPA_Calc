
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to GPA Calculator!


"""
def gpa_num(grade):
    
    standard = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    honors = {"A": 5, "B": 4, "C": 3, "D": 2, "F": 1}
    ap = {"A": 6, "B": 5, "C": 4, "D": 3, "F": 2}
    
    try:
        gnum = grade
        return str(gnum)
    except:
        return str("Nope")
        
def test_func():
    
    return "*"

df = pd.DataFrame(
    [
        {"Year": "",
         "Semester": "",
         "Class Name": "Enter Class Name",
         "Grade": "",
         "Converted": gpa_num('Grade'),
         "Honors?": False,
         "AP?": False}        
     ])
#creates an editable form

edf = st.data_editor(df,
               column_order = ["Year", "Semester", "Class Name", "Honors?", "AP?", "Grade", "Converted"],
               column_config = {"Year": st.column_config.SelectboxColumn("Year", options = ['9', '10', '11', '12']),
                                "Semester": st.column_config.SelectboxColumn("Semester", options= ['1', '2']),
                                "Grade": st.column_config.SelectboxColumn("Grade", options= ['A', 'B', 'C', 'D', 'F']),
                                "Honors?": st.column_config.CheckboxColumn("Honors?"),
                                "AP?": st.column_config.CheckboxColumn("AP?"),
                                "Converted": st.column_config.TextColumn("Converted")
                               },                                
                                   num_rows="dynamic",  
              )
num = gpa_num(df['Grade'])
edf["Converted"] = num
#st.write(edf)






