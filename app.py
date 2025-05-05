import streamlit as st
import matplotlib.pyplot as plt

st.title("Téglalap interaktív ábrája")

a = st.slider("a oldal", min_value=0.0, max_value=10.0, step=0.1, value=3.0)
b = st.slider("b oldal", min_value=0.0, max_value=10.0, step=0.1, value=4.0)

area = a * b
perimeter = 2 * (a + b)

st.write(f"**Terület**: {area:.2f}")
st.write(f"**Kerület**: {perimeter:.2f}")

fig, ax = plt.subplots()
ax.plot([0, a, a, 0, 0], [0, 0, b, b, 0], 'b-')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 11)
ax.set_aspect('equal')
ax.grid(True)

st.pyplot(fig)
