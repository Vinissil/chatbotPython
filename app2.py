import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Seu pedido está sendo preparado, em 40 minutos estará pronto.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}  Seu pedido está sendo preparado, em 40 minutos estará pronto.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Seu pedido está sendo preparado, em 40 minutos estará pronto.{os.linesep}')
    else:
        print('Digite apenas os números da lista.')

def start():
    # Apresentar o chatbot
    print('Olá! Seja bem-vindo ao Cosa Nostra, siga as instruções para fazer seu pedido.')
    # Pedir o nome 
    nome = input('Digite seu nome: ')
    # Pedir o e-mail
    email = input ('Digite seu e-mail: ')
    while True:
        # Oferecer o menu de opções
        resposta = input( 
        f'Qual o seu pedido?{os.linesep}[1] - Bife, Arroz, Feijão, Farofa, Salada e Fritas.{os.linesep}[2] - Frango, Arroz, Feijão, Farofa, Salada e Fritas.{os.linesep}[3] - Calabresa, Arroz, Feijão, Farofa, Salada e Fritas.{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()