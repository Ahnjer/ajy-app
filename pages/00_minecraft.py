import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="3D 직육면체 시뮬레이터", layout="centered")
st.title("📦 자유 크기 조절 + 확대/축소 가능한 3D 직육면체")

# 사용자 입력 받기
width = st.number_input("가로 (X축, 빨강)", min_value=0.1, value=2.0)
depth = st.number_input("세로 (Y축, 파랑)", min_value=0.1, value=3.0)
height = st.number_input("높이 (Z축, 초록)", min_value=0.1, value=4.0)

# 확대/축소 비율
scale = st.slider("확대/축소 비율", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

# 스케일 적용
width *= scale
depth *= scale
height *= scale

# 꼭짓점 좌표
def get_cuboid_vertices(w, d, h):
    x = [0, w, w, 0, 0, w, w, 0]
    y = [0, 0, d, d, 0, 0, d, d]
    z = [0, 0, 0, 0, h, h, h, h]
    return x, y, z

x, y, z = get_cuboid_vertices(width, depth, height)

# 면 정의 및 색상
faces = [
    ([0, 1, 2], "lightgray"), ([0, 2, 3], "lightgray"),  # 바닥
    ([4, 5, 6], "lightgray"), ([4, 6, 7], "lightgray"),  # 천장
    ([0, 1, 5], "red"), ([0, 5, 4], "red"),               # 앞면 (빨강)
    ([3, 2, 6], "red"), ([3, 6, 7], "red"),               # 뒷면 (빨강)
    ([0, 3, 7], "blue"), ([0, 7, 4], "blue"),             # 왼쪽 (파랑)
    ([1, 2, 6], "blue"), ([1, 6, 5], "blue"),             # 오른쪽 (파랑)
    ([4, 5, 6], "green"), ([4, 6, 7], "green")            # 윗면 (초록)
]

fig = go.Figure()

for (i, j, k), color in faces:
    fig.add_trace(go.Mesh3d(
        x=x, y=y, z=z,
        i=[i], j=[j], k=[k],
        color=color,
        opacity=0.6,
        showscale=False
    ))

fig.update_layout(
    scene=dict(
        xaxis_title="X (가로, 빨강)",
        yaxis_title="Y (세로, 파랑)",
        zaxis_title="Z (높이, 초록)",
        aspectmode='data'
    ),
    width=800,
    height=700
)

st.plotly_chart(fig, use_container_width=True)
