# Funções
'''
Crias um programa que calcula a quantidade de tinta necessária para pintar uma parede. O User deverá fornecer as seguintas informações:
Rendimento, Altura e Largura.
O programa deve mostrar na tela a mensagem: 'Você necessida de X latas de tinta'
Ex.:
Altura: 2m
        |
        |
        |
        |
        |____________
                    Largura:6m


                    ########
                    ########
                    ########
                    ########
                     TINTA (Lata rende pra 5m (parede))

Qual é o rendimento da lata? 4
Qual é a altura da parede? 2
Qual é a largura da parede? 5
Você precisa de 2.5 latas de tinta.
'''
# Rendimento de 15 m² por galão TINTA CHROMA KEY Verde | Galões de 3,685 litros.
'''
rend_lata = int(input('Qual é o rendimento da Lata de Tinta? '))
parede_alt = int(input('Qual é a altura da parede? '))
parede_larg = int(input('Qual é a largura da parede? '))

def lata_tinta():
    area = parede_alt * parede_larg
    total = area / rend_lata
    print(f' Você precisa de {total} latas de tinta')

lata_tinta()

'''
'''
rendimento = int(input('Qual é o rendimento da Lata de Tinta? '))
largura = int(input('Qual é a altura da parede? '))
altura = int(input('Qual é a largura da parede? '))


def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f' Você precisa de {total} latas de tinta')

calculo_tinta()

'''

























