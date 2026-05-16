import streamlit as st
import pandas as pd

st.title("강원생활도우미앱 2.0")
st.write("엑셀 파일을 업로드하여 조건에 맞는 장소를 추천받아보세요.")

def load_data(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df

uploaded_file = st.file_uploader(
    "장소 데이터 엑셀 파일을 업로드하세요",
    type=["xlsx"]
)

def show_data(df):
    st.subheader("전체 장소 데이터")
    st.dataframe(df)


















