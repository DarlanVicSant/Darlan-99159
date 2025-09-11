# Escrever um algoritimo que mostra os 
# numero pares entre 100 e 120

import streamlit as st
import time

st.title("Atividade 1")

st.header("Laços de repitição: For")


if st.button("Iniciar"):
    for i in range(100,121,2):
        st.info(i)
        time.sleep(2)