# Modules importation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

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

# Function to have the topn of handset for topm of manufacturer
# Function to extract the top n type of handset for the top m manufacturer
def topTypeManufact(df,nmanufact=3,ntype=5):
    topNManufact = df.loc[:,'Handset Manufacturer'].value_counts()[:nmanufact]
    res = pd.DataFrame(columns=['Manufacturer','Type','Count'])
    for manufacturer in topNManufact.index:
        temp = df.loc[df['Handset Manufacturer']==manufacturer,'Handset Type'].value_counts()[:ntype]
        temp = pd.DataFrame({'Manufacturer':[manufacturer]*ntype,'Type':temp.index,'Count':temp.to_list()})
        res = pd.concat([res,temp])
    return res.reset_index(drop=True)