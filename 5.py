import streamlit as st
import time

st.title("Atividade 6")

st.header("Contagem regressiva")

st.write("Solicite a um usuario um número e faça a contagem regressiva")

numero = st.number_input("Digite um numero ", step = 1, min_value = 0)

if st.button("Iniciar"):
    for i in range(numero,0, -1):
        st.warning(i)
        time.sleep(i)
    st.header("Fim")
    # st.balloons()
else:
    st.info("Informe um número")    