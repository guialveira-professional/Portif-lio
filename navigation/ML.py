import streamlit as st
import webbrowser

def Machine_learning():
    st.title("Machine Learning Projects")
    st.text("""This projects I developed using Machine learning techniques for classification. Click the button to go to the respective project repository in my github """)
    st.divider()
    col1,col2,col3,col4,col5 = st.columns([1, 0.5, 1.5, 0.3, 1])
    
    with col1:
        st.header("Spaceship Titanic")
        st.markdown(
        """<div style="text-align: justify;">For this project it was needed to extract, treat and prepare data in order to develop a ML model to classify if the passager was transported off or not.</div>
        <div style="text-align: justify;">To increase the model's accuracy, a hyper parameter fine tunning was made.</div>""",
        unsafe_allow_html=True)
        st.markdown("")
        titanic_bt = st.button("Go to repository", key="Titanic")
    
    with col3:
        st.header("Maintenance Classification")

        st.markdown(
        """<div style="text-align: justify;">This project used a coded dataset. The dataset consists in variables about maintenance components of a recently digitalized maintenance company.</div>
        <div style="text-align: justify;">The main point in this project is data cleanning, the dataset has a lot of handwrited missing values and the classes are unbalanced.</div>""",
        unsafe_allow_html=True)
        st.markdown("")
        MV_OD_bt = st.button("Go to Repository",key="Maintenance")
    
    if titanic_bt:
         webbrowser.open_new_tab('https://github.com/guialveira-professional/RandomForest_Hyperparameter_tunning')

    if MV_OD_bt:
         webbrowser.open_new_tab('https://github.com/guialveira-professional/Maintenance')