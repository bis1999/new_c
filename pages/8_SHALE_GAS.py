import streamlit as st
import pandas as pd 
import numpy as np 

import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.title("SHALE GAS")

DPR= pd.read_csv("Final_rig_data.csv")




page = st.sidebar.radio("Navigation", ["DPR", "DUC"])

regions = st.sidebar.radio("Regions", ["Oil Regions", "Natural Gas Regions","All Regions"])




if page == "DPR":

    reg = {"Natural Gas Regions":["Haynesville",'Appalachia'],
    "Oil Regions":['Anadarko', 'Bakken', 'DPR Regions', 'Eagle Ford', 'Niobrara', 'Permian']}

    regions = list(reg[regions])





    







    def pivot_gen(df, val, agg_='mean', idx='Month', cols='Year'):

        return pd.pivot_table(df, values=val, index=idx, columns=cols, aggfunc=agg_, margins=True)
       

    # Assuming you have the DataFrame 'your_dataframe' containing the data

    # Get the pivot tables

   

    year_start, year_end = st.slider('Select year range', min_value=2009, max_value=2023, value=(2018, 2023))
    month_start, month_end = st.slider('Select week range', min_value=1, max_value=12 ,value=(1, 12))


    filtered_df = DPR[(DPR['Year'] >= year_start) & (DPR['Year'] <= year_end)]
    filtered_df = filtered_df[(filtered_df['Month'] >= month_start) & (filtered_df['Month'] <=  month_end)]

    cols = ['Rig count',
       'Total production Crude Oil',
        'Total production Natural Gas']

    for j in regions:
        for k in cols:
            new_df = filtered_df [filtered_df ["Region"] == j]
            
            st.subheader("Piviots Tables for {} {}".format(j,k))
            st.dataframe(pivot_gen(filtered_df,k).round(2),width = 700)







else:
    df = pd.read_csv("DUC.csv")

    reg = {"Natural Gas Regions":["Haynesville",'Appalachia'],
    "Oil Regions":['Anadarko', 'Bakken',  'Eagle Ford', 'Niobrara', 'Permian'],
    "All Regions":["DPR Regions"]}


    

    

    def pivot_gen(df, val, agg_='mean', idx='Month', cols='Year'):
        return pd.pivot_table(df, values=val, index=idx, columns=cols, aggfunc=agg_, margins=True)

     



   


    

   



    


    year_start, year_end = st.slider('Select year range', min_value=2009, max_value=2023, value=(2018, 2023))
    month_start, month_end = st.slider('Select week range', min_value=1, max_value=12 ,value=(1, 12))


    filtered_df = df[(df['Year'] >= year_start) & (df['Year'] <= year_end)]
    filtered_df = filtered_df[(filtered_df['Month'] >= month_start) & (filtered_df['Month'] <=  month_end)]


    st.subheader("Piviots Tables for {}".format(page))

    for i in list(reg[regions]):
        for k in filtered_df.columns:
            if i in k:
                st.subheader(k)
                st.dataframe(pivot_gen(filtered_df,k).round(2),width = 700)
            else:
                pass

            





    

        


            


      