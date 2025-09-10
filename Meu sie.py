import streamlit as st

# Curso de cantadas
st.title("Curso de Kiwify")

# CANTADA 1
st.header("Curso de como fazer dinhero")
st.write("Curso 1")
st.write("Curso 2")

# Adicionando um botão
if st.button("clique aqui para adquirir o curso"):
    st.write("Chave pix copiada")

# Adicionando um controle deslizante (slider)
valor = st.slider("Escolha um valor", 0, 100, 50)
st.write(f"O valor escolhido é: {valor}")