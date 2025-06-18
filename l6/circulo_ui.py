import streamlit as st
from circulo import Circulo


c = Circulo()
col1,col2,col3,col4 = st.columns(4)


c.raio = col1.number_input("Digite o raio:",min_value=0)
with st.container(border=True):
    colleft,colright= st.columns(2)
    if colleft.button("Calcular area", type='primary',use_container_width=True,icon='😀'):
        colleft.write(f'Area = {c.calc_area():.2f}')
    if colright.button("Calcular circunferencia"):
        colleft.write(f'Circunferência= {c.calc_circunferencia():.2f}')

