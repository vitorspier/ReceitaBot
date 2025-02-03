import streamlit as st
from PIL import Image
import Inteligencia

st.set_page_config(layout='wide')
chave = st.secrets['GEMINI_CHAVE']

head1, head2, head3 = st.columns ([3, 2, 11])


st.title(":violet[RECEITA BOT]")
st.subheader("O seu assistente virtual para criar receitas!")

col1, col2 = st.columns([2,2])

with col1:
    st.header("Faça o upload de uma foto com os ingredientes")
    arquivo_foto = st.file_uploader("", type=["jpg", "jpeg", "png"])
    if arquivo_foto is not None:
        imagem = Image.open(arquivo_foto)
        st.image(imagem)
        with st.spinner ("O Receita Bot esta pesquisando..."):
            if st.button("Detectar Possíveis Receitas"):
                st.session_state.ingredientes = Inteligencia.detectar_ingredientes(chave, imagem)
                st.session_state.receitas = Inteligencia.possiveis_receitas(chave, st.session_state.ingredientes )

    if 'ingredientes' in st.session_state:
        st.write(f"Ingredientes Detectados: {st.session_state.ingredientes}")
        st.write ("Possíveis Receitas:")
        for id, receita in enumerate(st.session_state.receitas):
            st.write (f"{id}. {receita}")


with col2:
    if 'receitas' in st.session_state:
        st.header("Escolha uma Receita")
        receita_selecionada = st.selectbox("" , st.session_state.receitas)
        with st.spinner ("O Receita Bot esta criando a receita..."):
            if st.button ("Ver receita"):
                st.session_state.receita_completa = Inteligencia.receita_completa (chave,
                                                                                   st.session_state.ingredientes, receita_selecionada)
                st.write(st.session_state.receita_completa)