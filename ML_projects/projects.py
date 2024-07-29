import streamlit as st
from utils.icons import icons
import webbrowser

def space_titanic():
    
    st.header("Spaceship Titanic")
   
    st.markdown("""<h3 style='text-align: justify; color: blue;'>Technologies:</h2>""", unsafe_allow_html=True)
    icones = icons()
    python_sb = icones.python()
    scikit_sb = icones.scikit()
    pandas_sb = icones.pandas()
    matplot_sb = icones.matplot()
    numpy_sb = icones.numpy()
    seaborn_sb = icones.seaborn()
        
    python_sb
    pandas_sb
    scikit_sb
    matplot_sb
    seaborn_sb
    numpy_sb

    st.markdown("""<div style="text-align: justify;">Click below to see more details about this project</div>""",
            unsafe_allow_html=True)
    st.markdown("")

    col1,col2 = st.columns(2)
    with col1:
        details = st.button("See more", key="titanic")
    with col2:
        github = st.button("Github", key="titanic_git")

    if github:
         webbrowser.open_new_tab('https://github.com/guialveira-professional/RandomForest_Hyperparameter_tunning')
    
    
    if details:
        st.markdown("""<div style="text-align: justify;">This project I posted on a Kaggle competition. In this competition, my task was to build a model to determine if a passenger was transported or not based on the ship's information.

The procedure begins by separating the numeric and categorical columns, as the processing methods for these columns are different. Then, I had to clean the dataset before drawing any conclusions. Everything up to this point was done using pandas.

Before modeling, I always like to examine the correlations and try to extract any conclusions just by looking at the clean dataset. To make these insights more visible, I used the seaborn and matplotlib libraries to plot some graphs.

I drew my conclusions and combined them with the statistical insights to ensure that the features were suitable for modeling. The process for modeling was pretty standard, consisting of: splitting the train/test data, normalization, calculating class weights, training, evaluating, fine-tuning, and evaluating again. In the end, I achieved an accuracy of 81.2%.

In this notebook, just out of curiosity, I developed a neural network to analyze how it would learn with a small amount of data. Impressively, it performed quite well with just a little overfitting.</div>""",
            unsafe_allow_html=True)
        

def maintenance_classification():
    
    st.header("Maintenance classification")
    st.markdown("""<h3 style='text-align: justify; color: blue;'>Technologies:</h2>""", unsafe_allow_html=True)
    icones = icons()
    python_sb = icones.python()
    pandas_sb = icones.pandas()
    matplot_sb = icones.matplot()
    scikit_sb = icones.scikit() 
    seaborn_sb = icones.seaborn()
    scipy_sb = icones.scipy() 
    python_sb
    pandas_sb
    seaborn_sb
    matplot_sb    
    scikit_sb
    scipy_sb

    st.markdown("""<div style="text-align: justify;">Click below to see more details about this project</div>""",
            unsafe_allow_html=True)
    st.markdown("")
    
    col1,col2 = st.columns(2)
    
    with col1:
        details = st.button("See more", key="maintenance")
    with col2:
        github = st.button("Github",key = "maintenance_git")

    if github:
         webbrowser.open_new_tab('https://github.com/guialveira-professional/Maintenance')

    
    if details:
        st.markdown("""<div style="text-align: justify;">This project is a real case. The dataset was provided by a maintenance company that recently underwent a digitalization process. The dataset was encoded and is based on two maintenance classes: "pos" and "neg". The other columns are variables that might influence the type of maintenance. My mission was to develop a predictive model based on this dataset.

The first thing I did was explore and process the data using the pandas library. Then I extracted some statistical insights, such as mean, median, standard deviation, and correlation between some columns, using pandas and scipy for the calculations.

After that, I had to clean the entire dataset and prepare it for the definitive analysis. All missing data was labeled as "na", so I had to be careful not to lose any data. Then I conducted my final statistical analysis, examining the variables' distribution using violin plots and the correlation against the classes. The classes are categorical, so I had to label these columns. In this case, I used the LabelEncoder.

Finally, I started modeling. I used the Random Forest classifier for this case. I prepared the data by splitting it into training and testing datasets, then normalizing the numeric columns and training the model using the scikit-learn library. The data was unbalanced, so I calculated the weights accordingly. In the end, I achieved a recall metric of 75.2. I used this metric because I had a lot of false positives.</div>""",
            unsafe_allow_html=True)