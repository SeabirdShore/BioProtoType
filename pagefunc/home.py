import streamlit as st
import base64

def intro():
    md = '''
 Our Medical Data Analysis Software is a powerful tool designed to facilitate the analysis and interpretation of medical data for wetlab experiment. This software leverages clinical statistical methods to provide accurate and insightful results, enabling healthcare practitioners to be well-informed.
    '''
    st.markdown(md)
    md1 = '''
### Available Function 
- Confussion Matrix: validate the utility of Telepathy by compare its diagnosis with known result and compute common statistical values(Sensitivity & Specificity).
- Kaplan-Meier Method: predict the survival timeline of those using telepathy and traditional diagnosis method,  compare and discover the advantages of telepathy over traditional diagnostic methods
- Log-Rank Test: integrated in the module 'Survival Prediction' with Kaplan-Meier Method, act as the patch of Kaplan-Meier Method in the situation of similar survival timeline
'''
    md2='''
### Key Features:
- developed by the framework "Streamlit". Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. 
- deployed by Kubernetes. Kubernetes, also known as K8s, is an open source system for automatically deploying, scaling, and managing containerized applications. It combines the containers that make up an application into logical units for easy management and service discovery. 
- cache. If same function meets same data, it will output the result without calculation.
'''
    

    st.write(" ")
    with st.container(border=True):
     st.markdown(md1)
     st.write(" ")      
    with st.container(border=True):
     st.markdown(md2)

def main_bg(main_bg):
    main_bg_ext = "png"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

