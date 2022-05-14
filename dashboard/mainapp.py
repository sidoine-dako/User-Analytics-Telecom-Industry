# Modules importation
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import sys
sys.path.append('../scripts')
from utility_functions import *

# Data importation
df = pd.read_csv("../data/UniqueUser.csv")

# Table for the topn handset type
topn=st.number_input(label='Top n handset type',min_value=1,max_value=50,value=10,help="Choose a number to print the top handset type",key=1)

dfTopHandsetType = topN(df,'Handset Type',topn,undefined=False)
st.write(dfTopHandsetType)

# Table for the topn manufacturer
topm=st.number_input(label='Top m handset manufacturer',min_value=1,max_value=50,value=10,key=2)

dfTopHandsetMan = topN(df,'Handset Manufacturer',topm,undefined=False)
st.write(dfTopHandsetMan)

# Table of the top n type of handset for the top m manufacturer
topn2=st.number_input(label='Top n handset type',min_value=1,max_value=10,value=3,help="Choose a number to print the top handset type",key=3)
topm2=st.number_input(label='Top m handset manufacturer',min_value=1,max_value=10,value=5,key=4)
dfTopHandTMan = topTypeManufact(df,topm2,topn2)
st.write(dfTopHandTMan)