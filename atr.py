import streamlit as st
import time

st.title("Atividade 7")

st.header("Numeros inteiros")

st.write("Solicite a um usuario 5 número inteiro e some")


st.title("Calculadora de Soma de 5 Números")

st.write("Insira 5 números inteiros para calcular a soma.")


num1 = st.number_input("Número 1", value=0, step=1)
num2 = st.number_input("Número 2", value=0, step=1)
num3 = st.number_input("Número 3", value=0, step=1)
num4 = st.number_input("Número 4", value=0, step=1)
num5 = st.number_input("Número 5", value=0, step=1)


soma = num1 + num2 + num3 + num4 + num5

if st.button("Iniciar soma"):
    st.subheader("Resultado da Soma")
    st.write(f"A soma dos números é: **{soma}**")
else:
    st.info("Informe os numeros")