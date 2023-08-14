import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Seu pedido está sendo preparado, em 40 minutos seu lanche estará pronto.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}  Seu pedido está sendo preparado, em 40 minutos seu lanche estará pronto.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Seu pedido está sendo preparado, em 40 minutos seu lanche estará pronto.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} Seu pedido está sendo preparado, em 40 minutos seu lanche estará pronto.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome} Seu pedido está sendo preparado, em 40 minutos seu lanche estará pronto.{os.linesep}')
    elif resposta == '6':
        print(f'{os.linesep}{nome} Seu pedido está sendo preparado, em 40 minutos seu lanche estará pronto.{os.linesep}')
    elif resposta == '7':
        print(f'{os.linesep}{nome} Seu pedido está sendo preparado, em 40 minutos seu lanche estará pronto.{os.linesep}')
    elif resposta == '8':
        print(f'{os.linesep}{nome} Escolha um lanche e uma bebida, para acompanhar sua porção.{os.linesep}')
    elif resposta == '9':
        print(f'{os.linesep}{nome} Escolha um lanche e uma bebida, para acompanhar sua porção.{os.linesep}') 
    elif resposta == '10':
        print(f'{os.linesep}{nome}Escolha o seu lanche.{os.linesep}')
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
            f'Qual o seu pedido?{os.
            linesep}[1] - Italiano - Pão, Australiano, burguer 120g, queijo cheddar, picles,maionese e Ketchup.{os.
            linesep}[2] - Insalata - Pão brioche, burguer 120g, queijo cheddar, tomate, cebola roxa, alface americana e maionese.{os.
            linesep}[3] - Don Corleone - Pão brioche, burguer 120g, queijo cheddar, cebola e picle.{os.
            linesep}[4] - Al Pacino - Pão brioche, burguer 120g, queijo cheddar, bacon, picle, maionese.{os.
            linesep}[5] - O Poderoso Chefão - Pão australiano, burguer 120g, queijo cheddar, cebola roxa, barbecue e picles.{os.
            linesep}[6] - Piazza - Pão australiano, burguer 120g, queijo cheddar, bacon, tomate, rúcula.{os.
            linesep}[7] - Cosa Nostra - Pão brioche, burguer 120g, queijo gorgonzola, bacon e rúcula.{os.
            linesep}[8] - Acompanhamentos - Porção individual: Batata frita.{os.
            linesep}[9] - Acompanhamentos - Porção individual: Nuggets.{os.
            linesep}[10] - Combo - Transforme seu lanche num combo, escolha o seu refrigerante e acompanhamento.{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()