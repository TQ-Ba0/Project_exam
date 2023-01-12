import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
st.set_page_config(
    page_title="Students"
)
#Introduction
img = Image.open('images/Subject.png')
st.image(img,use_column_width=True)
st.title("Students")
st.markdown( """
    On this page you can see structure points in range each subject and in year by choice.
    """
)

# @st.cache
def load_data(year):
    path_file='diemthi'+str(year)+'.csv'
    temp = pd.read_csv(path_file)
    df = pd.DataFrame(temp)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    return df.round(2)

#sidebar
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',list(reversed(range(2019,2021))))
#repare data
df = load_data(selected_year)
sort_columns = np.array(df.columns)[:-1]
select_subjects = st.sidebar.multiselect('Subject',sort_columns,sort_columns)

st.markdown("# Our Data Set")
df_exam = df[select_subjects+['sbd']]
st.dataframe(df_exam)
select_point = st.sidebar.slider(
    'Select a range of point',
    0.0, 10.0,(4.0,5.0))
pointFrom , pointTo=select_point

def visualize_spectrum(subject):
    plt.figure(figsize=(25,12))
    plt.title(f"Spectrum of {subject}")
    t = plt.hist(df[subject],bins=np.round(np.arange(pointFrom,pointTo, 0.2),1),rwidth=0.5)
    return plt
def point_structure_in_range(subject):
    plt.figure(figsize=(25,12))
    plt.title(f"Percent of point in range of {subject}")
    t = plt.hist(df[subject],bins=np.round(np.arange(pointFrom,pointTo, 0.5),1),rwidth=0.5)
    res = dict(map(lambda i,j : (i,j) , t[1],t[0]))
    # keys=res.keys()
    # values=res.values()
    res = pd.DataFrame.from_dict(res,orient='index')
    res=res.reset_index()
    res.columns=['Points','Numbers of student']
    return res
def create_structure_pie_chart(subject):
    temp_dict= point_structure_in_range(subject)
    fig=px.pie(temp_dict,values='Numbers of student',names='Points')
    return fig
for subject in select_subjects:
    if subject != 'Ma_mon_ngoai_ngu':
        st.write(f"Spectrum of {subject}")
        st.pyplot(visualize_spectrum(subject))
        st.write(f"Point structure in range of {subject}")
        st.write(create_structure_pie_chart(subject))