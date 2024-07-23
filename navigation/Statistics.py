import streamlit as st
import webbrowser

def statistics():
    st.title("Statistic Projects")
    st.text("""This projects I developed using Statistics methods in time series. Click the button to go to the respective project repository in my github """)
    st.divider()
    col1,col2,col3,col4,col5 = st.columns([1, 0.5, 1, 0.5, 1])
    
    with col1:
        st.header("Financial Analist")
        st.markdown(
        """<div style="text-align: justify;">This project was developed to help financial analists. It is based on extracting some updated Macro economics insights and returning it's trend and how agressive it is.</div>
        <div style="text-align: justify;">The analisys is based on moving average and operation volume.</div>""",
        unsafe_allow_html=True)
        st.markdown("")
        financial_bt = st.button("Go to repository", key="financial")
    
    with col3:
        st.header("Outlier detection")

        st.markdown(
        """<div style="text-align: justify;">In this project I used an open source data from Kaggle to develop an outlier detector. </div>
        <div style="text-align: justify;">the tool plots all points out of a confidence interval. For those calculation some metrics as Mean absolute error and stardard deviation are used</div>""",
        unsafe_allow_html=True)
        st.markdown("")
        MV_OD_bt = st.button("Go to Repository",key="MV")
    
    if financial_bt:
         webbrowser.open_new_tab('https://github.com/guialveira-professional/Financial-Analist')

    if MV_OD_bt:
         webbrowser.open_new_tab('https://github.com/guialveira-professional/Statistics_time_series')
        