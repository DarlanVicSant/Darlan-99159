import streamlit as st

st.title('Atividade 3')
st.markdown('---')

st.write("Insira as 3 notas para calcular a média e verificar o status do aluno.")


nota1 = st.number_input('Digite a primeira nota:', min_value=0.0, max_value=10.0, step=0.1)
nota2 = st.number_input('Digite a segunda nota:', min_value=0.0, max_value=10.0, step=0.1)
nota3 = st.number_input('Digite a terceira nota:', min_value=0.0, max_value=10.0, step=0.1)

if st.button('Calcular Média'):

    if (nota1 + nota2 + nota3) > 0:
        media = (nota1 + nota2 + nota3) / 3

        st.subheader('Resultado')
        st.info(f"Media do aluno é: {media: .2f}")
   
        if media >= 7.0:
            st.success('**Situação: APROVADO**')
        elif media < 4.0:
            st.error('**Situação: REPROVADO**')
        else:
            st.warning('**Situação: RECUPERAÇÃO**')
    else:
        st.error('Por favor, insira as 3 notas para continuar.')