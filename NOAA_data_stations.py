import requests
import pandas as pd 
import numpy as np 

from stqdm import stqdm

from datetime import date
today = str(date.today())

url ="https://ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations={}&startDate=2010-01-01&endDate={}&includeAttributes=true&format=json"
chic_url = url.format('USW00094846',today)
iowa_burlington = url.format("USW00014937",today)
mins_st = url.format('USW00014922',today)
indianapolis_int = url.format('USW00093819',today)
ohio_john_Glenn = url.format('USW00014821',today)



bombay = url.format('IN012070800',today)
lucknow = url.format('IN023351400',today)
banglore = url.format('IN009010100',today)
chennai = url.format('IN020040900',today)
bihar_gatya = url.format('IN004051800',today)








# Add it to the streamlit 

soyabean_stations = {'USW00094846':"Chicago","USW00014933":"Iowa",
'USW00014922':"Minnesota",'USW00093819':'Indiana',
'USW00014821':'Ohio','IN012070800':"Bombay",
"IN023351400":"Lucknow",'IN020040900':"Chennai",'IN009010100':'Banglore','IN004051800':'Bihar'}

#soyabean = [chic_url,iowa_burlington,mins_st,indianapolis_int,ohio_john_Glenn]



def celsius_to_fahrenheit(celsius):
    celsius = celsius/10
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



def station_update():
	data_list = []


	for i in stqdm(list(soyabean_stations.keys())):
        
        

	    url_ = url.format(i,today)
	    print(soyabean_stations[i])
	    
	    
	    r = requests.get(url_)
	    dfs=pd.DataFrame(r.json())
	    #cols = ['DATE', 'STATION','TMAX', 'TAVG', 'TMIN']

	    dfs[['TMAX', 'TAVG', 'TMIN','PRCP']] = dfs[['TMAX', 'TAVG', 'TMIN','PRCP']].astype("float64")
	    dfs[['TMAX', 'TAVG', 'TMIN','PRCP']] = dfs[['TMAX', 'TAVG', 'TMIN','PRCP']].interpolate()
	    dfs["TAVG"]=dfs["TAVG"].map(celsius_to_fahrenheit)
	    dfs["Region"] = soyabean_stations[i]
	    dfs["DATE"] =  pd.to_datetime(dfs["DATE"])
	    
	    dfs["Week_number"] = dfs["DATE"].dt.isocalendar().week
	    dfs["Year"] = dfs["DATE"].dt.year
	    dfs["Month"] = dfs["DATE"].dt.month
	    dfs["PRCP"]=dfs["PRCP"]/254
	    dfs["HDD"] = dfs["TAVG"].apply(lambda x: 0 if 65-x<0 else 65-x)
	    dfs["CDD"] = dfs["TAVG"].apply(lambda x: 0 if x-65<0 else x-65)

        
	   
	    
	    data_list.append(dfs)

	    data = pd.concat(data_list)

	return data
    
    