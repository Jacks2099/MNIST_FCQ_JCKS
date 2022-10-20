import streamlit as st
st.title("Mi aplicación")
st.sidebar.header("Esta aplicación es solo un demo")
st.sidebar.image("http://fcq.uach.mx/images/institucionales/Logo-FCQ-sin-sombra.png")
boton = st.button("Globos")
if boton:
  st.balloon()
