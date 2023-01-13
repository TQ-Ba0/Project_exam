import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Subject"
)
#Introduction
img = Image.open('images/Subject.png')
st.image(img,use_column_width=True)
st.title("Subject")
st.markdown( """
    On this page you can see spectrum and comments of each subject and in year by choice.
    """
)

@st.cache
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
def visualize_spectrum(subject):
    plt.figure(figsize=(25,12))
    plt.title(f"Spectrum of {subject}")

    t = plt.hist(df[subject],bins=np.round(np.arange(0,10.1, 0.2),1),rwidth=0.5)
    hist, edges = t[0],t[1]

    plt.xticks(edges)
    plt.yticks(np.arange(0, max(hist)+1, 1000))

    plt.xlabel('scores')
    plt.ylabel('number of students')

    return plt

for subject in select_subjects:
    if subject != 'Ma_mon_ngoai_ngu':
        st.write(f"Spectrum of {subject}")
        st.pyplot(visualize_spectrum(subject))