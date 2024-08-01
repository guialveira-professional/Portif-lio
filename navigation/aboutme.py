import streamlit as st
def aboutme():
   
    st.button("Go back to Projects") #reset the variable
        

    st.markdown("""<h1 style='text-align: justify; color: white;'>About me</h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style='text-align: justify; color: white;'>Who am I?</h2>""", unsafe_allow_html=True)
    st.markdown("""<div style="text-align: justify;">I am a person who has always loved studying and facing challenges. Since I was 16 years old, when I truly discovered my interest in IT, I have been learning programming and applying it in my daily life, both in professional and personal environments. Much of my learning has been self-taught, an approach that has been most effective for me, involving observing, replicating, and creating tools from my creativity related to previous learnings.
The combination of these factors has given me the freedom to study technology in various fields. My favorites are computing, robotics, finance, and people management. Throughout my professional journey so far, I have had the opportunity to see and demonstrate how IT combined with business knowledge can be extremely effective and productive. It can contribute exceptionally to matters that require a more refined storytelling.
Besides technical knowledge, I highly value social interactions and mutual development of people. I believe that personal growth comes as a consequence of helping others develop and succeed. My strongest value is that there is no progress without self-development, and your most valuable resources are time and the people around you.
Thus, I always dedicate myself to fostering a relaxed and friendly environment for everyone, and I love learning and exchanging personal and professional experiences with all.</div>""",
            unsafe_allow_html=True)
    st.divider()
    st.markdown("")
    st.markdown("")
    
    st.markdown("""<h2 style='text-align: justify; color: white;'>Professional history</h2>""", unsafe_allow_html=True)

    st.markdown("""<div style="text-align: justify;">My professional journey began at 16 when I made a decision that would change the course of my life. I was studying at a prestigious school called Colégio da Fundação Salvador Arena, which I had entered through a highly competitive exam. At the same time, I was selected for the apprenticeship entrance exam at Volkswagen do Brasil. I decided to start my professional career early.

My first job was as an apprentice at Volkswagen through the SENAI institution. For two years, I received paid training in machining techniques, planning, programming, mechanics, and electronics for later application in productive areas. This experience also helped me develop soft skills, as I had to communicate with various people across different positions for practical assistance and project implementation negotiations.

At 18, I completed the course and was selected for the position of Toolmaker through another practical selection process. This technical role directly dealt with new investments in Volkswagen's new products. My proficiency in industrial programming, Python, and Power BI earned me a spot on the automation team.

I remained in the automation sector for over six years, learning about German procedures and standards and implementing new technologies. During this time, I improved my technical and programming skills in Ladder, C, and Python through personal studies, my degree in industrial automation, and most importantly, my postgraduate studies in data science and artificial intelligence.

It was at this point that I truly understood the power of data. I saw how a well-organized database, visualization tools, Python programming, and solid business knowledge could transform discussions.

I started with a few Power BI dashboards using .csv and Excel data files. These tools were suitable for executive and managerial presentations but did not meet operational needs. Faced with this challenge, I took it upon myself to resolve a chronic inventory problem in the automation sector, specifically in pneumatics. We had a high-turnover and diverse equipment inventory with many discrepancies between the purchasing team.

Initially, I organized a database using SQLite3 in Python for development and SQL for database creation and queries since the data volume was not large. A Power BI dashboard was developed for easy inventory status visualization, but the main problem of preventing unnecessary purchases remained unsolved. By using Python scripts to extract data from the database and performing exploratory and predictive analysis, we generated a priority list for all items based on minimum stock levels and turnover rates. Finally, we developed an accessible platform using available technologies to make the purchasing team's access easy and intuitive, utilizing SharePoint, Power Apps, and Power BI.

After this project, I realized the limitless potential of this area when combined with advanced machine learning and deep learning techniques. I am currently seeking an opportunity to enter this field with my expertise while continuing my studies for further improvement.</div>""",
            unsafe_allow_html=True)