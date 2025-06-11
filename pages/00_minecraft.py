import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# 블럭 데이터 정의
block_data = {
    "Crafting Table": {
        "description": "아이템을 제작할 수 있는 기본 제작대입니다.",
        "recipe": [
            ["Oak Planks", "Oak Planks"],
            ["Oak Planks", "Oak Planks"]
        ],
        "image_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/0/07/Crafting_Table_JE5_BE5.png"
    },
    "Oak Planks": {
        "description": "나무를 가공해서 만든 기본 블럭입니다.",
        "recipe": [
            ["Oak Log"]
        ],
        "image_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/55/Oak_Planks.png"
    },
    "Oak Log": {
        "description": "오크 나무에서 직접 얻을 수 있는 기본 자원입니다.",
        "recipe": None,
        "image_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/59/Oak_Log.png"
    },
    "Furnace": {
        "description": "아이템을 제련하거나 굽는 데 사용됩니다.",
        "recipe": [
            ["Cobblestone", "Cobblestone", "Cobblestone"],
            ["Cobblestone",     None,     "Cobblestone"],
            ["Cobblestone", "Cobblestone", "Cobblestone"]
        ],
        "image_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/9/9a/Furnace_JE5_BE5.png"
    },
    "Cobblestone": {
        "description": "돌을 곡괭이로 캤을 때 얻는 기본 건축 자재입니다.",
        "recipe": None,
        "image_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/7/74/Cobblestone.png"
    },
    "Stick": {
        "description": "도구나 무기 조합에 쓰이는 중요한 부품입니다.",
        "recipe": [
            [None],
            ["Oak Planks"],
            ["Oak Planks"]
        ],
        "image_url": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f7/Stick_JE2_BE2.png"
    }
}

# 블럭 선택
selected_block = st.selectbox("🧱 블럭을 선택하세요", list(block_data.keys()))

# 선택된 블럭 정보 표시
block = block_data[selected_block]
st.header(f"🧱 {selected_block}")
st.image(block["image_url"], width=100)
st.markdown(f"**설명:** {block['description']}")

# 조합식 시각화
if block["recipe"]:
    st.markdown("### 🧩 조합식")
    for row in block["recipe"]:
        cols = st.columns(len(row))
        for col, item in zip(cols, row):
            if item and item in block_data:
                response = requests.get(block_data[item]["image_url"])
                image = Image.open(BytesIO(response.content))
                col.image(image, width=50, caption=item)
            else:
                col.markdown(" ")
else:
    st.info("이 블럭은 자연에서 획득하거나 조합 없이 얻을 수 있습니다.")

