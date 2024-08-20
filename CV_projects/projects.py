import streamlit as st
from utils.icons import icons
import webbrowser

def chinese_digits():
    
    st.header("Chinese Digits")
    st.markdown("""<h3 style='text-align: justify; color: blue;'>Technologies:</h2>""", unsafe_allow_html=True)
    icones = icons()
    python_sb = icones.python()
    numpy_sb = icones.numpy()
    tensorflow_sb = icones.tensorflow()
        
    python_sb
    numpy_sb
    tensorflow_sb
    
    

    st.markdown("""<div style="text-align: justify;">Click below to see more details about this project</div>""",
            unsafe_allow_html=True)
    st.markdown("")

    col1,col2 = st.columns(2)
    with col1:
        details = st.button("See more", key="chinese")
    with col2:
        st.markdown("""<a href="https://github.com/guialveira-professional/Classificacao-de-imagem" target="_blank">Github</a>""",
                unsafe_allow_html=True)

    #if github:
     #   webbrowser.open_new_tab('https://github.com/guialveira-professional/Classificacao-de-imagem')
    
    
    if details:
        st.markdown("""<div style="text-align: justify;"></div>""",
            unsafe_allow_html=True)