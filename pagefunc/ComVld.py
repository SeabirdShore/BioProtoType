import pandas as pd 
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def test():
    st.title('Common Validation by Cofussion Matrix')
    st.write("To assist wetlab in validating Telepathy's utility, this page provides automated computation and visualization tools.")
    st.write("Integrated functions include confusion matrix, specificity and sensitivity calculations")
    st.image('./static/cfsmx.png',width = 800)
    st.divider()
    st.title("Upload Data")    
    cols = st.columns(2)
    with cols[0]:
        uploaded_files = st.file_uploader("only CSV file supported")
    with cols[1]:
        st.header("Requirements for data format")
        st.write("data is required to be in csv format, n rows and 3 columns, name is listed anonymized for privacy considerations, True_Result is the verified diagnostic result, Telepathy_diagnosis is the diagnostic result of the kit, the value of 1 indicates positive, 0 indicates negative")    
    st.divider()
    st.title("Data Description")
    if uploaded_files:
        df = pd.read_csv(uploaded_files)
        dfTrueResult = df['True_Result']
        dfTeleDiag = df['Telepathy_diagnosis']
        TrueResult = np.array(dfTrueResult)
        TeleDiag = np.array(dfTeleDiag)
        TrueResult = TrueResult.T
        TeleDiag = TeleDiag.T
        TP = np.sum((TrueResult == 1) & (TeleDiag == 1))
        TN = np.sum((TrueResult == 0) & (TeleDiag == 0))
        FP = np.sum((TrueResult == 0) & (TeleDiag == 1))
        FN = np.sum((TrueResult == 1) & (TeleDiag == 0))
        Sensitivity = TP/(TP+FN)
        Specificity = TN/(TN+FP)
        cols = st.columns(2)
        with cols[0]:
            st.header('Head of File')
            st.dataframe(df.head())
        
            
    st.divider()
    st.title("Calculation result")
    if uploaded_files:    
        data = [[TP,FN],[FP,TN]]
        # 创建一个2x2的数据框，使用annot参数显示数值
        ax = sns.heatmap(data, annot=True, fmt="d", cmap="YlGnBu")
        # 设置坐标轴标签
        ax.set_xlabel("Prediction",fontsize=20)
        ax.set_ylabel("KnownResult",fontsize=20)
        plt.xticks([0.5, 1.5], ['Positive', 'Negative'])
        plt.yticks([0.5, 1.5], ['Positive', 'Negative'])
        # 设置颜色条
        cbar = ax.collections[0].colorbar
        cbar.set_ticks([TP, FN, FP, TN])
        cbar.set_ticklabels([str(TP), str(FN), str(FP), str(TN)])
        # 显示图表
        cols = st.columns(2)
        with cols[1]:
             st.write(" ")
             st.write(" ")
             st.write(" ")
             st.write(" ")
             st.header("Statistical value")
             st.write("Sensitivity = ",Sensitivity," ; ","Specificity = ",Specificity,fontsize=20)
             st.write(" ")
             st.subheader("Notes on proper nouns")
             st.write("*Confusion Matrix is a tabular visual tool for evaluating the performance of a classification model. It compares the model's predictions to the real labels and divides them into four different categories: True Positive (TP), True Negative (TN), False Positive (FP), and False Negative (FN).")
             st.write("*Sensitivity, proportion of patients with positive results;Specificity, proportion of non-patients with negative results")
             
        with cols[0]: 
             st.header("   Confusion matrix")    
             st.pyplot()        