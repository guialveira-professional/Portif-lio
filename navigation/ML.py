import streamlit as st
import webbrowser
from ML_projects.projects import maintenance_classification
from ML_projects.projects import space_titanic

def Machine_learning():
    st.title("Machine Learning Projects")
    st.text("""This projects I developed using Machine learning techniques for classification.""")
    st.divider()
    col1,col2,col3,col4,col5 = st.columns([1.3, 0.5, 1.5, 0.3, 1])
    
    with col1:
        space_titanic()
    
    with col3:
        maintenance_classification()