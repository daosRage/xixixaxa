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


class Bot(Ship):
    def __init__(self, x, y, width, height, image_list, step, hp):
        super().__init__(x, y, width, height, image_list, step, hp)
        self.start_x = x
        self.start_y = y



#клас для пулі, якими стріляє бот, єдва методи руху по х та по у
class Bullet(pygame.Rect):
    def __init__(self, x, y, width, height, image, color, step):
        super().__init__(x, y, width, height)
        self.image = image
        self.color = color
        self.step = step
        self.start_x = self.x
        self.start_y = self.y
    

class Background():
    def __init__(self, width, height, image):
        self.height = height
        self.image1 = image
        self.image2 = image
        self.y1 = 0
        self.y2 = -height
    
    def move(self, window):
        self.y1 += 5
        self.y2 += 5
        if self.y1 >= self.height:
            self.y1 = - self.height
        if self.y2 >= self.height:
            self.y2 = - self.height

        window.blit(self.image1, (0, self.y1))
        window.blit(self.image2, (0, self.y2))