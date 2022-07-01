import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

## Path ##
path = r'C:\Users\vitor\Documents\Programas\Controle João\CONTROLE MATERIA PRIMA JUNHO 2022.xlsx'

## Functions ##
def formatData(path, sheet_name, new_columns=[]):
    
    df = pd.read_excel(path, sheet_name=sheet_name)
    for col in df.columns:
        nova = df.at[1, col]
        print(f"Trocando a coluna {col} por {nova}")
        new_columns.append(nova)

    df.columns = new_columns
    df.drop([0,1], inplace=True)

    return df

def plot_chart(df, materia):
    dados_plot = df.loc[df['MATÉRIA PRIMA '] == materia]
    fig, ax = plt.subplots(figsize=(8,6))
    ax = sns.barplot(x = 'DATA', y='QUANT.', data=dados_plot)

    return fig

## Main ##
df = formatData(path=path, sheet_name='CONTROLE SAÍDA')
df = df.astype(str)

st.title('Controle de estoque\n')
categoria_grafico = st.sidebar.selectbox('Selecione a matéria prima para apresentar no gráfico', options = df['MATÉRIA PRIMA '].unique())
figura = plot_chart(df, categoria_grafico)
st.pyplot(figura)