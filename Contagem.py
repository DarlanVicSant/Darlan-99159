import streamlit as st
import random
import time

# --- Configurações da página ---
st.set_page_config(
    page_title="Jogo do Tigrinho (Protótipo)",
    page_icon="🐅"
)

# --- Título e descrição ---
st.title("🐅 Jogo do Tigrinho 🐅")
st.markdown("""
    Bem-vindo ao nosso protótipo de jogo! Clique em "Rodar" para sortear
    os símbolos. Se os 3 símbolos forem iguais, você ganha!
""")

# --- Símbolos do jogo ---
simbolos = ["💎", "💰", "🍀", "🍇", "7️⃣"]

# --- Lógica do jogo ---
def rodar_jogo():
    """Simula o sorteio dos símbolos."""
    col1, col2, col3 = st.columns(3)

    # Inicia com símbolos "rodando"
    with col1:
        st.header("?")
    with col2:
        st.header("?")
    with col3:
        st.header("?")

    st.balloons()
    time.sleep(1) # Pequena pausa para a animação

    # Sorteia os símbolos
    resultado_sorteio = [random.choice(simbolos) for _ in range(3)]

    # Mostra o resultado final
    with col1:
        st.header(resultado_sorteio[0])
    with col2:
        st.header(resultado_sorteio[1])
    with col3:
        st.header(resultado_sorteio[2])

    # Verifica se o jogador ganhou
    if resultado_sorteio[0] == resultado_sorteio[1] == resultado_sorteio[2]:
        st.success("🎉 Parabéns, você ganhou! 🎉")
        st.balloons()
    else:
        st.error("🎰 Que pena, tente novamente! 🎰")


# --- Botão para iniciar o jogo ---
if st.button("Rodar"):
    st.markdown("---")
    rodar_jogo()
    st.markdown("---")