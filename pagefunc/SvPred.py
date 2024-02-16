import streamlit as st
import pandas as pd
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
import seaborn as sns

def info():
  st.title("Survival Prediction by Kaplan-Meier Method")
  with st.expander("See explanation"):
    st.markdown("#### Kaplan-Meier method, also known as product limit method. The idea is actually very simple, is to write Survival probability function S(t) as a recurrence. Suppose we have computed the survival function S(t1) for time t1, and we want to compute time t2 (t2&gt; The survival function value of t1), then the individual must first survive the time t1, and then survive from t1 to t2, expressed by the formula:")
    st.latex(r'''\begin{equation}
                 \begin{aligned}
    \LARGE S(t_2) = S(t_1) \times (1 - \frac{d}{n})
    \end{aligned}
    \end{equation}         
    ''')
    st.write("Where d represents the number of individuals who actually had an event during the period from t1 to t2; n represents the total number of individuals who are likely to have an event during the period t1 to t2 (which can be understood as the total number of individuals still alive at t1).")
    st.markdown("#### For the confidence interval estimation of survival probability distribution data, a formula based on Greenwood is as follows:")
    st.latex(r'''\begin{equation}
                 \begin{aligned}
                & \LARGE \widehat{S}(t) \pm z_{\alpha / 2} \sqrt{\widehat{\operatorname{Var}}[\widehat{S}(t)]} \quad \text { where } \\
                & \LARGE \widehat{\operatorname{Var}}[\widehat{S}(t)]=\widehat{S}(t)^2 \sum_{t_i \leq t} \frac{d_i}{n_i\left(n_i-d_i\right)}
                 \end{aligned}
                 \end{equation}
    ''')
    st.write("Where S(t) is the survival probability function, which is the cumulative product of the probability of not dying that we explained earlier.")
    cols = st.columns(6)
    with cols[1]:
      st.image("./static/scdemo.png",caption='plot_demo',width=700)
    cols = st.columns(7) 
    with cols[3]:
      st.link_button("Go to Reference", "https://www.math.wustl.edu/~sawyer/handouts/greenwood.pdf")
  st.divider()


def pred():   
  cols = st.columns(2)
  with cols[0]:
        st.title("Upload Data")   
        Uploaded_files = st.file_uploader("only CSV file supported")
        
  with cols[1]:
        st.header("input example")
        df0 = pd.read_csv('./pagefunc/data/sample1.csv')
        st.table(df0.head())

  st.divider()      
##############################################
  st.title("Results figure")        
  if Uploaded_files:
        df = pd.read_csv(Uploaded_files)
        kmf,kmf1 = calc(df)

        col1,col2,col3=st.columns([1,3,1])
        sns.countplot(x="Telepathy",hue="alive",data=df,)        
        col2.pyplot()
        col2.latex(r'''
        Figure1.Right \: Censor \: Count
''')        
        kmf.plot_survival_function()
        kmf1.plot_survival_function()
        col2.pyplot()
        col2.latex(r'''
        Figure2.Kaplan-Meier \: Lifeline
''')
##############################################
  st.divider()
  st.title("Log-Rank Test")
  with st.expander("See explanation"):
      st.write("After the KM method is used to draw multiple survival curves according to groups, the Log-rank test can be used to make up for it when direct observation is insufficient to determine whether there is a significant difference between multiple curves.There is no significant difference between the null hypothesis group and the Log-rank test. When the calculated P-value is less than 0.005, the null hypothesis is overturned, and the survival time distribution of the two groups is considered to be significantly different.")
      cols = st.columns(7)
      with cols[3]:
           st.link_button("Go to Reference", "https://www.math.wustl.edu/~sawyer/handouts/greenwood.pdf")
  if Uploaded_files:         
     results = logranktest(df)           
     st.write("the calculated P-value = ",results.p_value)

@st.cache_data
def calc(df):
    kmf = KaplanMeierFitter()
    kmf1 = KaplanMeierFitter()
    T=df[df['Telepathy'] == 1]["lifetime"]
    E=df[df['Telepathy'] == 1]["alive"].replace({0: 1, 1: 0})
    T1=df[df['Telepathy'] == 0]["lifetime"]
    E1=df[df['Telepathy'] == 0]["alive"].replace({0: 1, 1: 0})
    kmf.fit(T,E,label="Telepathy")
    kmf1.fit(T1,E1,label="Traditional")
    return kmf,kmf1

@st.cache_data
def logranktest(df):
    T=df[df['Telepathy'] == 1]["lifetime"]
    E=df[df['Telepathy'] == 1]["alive"].replace({0: 1, 1: 0})
    T1=df[df['Telepathy'] == 0]["lifetime"]
    E1=df[df['Telepathy'] == 0]["alive"].replace({0: 1, 1: 0})
    results = logrank_test(T, T1, E, E1, alpha=.99)
    return results