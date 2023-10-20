import pandas as pd 
import streamlit

import json 
import pandas as pd 
import streamlit as st 
import pickle
import calendar

import plotly.graph_objects as go
from plotly.subplots import make_subplots


with open("Wasde_count.json", 'r') as file:
    loaded_dict = json.load(file)

df = pd.read_csv("Wasde_data/WASDE_statis.csv")
stations = st.sidebar.radio('Commodity',(['Corn','Wheat']))
geo_dict = {"Corn":['United States',
 'Argentina',
 'Brazil',
 'Russia',
 'South Africa',
 'Ukraine',
 'European Union',
 'Canada',
 'Mexico',"World"],
 "Wheat":['United States',
 'Argentina',
 'Austria',
 'Canada',
 'European Union',
 'Russia',
 'Ukraine',
 'India',"World"]}
Geo = st.sidebar.radio('Geography',(geo_dict[stations]))

## commodities codes

commo_code = {"Wheat":410000,"Corn":440000}

st.title("WASDE Report")

project  = pd.read_csv("Projections.csv")

year_start, year_end = st.slider('Select year range', min_value=2001, max_value=2022, value=(2018, 2022))

commod =commo_code[stations]
reg =  loaded_dict[Geo]


def give_filtered_df(com_code,coun_code,data):
    com_df = data[data["commodityCode"] == com_code]
    #com_df = com_df[com_df["marketYear"] ==]
    

    
    
    com_df = com_df[com_df["countryCode"] == coun_code]
    columns_order = ['Area Harvested','Yield','Beginning Stocks','Production','Imports','Total Supply','Exports','FSI Consumption','Feed Dom. Consumption','Total Distribution','Ending Stocks']
    com_df['Attribute'] = com_df['Attribute'].astype('category')
    com_df['Attribute'] = com_df['Attribute'].cat.set_categories(columns_order)
                                                                
    com_df = com_df.sort_values(by='Attribute')
    com_df = com_df[com_df["Attribute"].notna()]
    
    return com_df

filtered_df = df[(df['marketYear'] >= year_start) & (df['marketYear'] <= year_end)]





filtered_df = give_filtered_df(commod,reg,filtered_df)

finalpiv = filtered_df.pivot_table(columns= "marketYear",values="value",index="Attribute")

st.subheader(stations + " "+ Geo + " Report")

st.dataframe((finalpiv).round(2),width = 2000,height = 600)





