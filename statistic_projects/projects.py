import streamlit as st
from utils.icons import icons
import webbrowser

def financial_analyst():
    
    st.header("Financial Analyst")
    st.markdown("""<h3 style='text-align: justify; color: blue;'>Technologies:</h2>""", unsafe_allow_html=True)
    icones = icons()
    python_sb = icones.python()
    yahoo_sb = icones.yahoo_finance()
    pandas_sb = icones.pandas()
    bcb_sb = icones.bcb()
        
    python_sb
    pandas_sb
    yahoo_sb
    bcb_sb

    st.markdown("""<div style="text-align: justify;">Click below to see more details about this project</div>""",
            unsafe_allow_html=True)
    st.markdown("")

    col1,col2 = st.columns(2)
    with col1:
        details = st.button("See more", key="financial")
    with col2:
         st.markdown("""<a href="https://www.linkedin.com/in/guilherme-alves-de-oliveira-914149258/" target="_blank">LinkedIn</a>""",
                unsafe_allow_html=True)

   # if github:
    #    webbrowser.open_new_tab('https://github.com/guialveira-professional/Financial-Analist')
    
    
    if details:
        st.markdown("""<div style="text-align: justify;">This project was developed to help financial analysts identify trends in macroeconomic indicators. First, I had to extract updated data from different sources. In this case, I used the Yahoo Finance library, the API BCB, and pandas datareader to extract specific data.

To determine macro trends over short and long periods, I calculated the moving average for all indicator prices and divided the analysis into short-term and long-term using different windows for the calculations. After calculating the moving averages, I needed to obtain a linear function and analyze its coefficient to see how aggressive the trend actually is. For this, I used the scipy library to build a linear regression using the moving average calculations over time. Based on the linear slope, the function classifies this number and provides a conclusion.

The last part is particularly useful for Brazilian investors, as it helps analyze the trend differences between Brazil and the USA. These calculations are useful for measuring Brazilian risks.</div>""",
            unsafe_allow_html=True)
        

def outlier_detection():
    
    st.header("Outlier detection")
    st.markdown("""<h3 style='text-align: justify; color: blue;'>Technologies:</h2>""", unsafe_allow_html=True)
    icones = icons()
    python_sb = icones.python()
    pandas_sb = icones.pandas()
    matplot_sb = icones.matplot()
    scikit_sb = icones.scikit()
    numpy_sb = icones.numpy()    
    python_sb
    pandas_sb
    matplot_sb    
    scikit_sb
    numpy_sb

    st.markdown("""<div style="text-align: justify;">Click below to see more details about this project</div>""",
            unsafe_allow_html=True)
    st.markdown("")
    
    col1,col2 = st.columns(2)
    
    with col1:
        details = st.button("See more", key="outlier")
    with col2:
         st.markdown("""<a href="https://www.linkedin.com/in/guilherme-alves-de-oliveira-914149258/" target="_blank">LinkedIn</a>""",
                unsafe_allow_html=True)

    #if github:
        #webbrowser.open_new_tab('https://github.com/guialveira-professional/Statistics_time_series')

    
    if details:
        st.markdown("""<div style="text-align: justify;">This project's objective is to show how powerful statistical analysis is. I'll use simple prediction methods, such as seasonal and trend predictions. For these predictions, I'll evaluate and plot the results. For the first part, I'll use an open dataset of beer production. The evaluation will be calculated using the numpy library, and the graphs will be plotted using matplotlib.

The second part shows how the moving average acts on your dataset, smoothing or indicating an actual trend. The smoothed dataset can be used to generate confidence intervals, and finally, these intervals can be used to identify outliers in your dataset. In conclusion, the function built is powerful and simple, using just the pandas library and some statistical indicators like standard deviation, mean absolute error, and moving average.</div>""",
            unsafe_allow_html=True)