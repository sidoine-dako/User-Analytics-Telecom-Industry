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
topn=st.number_input(label='Top n handset type',min_value=1,max_value=50,value=10,help="Choose a number to print the top handset type")

dfTopHandsetType = topN(df,'Handset Type',topn,undefined=False)
st.write(dfTopHandsetType)

# Table for the topn manufacturer
topm=st.number_input(label='Top m handset manufacturer',min_value=1,max_value=50,value=10)

dfTopHandsetMan = topN(df,'Handset Manufacturer',topm,undefined=False)
st.write(dfTopHandsetMan)