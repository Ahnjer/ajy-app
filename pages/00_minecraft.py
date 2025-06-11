    import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="3D 직육면체 시뮬레이터", layout="centered")
st.title("📦 3D 직육면체 시뮬레이터 (빨강-파랑-초록)")

# 입력
width = st.number_input("가로 (X축, 빨강)", min_value=0.1, value=2.0)
depth = st.number_input("세로 (Y축, 파랑)", min_value=0.1, value=3.0)
height = st.number_input("높이 (Z축, 초록)", min_value=0.1, value=4.0)

# 꼭짓점
x = [0, width, width, 0, 0, width, width, 0]
y = [0, 0, depth, depth, 0, 0, depth, depth]
z = [0, 0, 0, 0, height, height, height, height]

# 면 정의 (삼각형 2개씩)
faces = [
    # 바닥
    ([0, 1, 2], "lightgray"), ([0, 2, 3], "lightgray"),
    # 천장
    ([4, 5, 6], "lightgray"), ([4, 6, 7], "lightgray"),
    # 앞/뒤 (빨강)
    ([0, 1, 5], "red"), ([0, 5, 4], "red"),
    ([3, 2, 6], "red"), ([3, 6, 7], "red"),
    # 왼/오른쪽 (파랑)
    ([0, 3, 7], "blue"), ([0, 7, 4], "blue"),
    ([1, 2, 6], "blue"), ([1, 6, 5], "blue"),
    # 높이 강조 (초록) → 천장
    ([4, 5, 6], "green"), ([4, 6, 7], "green"),
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
        xaxis_title="가로 (X)",
        yaxis_title="세로 (Y)",
        zaxis_title="높이 (Z)"
    ),
    width=800,
    height=700
)

st.plotly_chart(fig, use_container_width=True)
