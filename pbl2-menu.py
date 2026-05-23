import pandas as pd
import streamlit as st


def load_file():
    uploaded_file = st.file_uploader(
        "장소 데이터 엑셀 파일을 업로드하세요", type=["xlsx"]
    )
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        return df
    else:
        st.info("엑셀 파일을 업로드하면 데이터가 표시됩니다")
        return None


def print_table(table, table_name):
    st.subheader(table_name)
    if len(table) > 0:
        st.dataframe(table)
    else:
        st.warning("출력할 장소가 없습니다")


# df를 매개변수(argument)로 받도록 수정하여 NameError를 방지합니다.
def get_user_input(df):
    selected_region = st.selectbox("지역을 선택하세요", df["지역"].unique())
    selected_budget = st.number_input(
        "사용 가능한 예산을 입력하세요", min_value=0, value=10000, step=1000
    )
    result = df[(df["지역"] == selected_region) & (df["예산"] <= selected_budget)]
    return result


def show_filter_places(result):
    if len(result) > 0:
        st.dataframe(result)
    else:
        st.warning("조건에 맞는 장소가 없습니다.")


def count_chart(df, key):
    key_count = df[key].value_counts()
    st.subheader(key + "별 장소 개수")
    st.bar_chart(key_count)


def average_chart(df, group, num):
    avg_score = df.groupby(group)[num].mean()
    st.subheader(group + "별 평균 " + num)
    st.bar_chart(avg_score)


# --- 메인 실행 흐름 ---
st.title("강원 생활 도우미 2.0")
st.write("엑셀 파일을 업로드하면 장소 데이터를 확인할 수 있습니다.")

df = load_file()

menu = st.sidebar.radio("메뉴를 선택하세요", ["업로드한 장소 데이터", "장소 검색"])

# 파일이 업로드된 경우에만 아래 로직이 실행됩니다.
if df is not None:
    if menu == "업로드한 장소 데이터":
        print_table(df, "업로드한 장소 데이터")
        st.markdown("---")
        st.subheader("데이터 통계 시각화")

        count_chart(df, "지역")
        count_chart(df, "유형")
        average_chart(df, "지역", "평점")

    elif menu == "장소 검색":
        st.markdown("---")
        st.subheader("조건별 장소 검색")

        result = get_user_input(df)
        show_filter_places(result)
