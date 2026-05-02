import streamlit as st

if "placelist" not in st.session_state:
    st.session_state.placelist = [
        {"이름": "가톨릭관동대학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "잔디가 좋지만, 관객석이 더러운 곳"},
        {"이름": "문성고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "고지대에 있어서 산에서 축구하는 느낌이 나는 곳"},
        {"이름": "강릉고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "소나무가 많아서 공기가 좋은곳"},
        {"이름": "제일고등학교", "지역": "강릉", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "축구부가 있어 최고의 잔디를 느낄 수 있는 곳"},
        {"이름": "강원대학교 강릉캠퍼스", "지역": "강릉", "잔디상태": "안좋음", "시간당 사용료": 20000, "한줄설명": "밤 11시까지 불이 켜지는 밤에도 축구하기 좋은 곳"},
        {"이름": "강남축구공원", "지역": "강릉", "잔디상태": "안좋음", "시간당 사용료": 50000, "한줄설명": "풋살장2개, 축구장2개가 있는 곳"},
        {"이름": "엑스포잔디광장", "지역": "속초", "잔디상태": "좋음", "시간당 사용료": 0, "한줄설명": "청초호 옆에 있어 호수도 갈 수 있지만, 골대가 없는 곳"},
        {"이름": "공지천인조잔디구장", "지역": "춘천", "잔디상태": "좋음", "시간당 사용료": 10000, "한줄설명": "손흥민이 어린시절 아버지와 함께 훈련하던 곳"}
    ]

def show_all_places(place_list):
    st.subheader("전체 장소 보기")
    for place in place_list:
        st.write(f"이름: {place['이름']} | 지역: {place['지역']} | 사용료: {place['시간당 사용료']}원")
        st.write(f"설명: {place['한줄설명']}")
        st.write("---")

def find_places(place_list, region, turf_condition, max_fee):
    result = []
    for place in place_list:
        if (place["지역"] == region and 
            place["잔디상태"] == turf_condition and 
            int(place["시간당 사용료"]) <= max_fee):
            result.append(place)
    return result

def add_place(name, region, turf_condition, fee, description):
    if name == "":
        st.warning("장소 이름은 반드시 입력해주세요.")
    else:
        st.session_state.placelist.append({
            "이름": name, "지역": region, "잔디상태": turf_condition, "시간당 사용료": fee, "한줄설명": description
        })
        st.success("새 장소가 추가되었습니다.")

st.title("강원생활도우미앱")

menu = st.sidebar.selectbox("기능을 선택하세요", ["전체 보기", "무료 장소 보기", "추천 받기", "장소 추가"])

current_placelist = st.session_state.placelist

if menu == "전체 보기":
    show_all_places(current_placelist)

elif menu == "무료 장소 보기":
    st.subheader("무료 장소 목록")
    for place in current_placelist:
        if place["시간당 사용료"] == 0:
            st.write(f"이름: {place['이름']} ({place['지역']})")
            st.write(f"설명: {place['한줄설명']}")
            st.write("---")

elif menu == "추천 받기":
    region = st.selectbox("지역", ["강릉", "속초", "춘천"])
    turf = st.selectbox("잔디상태", ["좋음", "안좋음"])
    budget = st.number_input("예산", min_value=0, value=50000)
    if st.button("추천 받기"):
        result = find_places(current_placelist, region, turf, budget)
        if result:
            for p in result:
                st.write(f"{p['이름']}: {p['한줄설명']}")
        else:
            st.write("조건에 맞는 장소가 없습니다.")

elif menu == "장소 추가":
    with st.form("add_form"):
        name = st.text_input("장소 이름")
        region = st.selectbox("지역", ["강릉", "속초", "춘천"])
        turf = st.selectbox("잔디", ["좋음", "안좋음"])
        fee = st.number_input("사용료", min_value=0)
        desc = st.text_input("설명")
        if st.form_submit_button("추가"):
            add_place(name, region, turf, fee, desc)
            st.success("추가 완료")
