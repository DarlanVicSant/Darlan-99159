# Verifique a idade de uma pessoa.
# Se menor que 18, mostre: Menor idade
# Caso contrario, mostre: Maior idade
# Usando streamlit

import streamlit as st

st.title("Verificando a idade")
 
numero1 = st.number_input(("Digite o numero 1: ") , value = 0 )
numero2 = st.number_input(("Digite o numero 2: ") , value = 0 )

    
soma = numero1 + numero2
media = numero1 / numero2
menor = numero1 - numero2
maior = numero1 * numero2


if st.button("Confirma?"):

      st.write(f"O primeiro número digitado foi: **{numero1}**")
      st.write(f"O segundo número digitado foi: **{numero2}**")
      st.write(f"Soma é igual: {soma}")
      st.write(f"A media é igual: {media}")
      st.write(f"Menor é igual: {menor}")
      st.write(f"Maior é igual: {maior}")


    