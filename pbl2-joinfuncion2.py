import streamlit as st
import pandas as pd

st.title("강원생활도우미앱 3.0")

uploaded_file = None

def home():
    st.subheader("앱 설명")
    st.write("이 앱은 엑셀 파일을 업로드하고, 장소 데이터와 데이터를 차트로 시각화된 데이터를 확인하고, 조건에 맞는 장소를 검색하는 앱입니다.")

    st.write("엑셀 파일에는 최소한 다음과 같은 데이터가 있어야합니다.")

    example = ["이름", "지역", "유형", "실내여부", "예산", "평점", "추천목적", "추천상황", "추천대상", "예약필요"]
    st.write(example)

def load_data(uploaded_file):
    place_df = pd.read_excel(uploaded_file, sheet_name="장소정보")
    recommend_df = pd.read_excel(uploaded_file, sheet_name="추천정보")
    return place_df, recommend_df


def join_data(place_df, recommend_df):
    merged_df = pd.merge(
        recommend_df,
        place_df,
        on="place_id",
        how="left"
    )

    return merged_df

def show_original_data(place_df, recommend_df):
    st.subheader("장소정보 시트")
    st.dataframe(place_df)

    st.subheader("추천정보 시트")
    st.dataframe(recommend_df)

def show_joined_data(df):
    st.subheader("조인된 데이터")
    st.dataframe(df)

def search_recommendations(df):
    st.sidebar.subheader("추천 장소 검색")

    selected_region = st.sidebar.selectbox(
        "지역 선택",
        df["지역"].unique()
    )

    selected_purpose = st.sidebar.selectbox(
        "추천목적 선택",
        df["추천목적"].unique()
    )

    selected_situation = st.sidebar.selectbox(
        "추천상황 선택",
        df["추천상황"].unique()
    )

    selected_target = st.sidebar.selectbox(
        "추천대상 선택",
        df["추천대상"].unique()
    )

    selected_budget = st.sidebar.number_input(
        "최대 예산",
        min_value=0,
        value=10000,
        step=1000
    )

    result = df[
        (df["지역"] == selected_region) &
        (df["추천목적"] == selected_purpose) &
        (df["추천상황"] == selected_situation) &
        (df["추천대상"] == selected_target) &
        (df["예산"] <= selected_budget)
    ]

    st.subheader("검색 결과")

    if len(result) > 0:
        st.dataframe(result)
    else:
        st.warning("조건에 맞는 추천 장소가 없습니다.")

def show_chart(df):
    st.subheader("데이터 시각화")

    chart_option = st.selectbox(
        "시각화 기준 선택",
        ["지역", "유형", "추천목적", "추천상황", "추천대상", "예약필요"]
    )

    chart_data = df[chart_option].value_counts()

    st.bar_chart(chart_data)

uploaded_file = st.file_uploader(
    "엑셀 파일을 업로드하세요",
    type=["xlsx"]
)


if uploaded_file is None:
    st.write("엑셀 파일을 업로드하면 장소 데이터를 확인할 수 있습니다.")
    st.info("엑셀 파일을 업로드하면 데이터가 표시됩니다")
    st.markdown("---")
    home()
    


if uploaded_file is not None:
    place_df, recommend_df = load_data(uploaded_file)
    merged_df = join_data(place_df, recommend_df)

    menu = st.selectbox(
        "메뉴 선택",
        ["원본 데이터 보기", "조인 데이터 보기", "추천 검색", "데이터 시각화"]
    )

    if menu == "원본 데이터 보기":
        show_original_data(place_df, recommend_df)

    elif menu == "조인 데이터 보기":
        show_joined_data(merged_df)

    elif menu == "추천 검색":
        search_recommendations(merged_df)

    elif menu == "데이터 시각화":
        show_chart(merged_df)
