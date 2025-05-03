import pandas as pd
from streamlit_option_menu import option_menu
from pags.home import fundo
from pags.adicionar import adicionar_registro
from pags.deletar import deletar_registro
from pags.editar import editar_registro

acoes = ['Adicionar', 'Editar', 'Deletar']
icons = ['bi bi-file-earmark-plus', "bi bi-pencil-square","bi bi-file-earmark-x"]


with pd.ExcelFile('danos_TESTES.xlsx') as xls:
        opcs = list(pd.read_excel(xls).PARCELA.unique())


def opcoes():
    selected = option_menu(
            menu_title=None,  # required
            options=acoes,
            icons=icons,
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
    return selected


def main():
    # fundo()
    
    escolha = opcoes()
    
    if escolha == acoes[0]:
        adicionar_registro()
        
    if escolha == acoes[1]:
        editar_registro()
    
    if escolha == acoes[2]:
        deletar_registro()
