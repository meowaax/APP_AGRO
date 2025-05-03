import streamlit as st
from streamlit_option_menu import option_menu
from pags.dados import adicionar_linha_excel, get_data
import pandas as pd
from pags.dados import get_parcela, get_planta, get_dano
from numpy import nan
from datetime import datetime


def adicionar_registro():
    
    st.markdown('## Novo Registro')
    
    data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    parcelas = get_parcela()
    st.markdown('#### Parcela:')
    parcela = st.selectbox("", parcelas, key='parcela', index=None)
    
    plantas = get_planta()
    st.markdown("#### Planta:")
    planta = st.selectbox("", plantas, key='planta', index=None)
    
    st.markdown("#### Presença de Spodoptera:")
    praga = st.radio('', ['Sim', 'Não'])

    danos = get_dano()
    st.markdown("#### Nota de Dano:")
    dano = st.select_slider("", options=danos)

    st.markdown("#### Altura da planta (cm):")
    altura = st.number_input("", min_value=0.0, step=0.1)
    
    st.markdown("#### Folhas (n°):")
    folhas = st.number_input("", min_value=0, step=1)
    
    st.markdown("#### Observação (opcional):")
    obs = st.text_area("")

  # Verificar se todos os campos obrigatórios foram preenchidos
    if parcela and planta and praga and dano and altura and folhas:
        if st.button("Adicionar"):
            cadastrar_registro(data, parcela, planta, praga, dano, altura, folhas, obs)
    else:
        st.warning("Por favor, preencha todos os campos obrigatórios antes de fazer o registro.")
        
    
def cadastrar_registro(data, parcela, planta, praga, dano, altura, folhas, obs):
    adicionar_linha_excel([data, parcela, planta, praga, dano, altura, folhas, obs])
    
    st.markdown('### Registro realizado com Sucesso!')
