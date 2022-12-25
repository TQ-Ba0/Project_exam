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
    ---
    ### Source
    - The data is taken from the github link of the author **BeeCost Trợ lý Mua Sắm** [GitHub Link](https://github.com/beecost/bee-university/tree/master/output_data/crawler/common) 👈
    ---
    ### About Dataset
    ### Subject
    This is a dataset about test scores that candidates achieved in the college entrance examination for the school year 2019 to 2021 in Vietnam.
    You can view statistics by subject and exam block.

    ### Content
    The dataset includes the student's identification number and the corresponding score of that student:

    sbd - Candidate number

    Van - Literature score

    Toan - Mathematics score

    Ma_mon_ngoai_ngu - Foreign language code

    Ngoai_ngu - Foreign language score

    - N1: English

    - N2: Russian

    - N3: French

    - N4: Chinese

    - N5: German

    - N6: Japanese

    Li - Physics score

    Hoa - Chemistry score

    Sinh - Biology score

    Su - History score

    Dia - Geography score

    GDCD - Civics score

    ### Author's words
    Hope this dataset helps the data analysis community.

    ---
    ### Members
    - The Website's designed by 4 people:
        - Trần Quốc Bảo - 20127449
        - Hồ Đăng Cao - 20127452
        - Đỗ Đức Duy - 20127476
        - Ngô Hữu Nhật Thanh - 20127327

"""
)