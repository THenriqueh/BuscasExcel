import pandas as pd


# Drscription of the code

# Open the Excel files

lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']

# For each file

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# Check if any value in the sales column of those files is greater than 55,000
# If greater than 55,000 -> Send a SMS with the name, month and sales of the selesman
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} o vendedor {vendedor} bateu a meta com o valor de {vendas} em vendas. Parabéns!!')
# If not be greater than 55,000 don't make nothing







