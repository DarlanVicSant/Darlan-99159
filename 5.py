# Escrever um algoritimo que mostra os 
# numero pares entre 100 e 120

import streamlit as st
import time

st.title("Atividade 4")

st.write("Escreva um numero e multiplique ele por 2")

numero = st.number_input("Digite um número: ", step=1)


if st.button("Iniciar"):
    for i in range(1,11):
        st.info(f"{numero} x {i} = {numero * i}")
        time.sleep(1)
    st.header("Fim")
