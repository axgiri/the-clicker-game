import pygame

image_path = 'data/data/org.test.myapp/files/app/'

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("first game")

icon = pygame.image.load('images/icon.jpg').convert()
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.png')
running = [
    pygame.image.load('images/right 1000x1000/1.png').convert_alpha(),
    pygame.image.load('images/right 1000x1000/2.png').convert_alpha(),
    pygame.image.load('images/right 1000x1000/3.png').convert_alpha(),
    pygame.image.load('images/right 1000x1000/4.png').convert_alpha(),
    pygame.image.load('images/right 1000x1000/5.png').convert_alpha(),
    pygame.image.load('images/right 1000x1000/6.png').convert_alpha(),
]

enemy = pygame.image.load('images/enemy.png').convert_alpha()

animation = 0
back = 0

speed = 10

character = 150

jump = 250
is_jump = False
jump_count = 10

enemies = []

gameplay = True

label = pygame.font.SysFont('arial', 40)

lose_label = label.render('you are loser', False, (0, 0, 255))
restart_label = label.render('restart', False, (255, 255, 0))
restart_label_rect = restart_label.get_rect(topleft=(300,600))



timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 3000)

run = True

while run:
    clock.tick(30)

    screen.blit(bg, (back, 0))
    screen.blit(bg, (back + 1000, 0))
    screen.blit(running[animation], (character, 500 + jump))

    if gameplay:


        character_rect = running[0].get_rect(topleft=(character, 500 + jump))

        if enemies:
            for el_rect in enemies:
                screen.blit(enemy, el_rect.topleft)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and character > 50:
            character -= speed
        elif keys[pygame.K_RIGHT] and character < 350:
            character += speed

        if not is_jump:
            if keys[pygame.K_UP]:
                is_jump = True
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    jump -= (jump_count ** 2) / 2
                else:
                    jump += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10

        if animation == 5:
            animation = 0
        else:
            animation += 1

        back -= 2
        if back == -1000:
            back = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == timer:
                enemy_rect = enemy.get_rect(topleft=(1000, 750))
                enemies.append(enemy_rect)

        if enemies:
            for el_rect in enemies:
                el_rect.x -= 10

        if enemies:
            for el_rect in enemies:
                if character_rect.colliderect(el_rect):
                    gameplay = False

    else:
        screen.fill((23, 209, 166))
        screen.blit(lose_label,(300, 500))
        screen.blit(restart_label, restart_label_rect)
        
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            character = 150
            enemies.clear()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.update()
pygame.quit()
