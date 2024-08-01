import streamlit as st
import webbrowser
from CV_projects.projects import chinese_digits
def computer_vision():
    st.title("Computer vision Projects")
    st.text("""This projects I developed using Computer vision techniques for classification.""")
    st.divider()
    col1,col2,col3,col4,col5 = st.columns([1, 0.5, 1, 0.5, 1])
    
    with col1:
        
        chinese_digits()
    