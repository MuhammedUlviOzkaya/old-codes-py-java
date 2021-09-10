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
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and (x + width) < 500:
        x += vel
    if not isJump:
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and (y + height) < 500:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
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




    window.fill((0,0,0))

    pygame.draw.rect(window, (45, 208, 233), (x, y, width, height))
    pygame.display.update()

pygame.quit()