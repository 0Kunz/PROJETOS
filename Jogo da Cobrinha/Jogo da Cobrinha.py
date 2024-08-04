import time
import pygame.display
from pygame.math import Vector2
from random import randint

pygame.init()
width = 1200
height = 800
space_game = speed = 50
tick = 60
path_file = f'{__file__}'
file_name = path_file.split('\\')[-1]
path = path_file.replace(file_name, 'Sprites\\')


class Snake:

    def __init__(self):
        self.body = [Vector2(7, 7), Vector2(6, 7), Vector2(5, 7)]
        self.direction = Vector2(1, 0)
        self.add = False

        self.head_up = pygame.image.load(f'{path}cabeça _w.png').convert_alpha()
        self.head_down = pygame.image.load(f'{path}cabeça _s.png').convert_alpha()
        self.head_left = pygame.image.load(f'{path}cabeça _a.png').convert_alpha()
        self.head_right = pygame.image.load(f'{path}cabeça _d.png').convert_alpha()

        self.tail_up = pygame.image.load(f'{path}cauda_w.png').convert_alpha()
        self.tail_down = pygame.image.load(f'{path}cauda_s.png').convert_alpha()
        self.tail_left = pygame.image.load(f'{path}cauda_a.png').convert_alpha()
        self.tail_right = pygame.image.load(f'{path}cauda_d.png').convert_alpha()

        self.curve_tr = pygame.image.load(f'{path}curva_wd_as.png').convert_alpha()
        self.curve_tl = pygame.image.load(f'{path}curva_ds_wa.png').convert_alpha()
        self.curve_br = pygame.image.load(f'{path}curva_aw_sd.png').convert_alpha()
        self.curve_bl = pygame.image.load(f'{path}curva_dw_sa.png').convert_alpha()

        self.body_vertical = pygame.image.load(f'{path}reta_up.png').convert_alpha()
        self.body_horizontal = pygame.image.load(f'{path}reta_down.png').convert_alpha()
        self.cruch_sound = pygame.mixer.Sound(f'{path}cruch.mp3')

    def draw_snake(self):
        self.uptade_head_graphics()
        self.uptade_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * space_game)
            y_pos = int(block.y * space_game)
            block_rect = pygame.Rect(x_pos, y_pos, space_game, space_game)
            if index == 0:
                janela.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                janela.blit(self.tail, block_rect)
            else:
                previos_block = self.body[index + 1] - block
                after_block = self.body[index - 1] - block
                if previos_block.x == after_block.x:
                    janela.blit(self.body_vertical, block_rect)
                elif previos_block.y == after_block.y:
                    janela.blit(self.body_horizontal, block_rect)
                else:
                    if previos_block.x == -1 and after_block.y == -1 or previos_block.y == -1 and after_block.x == -1:
                        janela.blit(self.curve_bl, block_rect)
                    elif previos_block.x == 1 and after_block.y == 1 or previos_block.y == 1 and after_block.x == 1:
                        janela.blit(self.curve_tr, block_rect)
                    elif previos_block.x == -1 and after_block.y == 1 or previos_block.y == 1 and after_block.x == -1:
                        janela.blit(self.curve_tl, block_rect)
                    else:
                        janela.blit(self.curve_br, block_rect)

    def move_snake(self):
        if self.add:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.add = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.add = True

    def uptade_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def uptade_tail_graphics(self):
        tail_relation = self.body[-1] - self.body[-2]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def play_cruch_sound(self):
        self.cruch_sound.play()

    def reset(self):
        self.body = [Vector2(7, 7), Vector2(6, 7), Vector2(5, 7)]
        self.direction = Vector2(0, 0)

class Apple:

    def __init__(self):
        self.randomize()

    def draw_apple(self):
        apple_rectangle = pygame.Rect(self.pos.x * space_game, self.pos.y * space_game, space_game, space_game)
        janela.blit(apple_image, apple_rectangle)

    def randomize(self):
        self.x = randint(0, 23)
        self.y = randint(0, 15)
        self.pos = Vector2(self.x, self.y)


class Main:

    def __init__(self):
        self.snake = Snake()
        self.fruit = Apple()

    def uptade(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_apple()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_cruch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < 24:
            self.game_over()
        elif not 0 <= self.snake.body[0].y < 16:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (11, 94, 170))
        score_x = int(space_game * 24 - 60)
        score_y = int(space_game * 16 - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple_image.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)
        pygame.draw.rect(janela, (11, 94, 170), bg_rect, 2)
        janela.blit(apple_image, apple_rect)
        janela.blit(score_surface, score_rect)


janela = pygame.display.set_mode((width, height))

pygame.display.set_caption('Jogo da Cobrinha')
apple_image = pygame.image.load(f'{path}apple.png').convert_alpha()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
main_game = Main()
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 25)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == SCREEN_UPDATE:
            main_game.uptade()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    janela.fill('black')
    main_game.draw_elements()
    pygame.display.flip()
    clock.tick(60)
