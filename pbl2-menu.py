# 아래 주석들은 한글 파일에서 복사하는 과정에서 띄어쓰기가 막 되어있거나 들여쓰기가 안 되어있어서 ai에게 올바르게 배열해달라고 요청했다가 ai가 멋대로 단 주석입니다


import pandas as pd
import streamlit as st

df = None

def home():
    st.subheader("앱 설명")
    st.write("이 앱은 엑셀 파일을 업로드하고, 장소 데이터와 데이터를 차트로 시각화된 데이터를 확인하고, 조건에 맞는 장소를 검색하는 앱입니다.")

    st.write("엑셀 파일에는 최소한 다음과 같은 데이터가 있어야합니다.")

    example = ["이름", "지역", "유형", "실내여부", "예산", "평점"]
    st.write(example)

def load_file():
    uploaded_file = st.sidebar.file_uploader(
        "장소 데이터 엑셀 파일을 업로드하세요", type=["xlsx"]
    )
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        return df
    else:
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

df = load_file()

# 파일이 업로드된 경우에만 아래 로직이 실행됩니다.
if df is None:
    st.write("엑셀 파일을 업로드하면 장소 데이터를 확인할 수 있습니다.")
    st.info("엑셀 파일을 업로드하면 데이터가 표시됩니다")
    st.markdown("---")
    home()

elif df is not None:
    menu = st.sidebar.radio("메뉴를 선택하세요", ["업로드한 장소 데이터", "장소 검색"])
    st.info("만약 메뉴가 보이지 않는다면 왼쪽 상단 구석에 위치한 사이드바를 여세요")
    
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
