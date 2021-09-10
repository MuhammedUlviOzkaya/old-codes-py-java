import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Buz")

x = 0
y = 450
width = 50
height = 50
vel = 10

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if x == 500:
        x = -50
    elif x == -50:
        x = 500
    if not isJump:
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel
        if y == -50:
            y = 500
        elif y == 500:
            y = -50
        if keys[pygame.K_SPACE]:
            isJump = True

        #gun



    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * neg * 0.5
            jumpCount -= 1


        else:
            isJump = False
            jumpCount = 10




    window.fill((0, 0, 0))

    if keys[pygame.K_BACKSPACE]:
        bullet_x = x + 50
        bullet_y = y + 30
        bullet_vel = 25
        pygame.draw.rect(window, (134, 131, 131), (bullet_x, bullet_y, 30, 10))

        while bullet_x < 500:

            bullet_x += bullet_vel
            pygame.draw.rect(window, (134, 131, 131), (bullet_x, bullet_y, 30, 10))



    pygame.draw.rect(window, (45, 208, 233), (x, y, width, height))
    pygame.display.update()

pygame.quit()