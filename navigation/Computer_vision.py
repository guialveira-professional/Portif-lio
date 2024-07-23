import streamlit as st
import webbrowser

def computer_vision():
    st.title("Computer vision Projects")
    st.text("""This projects I developed using Computer vision techniques for classification. Click the button to go to the respective project repository in my github """)
    st.divider()
    col1,col2,col3,col4,col5 = st.columns([1, 0.5, 1.5, 0.3, 1])
    
    with col1:
        st.header("Chinese digits")
        st.markdown(
        """<div style="text-align: justify;">In this project I develop a Convolutional neural networt to classify Chinese digits.</div>
        <div style="text-align: justify;">To train a CNN is necessary to treat and normalize the images. In this case I used the tensorflow framework</div>""",
        unsafe_allow_html=True)
        st.markdown("")
        titanic_bt = st.button("Go to repository", key="Chinese")
    
    
    
    if titanic_bt:
         webbrowser.open_new_tab('https://github.com/guialveira-professional/Classificacao-de-imagem')