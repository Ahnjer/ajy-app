import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="3D 직육면체 시뮬레이터", layout="centered")
st.title("📦 3D 직육면체 시뮬레이터 (방향별 색상)")

# 입력값 받기
width = st.number_input("가로 (X축, 빨강)", min_value=0.1, value=2.0)
depth = st.number_input("세로 (Y축, 파랑)", min_value=0.1, value=3.0)
height = st.number_input("높이 (Z축, 초록)", min_value=0.1, value=4.0)

# 꼭짓점 좌표
x = [0, width, width, 0, 0, width, width, 0]
y = [0, 0, depth, depth, 0, 0, depth, depth]
z = [0, 0, 0, 0, height, height, height, height]

# 각 면의 삼각형 정의
faces = [
    # 바닥 (투명 처리 가능)
    ([0, 1, 2], "lightgray"), ([0, 2, 3], "lightgray"),
    # 위
    ([4, 5, 6], "lightgray"), ([4, 6, 7], "lightgray"),
    # 앞 (빨강)
    ([0, 1, 5], "red"), ([0, 5, 4], "red"),
    # 뒤 (빨강)
    ([3, 2, 6], "red"), ([3, 6, 7], "red"),
    # 오른쪽 (파랑)
    ([1, 2, 6], "blue"), ([1, 6, 5], "blue"),
    # 왼쪽 (파랑)
    ([0, 3, 7], "blue"), ([0, 7, 4], "blue"),
    # 앞면 높이 (초록)
    ([4, 5, 6], "green"), ([4, 6, 7], "green")
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
        xaxis_title="X (가로)",
        yaxis_title="Y (세로)",
        zaxis_title="Z (높이)"
    ),
    width=800,
    height=700
)

st.plotly_chart(fig, use_container_width=True)
