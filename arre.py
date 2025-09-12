import streamlit as st

st.title("Atividade 2")

soma = 0 

for i in range(4):
    nota = st.number_input(f"Digite a {i+1} nota: ")
    soma = soma + nota

media = soma / 4

if st.button("Motrar o resultado"):
   st.info(f"Media é igual a {media}")