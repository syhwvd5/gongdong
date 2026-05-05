import streamlit as st
import pandas as pd

st.title("강원생활도우미 앱 2.0")
st.write("엑셀 파일을 업로드 할 수 있습니다.")

uploaded_file = st.file_uploader(
    "장소 데이터 엑셀 파일을 업로드해주세요.",
    type=["xlsx"]
)

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file, engine="openpyxl")

        st.success("엑셀 파일을 성공적으로 불러왔습니다.")
        st.subheader("업로드한 장소 목록")
        st.dataframe(df, use_container_width=True)

    except ImportError:
        st.error("openpyxl 패키지가 설치되어 있지 않습니다.")
        st.info("requirements.txt 파일에 openpyxl을 추가해주세요.")

    except Exception as e:
        st.error("엑셀 파일을 읽는 중 오류가 발생했습니다.")
        st.exception(e)

else:
    st.info("데이터를 저장한 엑셀(확장자 .xlsx) 파일을 업로드하세요.")
