import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="3D 직육면체 시뮬레이터", layout="centered")
st.title("📦 가로-세로-높이 색상 구분 직육면체 시뮬레이터")

# 입력
width = st.number_input("가로 (X, 빨강)", min_value=1.0, value=2.0)
depth = st.number_input("세로 (Y, 파랑)", min_value=1.0, value=3.0)
height = st.number_input("높이 (Z, 초록)", min_value=1.0, value=4.0)

# 꼭짓점 좌표
x = [0, width, width, 0, 0, width, width, 0]
y = [0, 0, depth, depth, 0, 0, depth, depth]
z = [0, 0, 0, 0, height, height, height, height]

# 각 면 구성 (삼각형 두 개로 구성)
faces = {
    "빨강 (가로)": [[0,1,5], [0,5,4], [3,2,6], [3,6,7]],
    "파랑 (세로)": [[0,3,7], [0,7,4], [1,2,6], [1,6,5]],
    "초록 (높이)": [[0,1,2], [0,2,3], [4,5,6], [4,6,7]]
}
colors = {
    "빨강 (가로)": "red",
    "파랑 (세로)": "blue",
    "초록 (높이)": "green"
}

# 각 면별로 Mesh3d 객체 만들기
fig = go.Figure()

for direction, tris in faces.items():
    fig.add_trace(go.Mesh3d(
        x=x, y=y, z=z,
        i=[t[0] for t in tris],
        j=[t[1] for t in tris],
        k=[t[2] for t in tris],
        color=colors[direction],
        opacity=0.5,
        name=direction,
        showscale=False
    ))

fig.update_layout(
    scene=dict(
        xaxis_title="X (가_
