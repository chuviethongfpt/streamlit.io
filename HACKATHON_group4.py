import pandas as pd
import numpy as np
import altair as alt
import PIL as Image
import base64
import seaborn as sns
import streamlit as st
import scipy.stats as stats
import math
import streamlit.components.v1 as components
import streamlit.components.v1 as stc 
import matplotlib.pyplot as plt
import os
import pickle
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import html5lib
from bs4 import BeautifulSoup
import codecs
import streamlit.components.v1 as components

st.title('DATAcracy HACKATHON')
st.subheader('Welcome to Group 4 - Handpick team 🌟')

#Upload file
# st.markdown("### **🗂️ Order Processed 🗂️**")
# csv_file= open("C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\order_processed.csv")
# dff1 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\order_processed.csv")
# st.dataframe(dff1)
# st.markdown("### **🗂️ Listening Processed 🗂️**")
# dff2 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\listening_processed.csv")
# st.dataframe(dff2)
# st.markdown("### **🗂️ User Processed 🗂️**")
# dff3 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\user_processed.csv")
# st.dataframe(dff3)
# st.markdown("### **🗂️ Cluster Processed 🗂️**")
# dff4 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\clustering_processed.csv")
# st.dataframe(dff4)

def load_df():
    df = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\basketanalysis1.csv")
    return df
def load_df1():
    df1 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\basketanalysis4.csv")
    return df1
def load_df2():
    df2 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\basketanalysis3.csv")
    return df2
def load_df3():
    df3 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\basketanalysis2.csv")
    return df3
def load_df4():
    df4 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\free1824.csv")
    return df4
def load_df5():
    df5 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\free2534.csv")
    return df5
def load_df6():
    df6 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\free3544.csv")
    return df6
def load_df7():
    df7 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\none.csv")
    return df7


df = load_df()
sector = df.groupby('antecedent')
df1 = load_df1()
sector1 = df1.groupby('antecedent')
df2 = load_df2()
sector2 = df2.groupby('antecedent')
df3 = load_df3()
sector3 = df3.groupby('antecedent')
df4 = load_df4()
sector4 = df4.groupby('antecedent')
df5 = load_df5()
sector5 = df5.groupby('antecedent')
df6 = load_df6()
sector6 = df6.groupby('antecedent')
df7 = load_df7()
sector7 = df7.groupby('antecedent')



#Sidebar
selected_age = st.sidebar.selectbox("📍 Age Range 📍", ["None","18-24", "25-34", "35-44"])
selected_type1= st.sidebar.checkbox("Paid-Users")
selected_type2= st.sidebar.checkbox("Free-Users")

current_df = df

if selected_age == None and selected_type1:
  print(selected_age, 'df')
  current_df = df
  sector = df['antecedent']
elif selected_age == None and selected_type2:
  print(selected_age, 'df 7')
  current_df = df7
  sector = df7['antecedent']
elif selected_age == '18-24' and selected_type1:
  print(selected_age, 'df 1')
  current_df = df1
  sector = df1['antecedent']
elif selected_age == '18-24' and selected_type2:
  print(selected_age, 'df 4')
  current_df = df4
  sector = df4['antecedent'] 
elif selected_age == '25-34' and selected_type1:
  print(selected_age, 'df 2')
  print(selected_type1)
  current_df = df2
  sector = df2['antecedent']
elif selected_age == '25-34' and selected_type2:
  print(selected_age, 'df 5')
  print(selected_type2)
  current_df = df5
  sector = df5['antecedent']
elif selected_age == '35-44' and selected_type2:
  print(selected_age, 'df 6')
  print(selected_type2)
  current_df = df6
  print(current_df)
  print(df6)
  sector = df6['antecedent']
else:
  print(selected_age, 'df 3')
  print(selected_type1)
  current_df = df3
  sector = df3['antecedent']

sorted_sector_unique = sorted(current_df['antecedent'].unique() )
selected_sector = st.sidebar.multiselect('Books', sorted_sector_unique, sorted_sector_unique)

# Filtering data
df_selected_sector = current_df[(current_df['antecedent'].isin(selected_sector)) ]

st.header('📚 Combo Recommendation 📚')
st.write('Data Info: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)

#HTML file
f = open('GFG.html','w')
html_template = """<html>
<head></head>
<body>
<h2>Dashboard</h2>
<iframe width="700" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiYTk5NDAwYzEtYzMxYS00ODJjLTgzMzQtNDAxZjZiYTg1YjUxIiwidCI6ImYwMWU5MzBhLWI1MmUtNDJiMS1iNzBmLWE4ODgyYjVkMDQzYiIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>
</body>
</html>
"""
f.write(html_template)
f.close()
file = codecs.open("GFG.html", 'r', "utf-8")
print(file.read())
components.html(html_template, height=900)
