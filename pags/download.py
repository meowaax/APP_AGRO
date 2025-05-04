import streamlit as st

def generate_registro_file():
    file_name = 'danos_TESTES.xlsx'
    with open(file_name, "rb") as template_file:
        template_byte = template_file.read()

        st.download_button(label="Clique para baixar o relatório em Excel",
                           data=template_byte,
                           file_name="danos_TESTES.xlsx",
                           mime='application/octet-stream')

def main():
    generate_registro_file()