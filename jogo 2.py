# Escrever um algoritimo que mostra os 
# numero pares entre 100 e 120

import streamlit as st
import random

# Configuração da página e título do jogo
st.set_page_config(layout="wide")
st.title("Jogo da Adivinhação de Números")
st.markdown("---")

# Inicializa o estado da sessão se ainda não tiver sido iniciado
if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 100)
    st.session_state.tentativas = 0
    st.session_state.vitorias = 0
    st.session_state.derrotas = 0
    st.session_state.status_jogo = "in_game"

# --- Lógica do Jogo ---

# Função para resetar o jogo
def resetar_jogo():
    st.session_state.numero_secreto = random.randint(1, 100)
    st.session_state.tentativas = 0
    st.session_state.status_jogo = "in_game"

# Formulário para o jogador fazer a adivinhação
with st.form(key="form_adivinhacao"):
    if st.session_state.status_jogo == "in_game":
        palpite = st.number_input("Tente adivinhar o número (entre 1 e 100):", min_value=1, max_value=100, step=1)
        enviar = st.form_submit_button("Adivinhar")

        if enviar:
            st.session_state.tentativas += 1
            if palpite == st.session_state.numero_secreto:
                st.success(f"Parabéns! Você adivinhou em {st.session_state.tentativas} tentativas.")
                st.session_state.vitorias += 1
                st.balloons()
                st.session_state.status_jogo = "vitoria"
            elif palpite < st.session_state.numero_secreto:
                st.warning("O número é maior.")
            else:
                st.warning("O número é menor.")
    
    # Mostra o botão para um novo jogo após a vitória
    if st.session_state.status_jogo != "in_game":
        if st.form_submit_button("Jogar Novamente"):
            resetar_jogo()
            st.rerun()

# --- Painel de Status do Jogo ---

st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tentativas", st.session_state.tentativas)

with col2:
    st.metric("Vitórias", st.session_state.vitorias)

with col3:
    st.metric("Derrotas", st.session_state.derrotas)