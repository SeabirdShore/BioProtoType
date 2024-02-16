import streamlit as st
import time

from pagefunc import home
from pagefunc import ComVld
from pagefunc import SvPred
from utils.components import footer_style, footer


st.set_page_config(
        page_title="BioProtoType",
        page_icon="./static/icon.png",
        layout="wide",
        initial_sidebar_state="auto"
    )

st.sidebar.image("./static/logo2.png")
st.sidebar.divider()
st.sidebar.write(" ")
option = st.sidebar.selectbox('Page  Navigator', ['home','Common Validation','Survival Prediction'])
st.sidebar.write('You selected:',option)
st.sidebar.divider()
st.sidebar.write("The Page is created for the WP of IGEM ZJU_CHINA, by Sibo Xiao, the intern of Software Team, Contact me via email (xspielberg@163.com)")

max_width_str = f"max-width: {80}%;"

st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
            unsafe_allow_html=True,
            )

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    
                }
        </style>
        """, unsafe_allow_html=True)


if option == 'home':
    st.image("./static/logo.png",width=1000)
    home.intro()

elif option == 'Survival Prediction':
    SvPred.info()
    SvPred.pred()

elif option == 'Common Validation':
    ComVld.test()

st.markdown(footer, unsafe_allow_html=True)
  
