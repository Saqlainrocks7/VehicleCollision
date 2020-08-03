import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

DATA_URL = ("C:/Users/SAQLAIN/Desktop/nyc_veh_coll.csv")

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard")

@st.cache(persist=True)
def load_data(nrows):
	data = pd.read_csv(DATA_URL, nrows = nrows, parse_dates = [['DATE','TIME']])
	data.dropna(subset = ['LATITUDE', 'LONGITUDE'], inplace = True)
	lowercase = lambda x: str(x).lower()
	data.rename(lowercase, axis='columns', inplace = True)
	#data.rename(columns ={'date_time':'date/time'},inplace=True)
	data.rename(columns ={'persons injured':'persons_injured'},inplace=True)
	data.rename(columns ={'pedestrians injured':'pedestrians_injured'},inplace=True)
	data.rename(columns ={'cyclists injured':'cyclists_injured'},inplace=True)
	data.rename(columns ={'motorists injured':'motorists_injured'},inplace=True)
	data.rename(columns ={'on street name':'on_street_name'},inplace=True)
	return data
	


data = load_data(100000)
original_data = data

st.header("Where are the most people injured in NYC?")
injured_people = st.slider("Number of persons injured in vehicle collisions", 0, 32)
st.map(data.query("persons_injured >= @injured_people")[["latitude","longitude"]].dropna(how = "any"))

st.header("How many collisions occur during a given time of a day?")
hour = st.slider("Hour to look at",0,23)
data = data[data["date_time"].dt.hour == hour]

st.markdown("Vehicle collisions between %i:00 and %i:00" % (hour, (hour + 1) % 24))

midpoint = (np.average(data['latitude']),np.average(data['longitude']))

st.write(pdk.Deck(
	map_style = "mapbox://styles/mapbox/light-v9",
	initial_view_state={
	   "latitude": midpoint[0],
	   "longitude": midpoint[1],
	   "zoom": 11,
	   "pitch": 50,
	},
	layers=[
	    pdk.Layer(
	    	"HexagonLayer",
	    	data = data[['date_time','latitude','longitude']],
	    	get_position = ['longitude','latitude'],
	    	radius = 100,
	    	extruded  = True,
	    	pickable = True,
	    	elevation_scale = True,
	    	elevation_range = [0,1000],
	    	),
	    ],
	))

st.subheader("Breakdown by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24))
filtered = data[(data['date_time'].dt.hour >= hour) & (data['date_time'].dt.hour < (hour + 1))]
hist = np.histogram(filtered['date_time'].dt.minute, bins=60, range=(0,60))[0]
chart_data = pd.DataFrame({'minute': range(60), 'crashes': hist})
fig = px.bar(chart_data, x='minute', y='crashes', hover_data=['minute','crashes'], height=400)
st.write(fig)

st.header("Top 5 dangerous streets by affected type")
select = st.selectbox("Affected type of people", ['Pedestrians','Cyclists','Motorists'])

if select == 'Pedestrians':
	st.write(original_data.query('pedestrians_injured >= 1')[['on_street_name','pedestrians_injured']].sort_values(by=['pedestrians_injured'], ascending = False).dropna(how='any')[:5])


elif select == 'Cyclists':
	st.write(original_data.query('cyclists_injured >= 1')[['on_street_name','cyclists_injured']].sort_values(by=['cyclists_injured'], ascending = False).dropna(how='any')[:5])


else: 
	st.write(original_data.query('motorists_injured >= 1')[['on_street_name','motorists_injured']].sort_values(by=['motorists_injured'], ascending = False).dropna(how='any')[:5])



if st.checkbox("Show Raw Data",False):
	st.subheader("Raw Data")
	st.write(data)

