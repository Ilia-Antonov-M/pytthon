import pygame
import sys
import random
import time

skorost = 0


class Game:
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 460
        self.red = pygame.Color("red")
        self.black = pygame.Color("blue")
        self.white = pygame.Color("green")
        self.brown = pygame.Color("brown")
        self.fps_controller = pygame.time.Clock()
        self.score = 0
        self.flag = True

    def dis(self):
        self.dispay = pygame.display.set_mode((
        self.screen_width, self.screen_height))
        pygame.display.set_caption('Питон')

    def event_loop(self, change_to):
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

    def refresh_screen(self):
        global skorost
        pygame.display.flip()
        game.fps_controller.tick(skorost)

    def show_score(self, choice=1):
        s_font = pygame.font.SysFont('arial', 24)
        s_surf = s_font.render(
            'Ochko: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        if choice == 1:
            s_rect.midtop = (80, 10)
        else:
            s_rect.midtop = (360, 120)
        self.dispay.blit(s_surf, s_rect)

    def game_over(self):
        go_font = pygame.font.SysFont('arial', 72)
        go_surf = go_font.render('Ti proigral', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.dispay.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        sys.exit()


class Python:
    def __init__(self, snake_color):
        # важные переменные - позиция головы змеи и его тела
        self.snake_head_pos = [100, 50]  # [x, y]
        # начальное тело змеи состоит из трех сегментов
        # голова змеи - первый элемент, хвост - последний
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color
        # направление движение змеи, изначально
        # зададимся вправо
        self.direction = "RIGHT"
        # куда будет меняться напрвление движения змеи
        # при нажатии соответствующих клавиш
        self.change_to = self.direction
        self.flag = True
    def validate_direction_and_change(self):
        """Изменияем направление движения змеи только в том случае,
        если оно не прямо противоположно текущему"""
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def change_head_position(self):
        """Изменияем положение головы змеи"""
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10

    def snake_body_mechanism(
            self, score, food_pos, screen_width, screen_height):
        # если вставлять просто snake_head_pos,
        # то на всех трех позициях в snake_body
        # окажется один и тот же список с одинаковыми координатами
        # и мы будем управлять змеей из одного квадрата
        self.snake_body.insert(0, list(self.snake_head_pos))
        # если съели еду
        if (self.snake_head_pos[0] == food_pos[0] and
                self.snake_head_pos[1] == food_pos[1]):
            # если съели еду то задаем новое положение еды случайным
            # образом и увеличивем score на один
            food_pos = [random.randrange(1, screen_width / 10) * 10,
                        random.randrange(1, screen_height / 10) * 10]
            score += 1
        else:
            self.snake_body.pop()
        return score, food_pos

    def draw_snake(self, play_surface, surface_color):
        global skorost
        while self.flag:
            play_surface.fill(pygame.Color("white"))
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 80, 145, 38), 1)
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 125, 145, 38), 1)
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 170, 145, 38), 1)
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 215, 145, 38), 1)
            pygame.draw.rect(play_surface, pygame.Color("black"), (305, 260, 145, 38), 1)
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
            dispay.blit(easy1, (305, 118))
            dispay.blit(normal1, (305, 167))
            dispay.blit(hard1, (305, 212))
            dispay.blit(veryeasy1, (305, 73))
            dispay.blit(veryhard1, (305, 253))
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
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(
                    play_surface, self.snake_color, pygame.Rect(
                        pos[0], pos[1], 10, 10))

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        if any((
                self.snake_head_pos[0] > screen_width - 10
                or self.snake_head_pos[0] < 0,
                self.snake_head_pos[1] > screen_height - 10
                or self.snake_head_pos[1] < 0
        )):
            game_over()
        for block in self.snake_body[1:]:
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                game_over()


class Eda:
    def __init__(self, food_color, screen_width, screen_height):
        """Инит еды"""
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randrange(1, screen_width / 10) * 10,
                         random.randrange(1, screen_height / 10) * 10]

    def draw_food(self, play_surface):
        """Отображение еды"""
        pygame.draw.rect(
            play_surface, self.food_color, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_size_x, self.food_size_y))


game = Game()
snake = Python(pygame.Color("black"))
food = Eda(pygame.Color("red"), 720, 460)
pygame.init()
game.dis()
while True:
    snake.change_to = game.event_loop(snake.change_to)
    snake.validate_direction_and_change()
    snake.change_head_position()
    game.score, food.food_pos = snake.snake_body_mechanism(
        game.score, food.food_pos, game.screen_width,
        game.screen_height)
    snake.draw_snake(game.dispay, game.white)
    food.draw_food(game.dispay)
    snake.check_for_boundaries(
        game.game_over, game.screen_width, game.screen_height)
    x = 0
    while x != 720:
        x += 10
        pygame.draw.line(game.dispay, pygame.Color("black"), (0, x), (720, x), 1)
        pygame.draw.line(game.dispay, pygame.Color("black"), (x, 0), (x, 720), 1)
    game.show_score()
    game.refresh_screen()
