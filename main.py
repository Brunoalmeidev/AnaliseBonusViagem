import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACec3d37b9c1daba201ccb69a8f8f3af5b"
# Your Auth Token from twilio.com/console
auth_token  = "bbeee9607cf34d0f91b72a43eb92b49c"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5512991842249", 
            from_="+17816093365",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)


# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

