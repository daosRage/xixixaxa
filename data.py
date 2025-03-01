import pygame
import os

pygame.init()                       #ініціалізуємо всі модулі пайгейма

size_window = (1200, 800)           #кортеж з розмірами вікна
size_hero = (100, 96)                #кортеж з розмірами героя
size_bot = (32, 50)                #кортеж з розмірами ботів
size_bg = (1200, 3000)
colors = {                          #словник з кольорами
            "WHITE": (255,255,255),
            "BLACK": (0,0,0)
          }
FPS = 120                            #кількість кадрів на секунду


bullet_dict = dict()                #словник для пуль
bot_list = list()                   #список ботів

abs_path = os.path.abspath(__file__ + "/..")    #абсолютний шлях до папки проекта

hero_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero0.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero2.png")), size_hero)
]
bg_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bg.png")), size_bg)
#bot_1_image_list = [
#    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bot_1_0.png")), size_bot),
#    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bot_1_1.png")), size_bot),
#    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "bot_1_2.png")), size_bot)
#]

hp_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "heart.png")), (20,20))