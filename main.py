import streamlit as st
import folium
from streamlit_folium import st_folium

# 스페인 여행지 데이터
destinations = {
    "바르셀로나": {
        "coords": (41.3851, 2.1734),
        "description": "가우디의 도시 바르셀로나는 사그라다 파밀리아 성당, 구엘 공원, 바르셀로네타 해변 등으로 유명합니다.",
        "highlights": [
            "사그라다 파밀리아",
            "구엘 공원",
            "람블라스 거리",
            "바르셀로네타 해변"
        ]
    },
    "마드리드": {
        "coords": (40.4168, -3.7038),
        "description": "스페인의 수도 마드리드는 프라도 미술관, 왕궁, 그란비아 거리 등으로 역사와 문화가 가득한 도시입니다.",
        "highlights": [
            "마드리드 왕궁",
            "프라도 미술관",
            "레티로 공원",
            "그란 비아"
        ]
    },
    "세비야": {
        "coords": (37.3891, -5.9845),
        "description": "안달루시아 지방의 중심 도시 세비야는 플라멩코와 알카사르 궁전, 세비야 대성당으로 유명합니다.",
        "highlights": [
            "알카사르",
            "세비야 대성당",
            "히랄다 탑",
            "스페인 광장"
        ]
    }
}

# Streamlit UI
st.set_page_config(page_title="스페인 여행 가이드", layout="wide")

st.title("🇪🇸 스페인 여행지 가이드")
st.write("스페인의 주요 도시를 선택하고, 여행 정보를 확인하세요!")

# 도시 선택
city = st.selectbox("도시 선택", list(destinations.keys()))

# 도시 정보 표시
info = destinations[city]
st.subheader(f"📍 {city}")
st.markdown(f"**설명**: {info['description']}")
st.markdown("**주요 명소:**")
for place in info['highlights']:
    st.markdown(f"- {place}")

# 지도 생성
m = folium.Map(location=info['coords'], zoom_start=6)
folium.Marker(info['coords'], tooltip=city, popup=city).add_to(m)

# 지도 표시
st_folium(m, width=700, height=500)
