import streamlit as st

class icons:
    def __init__(self):
        pass
    def python(self):

        self.col1,self.col2,self.col3 = st.columns([0.5,1,1.3])
        with self.col1:
            st.image("imagens\ico_python.jpg", width=55)

        with self.col2:
            st.markdown("")
            st.markdown("""<h5 style='text-align: justify; color: white;'>python</h2>""", unsafe_allow_html=True)

    def pandas(self):
        self.col1,self.col2,self.col3 = st.columns([0.5,1,1.3])
        with self.col1:
            st.image("imagens\ico_pandas.png", width=55)

        with self.col2:
            st.markdown("")
            st.markdown("""<h5 style='text-align: justify; color: white;'>pandas</h2>""", unsafe_allow_html=True)

    def yahoo_finance(self):
        self.col1,self.col2,self.col3 = st.columns([0.5,1,1.3])
        with self.col1:
            st.image("imagens\ico_yahoo_finance.png", width=55)

        with self.col2:
            
            st.markdown("""<h5 style='text-align: justify; color: white;'>Yahoo Finance</h2>""", unsafe_allow_html=True)

    def bcb(self):
        self.col1,self.col2,self.col3 = st.columns([0.5,1,1.3])
        with self.col1:
            st.image("imagens\ico_BCB.png", width=55)

        with self.col2:
            st.markdown("")
            st.markdown("""<h5 style='text-align: justify; color: white;'>API BCB</h2>""", unsafe_allow_html=True)

    def matplot(self):
        self.col1,self.col2,self.col3 = st.columns([0.5,1,1.3])
        with self.col1:
            st.image("imagens\ico_matplot.png", width=55)

        with self.col2:
            st.markdown("")
            st.markdown("""<h5 style='text-align: justify; color: white;'>Matplotlib</h2>""", unsafe_allow_html=True)

    def scikit(self):
        self.col1,self.col2,self.col3 = st.columns([0.5,1,1.3])
        with self.col1:
            st.image("imagens\ico_scikit.png", width=55)

        with self.col2:
            st.markdown("")
            st.markdown("""<h5 style='text-align: justify; color: white;'>Scikit-learn</h2>""", unsafe_allow_html=True)

    def numpy(self):
        self.col1,self.col2,self.col3 = st.columns([0.5,1,1.3])
        with self.col1:
            st.image("imagens\ico_numpy.png", width=55)

        with self.col2:
            st.markdown("")
            st.markdown("""<h5 style='text-align: justify; color: white;'>Numpy</h2>""", unsafe_allow_html=True)

    def seaborn(self):
        self.col1,self.col2,self.col3 = st.columns([0.5,1,1.3])
        with self.col1:
            st.image("imagens\ico_seaborn.png", width=55)

        with self.col2:
            st.markdown("")
            st.markdown("""<h5 style='text-align: justify; color: white;'>Seaborn</h2>""", unsafe_allow_html=True)

    def scipy(self):
        self.col1,self.col2,self.col3 = st.columns([0.5,1,1.3])
        with self.col1:
            st.image("imagens\ico_scipy.png", width=55)

        with self.col2:
            st.markdown("")
            st.markdown("""<h5 style='text-align: justify; color: white;'>Scipy</h2>""", unsafe_allow_html=True)