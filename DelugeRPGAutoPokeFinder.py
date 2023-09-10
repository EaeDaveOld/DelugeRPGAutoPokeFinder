import random
import pyautogui as auto
import pyperclip
import time

pokesearch = input('Digite o nome do Pokémon que deseja encontrar: ').lower()
pokemon_encontrado = False
tentativas = 0

# Aperta o botão do Pokémon encontrado
def botao_pokemon_encontrado():
    auto.click(x=1065, y=475)

def botao_nome_pokemon():
    auto.click(x=717, y=193)

def botao_close():
    auto.click(x=1206, y=582)

# Movimenta o personagem no mapa de forma aleatória
def automove():
    time.sleep(0.6)
    teclas = ['a', 'w', 'd', 's']
    tecla_escolhida = random.choices(teclas)
    auto.press(tecla_escolhida)
    time.sleep(2)

botao_nome_pokemon()

# Encontra o Pokémon solicitado
def findpokemon():
    global pokename, pokesearch, pokemon_encontrado, tentativas
    while pokemon_encontrado == False:
        
        
        botao_pokemon_encontrado()
        time.sleep(1.5)
        
        
        time.sleep(0.5)
        
        # Double Click to Select Text
        botao_nome_pokemon()
        botao_nome_pokemon()
        
        auto.hotkey('ctrl', 'c')
        pokename = pyperclip.paste().lower()
        tentativas += 1
        
        if pokename == pokesearch:
            print(f'O Pokémon {pokesearch} foi encontrado! ({tentativas}x)')
            botao_close()
            pokemon_encontrado = True
        else:
            print(f'Não foi possível encontrar o {pokesearch} - {pokename} ({tentativas}x)')
            botao_close()
            automove()

automove()
findpokemon()