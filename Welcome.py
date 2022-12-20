import streamlit as st 
import pandas as pd


st.set_page_config(
    page_title='Welcome',
    page_icon="👋"
)
st.write("# Data analysis of national high school exam scores ! 👋")
st.sidebar.success("Select a demo above")
st.markdown(
       """
    This is a dataset about test scores that candidates achieved in the college entrance examination for the school 
     year from 2019 to 2021 in Vietnam. You can view statistics by subject and exam block
    ### Data Soure?
    - The data is taken from the github link of the author **BeeCost Trợ lý Mua Sắm** [Link GitHub](https://github.com/beecost/bee-university/tree/master/output_data/crawler/common) 👈
    ### Members
    - Teams have 4 people:
        - Trần Quốc Bảo
        - Hồ Đăng Cao 
        - Đỗ Đức Duy
        - Ngô Hữu Nhật Thanh

"""
)