import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from pags.dados import get_parcela, get_dano, get_datas, get_planta, editar_linha_excel


def editar_registro():
    st.markdown("## Editar Registro")
    
    datas = get_datas()
    st.markdown('#### Data do registro:')
    data = st.selectbox("", datas, key='data', index=None)

    # Obter a lista de parcelas existentes
    parcelas = get_parcela()
    # Selecionar uma parcela existente
    st.markdown('#### Parcela:')
    parcela = st.selectbox("", parcelas, key='parcela', index=None)

    plantas = get_planta()
    st.markdown('#### Planta: ')
    planta = st.selectbox("", plantas, key='planta', index=None)

    if data and parcela and planta:
        # Adicionar campos de edição
        st.markdown("## Campos de Edição")
    
        st.markdown("#### Presença de Spodoptera:")
        praga = st.radio('', ['Sim', 'Não'])

        st.markdown("#### Nota de Dano:")
        dano = st.select_slider("", options=get_dano())

        st.markdown("#### Altura da planta (cm):")
        altura = st.number_input("", min_value=0.0, step=0.1)
        
        st.markdown("#### Folhas (n°):")
        folhas = st.number_input("", min_value=0, step=1)
        
        st.markdown("#### Observação (opcional):")
        obs = st.text_area("")

        editar = [(4,praga), (5,dano), (6,altura), (7,folhas), (8,obs)]

        
        dados_antigo = [data, parcela, planta]
        if st.button("Editar Registro"):
            if editar_linha_excel(dados_antigo, editar):
                st.markdown("### Registro editado com sucesso.")
            else:
                st.markdown("### Registro não encontrado.")
    else:
        st.warning("Por favor, preencha todos os campos obrigatórios antes de editar o registro.")
    