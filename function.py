from data import *

class Ship(pygame.Rect):
    def __init__(self, x, y, width, height, image_list, step, hp):
        super().__init__(x, y, width, height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.image_count = 10
        self.change_image = int(FPS / 5)
        self.step = step
        self.hp = hp
    
    #функція для зміни картинок раз в декілька кадрів(створення анімації)
    def move_image(self):
        if self.image_count == len(self.image_list) * self.change_image - 1:
            self.image_count = 10
        if self.image_count % self.change_image == 0:
            self.image = self.image_list[self.image_count // self.change_image]
        self.image_count += 1


class Hero(Ship):
    def __init__(self, x, y, width, height, image_list, step, hp):
        super().__init__(x, y, width, height, image_list, step, hp)
        self.start_x = self.x
        self.start_y = self.y
        self.move_check = {"up": False, "down": False, "left": False, "right": False}

    #функція руху героя
    def move(self, window):

        if self.move_check["up"] and self.y > 0:
            self.y -= self.step

        if self.move_check["down"] and self.y < size_window[1] - self.height:
            self.y += self.step

        if self.move_check["left"] and self.x > 0:
            self.x -= self.step

        if self.move_check["right"] and self.x < size_window[0] - self.width:
            self.x += self.step

        #перевірка на рух, якщо рухаємся, то у персонажа мінємо картинки(створюємо анімацію) 
        # інакше залишаємо картинку де персонаж стоїть
        if True in list(self.move_check.values()):
            self.move_image()
        else:
            self.image = self.image_list[0]

        window.blit(self.image, (self.x, self.y)) 
    
    def minus_heart(self, bullets):
        index = self.collidelist(bullets)
        if index != -1:
            self.hp -= 1
            bullets.pop(index)
    



class Bot(Ship):

    bot_list = list()

    def __init__(self, x, y, width, height, image_list, step, hp, damage_index):
        super().__init__(x, y, width, height, image_list, step, hp)
        self.start_x = x
        self.start_y = y
        self.damage_index = damage_index
        self.start_shoot = 2000
        self.delay_shoot = random.randint(2000, 2800)

    def move(self, window):

        self.y += self.step

        self.move_image()
        window.blit(self.image, (self.x, self.y))
    
    def remove(self, bullets):
        index = self.collidelist(bullets)
        if index != -1:
            bullets.pop(index)
            Bot.bot_list.remove(self)
    def collide_hero(self, hero):
        if self.colliderect(hero):
            hero.hp -= self.damage_index
            Bot.bot_list.remove(self)


    def shoot(self, end_shoot):#для стрільби бота
        if end_shoot - self.start_shoot > self.delay_shoot:
            bullet_list_bot.append(Bullet(self.centerx -10/2, self.bottom, 10, 20, None, colors["BLUE"], 3))
            self.start_shoot = end_shoot



#клас для пулі, якими стріляє бот, єдва методи руху по х та по у
class Bullet(pygame.Rect):
    def __init__(self, x, y, width, height, image, color, step):
        super().__init__(x, y, width, height)
        self.image = image
        self.color = color
        self.step = step
        self.start_x = self.x
        self.start_y = self.y
    
    def move(self, window):
        self.y += self.step
        pygame.draw.rect(window, self.color, self)
    

class Background():
    def __init__(self, width, height, image):
        self.height = height
        self.image1 = image
        self.image2 = image
        self.y1 = 0
        self.y2 = -height
        self.speed = 2
    
    def move(self, window):
        self.y1 += self.speed
        self.y2 += self.speed
        if self.y1 >= self.height:
            self.y1 = - self.height
        if self.y2 >= self.height:
            self.y2 = - self.height

        window.blit(self.image1, (0, self.y1))
        window.blit(self.image2, (0, self.y2))