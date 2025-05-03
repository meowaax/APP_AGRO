import streamlit as st
from pags.dados import get_parcela, deletar_linha_excel, get_datas, get_planta

def deletar_registro():
    st.markdown("## Deletar Boleto")

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
    
    # Verificar se todos os campos obrigatórios foram preenchidos
    if data and parcela and planta:
        if st.button("Deletar Registro"):
            if deletar_linha_excel(data, parcela, planta):
                st.markdown("### Registro deletado com sucesso.")
            else:
                st.markdown("### Registro não encontrado.")
    else:
        st.warning("Por favor, preencha todos os campos obrigatórios antes de deletar o registro.")
