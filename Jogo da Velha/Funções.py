import pygame.mixer_music

cordenadas = [[0, 0], [250, 0], [500, 0], [0, 250], [250, 250], [500, 250], [0, 500], [250, 500], [500, 500]]
jogador = True


def jogar(janela, fonte, text):
    janela.fill((0, 0, 0))
    pygame.draw.rect(janela, (245, 245, 200), (0, 250, 750, 225))
    label2 = fonte.render(text, 1, (0, 0, 0))
    janela.blit(label2, (0, 260))
    botao_sim = pygame.Surface((200, 100))
    botao_nao = pygame.Surface((200, 100))
    sim = fonte.render('SIM', True, (0, 0, 0))
    nao = fonte.render('NÃO', True, (0, 0, 0))
    botao_nao.fill((255, 100, 100))
    botao_sim.fill((100, 255, 100))
    botao_nao.blit(nao, (5, 5))
    botao_sim.blit(sim, (16, 16))
    janela.blit(botao_nao, (440, 352))
    janela.blit(botao_sim, (105, 352))
    return [False, text]


def jogo(janela, bg, label):
    janela.fill((0, 0, 0))
    janela.blit(bg, (0, 0))
    janela.blit(label, (0, 750))
    return [True, '']


def vez(lugar, jogadoro, jogadorx, o2, x2):
    lugar.fill('black', (650, 750, 100, 100))
    if jogador:
        imagem = jogadorx
        player = x2
    else:
        imagem = jogadoro
        player = o2
    lugar.blit(player, (650, 750))
    return imagem


def play(lugar, jogada, imagem, pathm):
    global jogador, cordenadas
    vitor = False
    ocupadas = list()
    vit = list()
    vitorias = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    x = y = 250
    c = 0
    for lin in range(0, 3):
        for a in range(0, 3):
            if cordenadas[c][0] <= jogada[0] <= x and cordenadas[c][1] <= jogada[1] <= y:
                try:
                    if not cordenadas[c][2]:
                        lugar.blit(imagem, cordenadas[c])
                        cordenadas[c].append(True)
                        cordenadas[c].append(jogador)
                        jogador = not jogador
                    else:
                        print('jogada inválida')
                except IndexError:
                    lugar.blit(imagem, cordenadas[c])
                    cordenadas[c].append(True)
                    cordenadas[c].append(jogador)
                    jogador = not jogador
            c += 1
            x += 250
        x = 250
        y += 250
    for ocup in range(0, 9):
        try:
            if cordenadas[ocup][2]:
                ocupadas.append(ocup)
        except IndexError:
            pass
    for vitoria in vitorias:
        if vitor:
            break
        else:
            for num in ocupadas:
                if num in vitoria:
                    vit.append(num)
            if len(vit) == 3:
                if cordenadas[vit[0]][3] == cordenadas[vit[1]][3] == cordenadas[vit[2]][3]:
                    vitor = True
            vit = list()
    if vitor:
        aquele = 'x' if not jogador else 'o'
        text = f'"{aquele.upper()}" wins, revanche?'
        cordenadas = [[0, 0], [250, 0], [500, 0], [0, 250], [250, 250], [500, 250], [0, 500], [250, 500], [500, 500]]
        pygame.mixer_music.load(f'{pathm}Ayrton-Senna-Tema-da-vitoria_-.mp3')
        pygame.mixer.music.play(pygame.MOUSEBUTTONDOWN)
        return [False, text]
    elif len(ocupadas) == 9:
        cordenadas = [[0, 0], [250, 0], [500, 0], [0, 250], [250, 250], [500, 250], [0, 500], [250, 500], [500, 500]]
        text = 'VELHA!, mais uma?'
        pygame.mixer_music.load(f'{pathm}Derrota.mp3')
        pygame.mixer.music.play(pygame.MOUSEBUTTONDOWN)
        return [False, text]
    else:
        return [True, '']
