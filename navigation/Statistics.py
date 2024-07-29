import streamlit as st
import webbrowser
from statistic_projects.projects import financial_analyst
from statistic_projects.projects import outlier_detection

def statistics():
    st.title("Statistic Projects")
    st.text("""This projects I developed using Statistics methods in time series.""")
    st.divider()
    col1,col2,col3,col4,col5 = st.columns([1, 0.5, 1, 0.5, 1])
    
    with col1:
        
        financial_analyst()
        
    
    with col3:
        
        outlier_detection()