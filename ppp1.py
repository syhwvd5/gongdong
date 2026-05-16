import streamlit as st
import pandas as pd


def load_data(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df


def show_data(df):
    st.subheader("전체 장소 데이터")
    st.dataframe(df)



