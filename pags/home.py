import pandas as pd
import streamlit as st
from datetime import datetime, date
from babel.numbers import format_currency
import base64

def fundo():
    local_image_path = "assets/fundo.jpg"

    with open(local_image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    data_url = f"data:image/jpeg;base64,{base64_image}"

    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("{data_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: local;
            width: 100vw;
            height: 100vh;
        }}

        [data-testid="stSidebar"] > div:first-child {{
        background-image: url("../assets/fundo2.jpg");
        background-position: center;
        margin-left: 0;
        background-repeat: no-repeat;
        background-size: contain;
        background-attachment: fixed;
        }}

        [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}

        [data-testid="stToolbar"] {{
        right: 2rem;
        }}
        <style>
    """


    st.markdown(page_bg_img, unsafe_allow_html=True)

def read_data(file_path):
    with pd.ExcelFile(file_path) as xls:
        return pd.read_excel(xls)

def filter_by_parcela(data, parcela):
    return data[(data['PARCELA'].isin(parcela))]

"""def filter_by_data(data, status, start_date, end_date):
    return data[(data['PLANTA'].isin(status)) &
                (data['DATA'].between(start_date, end_date))]"""

def display_data(data, title):
    st.write(f"Exibindo dados {title}")
    st.dataframe(data)

def display_total_value(data, status):
    total_value = data['FOLHAS'].sum()
    st.write(f"Folhas infectadas {status}: {total_value}")

def main():
    fundo()
    planilha_path = "danos_TESTES.xlsx"
    dados = read_data(planilha_path)

    sele = st.sidebar.selectbox(
        'Buscar',
        ('Todos', 'Parcela',))

    if sele == 'Todos':
        dados_filtrados = dados[(dados['DATA'].notna())]
        display_data(dados_filtrados, 'Todos')
        
    elif sele == 'Parcela':
        options = st.sidebar.multiselect(
            'Selecione a parcela',
            ['A', 'B', 'C']
        )
        dados_filtrados = filter_by_parcela(dados, options)
        display_data(dados_filtrados, f" por parcela {options}")
        
