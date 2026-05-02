import streamlit as st

if "placelist" not in st.session_state:
    st.session_state.placelist = [
        {"이름": "강릉 시립도서관", "지역": "강릉", "실내여부": "실내", "예산": 0, "한줄 설명": "조용히 공부하기 좋은 공간"},
        {"이름": "강릉 중앙시장", "지역": "강릉", "실내여부": "실내", "예산": 10000, "한줄 설명": "저렴하게 식사할 수 있는 시장"},
        {"이름": "속초해변", "지역": "속초", "실내여부": "실외", "예산": 0, "한줄 설명": "바다를 보며 쉬기 좋은 장소"},
        {"이름": "춘천 시립도서관", "지역": "춘천", "실내여부": "실내", "예산": 0, "한줄 설명": "학습과 독서에 적합한 공간"}
    ]

if "regions" not in st.session_state:
    st.session_state.regions = ["강릉", "속초", "춘천"]

def get_recommendations(data, region, indoor):
    result = []
    for place in data:
        if place["지역"] == region and place["실내여부"] == indoor:
            result.append(place)
    return result

def add_place(data, name, region, indoor, budget, description):
    result = []
    for place in data:
        result.append(place)
    new_place = {
        "이름": name,
        "지역": region,
        "실내여부": indoor,
        "예산": budget,
        "한줄 설명": description
    }
    result.append(new_place)
    return result

st.title("강원 청소년 생활 도우미")



new_region = st.text_input("새 지역 입력")

if st.button("지역 추가"):
    if new_region != "":
        if new_region not in st.session_state.regions:
            st.session_state.regions.append(new_region)
            st.success("지역이 추가되었습니다.")
        else:
            st.warning("이미 있는 지역입니다.")
    else:
        st.warning("지역 이름을 입력하세요.")


new_name = st.text_input("이름")
new_region = st.selectbox("지역", st.session_state.regions)
new_indoor = st.radio("실내 여부", ["실내", "실외"])
new_budget = st.number_input("예산", min_value=0)
new_description = st.text_input("한줄 설명")


if len(new_name) != len(set(st.session_state.regions)):
    exists = False
    for place in st.session_state.placelist:
        if place["이름"] == new_name:
            exists = True
    if exists:
        st.warning("이미 그 장소가 있습니다")
    else:
        st.session_state.placelist = add_place(st.session_state.placelist, new_name, new_place_region, new_indoor, new_budget, new_description)
        st.success("장소가 추가되었습니다.")
else:
    st.warning("장소 이름을 입력하세요")
        


selected_region = st.selectbox("지역을 선택하세요", st.session_state.regions)
selected_indoor = st.radio("실내 여부를 선택하세요", ["실내", "실외"])

if st.button("추천 보기"):
    recommendations = get_recommendations(st.session_state.placelist, selected_region, selected_indoor)

    if len(recommendations) == 0:
        st.write("조건에 맞는 장소가 없습니다")
    else:
        for place in recommendations:
            st.write(place["이름"])
            st.write(place["한줄 설명"])
            st.write("---")
