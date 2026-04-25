import streamlit as st

places = [
    {"이름": "강릉 시립도서관", "지역": "강릉", "실내여부": "실내", "예산": 0, "한줄 설명": "조용히 공부하기 좋은 공간"},
    {"이름": "강릉 중앙시장", "지역": "강릉", "실내여부": "실내", "예산": 10000, "한줄 설명": "저렴하게 식사할 수 있는 시장"},
    {"이름": "속초해변", "지역": "속초", "실내여부": "실외", "예산": 0, "한줄 설명": "바다를 보며 쉬기 좋은 장소"},
    {"이름": "춘천 시립도서관", "지역": "춘천", "실내여부": "실내", "예산": 0, "한줄 설명": "학습과 독서에 적합한 공간"}
]

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

st.subheader("장소 추가하기")
new_name = st.text_input("이름")
new_region = st.selectbox("지역", ["강릉", "속초", "춘천"])
new_indoor = st.radio("실내 여부", ["실내", "실외"])
new_budget = st.number_input("예산", min_value = 0)
new_description = st.text_input("한줄 설명")

if st.button("장소 추가"):
    if new_name != "":
        exists = False
        for place in places:
            if place["이름"] == new_name:
                exists = True
        if exists:
            st.warning("이미 '이름'이(가) 있습니다")
        else:
            places = add_place(places, new_name, new_region, new_indoor, new_budget, new_description)
            st.success("장소가 추가되었습니다.")
    else:
        st.warning("장소 이름을 입력하세요")
        

selected_region = st.selectbox("지역을 선택하세요", ["강릉", "속초", "춘천"])
selected_indoor = st.radio("실내 여부를 선택하세요", ["실내", "실외"])

if st.button("추천 보기"):
    recommendations = get_recommendations(places, selected_region, selected_indoor)

    if len(recommendations) == 0:
        st.write("조건에 맞는 장소가 없습니다")
    else:
        for place in recommendations:
            st.write(place["이름"])
            st.write(place["한줄 설명"])
            st.write("---")
