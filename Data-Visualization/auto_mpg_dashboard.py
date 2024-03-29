import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

#set the style for seaborn
sns.set_style('darkgrid')

#Title of Dashboard
st.title('Dashboard for Auto MPG Dataset')

@st.cache
def load_data():
    """Utility function for loading the autompg dataset as a dataframe"""
    df=pd.read_csv('data/clean_auto_mpg.csv')
    return df

#Load Dataset
data=load_data()
numeric_columns = data.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
print(numeric_columns)

#checkbox widget
checkbox = st.sidebar.checkbox('Reveal Data')
print(checkbox)

if checkbox:
    # st.write(data)
    st.dataframe(data=data)

#Create scatterplots
st.sidebar.subheader("Scatter Plot Setup")

#Add select widget
select_box1 = st.sidebar.selectbox(label='X axis', options = numeric_columns)
print(select_box1)
select_box2 = st.sidebar.selectbox(label='Y axis', options = numeric_columns)
print(select_box2)

#Create Scatterplot
sns.relplot(x=select_box1, y=select_box2, data=data)
st.pyplot()

# create histograms
st.sidebar.subheader("Histogram")
select_box3 = st.sidebar.selectbox(label="Feature", options=numeric_columns)
histogram_slider = st.sidebar.slider(label="Number of Bins",min_value=5, max_value=100, value=30)
sns.distplot(data[select_box3], bins=histogram_slider)
st.pyplot()

# create jointplot
st.sidebar.subheader("Joint plot")
select_box3 = st.sidebar.selectbox(label='x', options=numeric_columns)
select_box4 = st.sidebar.selectbox(label="y", options=numeric_columns)
sns.jointplot(x=select_box3, y=select_box4, data=data)
st.pyplot()
