import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

## Functions ##
def mostra_qntd_linhas(dataframe):
    
    #Elemento de range, para o usuario selecionar a quantidade de linhas que será mostrado na tabela
    qntd_linhas = st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value = 1, max_value = len(dataframe), step = 1)

    #Mostrando as linhas da tabela conforme o usuario selecionar
    st.write(dataframe.head(qntd_linhas).style.format(subset = ['Valor'], formatter="{:.2f}"))

def plot_estoque(dataframe, categoria):

    dados_plot = dataframe.query('Categoria == @categoria')

    fig, ax = plt.subplots(figsize=(8,6))
    ax = sns.barplot(x = 'Produto', y = 'Quantidade', data = dados_plot)
    ax.set_title(f'Quantidade em estoque dos produtos de {categoria}', fontsize = 16)
    ax.set_xlabel('Produtos', fontsize = 12)
    ax.tick_params(rotation = 20, axis = 'x')
    ax.set_ylabel('Quantidade', fontsize = 12)
  
    return fig

## Paths ##
path = r'C:\Users\vitor\Documents\Programas\Streamlite\Artigo_Streamlit_Alura-main\estoque.csv'

## Main ##
# importando os dados
dados = pd.read_csv(path)

st.title('Análise de estoque\n')
st.write('Nesse projeto vamos analisar a quantidade de produtos em estoque, por categoria,  de uma base de dados de produtos de supermercado')

# filtros para a tabela
opcao_1 = st.sidebar.checkbox('Mostrar tabela')
if opcao_1:

    st.sidebar.markdown('## Filtro para a tabela')

    categorias = list(dados['Categoria'].unique())
    categorias.append('Todas')

    categoria = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options = categorias)

    if categoria != 'Todas':
        df_categoria = dados.query('Categoria == @categoria')
        mostra_qntd_linhas(df_categoria)      
    else:
        mostra_qntd_linhas(dados)

opcao_2 = st.sidebar.checkbox('Mostrar grafico')

if opcao_2:
    # filtro para o gráfico
    st.sidebar.markdown('## Filtro para o gráfico')

    categoria_grafico = st.sidebar.selectbox('Selecione a categoria para apresentar no gráfico', options = dados['Categoria'].unique())
    figura = plot_estoque(dados, categoria_grafico)
    st.pyplot(figura)



