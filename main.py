import streamlit as st
import folium
from streamlit_folium import st_folium

# 여행지 데이터
destinations = {
    "스페인": {
        "바르셀로나": {
            "coords": (41.3851, 2.1734),
            "description": "가우디의 도시 바르셀로나는 사그라다 파밀리아 성당, 구엘 공원 등으로 유명합니다.",
            "highlights": ["사그라다 파밀리아", "구엘 공원", "람블라스 거리"]
        },
        "마드리드": {
            "coords": (40.4168, -3.7038),
            "description": "스페인의 수도 마드리드는 역사와 예술이 살아 있는 도시입니다.",
            "highlights": ["프라도 미술관", "마드리드 왕궁", "레티로 공원"]
        }
    },
    "대한민국": {
        "서울": {
            "coords": (37.5665, 126.9780),
            "description": "한국의 수도 서울은 전통과 현대가 공존하는 도시입니다.",
            "highlights": ["경복궁", "남산타워", "홍대거리"]
        },
        "부산": {
            "coords": (35.1796, 129.0756),
            "description": "한국 제2의 도시 부산은 해운대 해수욕장과 감천문화마을로 유명합니다.",
            "highlights": ["해운대", "감천문화마을", "자갈치 시장"]
        }
    },
    "미국": {
        "뉴욕": {
            "coords": (40.7128, -74.0060),
            "description": "미국 최대 도시 뉴욕은 자유의 여신상과 센트럴 파크 등으로 유명합니다.",
            "highlights": ["타임스퀘어", "자유의 여신상", "센트럴 파크"]
        },
        "샌프란시스코": {
            "coords": (37.7749, -122.4194),
            "description": "서부의 매력적인 도시 샌프란시스코는 금문교와 알카트라즈 섬으로 유명합니다.",
            "highlights": ["금문교", "알카트라즈 섬", "피셔맨스 워프"]
        }
    }
}

# Streamlit 설정
st.set_page_config(page_title="세계 여행 가이드", layout="wide")

st.title("🌏 세계 여행지 가이드")
st.markdown("여행하고 싶은 국가와 도시를 선택해보세요!")

# 국가 및 도시 선택
selected_country = st.selectbox("국가 선택", list(destinations.keys()))
selected_city = st.selectbox("도시 선택", list(destinations[selected_country].keys()))

# 선택된 도시 정보
info = destinations[selected_country][selected_city]

st.subheader(f"📍 {selected_city} ({selected_country})")
st.markdown(f"**설명**: {info['description']}")
st.markdown("**주요 명소:**")
for place in info['highlights']:
    st.markdown(f"- {place}")

# 지도 생성
m = folium.Map(location=info['coords'], zoom_start=6)
folium.Marker(
    info['coords'],
    tooltip=selected_city,
    popup=selected_city,
    icon=folium.Icon(color='red', icon='glyphicon-map-marker')
).add_to(m)

# 지도 표시
st_folium(m, width=700, height=500)
