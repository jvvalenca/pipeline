import streamlit as st
import contrato
from datetime import datetime, time

def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data =st.date_input("Data da compra")
    hora = st.time_input("Hora da compra")
    valor = st.number_input("Valor da venda, min_value=0.0, format=%.2f")
    quantidade = st.number_input("Quantidade de produtos")
    produto = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])

    if st.button("Salvar"):

       data_hora = datetime.combine(data, hora)
       st.write("***Dados da Venda:***")
       st.write(f"E-mail do Vendedor: {email}")
       st.write(f"Data da Venda: {data}")
       st.write(f"Hora da Venda: {hora}")
       st.write(f"Data e Hora da Venda: {data_hora}")
       st.write(f"Valor da Venda: {valor}")
       st.write(f"Quantidade do Produto: {quantidade}")
       st.write(f"Produto: {produto}")

if __name__=="__main__":
    main()