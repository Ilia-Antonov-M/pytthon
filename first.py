import pygame
import sys
import random
import time

skorost = 0
tor = 0
life = 1
pro = 0


class Game:
    def __init__(self):
        self.width = 720
        self.height = 460
        self.red = pygame.Color("red")
        self.black = pygame.Color("blue")
        self.white = pygame.Color("green")
        self.brown = pygame.Color("brown")
        self.fps_controller = pygame.time.Clock()
        self.score = 0
        self.flag = True

    def dis(self):
        self.dispay = pygame.display.set_mode((
        self.width, self.height))
        pygame.display.set_caption('Питон')

    def proverka(self, change_to):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d') or event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a') or event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w') or event.key == pygame.K_UP:
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s') or event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return change_to

    def otobrazenie(self):
        global skorost
        pygame.display.flip()
        game.fps_controller.tick(skorost)

    def rez(self, choice=1):
        s_font = pygame.font.SysFont('arial', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        if choice == 1:
            s_rect.midtop = (80, 10)
        else:
            s_rect.midtop = (360, 120)
        self.dispay.blit(s_surf, s_rect)

    def okonchanie(self):
        go_font = pygame.font.SysFont('arial', 72)
        go_surf = go_font.render('Ti proigral', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.dispay.fill(pygame.Color("green"))
        self.dispay.blit(go_surf, go_rect)
        self.rez(0)
        pygame.draw.rect(self.dispay, pygame.Color("black"), (295, 200, 145, 38), 1)
        pygame.draw.rect(self.dispay, pygame.Color("black"), (295, 255, 145, 38), 1)
        restart = pygame.font.SysFont('arial', 36)
        restart1 = restart.render('restart', True, pygame.Color("blue"))
        exit = pygame.font.SysFont('arial', 36)
        exit1 = exit.render('exit', True, pygame.Color("blue"))
        self.dispay.blit(restart1, (305, 200))
        self.dispay.blit(exit1, (305, 255))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 440 >= event.pos[0] >= 295 and 200 <= event.pos[1] <= 238:
                            return 0
                        elif 440 >= event.pos[0] >= 295 and 255 <= event.pos[1] <= 293:
                            return 1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()


    def pole(self):
        x = 0
        while x != 720:
            x += 10
            pygame.draw.line(game.dispay, pygame.Color("black"), (0, x), (720, x), 1)
            pygame.draw.line(game.dispay, pygame.Color("black"), (x, 0), (x, 720), 1)


class Python:
    def __init__(self, snake_color):
        self.snake_head_pos = [100, 50]  # [x, y]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color
        self.direction = "RIGHT"
        self.change_to = self.direction
        self.flag = True

    def napravlenie(self):
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def izmenenie_polozenia(self):
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10
        if tor:
            self.snake_head_pos[0] %= 720
            self.snake_head_pos[1] %= 460

    def kushat(
            self, score, food_pos, screen_width, screen_height):
        self.snake_body.insert(0, list(self.snake_head_pos))
        if (self.snake_head_pos[0] == food_pos[0] and
                self.snake_head_pos[1] == food_pos[1]):
            food_pos = [random.randrange(1, screen_width / 10) * 10,
                        random.randrange(1, screen_height / 10) * 10]
            score += 1
        else:
            self.snake_body.pop()
        return score, food_pos

    def risovanie(self, play_surface, surface_color):
        global skorost, tor, life
        while self.flag:
            play_surface.fill(pygame.Color("white"))
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 80, 145, 38), 1)
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 125, 145, 38), 1)
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 170, 145, 38), 1)
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 215, 145, 38), 1)
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 260, 145, 38), 1)
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 305, 145, 38), 1)
            pygame.draw.line(play_surface, pygame.Color("black"), (377, 305), (377, 342), 1)
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 350, 145, 38), 1)
            pygame.draw.line(play_surface, pygame.Color("black"), (377, 350), (377, 388), 1)
            easy = pygame.font.SysFont('arial', 40)
            easy1 = easy.render('Easy', True, pygame.Color("red"))
            normal = pygame.font.SysFont('arial', 40)
            normal1 = normal.render('Normal', True, pygame.Color("red"))
            hard = pygame.font.SysFont('arial', 40)
            hard1 = hard.render('Hard', True, pygame.Color("red"))
            veryeasy = pygame.font.SysFont('arial', 40)
            veryeasy1 = veryeasy.render('Very easy', True, pygame.Color("red"))
            veryhard = pygame.font.SysFont('arial', 40)
            veryhard1 = veryhard.render('Very hard', True, pygame.Color("red"))
            dispay = game.dispay
            tor1 = pygame.font.SysFont('arial', 40)
            tor2 = tor1.render("tor", True, pygame.Color("red"))
            off = pygame.font.SysFont('arial', 40)
            off1 = off.render("off", True, pygame.Color("red"))
            on = pygame.font.SysFont('arial', 40)
            on1 = on.render("on", True, pygame.Color("red"))
            life1 = pygame.font.SysFont('arial', 40)
            life2 = life1.render("life", True, pygame.Color("red"))
            life3 = life1.render(str(life), True, pygame.Color("red"))
            dispay.blit(easy1, (305, 118))
            dispay.blit(normal1, (305, 167))
            dispay.blit(hard1, (305, 212))
            dispay.blit(veryeasy1, (305, 73))
            dispay.blit(veryhard1, (305, 253))
            dispay.blit(tor2, (306, 302))
            dispay.blit(life2, (306, 348))
            dispay.blit(life3, (395, 348))
            if tor:
                dispay.blit(on1, (380, 300))
            else:
                dispay.blit(off1, (380, 300))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 305 <= event.pos[0] <= 450 and 125 <= event.pos[1] <= 163:
                            skorost = 15
                            self.flag = False
                        elif 305 <= event.pos[0] <= 450 and 170 <= event.pos[1] <= 208:
                            skorost = 20
                            self.flag = False
                        elif 305 <= event.pos[0] <= 450 and 215 <= event.pos[1] <= 253:
                            skorost = 30
                            self.flag = False
                        elif 305 <= event.pos[0] <= 450 and 80 <= event.pos[1] <= 118:
                            skorost = 10
                            self.flag = False
                        elif 305 <= event.pos[0] <= 450 and 260 <= event.pos[1] <= 298:
                            skorost = 40
                            self.flag = False
                        elif 377 <= event.pos[0] <= 450 and 305 <= event.pos[1] <= 343:
                            tor = 1 - tor
                        elif 377 <= event.pos[0] <= 450 and 350 <= event.pos[1] <= 388:
                            life += 1
                            if life == 10:
                                life = 1
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(
                    play_surface, self.snake_color, pygame.Rect(
                        pos[0], pos[1], 10, 10))

    def proverkagran(self, game_over, screen_width, screen_height):
        global life
        if any((
                self.snake_head_pos[0] > screen_width - 10
                or self.snake_head_pos[0] < 0,
                self.snake_head_pos[1] > screen_height - 10
                or self.snake_head_pos[1] < 0
        )):
            if life == 1:
                if game_over():
                    pygame.quit()
                    sys.exit()
                else:
                    self.snake_head_pos = [100, 50]  # [x, y]
                    self.snake_body = [[100, 50], [90, 50], [80, 50]]
                    self.direction = "RIGHT"
                    self.change_to = self.direction
            else:
                self.snake_head_pos = [100, 50]  # [x, y]
                self.snake_body = [[100, 50], [90, 50], [80, 50]]
                time.sleep(1)
                life -= 1
                self.direction = "RIGHT"
                self.change_to = self.direction
        for block in self.snake_body[1:]:
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                if life == 1:
                    if game_over() == 1:
                        self.direction = "RIGHT"
                        self.change_to = self.direction
                        self.snake_head_pos = [100, 50]  # [x, y]
                        self.snake_body = [[100, 50], [90, 50], [80, 50]]
                    else:
                        pygame.quit()
                        sys.exit()
                else:
                    self.snake_head_pos = [100, 50]  # [x, y]
                    self.snake_body = [[100, 50], [90, 50], [80, 50]]
                    time.sleep(1)
                    life -= 1
                    self.direction = "RIGHT"
                    self.change_to = self.direction


class Eda:
    def __init__(self, food_color, screen_width, screen_height):
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randrange(1, screen_width / 10) * 10,
                         random.randrange(1, screen_height / 10) * 10]

    def risovanie(self, play_surface):
        pygame.draw.rect(
            play_surface, self.food_color, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_size_x, self.food_size_y))


game = Game()
snake = Python(pygame.Color("black"))
food = Eda(pygame.Color("red"), 720, 460)
pygame.init()
game.dis()


def sous():
    snake.change_to = game.proverka(snake.change_to)
    snake.napravlenie()
    snake.izmenenie_polozenia()
    game.score, food.food_pos = snake.kushat(
        game.score, food.food_pos, game.width,
        game.height)
    snake.risovanie(game.dispay, game.white)
    food.risovanie(game.dispay)
    snake.proverkagran(
        game.okonchanie, game.width, game.height)
    game.pole()
    game.rez()
    game.otobrazenie()


while True:
    sous()
