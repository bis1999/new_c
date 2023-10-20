import pandas as pd 
import streamlit


import pandas as pd 
import streamlit as st 
import pickle
import calendar

import plotly.graph_objects as go
from plotly.subplots import make_subplots



df = st.session_state["NOAA_data_soyabean"] 
# pd.read_csv("NOAA_GLOBAL/NOAA_data_soyabean.csv")


per = {"Daily":"Week_number","Monthly":"Month"}
attr = {"Rainfall":"PRCP","Temperature":"TAVG","HDD":"HDD","CDD":"CDD"}
agf = {"PRCP":"sum","TAVG":"mean"}
metric = {"PRCP":"(inches)","TAVG":"(Fahrenheit)"}

st.title("NOAA Stations")







stations = st.sidebar.radio('Stations',(['Soyabean','Sugar']))
period = st.sidebar.radio('Period',(['Daily','Monthly','Season']))
attributes = st.sidebar.radio('Attributes',(["Rainfall","Temperature","HDD","CDD"]))


df["DATE"] = pd.to_datetime(df["DATE"])
df["Day"] = df["DATE"].dt.day


months = list(calendar.month_name)[1:]
mons_dic = dict(zip(months,list(range(1,13))))



if period == "Daily":

    sta = {"Soyabean":['Chicago', 'Indiana', 'Iowa', 'Minnesota', 'Ohio'],
                "Sugar":["Bombay","Lucknow","Banglore","Chennai","Bihar"]}


    
    m = st.selectbox("Select the month",list(range(1,13)))
    

    year_start, year_end = st.slider('Select year range', min_value=2016, max_value=2023, value=(2018, 2023))




    filtered_df = df[df["Month"] == m]
    filtered_df = filtered_df [(filtered_df ['Year'] >= year_start) & (filtered_df ['Year'] <= year_end)]

    val = attr[attributes]


    for i in  list(sta[stations]):

        st.subheader(i + " ")
        


        df  = filtered_df[filtered_df["Region"] == i]
        result = df.pivot_table(columns='Year',values =val,index ="Day")
        row_means = result.mean(axis=1)
        col_sum = result.sum(axis=0)
        overall_mean = result.values.mean()
        

        # Insert means as a new row and a new column
        result.loc["Sum", :] = col_sum
        result.loc[:, "Mean"] = row_means
        
        st.dataframe((result).round(2),width = 700)
            


    










    





else:




    sta = {"Soyabean":['Chicago', 'Indiana', 'Iowa', 'Minnesota', 'Ohio'],
                "Sugar":["Bombay","Lucknow","Banglore","Chennai","Bihar"]}







    

    




    def pivot_generation(df,val,cols,idx,agf):
        return df.pivot_table(columns=cols,values =val,index =idx,aggfunc=agf)


    year_start, year_end = st.slider('Select year range', min_value=2016, max_value=2023, value=(2018, 2023))
    month_start, month_end = st.slider('Select month range', min_value=1, max_value=12, value=(1, 12))
    week_start, week_end = st.slider('Select week range', min_value=1, max_value=52, value=(1, 52))



    filtered_df = df[(df['Year'] >= year_start) & (df['Year'] <= year_end)]
    filtered_df = filtered_df[(filtered_df['Month'] >= month_start) & (filtered_df['Month'] <= month_end)]
    filtered_df = filtered_df[(filtered_df['Week_number'] >= week_start) & (filtered_df['Week_number'] <= week_end)]


    #st.subheader("Piviots Tables for {}".format(padd))

    val= attr[attributes]
    cols = "Year"
    idx = per[period]


     
    met = metric[val]



    for i in  list(sta[stations]):
        st.subheader(i + " " +met)
        


        df  = filtered_df[filtered_df["Region"] == i]
        result = pivot_generation(df,val,cols,idx,agf[val])
        row_means = result.mean(axis=1)
        col_means = result.mean(axis=0)
        overall_mean = result.values.mean()

        # Insert means as a new row and a new column
        result.loc["Mean", :] = col_means
        result.loc[:, "Mean"] = row_means
        result.at["Mean", "Mean"] = overall_mean

        col_sum = result.sum(axis=0)
        overall_mean = result.values.mean()
        

        # Insert means as a new row and a new column
        result.loc["Sum", :] = col_sum
        
            
        st.dataframe((result).round(2),width = 700)





	
	





