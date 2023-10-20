import pandas as pd 
import streamlit


import pandas as pd 
import streamlit as st 
import pickle
import calendar

import plotly.graph_objects as go
from plotly.subplots import make_subplots



df_oil = pd.read_csv("oil_914.csv")


df_gas = pd.read_csv("gas_914.csv")



type_ = st.sidebar.radio('TYPE',(['GAS','OIL']))




if type_  == "GAS":
    st.title("914 GAS Data")

    year_start, year_end = st.slider('Select year range', min_value=2016, max_value=2023, value=(2018, 2023))
    month_start, month_end = st.slider('Select month range', min_value=1, max_value=12, value=(1, 12))

    colsgas = ['Alaska Natural Gas Gross Withdrawals (Million Cubic Feet per Day)',
       'Colorado Natural Gas Gross Withdrawals (Million Cubic Feet per Day)',
       'Louisiana Natural Gas Gross Withdrawals (Million Cubic Feet per Day)',
       'New Mexico Natural Gas Gross Withdrawals (Million Cubic Feet per Day)',
       'Ohio Natural Gas Gross Withdrawals (Million Cubic Feet per Day)',
       'Oklahoma Natural Gas Gross Withdrawals (Million Cubic Feet per Day)',
       'Pennsylvania Natural Gas Gross Withdrawals (Million Cubic Feet per Day)',
       'Texas Natural Gas Gross Withdrawals (Million Cubic Feet per Day)',
       'West Virginia Natural Gas Gross Withdrawals (Million Cubic Feet per Day)']

    filtered_df = df_gas[(df_gas['Year'] >= year_start) & (df_gas['Year'] <= year_end)]
    filtered_df = filtered_df[(filtered_df['Month'] >= month_start) & (filtered_df['Month'] <= month_end)]
    


    for i in  list(colsgas):
        st.subheader(i + " " )
        
        
        result = filtered_df.pivot_table(index = "Month",columns="Year",values = i)
        

        # Insert means as a new row and a new colu
            
        st.dataframe((result).round(2),width = 700)

else:

    st.title("914 OIL Data")

    year_start, year_end = st.slider('Select year range', min_value=2016, max_value=2023, value=(2018, 2023))
    month_start, month_end = st.slider('Select month range', min_value=1, max_value=12, value=(1, 12))

    colsgas = [ 'Alaska Field Production of Crude Oil (Thousand Barrels per Day)',
       'Colorado Field Production of Crude Oil (Thousand Barrels per Day)',
       'Federal Offshore--Gulf of Mexico Field Production of Crude Oil (Thousand Barrels per Day)',
       'New Mexico Field Production of Crude Oil (Thousand Barrels per Day)',
       'North Dakota Field Production of Crude Oil (Thousand Barrels per Day)',
       'Oklahoma Field Production of Crude Oil (Thousand Barrels per Day)',
       'Texas Field Production of Crude Oil (Thousand Barrels per Day)']

    filtered_df = df_oil[(df_oil['Year'] >= year_start) & (df_oil['Year'] <= year_end)]
    filtered_df = filtered_df[(filtered_df['Month'] >= month_start) & (filtered_df['Month'] <= month_end)]
    


    for i in  list(colsgas):
        st.subheader(i + " " )
        
        
        result = filtered_df.pivot_table(index = "Month",columns="Year",values = i)
        

        # Insert means as a new row and a new colu
            
        st.dataframe((result).round(2),width = 700)






