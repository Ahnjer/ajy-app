import streamlit as st
import plotly.graph_objects as go

st.title("📦 3D 직육면체 시뮬레이터")

# 사용자 입력
width = st.number_input("가로 (X축)", min_value=1.0, value=2.0)
depth = st.number_input("세로 (Y축)", min_value=1.0, value=3.0)
height = st.number_input("높이 (Z축)", min_value=1.0, value=4.0)

# 꼭짓점 좌표 계산
x = [0, width, width, 0, 0, width, width, 0]
y = [0, 0, depth, depth, 0, 0, depth, depth]
z = [0, 0, 0, 0, height, height, height, height]

# 면을 정의 (삼각형 두 개로 하나의 면 구성)
faces = [
    [0,1,2], [0,2,3], # 아래면
    [4,5,6], [4,6,7], # 윗면
    [0,1,5], [0,5,4], # 앞면
    [2,3,7], [2,7,6], # 뒷면
    [1,2,6], [1,6,5], # 오른면
    [0,3,7], [0,7,4]  # 왼면
]

# 시각화
fig = go.Figure(data=[
    go.Mesh3d(
        x=x, y=y, z=z,
        i=[f[0] for f in faces],
        j=[f[1] for f in faces],
        k=[f[2] for f in faces],
        color='lightblue',
        opacity=0.50
    )
])

fig.update_layout(
    scene=dict(
        xaxis_title='X (가로)',
        yaxis_title='Y (세로)',
        zaxis_title='Z (높이)'
    ),
    width=700,
    height=700
)

st.plotly_chart(fig)
