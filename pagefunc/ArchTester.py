import streamlit as st


def formula():
    st.latex(r'''
       \LARGE ReLU:\large f(x) = \left\{ \begin{array}{ll}
             x & \textrm{if $x>=0$}\\
             0 & \textrm{if $x<0$}
            \end{array} \right.
    ''')

@st.cache_data
def cal(x):
  for _ in range(10000):    
    if x>=0:
       y=x
    else:
       y=0

    return y