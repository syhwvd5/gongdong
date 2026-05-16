import streamlit as st
import pandas as pd

st.title("강원생활도우미앱 2.0")
st.write("엑셀 파일을 업로드하여 조건에 맞는 장소를 추천받아보세요.")

def load_data(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df

uploaded_file = st.file_uploader(
    "장소 데이터 엑셀 파일을 업로드하세요(파일 확장자: [.xlsx])",
    type=["xlsx"]
)

def show_data(df):
    st.subheader("전체 장소 데이터")
    st.dataframe(df)

def filter_places(df, selected_region, selected_budget):
    result = df[
        (df["지역"] == selected_region) &
        (df["예산"] <= selected_budget)
    ]

    result = result.sort_values("평점", ascending=False)

    return result

def get_user_input(df):
    selected_region = st.selectbox("지역을 선택하세요", df["지역"].unique())

    selected_budget = st.number_input(
        "사용 가능한 예산을 입력하세요",
        min_value=0,
        value=10000,
        step=1000
    )
















if uploaded_file is not None:
    df = load_data(uploaded_file)

    show_data(df)

    selected_region, selected_budget = get_user_input(df)

    result = filter_places(df, selected_region, selected_budget)

    show_result(result)

    show_charts(df)

else:
    st.info("엑셀 파일을 업로드하면 앱이 실행됩니다.")
