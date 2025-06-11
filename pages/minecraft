import streamlit as st
import folium
from folium import IFrame
from streamlit_folium import st_folium

# 블럭 데이터 예시
block_data = {
    "Crafting Table": {
        "description": "아이템을 제작할 수 있는 기본 제작대입니다.",
        "recipe": {
            "needed": ["Oak Planks", "Oak Planks", "Oak Planks", "Oak Planks"],
            "layout": [
                ["Oak Planks", "Oak Planks"],
                ["Oak Planks", "Oak Planks"]
            ]
        },
        "image_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/0/07/Crafting_Table_JE5_BE5.png",  # CC License
        "location": [37.5665, 126.9780]  # 서울 예시
    },
    "Oak Planks": {
        "description": "나무를 가공해서 만든 기본 블럭입니다.",
        "recipe": {
            "needed": ["Oak Log"],
            "layout": [["Oak Log"]]
        },
        "image_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/55/Oak_Planks.png",
        "location": [35.1796, 129.0756]  # 부산 예시
    }
}

# 지도 생성
m = folium.Map(location=[36.5, 127.5], zoom_start=6)

# 블럭을 지도에 추가
for name, data in block_data.items():
    html = f"""
    <h4>{name}</h4>
    <img src="{data['image_url']}" width="100"><br>
    <p>{data['description']}</p>
    <b>조합식:</b>
    <ul>
        {''.join(f"<li>{item}</li>" for item in data['recipe']['needed'])}
    </ul>
    """
    iframe = IFrame(html, width=200, height=300)
    popup = folium.Popup(iframe, max_width=250)
    folium.Marker(location=data["location"], popup=popup, tooltip=name).add_to(m)

# 스트림릿 출력
st.title("🧱 마인크래프트 블럭 가이드")
st.write("마인크래프트의 대표 블럭과 조합식을 지도 위에서 확인해보세요.")
st_data = st_folium(m, width=700, height=500)
