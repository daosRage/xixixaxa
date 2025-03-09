from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("ЛАБІРИНТ")

def run():
    game = True
    start_time_bot = 0
    clock = pygame.time.Clock()         #створюємо обєкт часу

    #створення обєктів героя
    hero = Hero(size_window[0] // 2 - size_hero[0] // 2, 
                size_window[1] - size_hero[1], 
                size_hero[0],
                size_hero[1],
                hero_image_list,
                5, 
                5)
    
    
    background = Background(size_bg[0], size_bg[1], bg_image)
    #створення обєкта шрифта
    font = pygame.font.Font(None, 35)


    while game:
        events = pygame.event.get()     #список всіх подій, для зручності, записали в змінну events
        background.move(window)

        #HP
        window.blit(hp_image, (5, 5))
        window.blit(font.render(f"x{hero.hp}", True, (250,100,50)), (27, 5))

        
        #запуск руху героя, ботів та пуль
        hero.move(window)

        hero.minus_heart(bullet_list_bot)

        end_time_bot = pygame.time.get_ticks()
        if end_time_bot - start_time_bot >= 2000:
            start_time_bot = end_time_bot
            Bot.bot_list.append(Bot(
                random.randint(0, size_window[0] - size_bot[0]),
                - size_bot[1],
                size_bot[0],
                size_bot[1],
                bot_1_image_list,
                1,
                1,
                1
                ))
        for bot in Bot.bot_list:
            bot.move(window)
            bot.remove(bullet_list_hero)
            bot.shoot(end_time_bot)
            bot.collide_hero(hero)

        
        for bullet in bullet_list_hero:
            bullet.move(window)
        
        for bullet in bullet_list_bot:
            bullet.move(window)

        #COLLIDE BOT&BULLET

    

        #перебираємо список всіх подій зовнішнього світу
        for event in events:
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.move_check["up"] = True
                if event.key == pygame.K_s:
                    hero.move_check["down"] = True
                if event.key == pygame.K_a:
                    hero.move_check["left"] = True
                if event.key == pygame.K_d:
                    hero.move_check["right"] = True
                if event.key == pygame.K_SPACE:
                    bullet_list_hero.append(Bullet(
                        hero.centerx - 10/2, hero.y, 10, 20, None, colors["RED"], -5
                        ))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.move_check["up"] = False
                if event.key == pygame.K_s:
                    hero.move_check["down"] = False
                if event.key == pygame.K_a:
                    hero.move_check["left"] = False
                if event.key == pygame.K_d:
                    hero.move_check["right"] = False
            
                

        clock.tick(FPS)                 #встановили кількість кадрів на секунду
        pygame.display.flip()           #оновлюємо всі зміни на екрані, що стались за кадр

run()