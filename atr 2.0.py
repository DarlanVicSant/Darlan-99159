import streamlit as st
import time

st.title("Laço repitiçao")
 
st.header("Contagem numeros pares")

pares = (num for num in range(100,121) if num & 2 == 0)

if st.button("Iniciar"):
 st.write("Os numeros pares são:") 
 for p in pares: 
    st.write(p)

    


    