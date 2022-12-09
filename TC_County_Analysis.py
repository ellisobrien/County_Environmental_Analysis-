#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:26:07 2022

@author: ellisobrien
"""


#data processing and manipulatation
import pandas as pd
import numpy as np
from urllib.request import urlopen
import json

#visualization
import plotly.express as px
import plotly 

#dashboard
import streamlit as st

#hading dashboard
st.title("Transformative Communities Environmental Justice Analysis")
st.subheader('Environmental Impact Data Collaborative')
st.markdown('_This dashboard provides a tool to visualize relevent environmental and socio-economic data for 10 counties that have been identified as transformative communities by Dream.Org. This data comes from the Climate and Economic Justice Screening Tool (CEJST) and the National Risk Index (NRI). These data sets can be found on the Redivis platform maintained by the EIDC._')


csv= pd.read_csv("https://raw.githubusercontent.com/ellisobrien/County_Environmental_Analysis-/main/TC_County_Data.csv",
                   dtype={"FIPS": str})


with urlopen('https://raw.githubusercontent.com/ellisobrien/County_Environmental_Analysis-/main/TC_County.json') as response:
    tracts = json.load(response)
    
    
#county
County_Name=st.selectbox(label="Select Region for Maps",
options=('Fresno County', 'District of Columbia', 'Wayne County', 'Navajo County', 'Miami-Dade County', 'Chatham County',
'Denver County','Lumbee River', 'Clark County','Mineral County'))

#Enter Variables to Map here 
variable_to_map='Identified_as_disadvantaged'

#Enter Description 
Sepher_description='Disadvantaged'

map_dat = csv[['FIPS', 'County_Name', variable_to_map]]

if County_Name == 'Fresno County':
    x=36.137084
    y=-120.254154
elif County_Name == 'District of Columbia':
    x=38.905552
    y=-77.071546
elif County_Name == 'Wayne County':
    x=42.344638
    y=-83.130381
elif County_Name == 'Navajo County':
    x=36.242564
    y=-110.4296 
elif County_Name == 'Miami-Dade County':
    x=25.77903
    y=-80.192111
elif County_Name == 'Chatham County':
    x=32.078943
    y=-81.072284
elif County_Name == 'Denver County':
    x=39.797693
    y=-104.866388
elif County_Name == 'Lumbee River':
    x=35.162197
    y=-79.33073
elif County_Name == 'Clark County':
    x=36.188512
    y=-115.18604
elif County_Name == 'Mineral County':
    x=38.51039764409562
    y=-118.34411186319021

st.subheader('Figure 1: Justice40 Status by Census Tract')

#defining function to map input variable  
def tract_map(input_var):
    fig1 = px.choropleth_mapbox(map_dat, geojson=tracts, locations='FIPS', featureidkey="properties.FIPS", color=input_var,
                             color_discrete_map={"Not Disadvantaged": "DarkBlue", "Disadvantaged": "DarkRed"},
                               mapbox_style="carto-positron",
                               zoom=6,  center = {"lat": x, "lon": y},
                               opacity=0.5, 
                               labels={input_var:Sepher_description}
                              )
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig1.update_traces(marker_line_width=0, marker_opacity=0.7)
    fig1.update_geos(fitbounds="locations")
    st.plotly_chart(fig1)
    
#running mapping function 
tract_map(variable_to_map)

st.subheader('Figure 2: Justice40 Factors by Census Tract')

#Enter Variables to Map here 
variable_to_map_two=st.selectbox(label="Select Variable",
options=('PM2_5_in_the_air', 'Housing_burden__percent_', 'Percent_pre_1960s_housing__lead_paint_indicator_', 'Median_value_____of_owner_occupied_housing_units', 'Proximity_to_NPL__Superfund__sites', 'Wastewater_discharge', 'Diagnosed_diabetes_among_adults_aged_greater_than_or_equal_t', 'Current_asthma_among_adults_aged_greater_than_or_equal_to_18', 'Life_expectancy__years_', 'Unemployment__percent_', 'Percent_of_individuals___100__Federal_Poverty_Line', 'Percent_individuals_age_25_or_over_with_less_than_high_schoo_2' ))

map_dat2 = csv[['FIPS', 'County_Name', variable_to_map_two]]

lower_bound_draft=map_dat2[[variable_to_map_two]].min()
low=lower_bound_draft[0]
upper_bound_draft=map_dat2[[variable_to_map_two]].max()
up=upper_bound_draft[0]

pylow = low.item()

pyup = up.item()



Map_Range = st.slider(
    'Edit Map Range',
    0.0, up, (pylow, pyup))


def tract_map2(input_var):
    fig2 = px.choropleth_mapbox(map_dat2, geojson=tracts, locations='FIPS', featureidkey="properties.FIPS", color=input_var,
                               color_continuous_scale="balance",
                               range_color=Map_Range,
                               mapbox_style="carto-positron",
                               zoom=6,  center = {"lat": x, "lon": y},
                               opacity=0.5, 
                              )
    fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig2.update_traces(marker_line_width=0, marker_opacity=0.7)
    st.plotly_chart(fig2)
    
#running mapping function 
tract_map2(variable_to_map_two)


st.subheader('Figure 3: National Risk Index Data by Census Tract')

#Enter Variables to Map here 
variable_to_map_three=st.selectbox(label="Select Variable",
options=('National Risk Index - Score - Composite', 'Population (2016)', 'Building Value ($)',	'Agriculture Value ($)', 'Area (sq mi)', 'National Risk Index - Rating - Composite',	'National Risk Index - National Percentile - Composite',	'National Risk Index - State Percentile - Composite',	'Expected Annual Loss - Score - Composite',	'Expected Annual Loss - Rating - Composite',	'Expected Annual Loss - National Percentile - Composite',	'Expected Annual Loss - State Percentile - Composite',	'Expected Annual Loss - Total - Composite',	'Expected Annual Loss - Building Value - Composite',	'Expected Annual Loss - Population - Composite',	'Expected Annual Loss - Population Equivalence - Composite',	'Expected Annual Loss - Agriculture Value - Composite',	'Social Vulnerability - Score',	'Social Vulnerability - Rating',	'Social Vulnerability - National Percentile',	'Social Vulnerability - State Percentile',	'Social Vulnerability - Value',	'Community Resilience - Score',	'Community Resilience - Rating',	'Community Resilience - National Percentile',	'Community Resilience - State Percentile',	'Community Resilience - Value',	'Avalanche - Number of Events',	'Avalanche - Annualized Frequency',	'Avalanche - Exposure - Building Value',	'Avalanche - Exposure - Population',	'Avalanche - Exposure - Population Equivalence',	'Avalanche - Exposure - Total',	'Avalanche - Historic Loss Ratio - Buildings',	'Avalanche - Historic Loss Ratio - Population',	'Avalanche - Historic Loss Ratio - Total Rating',	'Avalanche - Expected Annual Loss - Building Value',	'Avalanche - Expected Annual Loss - Population',	'Avalanche - Expected Annual Loss - Population Equivalence',	'Avalanche - Expected Annual Loss - Total',	'Avalanche - Expected Annual Loss Score',	'Avalanche - Expected Annual Loss Rating',	'Avalanche - Hazard Type Risk Index Score',	'Avalanche - Hazard Type Risk Index Rating',	'Coastal Flooding - Annualized Frequency',	'Coastal Flooding - Exposure - Building Value',	'Coastal Flooding - Exposure - Population',	'Coastal Flooding - Exposure - Population Equivalence',	'Coastal Flooding - Exposure - Total',	'Coastal Flooding - Historic Loss Ratio - Buildings',	'Coastal Flooding - Historic Loss Ratio - Population',	'Coastal Flooding - Historic Loss Ratio - Total Rating',	'Coastal Flooding - Expected Annual Loss - Building Value',	'Coastal Flooding - Expected Annual Loss - Population',	'Coastal Flooding - Expected Annual Loss - Population Equivalence',	'Coastal Flooding - Expected Annual Loss - Total',	'Coastal Flooding - Expected Annual Loss Score',	'Coastal Flooding - Expected Annual Loss Rating',	'Coastal Flooding - Hazard Type Risk Index Score',	'Coastal Flooding - Hazard Type Risk Index Rating',	'Cold Wave - Number of Events',	'Cold Wave - Annualized Frequency',	'Cold Wave - Exposure - Building Value',	'Cold Wave - Exposure - Population',	'Cold Wave - Exposure - Population Equivalence',	'Cold Wave - Exposure - Agriculture Value',	'Cold Wave - Exposure - Total',	'Cold Wave - Historic Loss Ratio - Buildings',	'Cold Wave - Historic Loss Ratio - Population',	'Cold Wave - Historic Loss Ratio - Agriculture',	'Cold Wave - Historic Loss Ratio - Total Rating',	'Cold Wave - Expected Annual Loss - Building Value',	'Cold Wave - Expected Annual Loss - Population',	'Cold Wave - Expected Annual Loss - Population Equivalence',	'Cold Wave - Expected Annual Loss - Agriculture Value',	'Cold Wave - Expected Annual Loss - Total',	'Cold Wave - Expected Annual Loss Score',	'Cold Wave - Expected Annual Loss Rating',	'Cold Wave - Hazard Type Risk Index Score',	'Cold Wave - Hazard Type Risk Index Rating',	'Drought - Number of Events',	'Drought - Annualized Frequency',	'Drought - Exposure - Agriculture Value',	'Drought - Exposure - Total',	'Drought - Historic Loss Ratio - Agriculture',	'Drought - Historic Loss Ratio - Total Rating',	'Drought - Expected Annual Loss - Agriculture Value',	'Drought - Expected Annual Loss - Total',	'Drought - Expected Annual Loss Score',	'Drought - Expected Annual Loss Rating',	'Drought - Hazard Type Risk Index Score',	'Drought - Hazard Type Risk Index Rating',	'Earthquake - Annualized Frequency',	'Earthquake - Exposure - Building Value',	'Earthquake - Exposure - Population',	'Earthquake - Exposure - Population Equivalence',	'Earthquake - Exposure - Total',	'Earthquake - Historic Loss Ratio - Buildings',	'Earthquake - Historic Loss Ratio - Population',	'Earthquake - Historic Loss Ratio - Total Rating',	'Earthquake - Expected Annual Loss - Building Value',	'Earthquake - Expected Annual Loss - Population',	'Earthquake - Expected Annual Loss - Population Equivalence',	'Earthquake - Expected Annual Loss - Total',	'Earthquake - Expected Annual Loss Score',	'Earthquake - Expected Annual Loss Rating',	'Earthquake - Hazard Type Risk Index Score',	'Earthquake - Hazard Type Risk Index Rating',	'Hail - Number of Events',	'Hail - Annualized Frequency',	'Hail - Exposure - Building Value',	'Hail - Exposure - Population',	'Hail - Exposure - Population Equivalence',	'Hail - Exposure - Agriculture Value',	'Hail - Exposure - Total',	'Hail - Historic Loss Ratio - Buildings',	'Hail - Historic Loss Ratio - Population',	'Hail - Historic Loss Ratio - Agriculture',	'Hail - Historic Loss Ratio - Total Rating',	'Hail - Expected Annual Loss - Building Value',	'Hail - Expected Annual Loss - Population',	'Hail - Expected Annual Loss - Population Equivalence',	'Hail - Expected Annual Loss - Agriculture Value',	'Hail - Expected Annual Loss - Total',	'Hail - Expected Annual Loss Score',	'Hail - Expected Annual Loss Rating',	'Hail - Hazard Type Risk Index Score',	'Hail - Hazard Type Risk Index Rating',	'Heat Wave - Number of Events',	'Heat Wave - Annualized Frequency',	'Heat Wave - Exposure - Building Value',	'Heat Wave - Exposure - Population',	'Heat Wave - Exposure - Population Equivalence',	'Heat Wave - Exposure - Agriculture Value',	'Heat Wave - Exposure - Total',	'Heat Wave - Historic Loss Ratio - Buildings',	'Heat Wave - Historic Loss Ratio - Population',	'Heat Wave - Historic Loss Ratio - Agriculture',	'Heat Wave - Historic Loss Ratio - Total Rating',	'Heat Wave - Expected Annual Loss - Building Value',	'Heat Wave - Expected Annual Loss - Population',	'Heat Wave - Expected Annual Loss - Population Equivalence',	'Heat Wave - Expected Annual Loss - Agriculture Value',	'Heat Wave - Expected Annual Loss - Total',	'Heat Wave - Expected Annual Loss Score',	'Heat Wave - Expected Annual Loss Rating',	'Heat Wave - Hazard Type Risk Index Score',	'Heat Wave - Hazard Type Risk Index Rating',	'Hurricane - Number of Events',	'Hurricane - Annualized Frequency',	'Hurricane - Exposure - Building Value',	'Hurricane - Exposure - Population',	'Hurricane - Exposure - Population Equivalence',	'Hurricane - Exposure - Agriculture Value',	'Hurricane - Exposure - Total',	'Hurricane - Historic Loss Ratio - Buildings',	'Hurricane - Historic Loss Ratio - Population',	'Hurricane - Historic Loss Ratio - Agriculture',	'Hurricane - Historic Loss Ratio - Total Rating',	'Hurricane - Expected Annual Loss - Building Value',	'Hurricane - Expected Annual Loss - Population',	'Hurricane - Expected Annual Loss - Population Equivalence',	'Hurricane - Expected Annual Loss - Agriculture Value',	'Hurricane - Expected Annual Loss - Total',	'Hurricane - Expected Annual Loss Score',	'Hurricane - Expected Annual Loss Rating',	'Hurricane - Hazard Type Risk Index Score',	'Hurricane - Hazard Type Risk Index Rating',	'Ice Storm - Number of Events',	'Ice Storm - Annualized Frequency',	'Ice Storm - Exposure - Building Value',	'Ice Storm - Exposure - Population',	'Ice Storm - Exposure - Population Equivalence',	'Ice Storm - Exposure - Total',	'Ice Storm - Historic Loss Ratio - Buildings',	'Ice Storm - Historic Loss Ratio - Population',	'Ice Storm - Historic Loss Ratio - Total Rating',	'Ice Storm - Expected Annual Loss - Building Value',	'Ice Storm - Expected Annual Loss - Population',	'Ice Storm - Expected Annual Loss - Population Equivalence',	'Ice Storm - Expected Annual Loss - Total',	'Ice Storm - Expected Annual Loss Score',	'Ice Storm - Expected Annual Loss Rating',	'Ice Storm - Hazard Type Risk Index Score',	'Ice Storm - Hazard Type Risk Index Rating',	'Landslide - Number of Events',	'Landslide - Annualized Frequency',	'Landslide - Exposure - Building Value',	'Landslide - Exposure - Population',	'Landslide - Exposure - Population Equivalence',	'Landslide - Exposure - Total',	'Landslide - Historic Loss Ratio - Buildings',	'Landslide - Historic Loss Ratio - Population',	'Landslide - Historic Loss Ratio - Total Rating',	'Landslide - Expected Annual Loss - Building Value',	'Landslide - Expected Annual Loss - Population',	'Landslide - Expected Annual Loss - Population Equivalence',	'Landslide - Expected Annual Loss - Total',	'Landslide - Expected Annual Loss Score',	'Landslide - Expected Annual Loss Rating',	'Landslide - Hazard Type Risk Index Score',	'Landslide - Hazard Type Risk Index Rating',	'Lightning - Number of Events',	'Lightning - Annualized Frequency',	'Lightning - Exposure - Building Value',	'Lightning - Exposure - Population',	'Lightning - Exposure - Population Equivalence',	'Lightning - Exposure - Total',	'Lightning - Historic Loss Ratio - Buildings',	'Lightning - Historic Loss Ratio - Population',	'Lightning - Historic Loss Ratio - Total Rating',	'Lightning - Expected Annual Loss - Building Value',	'Lightning - Expected Annual Loss - Population',	'Lightning - Expected Annual Loss - Population Equivalence',	'Lightning - Expected Annual Loss - Total',	'Lightning - Expected Annual Loss Score',	'Lightning - Expected Annual Loss Rating',	'Lightning - Hazard Type Risk Index Score',	'Lightning - Hazard Type Risk Index Rating',	'Riverine Flooding - Number of Events',	'Riverine Flooding - Annualized Frequency',	'Riverine Flooding - Exposure - Building Value',	'Riverine Flooding - Exposure - Population',	'Riverine Flooding - Exposure - Population Equivalence',	'Riverine Flooding - Exposure - Agriculture Value',	'Riverine Flooding - Exposure - Total',	'Riverine Flooding - Historic Loss Ratio - Buildings',	'Riverine Flooding - Historic Loss Ratio - Population',	'Riverine Flooding - Historic Loss Ratio - Agriculture',	'Riverine Flooding - Historic Loss Ratio - Total Rating',	'Riverine Flooding - Expected Annual Loss - Building Value',	'Riverine Flooding - Expected Annual Loss - Population',	'Riverine Flooding - Expected Annual Loss - Population Equivalence',	'Riverine Flooding - Expected Annual Loss - Agriculture Value',	'Riverine Flooding - Expected Annual Loss - Total',	'Riverine Flooding - Expected Annual Loss Score',	'Riverine Flooding - Expected Annual Loss Rating',	'Riverine Flooding - Hazard Type Risk Index Score',	'Riverine Flooding - Hazard Type Risk Index Rating',	'Strong Wind - Number of Events',	'Strong Wind - Annualized Frequency',	'Strong Wind - Exposure - Building Value',	'Strong Wind - Exposure - Population',	'Strong Wind - Exposure - Population Equivalence',	'Strong Wind - Exposure - Agriculture Value',	'Strong Wind - Exposure - Total',	'Strong Wind - Historic Loss Ratio - Buildings',	'Strong Wind - Historic Loss Ratio - Population',	'Strong Wind - Historic Loss Ratio - Agriculture',	'Strong Wind - Historic Loss Ratio - Total Rating',	'Strong Wind - Expected Annual Loss - Building Value',	'Strong Wind - Expected Annual Loss - Population',	'Strong Wind - Expected Annual Loss - Population Equivalence',	'Strong Wind - Expected Annual Loss - Agriculture Value',	'Strong Wind - Expected Annual Loss - Total',	'Strong Wind - Expected Annual Loss Score',	'Strong Wind - Expected Annual Loss Rating',	'Strong Wind - Hazard Type Risk Index Score',	'Strong Wind - Hazard Type Risk Index Rating',	'Tornado - Number of Events',	'Tornado - Annualized Frequency',	'Tornado - Exposure - Building Value',	'Tornado - Exposure - Population',	'Tornado - Exposure - Population Equivalence',	'Tornado - Exposure - Agriculture Value',	'Tornado - Exposure - Total',	'Tornado - Historic Loss Ratio - Buildings',	'Tornado - Historic Loss Ratio - Population',	'Tornado - Historic Loss Ratio - Agriculture',	'Tornado - Historic Loss Ratio - Total Rating',	'Tornado - Expected Annual Loss - Building Value',	'Tornado - Expected Annual Loss - Population',	'Tornado - Expected Annual Loss - Population Equivalence',	'Tornado - Expected Annual Loss - Agriculture Value',	'Tornado - Expected Annual Loss - Total',	'Tornado - Expected Annual Loss Score',	'Tornado - Expected Annual Loss Rating',	'Tornado - Hazard Type Risk Index Score',	'Tornado - Hazard Type Risk Index Rating',	'Tsunami - Number of Events',	'Tsunami - Annualized Frequency',	'Tsunami - Exposure - Building Value',	'Tsunami - Exposure - Population',	'Tsunami - Exposure - Population Equivalence',	'Tsunami - Exposure - Total',	'Tsunami - Historic Loss Ratio - Buildings',	'Tsunami - Historic Loss Ratio - Population',	'Tsunami - Historic Loss Ratio - Total Rating',	'Tsunami - Expected Annual Loss - Building Value',	'Tsunami - Expected Annual Loss - Population',	'Tsunami - Expected Annual Loss - Population Equivalence',	'Tsunami - Expected Annual Loss - Total',	'Tsunami - Expected Annual Loss Score',	'Tsunami - Expected Annual Loss Rating',	'Tsunami - Hazard Type Risk Index Score',	'Tsunami - Hazard Type Risk Index Rating',	'Volcanic Activity - Number of Events',	'Volcanic Activity - Annualized Frequency',	'Volcanic Activity - Exposure - Building Value',	'Volcanic Activity - Exposure - Population',	'Volcanic Activity - Exposure - Population Equivalence',	'Volcanic Activity - Exposure - Total',	'Volcanic Activity - Historic Loss Ratio - Buildings',	'Volcanic Activity - Historic Loss Ratio - Population',	'Volcanic Activity - Historic Loss Ratio - Total Rating',	'Volcanic Activity - Expected Annual Loss - Building Value',	'Volcanic Activity - Expected Annual Loss - Population',	'Volcanic Activity - Expected Annual Loss - Population Equivalence',	'Volcanic Activity - Expected Annual Loss - Total',	'Volcanic Activity - Expected Annual Loss Score',	'Volcanic Activity - Expected Annual Loss Rating',	'Volcanic Activity - Hazard Type Risk Index Score',	'Volcanic Activity - Hazard Type Risk Index Rating',	'Wildfire - Annualized Frequency',	'Wildfire - Exposure - Building Value',	'Wildfire - Exposure - Population',	'Wildfire - Exposure - Population Equivalence',	'Wildfire - Exposure - Agriculture Value',	'Wildfire - Exposure - Total',	'Wildfire - Historic Loss Ratio - Buildings',	'Wildfire - Historic Loss Ratio - Population',	'Wildfire - Historic Loss Ratio - Agriculture',	'Wildfire - Historic Loss Ratio - Total Rating',	'Wildfire - Expected Annual Loss - Building Value',	'Wildfire - Expected Annual Loss - Population',	'Wildfire - Expected Annual Loss - Population Equivalence',	'Wildfire - Expected Annual Loss - Agriculture Value',	'Wildfire - Expected Annual Loss - Total',	'Wildfire - Expected Annual Loss Score',	'Wildfire - Expected Annual Loss Rating',	'Wildfire - Hazard Type Risk Index Score',	'Wildfire - Hazard Type Risk Index Rating',	'Winter Weather - Number of Events',	'Winter Weather - Annualized Frequency',	'Winter Weather - Exposure - Building Value',	'Winter Weather - Exposure - Population',	'Winter Weather - Exposure - Population Equivalence',	'Winter Weather - Exposure - Agriculture Value',	'Winter Weather - Exposure - Total',	'Winter Weather - Historic Loss Ratio - Buildings',	'Winter Weather - Historic Loss Ratio - Population',	'Winter Weather - Historic Loss Ratio - Agriculture',	'Winter Weather - Historic Loss Ratio - Total Rating',	'Winter Weather - Expected Annual Loss - Building Value',	'Winter Weather - Expected Annual Loss - Population',	'Winter Weather - Expected Annual Loss - Population Equivalence',	'Winter Weather - Expected Annual Loss - Agriculture Value',	'Winter Weather - Expected Annual Loss - Total',	'Winter Weather - Expected Annual Loss Score',	'Winter Weather - Expected Annual Loss Rating',	'Winter Weather - Hazard Type Risk Index Score',	'Winter Weather - Hazard Type Risk Index Rating', ))

map_dat3 = csv[['FIPS', 'County_Name', variable_to_map_three]]

lower_bound_draft2=map_dat3[[variable_to_map_three]].min()
low2=lower_bound_draft2[0]
upper_bound_draft2=map_dat3[[variable_to_map_three]].max()
up2=upper_bound_draft2[0]

pylow2 = low2.item()

pyup2 = up2.item()


Map_Range2 = st.slider(
    'Edit Map Range',
    0.0, pyup2, (pylow2, pyup2))

def tract_map3(input_var):
    fig3 = px.choropleth_mapbox(map_dat3, geojson=tracts, locations='FIPS', featureidkey="properties.FIPS", color=input_var,
                               color_continuous_scale="balance",
                               range_color=Map_Range2,
                               mapbox_style="carto-positron",
                               zoom=6,  center = {"lat": x, "lon": y},
                               opacity=0.5, 
                              )
    fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig3.update_traces(marker_line_width=0, marker_opacity=0.7)
    st.plotly_chart(fig3)
tract_map3(variable_to_map_three)



st.subheader('Figure 4: Relationship Between Variables (All Counties)')


variable_to_map_x=st.selectbox(label="Select X Variable",
options=('National Risk Index - Score - Composite', 'Population (2016)', 'Building Value ($)',	'Agriculture Value ($)', 'Area (sq mi)', 'National Risk Index - Rating - Composite',	'National Risk Index - National Percentile - Composite',	'National Risk Index - State Percentile - Composite',	'Expected Annual Loss - Score - Composite',	'Expected Annual Loss - Rating - Composite',	'Expected Annual Loss - National Percentile - Composite',	'Expected Annual Loss - State Percentile - Composite',	'Expected Annual Loss - Total - Composite',	'Expected Annual Loss - Building Value - Composite',	'Expected Annual Loss - Population - Composite',	'Expected Annual Loss - Population Equivalence - Composite',	'Expected Annual Loss - Agriculture Value - Composite',	'Social Vulnerability - Score',	'Social Vulnerability - Rating',	'Social Vulnerability - National Percentile',	'Social Vulnerability - State Percentile',	'Social Vulnerability - Value',	'Community Resilience - Score',	'Community Resilience - Rating',	'Community Resilience - National Percentile',	'Community Resilience - State Percentile',	'Community Resilience - Value',	'Avalanche - Number of Events',	'Avalanche - Annualized Frequency',	'Avalanche - Exposure - Building Value',	'Avalanche - Exposure - Population',	'Avalanche - Exposure - Population Equivalence',	'Avalanche - Exposure - Total',	'Avalanche - Historic Loss Ratio - Buildings',	'Avalanche - Historic Loss Ratio - Population',	'Avalanche - Historic Loss Ratio - Total Rating',	'Avalanche - Expected Annual Loss - Building Value',	'Avalanche - Expected Annual Loss - Population',	'Avalanche - Expected Annual Loss - Population Equivalence',	'Avalanche - Expected Annual Loss - Total',	'Avalanche - Expected Annual Loss Score',	'Avalanche - Expected Annual Loss Rating',	'Avalanche - Hazard Type Risk Index Score',	'Avalanche - Hazard Type Risk Index Rating',	'Coastal Flooding - Annualized Frequency',	'Coastal Flooding - Exposure - Building Value',	'Coastal Flooding - Exposure - Population',	'Coastal Flooding - Exposure - Population Equivalence',	'Coastal Flooding - Exposure - Total',	'Coastal Flooding - Historic Loss Ratio - Buildings',	'Coastal Flooding - Historic Loss Ratio - Population',	'Coastal Flooding - Historic Loss Ratio - Total Rating',	'Coastal Flooding - Expected Annual Loss - Building Value',	'Coastal Flooding - Expected Annual Loss - Population',	'Coastal Flooding - Expected Annual Loss - Population Equivalence',	'Coastal Flooding - Expected Annual Loss - Total',	'Coastal Flooding - Expected Annual Loss Score',	'Coastal Flooding - Expected Annual Loss Rating',	'Coastal Flooding - Hazard Type Risk Index Score',	'Coastal Flooding - Hazard Type Risk Index Rating',	'Cold Wave - Number of Events',	'Cold Wave - Annualized Frequency',	'Cold Wave - Exposure - Building Value',	'Cold Wave - Exposure - Population',	'Cold Wave - Exposure - Population Equivalence',	'Cold Wave - Exposure - Agriculture Value',	'Cold Wave - Exposure - Total',	'Cold Wave - Historic Loss Ratio - Buildings',	'Cold Wave - Historic Loss Ratio - Population',	'Cold Wave - Historic Loss Ratio - Agriculture',	'Cold Wave - Historic Loss Ratio - Total Rating',	'Cold Wave - Expected Annual Loss - Building Value',	'Cold Wave - Expected Annual Loss - Population',	'Cold Wave - Expected Annual Loss - Population Equivalence',	'Cold Wave - Expected Annual Loss - Agriculture Value',	'Cold Wave - Expected Annual Loss - Total',	'Cold Wave - Expected Annual Loss Score',	'Cold Wave - Expected Annual Loss Rating',	'Cold Wave - Hazard Type Risk Index Score',	'Cold Wave - Hazard Type Risk Index Rating',	'Drought - Number of Events',	'Drought - Annualized Frequency',	'Drought - Exposure - Agriculture Value',	'Drought - Exposure - Total',	'Drought - Historic Loss Ratio - Agriculture',	'Drought - Historic Loss Ratio - Total Rating',	'Drought - Expected Annual Loss - Agriculture Value',	'Drought - Expected Annual Loss - Total',	'Drought - Expected Annual Loss Score',	'Drought - Expected Annual Loss Rating',	'Drought - Hazard Type Risk Index Score',	'Drought - Hazard Type Risk Index Rating',	'Earthquake - Annualized Frequency',	'Earthquake - Exposure - Building Value',	'Earthquake - Exposure - Population',	'Earthquake - Exposure - Population Equivalence',	'Earthquake - Exposure - Total',	'Earthquake - Historic Loss Ratio - Buildings',	'Earthquake - Historic Loss Ratio - Population',	'Earthquake - Historic Loss Ratio - Total Rating',	'Earthquake - Expected Annual Loss - Building Value',	'Earthquake - Expected Annual Loss - Population',	'Earthquake - Expected Annual Loss - Population Equivalence',	'Earthquake - Expected Annual Loss - Total',	'Earthquake - Expected Annual Loss Score',	'Earthquake - Expected Annual Loss Rating',	'Earthquake - Hazard Type Risk Index Score',	'Earthquake - Hazard Type Risk Index Rating',	'Hail - Number of Events',	'Hail - Annualized Frequency',	'Hail - Exposure - Building Value',	'Hail - Exposure - Population',	'Hail - Exposure - Population Equivalence',	'Hail - Exposure - Agriculture Value',	'Hail - Exposure - Total',	'Hail - Historic Loss Ratio - Buildings',	'Hail - Historic Loss Ratio - Population',	'Hail - Historic Loss Ratio - Agriculture',	'Hail - Historic Loss Ratio - Total Rating',	'Hail - Expected Annual Loss - Building Value',	'Hail - Expected Annual Loss - Population',	'Hail - Expected Annual Loss - Population Equivalence',	'Hail - Expected Annual Loss - Agriculture Value',	'Hail - Expected Annual Loss - Total',	'Hail - Expected Annual Loss Score',	'Hail - Expected Annual Loss Rating',	'Hail - Hazard Type Risk Index Score',	'Hail - Hazard Type Risk Index Rating',	'Heat Wave - Number of Events',	'Heat Wave - Annualized Frequency',	'Heat Wave - Exposure - Building Value',	'Heat Wave - Exposure - Population',	'Heat Wave - Exposure - Population Equivalence',	'Heat Wave - Exposure - Agriculture Value',	'Heat Wave - Exposure - Total',	'Heat Wave - Historic Loss Ratio - Buildings',	'Heat Wave - Historic Loss Ratio - Population',	'Heat Wave - Historic Loss Ratio - Agriculture',	'Heat Wave - Historic Loss Ratio - Total Rating',	'Heat Wave - Expected Annual Loss - Building Value',	'Heat Wave - Expected Annual Loss - Population',	'Heat Wave - Expected Annual Loss - Population Equivalence',	'Heat Wave - Expected Annual Loss - Agriculture Value',	'Heat Wave - Expected Annual Loss - Total',	'Heat Wave - Expected Annual Loss Score',	'Heat Wave - Expected Annual Loss Rating',	'Heat Wave - Hazard Type Risk Index Score',	'Heat Wave - Hazard Type Risk Index Rating',	'Hurricane - Number of Events',	'Hurricane - Annualized Frequency',	'Hurricane - Exposure - Building Value',	'Hurricane - Exposure - Population',	'Hurricane - Exposure - Population Equivalence',	'Hurricane - Exposure - Agriculture Value',	'Hurricane - Exposure - Total',	'Hurricane - Historic Loss Ratio - Buildings',	'Hurricane - Historic Loss Ratio - Population',	'Hurricane - Historic Loss Ratio - Agriculture',	'Hurricane - Historic Loss Ratio - Total Rating',	'Hurricane - Expected Annual Loss - Building Value',	'Hurricane - Expected Annual Loss - Population',	'Hurricane - Expected Annual Loss - Population Equivalence',	'Hurricane - Expected Annual Loss - Agriculture Value',	'Hurricane - Expected Annual Loss - Total',	'Hurricane - Expected Annual Loss Score',	'Hurricane - Expected Annual Loss Rating',	'Hurricane - Hazard Type Risk Index Score',	'Hurricane - Hazard Type Risk Index Rating',	'Ice Storm - Number of Events',	'Ice Storm - Annualized Frequency',	'Ice Storm - Exposure - Building Value',	'Ice Storm - Exposure - Population',	'Ice Storm - Exposure - Population Equivalence',	'Ice Storm - Exposure - Total',	'Ice Storm - Historic Loss Ratio - Buildings',	'Ice Storm - Historic Loss Ratio - Population',	'Ice Storm - Historic Loss Ratio - Total Rating',	'Ice Storm - Expected Annual Loss - Building Value',	'Ice Storm - Expected Annual Loss - Population',	'Ice Storm - Expected Annual Loss - Population Equivalence',	'Ice Storm - Expected Annual Loss - Total',	'Ice Storm - Expected Annual Loss Score',	'Ice Storm - Expected Annual Loss Rating',	'Ice Storm - Hazard Type Risk Index Score',	'Ice Storm - Hazard Type Risk Index Rating',	'Landslide - Number of Events',	'Landslide - Annualized Frequency',	'Landslide - Exposure - Building Value',	'Landslide - Exposure - Population',	'Landslide - Exposure - Population Equivalence',	'Landslide - Exposure - Total',	'Landslide - Historic Loss Ratio - Buildings',	'Landslide - Historic Loss Ratio - Population',	'Landslide - Historic Loss Ratio - Total Rating',	'Landslide - Expected Annual Loss - Building Value',	'Landslide - Expected Annual Loss - Population',	'Landslide - Expected Annual Loss - Population Equivalence',	'Landslide - Expected Annual Loss - Total',	'Landslide - Expected Annual Loss Score',	'Landslide - Expected Annual Loss Rating',	'Landslide - Hazard Type Risk Index Score',	'Landslide - Hazard Type Risk Index Rating',	'Lightning - Number of Events',	'Lightning - Annualized Frequency',	'Lightning - Exposure - Building Value',	'Lightning - Exposure - Population',	'Lightning - Exposure - Population Equivalence',	'Lightning - Exposure - Total',	'Lightning - Historic Loss Ratio - Buildings',	'Lightning - Historic Loss Ratio - Population',	'Lightning - Historic Loss Ratio - Total Rating',	'Lightning - Expected Annual Loss - Building Value',	'Lightning - Expected Annual Loss - Population',	'Lightning - Expected Annual Loss - Population Equivalence',	'Lightning - Expected Annual Loss - Total',	'Lightning - Expected Annual Loss Score',	'Lightning - Expected Annual Loss Rating',	'Lightning - Hazard Type Risk Index Score',	'Lightning - Hazard Type Risk Index Rating',	'Riverine Flooding - Number of Events',	'Riverine Flooding - Annualized Frequency',	'Riverine Flooding - Exposure - Building Value',	'Riverine Flooding - Exposure - Population',	'Riverine Flooding - Exposure - Population Equivalence',	'Riverine Flooding - Exposure - Agriculture Value',	'Riverine Flooding - Exposure - Total',	'Riverine Flooding - Historic Loss Ratio - Buildings',	'Riverine Flooding - Historic Loss Ratio - Population',	'Riverine Flooding - Historic Loss Ratio - Agriculture',	'Riverine Flooding - Historic Loss Ratio - Total Rating',	'Riverine Flooding - Expected Annual Loss - Building Value',	'Riverine Flooding - Expected Annual Loss - Population',	'Riverine Flooding - Expected Annual Loss - Population Equivalence',	'Riverine Flooding - Expected Annual Loss - Agriculture Value',	'Riverine Flooding - Expected Annual Loss - Total',	'Riverine Flooding - Expected Annual Loss Score',	'Riverine Flooding - Expected Annual Loss Rating',	'Riverine Flooding - Hazard Type Risk Index Score',	'Riverine Flooding - Hazard Type Risk Index Rating',	'Strong Wind - Number of Events',	'Strong Wind - Annualized Frequency',	'Strong Wind - Exposure - Building Value',	'Strong Wind - Exposure - Population',	'Strong Wind - Exposure - Population Equivalence',	'Strong Wind - Exposure - Agriculture Value',	'Strong Wind - Exposure - Total',	'Strong Wind - Historic Loss Ratio - Buildings',	'Strong Wind - Historic Loss Ratio - Population',	'Strong Wind - Historic Loss Ratio - Agriculture',	'Strong Wind - Historic Loss Ratio - Total Rating',	'Strong Wind - Expected Annual Loss - Building Value',	'Strong Wind - Expected Annual Loss - Population',	'Strong Wind - Expected Annual Loss - Population Equivalence',	'Strong Wind - Expected Annual Loss - Agriculture Value',	'Strong Wind - Expected Annual Loss - Total',	'Strong Wind - Expected Annual Loss Score',	'Strong Wind - Expected Annual Loss Rating',	'Strong Wind - Hazard Type Risk Index Score',	'Strong Wind - Hazard Type Risk Index Rating',	'Tornado - Number of Events',	'Tornado - Annualized Frequency',	'Tornado - Exposure - Building Value',	'Tornado - Exposure - Population',	'Tornado - Exposure - Population Equivalence',	'Tornado - Exposure - Agriculture Value',	'Tornado - Exposure - Total',	'Tornado - Historic Loss Ratio - Buildings',	'Tornado - Historic Loss Ratio - Population',	'Tornado - Historic Loss Ratio - Agriculture',	'Tornado - Historic Loss Ratio - Total Rating',	'Tornado - Expected Annual Loss - Building Value',	'Tornado - Expected Annual Loss - Population',	'Tornado - Expected Annual Loss - Population Equivalence',	'Tornado - Expected Annual Loss - Agriculture Value',	'Tornado - Expected Annual Loss - Total',	'Tornado - Expected Annual Loss Score',	'Tornado - Expected Annual Loss Rating',	'Tornado - Hazard Type Risk Index Score',	'Tornado - Hazard Type Risk Index Rating',	'Tsunami - Number of Events',	'Tsunami - Annualized Frequency',	'Tsunami - Exposure - Building Value',	'Tsunami - Exposure - Population',	'Tsunami - Exposure - Population Equivalence',	'Tsunami - Exposure - Total',	'Tsunami - Historic Loss Ratio - Buildings',	'Tsunami - Historic Loss Ratio - Population',	'Tsunami - Historic Loss Ratio - Total Rating',	'Tsunami - Expected Annual Loss - Building Value',	'Tsunami - Expected Annual Loss - Population',	'Tsunami - Expected Annual Loss - Population Equivalence',	'Tsunami - Expected Annual Loss - Total',	'Tsunami - Expected Annual Loss Score',	'Tsunami - Expected Annual Loss Rating',	'Tsunami - Hazard Type Risk Index Score',	'Tsunami - Hazard Type Risk Index Rating',	'Volcanic Activity - Number of Events',	'Volcanic Activity - Annualized Frequency',	'Volcanic Activity - Exposure - Building Value',	'Volcanic Activity - Exposure - Population',	'Volcanic Activity - Exposure - Population Equivalence',	'Volcanic Activity - Exposure - Total',	'Volcanic Activity - Historic Loss Ratio - Buildings',	'Volcanic Activity - Historic Loss Ratio - Population',	'Volcanic Activity - Historic Loss Ratio - Total Rating',	'Volcanic Activity - Expected Annual Loss - Building Value',	'Volcanic Activity - Expected Annual Loss - Population',	'Volcanic Activity - Expected Annual Loss - Population Equivalence',	'Volcanic Activity - Expected Annual Loss - Total',	'Volcanic Activity - Expected Annual Loss Score',	'Volcanic Activity - Expected Annual Loss Rating',	'Volcanic Activity - Hazard Type Risk Index Score',	'Volcanic Activity - Hazard Type Risk Index Rating',	'Wildfire - Annualized Frequency',	'Wildfire - Exposure - Building Value',	'Wildfire - Exposure - Population',	'Wildfire - Exposure - Population Equivalence',	'Wildfire - Exposure - Agriculture Value',	'Wildfire - Exposure - Total',	'Wildfire - Historic Loss Ratio - Buildings',	'Wildfire - Historic Loss Ratio - Population',	'Wildfire - Historic Loss Ratio - Agriculture',	'Wildfire - Historic Loss Ratio - Total Rating',	'Wildfire - Expected Annual Loss - Building Value',	'Wildfire - Expected Annual Loss - Population',	'Wildfire - Expected Annual Loss - Population Equivalence',	'Wildfire - Expected Annual Loss - Agriculture Value',	'Wildfire - Expected Annual Loss - Total',	'Wildfire - Expected Annual Loss Score',	'Wildfire - Expected Annual Loss Rating',	'Wildfire - Hazard Type Risk Index Score',	'Wildfire - Hazard Type Risk Index Rating',	'Winter Weather - Number of Events',	'Winter Weather - Annualized Frequency',	'Winter Weather - Exposure - Building Value',	'Winter Weather - Exposure - Population',	'Winter Weather - Exposure - Population Equivalence',	'Winter Weather - Exposure - Agriculture Value',	'Winter Weather - Exposure - Total',	'Winter Weather - Historic Loss Ratio - Buildings',	'Winter Weather - Historic Loss Ratio - Population',	'Winter Weather - Historic Loss Ratio - Agriculture',	'Winter Weather - Historic Loss Ratio - Total Rating',	'Winter Weather - Expected Annual Loss - Building Value',	'Winter Weather - Expected Annual Loss - Population',	'Winter Weather - Expected Annual Loss - Population Equivalence',	'Winter Weather - Expected Annual Loss - Agriculture Value',	'Winter Weather - Expected Annual Loss - Total',	'Winter Weather - Expected Annual Loss Score',	'Winter Weather - Expected Annual Loss Rating',	'Winter Weather - Hazard Type Risk Index Score',	'Winter Weather - Hazard Type Risk Index Rating', 'PM2_5_in_the_air', 'Housing_burden__percent_', 'Percent_pre_1960s_housing__lead_paint_indicator_', 'Median_value_____of_owner_occupied_housing_units', 'Proximity_to_NPL__Superfund__sites', 'Wastewater_discharge', 'Diagnosed_diabetes_among_adults_aged_greater_than_or_equal_t', 'Current_asthma_among_adults_aged_greater_than_or_equal_to_18', 'Life_expectancy__years_', 'Unemployment__percent_', 'Percent_of_individuals___100__Federal_Poverty_Line', 'Percent_individuals_age_25_or_over_with_less_than_high_schoo_2'))

#Enter X variable and Description 
lower_bound_draft3=csv[[variable_to_map_x]].min()
low3=lower_bound_draft3[0]

upper_bound_draft3=csv[[variable_to_map_x]].max()
up3=upper_bound_draft3[0]

pylow3 = low3.item()

pyup3 = up3.item()

Map_Rangex = st.slider(
    'Edit X Range',
    0.0, pyup3, (pylow3, pyup3))


#Enter Variables to Map here 
variable_to_map_y=st.selectbox(label="Select Y Variable",
options=('Percent_of_individuals___100__Federal_Poverty_Line', 'PM2_5_in_the_air', 'Housing_burden__percent_', 'Percent_pre_1960s_housing__lead_paint_indicator_', 'Median_value_____of_owner_occupied_housing_units', 'Proximity_to_NPL__Superfund__sites', 'Wastewater_discharge', 'Diagnosed_diabetes_among_adults_aged_greater_than_or_equal_t', 'Current_asthma_among_adults_aged_greater_than_or_equal_to_18', 'Life_expectancy__years_', 'Unemployment__percent_', 'Percent_individuals_age_25_or_over_with_less_than_high_schoo_2''National Risk Index - Score - Composite', 'Population (2016)', 'Building Value ($)',	'Agriculture Value ($)', 'Area (sq mi)', 'National Risk Index - Rating - Composite',	'National Risk Index - National Percentile - Composite',	'National Risk Index - State Percentile - Composite',	'Expected Annual Loss - Score - Composite',	'Expected Annual Loss - Rating - Composite',	'Expected Annual Loss - National Percentile - Composite',	'Expected Annual Loss - State Percentile - Composite',	'Expected Annual Loss - Total - Composite',	'Expected Annual Loss - Building Value - Composite',	'Expected Annual Loss - Population - Composite',	'Expected Annual Loss - Population Equivalence - Composite',	'Expected Annual Loss - Agriculture Value - Composite',	'Social Vulnerability - Score',	'Social Vulnerability - Rating',	'Social Vulnerability - National Percentile',	'Social Vulnerability - State Percentile',	'Social Vulnerability - Value',	'Community Resilience - Score',	'Community Resilience - Rating',	'Community Resilience - National Percentile',	'Community Resilience - State Percentile',	'Community Resilience - Value',	'Avalanche - Number of Events',	'Avalanche - Annualized Frequency',	'Avalanche - Exposure - Building Value',	'Avalanche - Exposure - Population',	'Avalanche - Exposure - Population Equivalence',	'Avalanche - Exposure - Total',	'Avalanche - Historic Loss Ratio - Buildings',	'Avalanche - Historic Loss Ratio - Population',	'Avalanche - Historic Loss Ratio - Total Rating',	'Avalanche - Expected Annual Loss - Building Value',	'Avalanche - Expected Annual Loss - Population',	'Avalanche - Expected Annual Loss - Population Equivalence',	'Avalanche - Expected Annual Loss - Total',	'Avalanche - Expected Annual Loss Score',	'Avalanche - Expected Annual Loss Rating',	'Avalanche - Hazard Type Risk Index Score',	'Avalanche - Hazard Type Risk Index Rating',	'Coastal Flooding - Annualized Frequency',	'Coastal Flooding - Exposure - Building Value',	'Coastal Flooding - Exposure - Population',	'Coastal Flooding - Exposure - Population Equivalence',	'Coastal Flooding - Exposure - Total',	'Coastal Flooding - Historic Loss Ratio - Buildings',	'Coastal Flooding - Historic Loss Ratio - Population',	'Coastal Flooding - Historic Loss Ratio - Total Rating',	'Coastal Flooding - Expected Annual Loss - Building Value',	'Coastal Flooding - Expected Annual Loss - Population',	'Coastal Flooding - Expected Annual Loss - Population Equivalence',	'Coastal Flooding - Expected Annual Loss - Total',	'Coastal Flooding - Expected Annual Loss Score',	'Coastal Flooding - Expected Annual Loss Rating',	'Coastal Flooding - Hazard Type Risk Index Score',	'Coastal Flooding - Hazard Type Risk Index Rating',	'Cold Wave - Number of Events',	'Cold Wave - Annualized Frequency',	'Cold Wave - Exposure - Building Value',	'Cold Wave - Exposure - Population',	'Cold Wave - Exposure - Population Equivalence',	'Cold Wave - Exposure - Agriculture Value',	'Cold Wave - Exposure - Total',	'Cold Wave - Historic Loss Ratio - Buildings',	'Cold Wave - Historic Loss Ratio - Population',	'Cold Wave - Historic Loss Ratio - Agriculture',	'Cold Wave - Historic Loss Ratio - Total Rating',	'Cold Wave - Expected Annual Loss - Building Value',	'Cold Wave - Expected Annual Loss - Population',	'Cold Wave - Expected Annual Loss - Population Equivalence',	'Cold Wave - Expected Annual Loss - Agriculture Value',	'Cold Wave - Expected Annual Loss - Total',	'Cold Wave - Expected Annual Loss Score',	'Cold Wave - Expected Annual Loss Rating',	'Cold Wave - Hazard Type Risk Index Score',	'Cold Wave - Hazard Type Risk Index Rating',	'Drought - Number of Events',	'Drought - Annualized Frequency',	'Drought - Exposure - Agriculture Value',	'Drought - Exposure - Total',	'Drought - Historic Loss Ratio - Agriculture',	'Drought - Historic Loss Ratio - Total Rating',	'Drought - Expected Annual Loss - Agriculture Value',	'Drought - Expected Annual Loss - Total',	'Drought - Expected Annual Loss Score',	'Drought - Expected Annual Loss Rating',	'Drought - Hazard Type Risk Index Score',	'Drought - Hazard Type Risk Index Rating',	'Earthquake - Annualized Frequency',	'Earthquake - Exposure - Building Value',	'Earthquake - Exposure - Population',	'Earthquake - Exposure - Population Equivalence',	'Earthquake - Exposure - Total',	'Earthquake - Historic Loss Ratio - Buildings',	'Earthquake - Historic Loss Ratio - Population',	'Earthquake - Historic Loss Ratio - Total Rating',	'Earthquake - Expected Annual Loss - Building Value',	'Earthquake - Expected Annual Loss - Population',	'Earthquake - Expected Annual Loss - Population Equivalence',	'Earthquake - Expected Annual Loss - Total',	'Earthquake - Expected Annual Loss Score',	'Earthquake - Expected Annual Loss Rating',	'Earthquake - Hazard Type Risk Index Score',	'Earthquake - Hazard Type Risk Index Rating',	'Hail - Number of Events',	'Hail - Annualized Frequency',	'Hail - Exposure - Building Value',	'Hail - Exposure - Population',	'Hail - Exposure - Population Equivalence',	'Hail - Exposure - Agriculture Value',	'Hail - Exposure - Total',	'Hail - Historic Loss Ratio - Buildings',	'Hail - Historic Loss Ratio - Population',	'Hail - Historic Loss Ratio - Agriculture',	'Hail - Historic Loss Ratio - Total Rating',	'Hail - Expected Annual Loss - Building Value',	'Hail - Expected Annual Loss - Population',	'Hail - Expected Annual Loss - Population Equivalence',	'Hail - Expected Annual Loss - Agriculture Value',	'Hail - Expected Annual Loss - Total',	'Hail - Expected Annual Loss Score',	'Hail - Expected Annual Loss Rating',	'Hail - Hazard Type Risk Index Score',	'Hail - Hazard Type Risk Index Rating',	'Heat Wave - Number of Events',	'Heat Wave - Annualized Frequency',	'Heat Wave - Exposure - Building Value',	'Heat Wave - Exposure - Population',	'Heat Wave - Exposure - Population Equivalence',	'Heat Wave - Exposure - Agriculture Value',	'Heat Wave - Exposure - Total',	'Heat Wave - Historic Loss Ratio - Buildings',	'Heat Wave - Historic Loss Ratio - Population',	'Heat Wave - Historic Loss Ratio - Agriculture',	'Heat Wave - Historic Loss Ratio - Total Rating',	'Heat Wave - Expected Annual Loss - Building Value',	'Heat Wave - Expected Annual Loss - Population',	'Heat Wave - Expected Annual Loss - Population Equivalence',	'Heat Wave - Expected Annual Loss - Agriculture Value',	'Heat Wave - Expected Annual Loss - Total',	'Heat Wave - Expected Annual Loss Score',	'Heat Wave - Expected Annual Loss Rating',	'Heat Wave - Hazard Type Risk Index Score',	'Heat Wave - Hazard Type Risk Index Rating',	'Hurricane - Number of Events',	'Hurricane - Annualized Frequency',	'Hurricane - Exposure - Building Value',	'Hurricane - Exposure - Population',	'Hurricane - Exposure - Population Equivalence',	'Hurricane - Exposure - Agriculture Value',	'Hurricane - Exposure - Total',	'Hurricane - Historic Loss Ratio - Buildings',	'Hurricane - Historic Loss Ratio - Population',	'Hurricane - Historic Loss Ratio - Agriculture',	'Hurricane - Historic Loss Ratio - Total Rating',	'Hurricane - Expected Annual Loss - Building Value',	'Hurricane - Expected Annual Loss - Population',	'Hurricane - Expected Annual Loss - Population Equivalence',	'Hurricane - Expected Annual Loss - Agriculture Value',	'Hurricane - Expected Annual Loss - Total',	'Hurricane - Expected Annual Loss Score',	'Hurricane - Expected Annual Loss Rating',	'Hurricane - Hazard Type Risk Index Score',	'Hurricane - Hazard Type Risk Index Rating',	'Ice Storm - Number of Events',	'Ice Storm - Annualized Frequency',	'Ice Storm - Exposure - Building Value',	'Ice Storm - Exposure - Population',	'Ice Storm - Exposure - Population Equivalence',	'Ice Storm - Exposure - Total',	'Ice Storm - Historic Loss Ratio - Buildings',	'Ice Storm - Historic Loss Ratio - Population',	'Ice Storm - Historic Loss Ratio - Total Rating',	'Ice Storm - Expected Annual Loss - Building Value',	'Ice Storm - Expected Annual Loss - Population',	'Ice Storm - Expected Annual Loss - Population Equivalence',	'Ice Storm - Expected Annual Loss - Total',	'Ice Storm - Expected Annual Loss Score',	'Ice Storm - Expected Annual Loss Rating',	'Ice Storm - Hazard Type Risk Index Score',	'Ice Storm - Hazard Type Risk Index Rating',	'Landslide - Number of Events',	'Landslide - Annualized Frequency',	'Landslide - Exposure - Building Value',	'Landslide - Exposure - Population',	'Landslide - Exposure - Population Equivalence',	'Landslide - Exposure - Total',	'Landslide - Historic Loss Ratio - Buildings',	'Landslide - Historic Loss Ratio - Population',	'Landslide - Historic Loss Ratio - Total Rating',	'Landslide - Expected Annual Loss - Building Value',	'Landslide - Expected Annual Loss - Population',	'Landslide - Expected Annual Loss - Population Equivalence',	'Landslide - Expected Annual Loss - Total',	'Landslide - Expected Annual Loss Score',	'Landslide - Expected Annual Loss Rating',	'Landslide - Hazard Type Risk Index Score',	'Landslide - Hazard Type Risk Index Rating',	'Lightning - Number of Events',	'Lightning - Annualized Frequency',	'Lightning - Exposure - Building Value',	'Lightning - Exposure - Population',	'Lightning - Exposure - Population Equivalence',	'Lightning - Exposure - Total',	'Lightning - Historic Loss Ratio - Buildings',	'Lightning - Historic Loss Ratio - Population',	'Lightning - Historic Loss Ratio - Total Rating',	'Lightning - Expected Annual Loss - Building Value',	'Lightning - Expected Annual Loss - Population',	'Lightning - Expected Annual Loss - Population Equivalence',	'Lightning - Expected Annual Loss - Total',	'Lightning - Expected Annual Loss Score',	'Lightning - Expected Annual Loss Rating',	'Lightning - Hazard Type Risk Index Score',	'Lightning - Hazard Type Risk Index Rating',	'Riverine Flooding - Number of Events',	'Riverine Flooding - Annualized Frequency',	'Riverine Flooding - Exposure - Building Value',	'Riverine Flooding - Exposure - Population',	'Riverine Flooding - Exposure - Population Equivalence',	'Riverine Flooding - Exposure - Agriculture Value',	'Riverine Flooding - Exposure - Total',	'Riverine Flooding - Historic Loss Ratio - Buildings',	'Riverine Flooding - Historic Loss Ratio - Population',	'Riverine Flooding - Historic Loss Ratio - Agriculture',	'Riverine Flooding - Historic Loss Ratio - Total Rating',	'Riverine Flooding - Expected Annual Loss - Building Value',	'Riverine Flooding - Expected Annual Loss - Population',	'Riverine Flooding - Expected Annual Loss - Population Equivalence',	'Riverine Flooding - Expected Annual Loss - Agriculture Value',	'Riverine Flooding - Expected Annual Loss - Total',	'Riverine Flooding - Expected Annual Loss Score',	'Riverine Flooding - Expected Annual Loss Rating',	'Riverine Flooding - Hazard Type Risk Index Score',	'Riverine Flooding - Hazard Type Risk Index Rating',	'Strong Wind - Number of Events',	'Strong Wind - Annualized Frequency',	'Strong Wind - Exposure - Building Value',	'Strong Wind - Exposure - Population',	'Strong Wind - Exposure - Population Equivalence',	'Strong Wind - Exposure - Agriculture Value',	'Strong Wind - Exposure - Total',	'Strong Wind - Historic Loss Ratio - Buildings',	'Strong Wind - Historic Loss Ratio - Population',	'Strong Wind - Historic Loss Ratio - Agriculture',	'Strong Wind - Historic Loss Ratio - Total Rating',	'Strong Wind - Expected Annual Loss - Building Value',	'Strong Wind - Expected Annual Loss - Population',	'Strong Wind - Expected Annual Loss - Population Equivalence',	'Strong Wind - Expected Annual Loss - Agriculture Value',	'Strong Wind - Expected Annual Loss - Total',	'Strong Wind - Expected Annual Loss Score',	'Strong Wind - Expected Annual Loss Rating',	'Strong Wind - Hazard Type Risk Index Score',	'Strong Wind - Hazard Type Risk Index Rating',	'Tornado - Number of Events',	'Tornado - Annualized Frequency',	'Tornado - Exposure - Building Value',	'Tornado - Exposure - Population',	'Tornado - Exposure - Population Equivalence',	'Tornado - Exposure - Agriculture Value',	'Tornado - Exposure - Total',	'Tornado - Historic Loss Ratio - Buildings',	'Tornado - Historic Loss Ratio - Population',	'Tornado - Historic Loss Ratio - Agriculture',	'Tornado - Historic Loss Ratio - Total Rating',	'Tornado - Expected Annual Loss - Building Value',	'Tornado - Expected Annual Loss - Population',	'Tornado - Expected Annual Loss - Population Equivalence',	'Tornado - Expected Annual Loss - Agriculture Value',	'Tornado - Expected Annual Loss - Total',	'Tornado - Expected Annual Loss Score',	'Tornado - Expected Annual Loss Rating',	'Tornado - Hazard Type Risk Index Score',	'Tornado - Hazard Type Risk Index Rating',	'Tsunami - Number of Events',	'Tsunami - Annualized Frequency',	'Tsunami - Exposure - Building Value',	'Tsunami - Exposure - Population',	'Tsunami - Exposure - Population Equivalence',	'Tsunami - Exposure - Total',	'Tsunami - Historic Loss Ratio - Buildings',	'Tsunami - Historic Loss Ratio - Population',	'Tsunami - Historic Loss Ratio - Total Rating',	'Tsunami - Expected Annual Loss - Building Value',	'Tsunami - Expected Annual Loss - Population',	'Tsunami - Expected Annual Loss - Population Equivalence',	'Tsunami - Expected Annual Loss - Total',	'Tsunami - Expected Annual Loss Score',	'Tsunami - Expected Annual Loss Rating',	'Tsunami - Hazard Type Risk Index Score',	'Tsunami - Hazard Type Risk Index Rating',	'Volcanic Activity - Number of Events',	'Volcanic Activity - Annualized Frequency',	'Volcanic Activity - Exposure - Building Value',	'Volcanic Activity - Exposure - Population',	'Volcanic Activity - Exposure - Population Equivalence',	'Volcanic Activity - Exposure - Total',	'Volcanic Activity - Historic Loss Ratio - Buildings',	'Volcanic Activity - Historic Loss Ratio - Population',	'Volcanic Activity - Historic Loss Ratio - Total Rating',	'Volcanic Activity - Expected Annual Loss - Building Value',	'Volcanic Activity - Expected Annual Loss - Population',	'Volcanic Activity - Expected Annual Loss - Population Equivalence',	'Volcanic Activity - Expected Annual Loss - Total',	'Volcanic Activity - Expected Annual Loss Score',	'Volcanic Activity - Expected Annual Loss Rating',	'Volcanic Activity - Hazard Type Risk Index Score',	'Volcanic Activity - Hazard Type Risk Index Rating',	'Wildfire - Annualized Frequency',	'Wildfire - Exposure - Building Value',	'Wildfire - Exposure - Population',	'Wildfire - Exposure - Population Equivalence',	'Wildfire - Exposure - Agriculture Value',	'Wildfire - Exposure - Total',	'Wildfire - Historic Loss Ratio - Buildings',	'Wildfire - Historic Loss Ratio - Population',	'Wildfire - Historic Loss Ratio - Agriculture',	'Wildfire - Historic Loss Ratio - Total Rating',	'Wildfire - Expected Annual Loss - Building Value',	'Wildfire - Expected Annual Loss - Population',	'Wildfire - Expected Annual Loss - Population Equivalence',	'Wildfire - Expected Annual Loss - Agriculture Value',	'Wildfire - Expected Annual Loss - Total',	'Wildfire - Expected Annual Loss Score',	'Wildfire - Expected Annual Loss Rating',	'Wildfire - Hazard Type Risk Index Score',	'Wildfire - Hazard Type Risk Index Rating',	'Winter Weather - Number of Events',	'Winter Weather - Annualized Frequency',	'Winter Weather - Exposure - Building Value',	'Winter Weather - Exposure - Population',	'Winter Weather - Exposure - Population Equivalence',	'Winter Weather - Exposure - Agriculture Value',	'Winter Weather - Exposure - Total',	'Winter Weather - Historic Loss Ratio - Buildings',	'Winter Weather - Historic Loss Ratio - Population',	'Winter Weather - Historic Loss Ratio - Agriculture',	'Winter Weather - Historic Loss Ratio - Total Rating',	'Winter Weather - Expected Annual Loss - Building Value',	'Winter Weather - Expected Annual Loss - Population',	'Winter Weather - Expected Annual Loss - Population Equivalence',	'Winter Weather - Expected Annual Loss - Agriculture Value',	'Winter Weather - Expected Annual Loss - Total',	'Winter Weather - Expected Annual Loss Score',	'Winter Weather - Expected Annual Loss Rating',	'Winter Weather - Hazard Type Risk Index Score',	'Winter Weather - Hazard Type Risk Index Rating'))

lower_bound_draft4=csv[[variable_to_map_y]].min()
low4=lower_bound_draft4[0]

upper_bound_draft4=csv[[variable_to_map_y]].max()
up4=upper_bound_draft4[0]

pylow4 = low4.item()

pyup4 = up4.item()

Map_Rangey = st.slider(
    'Edit Y Range',
    0.0, pyup4, (pylow4, pyup4))


#Enter Y Variable and Description
y_value='Percent_of_individuals___100__Federal_Poverty_Line'

csv=csv.sort_values(by='Identified_as_disadvantaged', ascending=False)

def scatter_plot(x_value, y_value):
    fig4 = px.scatter(csv, x=x_value, y=y_value,
                     size="Total_population",
                     color='Identified_as_disadvantaged',
                     size_max=15,
                     labels={
                     'Identified_as_disadvantaged':'Disadvantaged'
                 },  template="simple_white", trendline="ols"
)

    fig4.update_layout(transition_duration=500, xaxis_range=Map_Rangex, yaxis_range=Map_Rangey)
    st.plotly_chart(fig4)
    
    
#running function 
scatter_plot(variable_to_map_x, variable_to_map_y)

st.subheader('Figure 5: Expected Annual Loss by Peril')

County_Name2=st.selectbox(label="Select Region",
options=('Fresno County', 'District of Columbia', 'Wayne County', 'Miami-Dade County', 'Navajo County', 'Chatham County',
'Denver County','Lumbee River', 'Clark County','Mineral County'))



map_dat5 = csv
map_dat5=map_dat5[map_dat5.County_Name == County_Name2]


df_peril=map_dat5[['Avalanche - Expected Annual Loss - Total',
'Coastal Flooding - Expected Annual Loss - Total',
'Cold Wave - Expected Annual Loss - Total',
'Drought - Expected Annual Loss - Total',
'Earthquake - Expected Annual Loss - Total',
'Hail - Expected Annual Loss - Total',
'Heat Wave - Expected Annual Loss - Total',
'Hurricane - Expected Annual Loss - Total',
'Ice Storm - Expected Annual Loss - Total',
'Landslide - Expected Annual Loss - Total',
'Lightning - Expected Annual Loss - Total',
'Riverine Flooding - Expected Annual Loss - Total',
'Strong Wind - Expected Annual Loss - Total',
'Tornado - Expected Annual Loss - Total',
'Tsunami - Expected Annual Loss - Total',
'Volcanic Activity - Expected Annual Loss - Total',
'Wildfire - Expected Annual Loss - Total',
'Winter Weather - Expected Annual Loss - Total']]


df_peril.rename(columns={'Avalanche - Expected Annual Loss - Total':'Avalanche',
'Coastal Flooding - Expected Annual Loss - Total':'Coastal Flooding',
'Cold Wave - Expected Annual Loss - Total':'Cold Wave',
'Drought - Expected Annual Loss - Total':'Drought',
'Earthquake - Expected Annual Loss - Total':'Earthquake',
'Hail - Expected Annual Loss - Total':'Hail',
'Heat Wave - Expected Annual Loss - Total':'Heat Wave',
'Hurricane - Expected Annual Loss - Total':'Hurricane',
'Ice Storm - Expected Annual Loss - Total':'Ice Storm',
'Landslide - Expected Annual Loss - Total':'Landslide',
'Lightning - Expected Annual Loss - Total':'Lightning',
'Riverine Flooding - Expected Annual Loss - Total':'Riverine',
'Strong Wind - Expected Annual Loss - Total':'Strong Wind',
'Tornado - Expected Annual Loss - Total':'Tornado',
'Tsunami - Expected Annual Loss - Total':'Tsunami',
'Volcanic Activity - Expected Annual Loss - Total':'Volcanic Activity',
'Wildfire - Expected Annual Loss - Total':'Wildfire',
'Winter Weather - Expected Annual Loss - Total': 'Winter Weather'
                  },    inplace=True) 


df_peril=df_peril.sum()
df_peril=df_peril.to_frame() 
df_peril.reset_index(inplace=True)
df_peril.rename(columns={0: 'Expected Annual Loss'},
          inplace=True)

df_peril=df_peril.sort_values(by=['Expected Annual Loss'], ascending=False)

fig5 = px.bar(df_peril, x='index', y='Expected Annual Loss',
                     labels={"index": "<b> Peril </b>", 'Expected Annual Loss': '<b>Expected Annual Loss</b>' },
                    template="simple_white"
                )
fig5.update_traces(marker_color='DarkRed')
    #displaying viz 
st.plotly_chart(fig5)



