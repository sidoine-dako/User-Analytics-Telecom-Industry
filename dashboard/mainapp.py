# Modules importation
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import sys
sys.path.append('../scripts')

# UTILITY FUNCTIONS
# Function to have the top n and plot of top n
def topN(df,col,topn,undefined=True,rend=False):
    if undefined==False:
        topN = df.loc[df[col]!='undefined',col].value_counts()[:topn]
    else:
        topN = df.loc[:,col].value_counts()[:topn]
    if rend==True:
        fig = px.bar(x=topN.index,height=topN.values,labels={'x':'Handset','y':'# of occurence'})
        st.plotly_chart(fig)
    return topN

# Function to extract the top n type of handset for the top m manufacturer
def topTypeManufact(df,nmanufact=3,ntype=5):
    topNManufact = topN(df,'Handset Manufacturer',topn=nmanufact,undefined=False)
    res = pd.DataFrame(columns=['Manufacturer','Type','Count'])
    for manufacturer in topNManufact.index:
        temp = df.loc[df['Handset Manufacturer']==manufacturer,'Handset Type'].value_counts()[:ntype]
        temp2 = pd.DataFrame({'Manufacturer':[manufacturer]*ntype,'Type':temp.index,'Count':temp.to_list()})
        res = pd.concat([res,temp2])
    return res.reset_index(drop=True)

########################################################################################################

# Data importation
df = pd.read_csv("../data/UniqueUser.csv")
st.title('Tellco Data Analysis')
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