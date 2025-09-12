import streamlit as st


st.title("Laços repitiçao - While")

nota1 = st.number_input("Digite uma nota: ", step=1)
nota2 = st.number_input("Digite outra nota: ", step=1)

soma = 0
media = nota1 / nota2 

if st.button("Iniciar"):
        if nota1 < 0 or nota2 < 10:
            st.warning("A nota deve ser entre 0 e 10")
            st.write(f"A media é igual {media}")
