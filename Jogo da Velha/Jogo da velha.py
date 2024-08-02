from Funções import *
import pygame.display
import pygame

pygame.init()
path = 'C:\\Users\\PC\\PycharmProjects\\Cursoemvídeo\\EXS\\PROJETOS\\Jogo da Velha\\Imagens\\'
pathm = 'C:\\Users\\PC\\PycharmProjects\\Cursoemvídeo\\EXS\\PROJETOS\\Jogo da Velha\\músicas\\'
janela = pygame.display.set_mode((750, 850))
pygame.mixer.music.load(f'{pathm}Death Note - Ls Theme.mp3')
icone = pygame.image.load(f'{path}icone.png')
Bg = pygame.image.load(f'{path}Jogo da velha.png')
x = pygame.image.load(f'{path}x.png')
o = pygame.image.load(f'{path}o.png')
x2 = pygame.image.load(f'{path}x2.png')
o2 = pygame.image.load(f'{path}o2.png')
pygame.display.set_caption('JOGO DA VELHA')
pygame.display.set_icon(icone)
fonte = pygame.font.SysFont('Jacquard 12', 110)
jogos = [False, 'gostaria de jogar?']
label = fonte.render('Vez do Jogador: ', 1, (255, 255, 255))
botao_simrect = pygame.Rect(105, 352, 200, 100)
botao_naorect = pygame.Rect(440, 352, 200, 100)
clock = pygame.time.Clock()
pygame.display.update()
pygame.mixer.music.play(pygame.QUIT)
running = True

while running:
    if jogos[0]:
        imagem = vez(janela, o, x, o2, x2)
    else:
        jogos = jogar(janela, fonte, jogos[1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            if not jogos[0]:
                if botao_naorect.collidepoint(click):
                    quit()
                if botao_simrect.collidepoint(click):
                    jogos = jogo(janela, Bg, label)
                    pygame.mixer.music.load(f'{pathm}Death Note - Ls Theme.mp3')
                    pygame.mixer.music.play(pygame.QUIT)
            else:
                jogos = play(janela, click, imagem, pathm)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
