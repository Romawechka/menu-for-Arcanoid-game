import pygame
import Image_creator as ic

pygame.init()

display = pygame.display.set_mode((800, 800))
display.fill((255, 180, 255))

def load_image(gg):
    im1 = pygame.image.load(gg)
    return im1



#ic.resize_image()





def get_event(button, event):
    if button.rect.collidepoint(pygame.mouse.get_pos()):
        print('q')
        button_sound = pygame.mixer.Sound("sounds\click_sound.WAV")
        pygame.mixer.Sound.play(button_sound)



im = pygame.image.load('resourse\\buttons.png')
im = im.subsurface([1978, 900, 1031, 262])
im.set_colorkey([255, 255, 255])
im = pygame.transform.scale(im, (240, int(240*0.35)))



all_sp = pygame.sprite.Group()

button = pygame.sprite.Sprite()
button.image = im
#button.rect = ([10, 200, 20, 20])
button.rect = button.image.get_rect()

#print(button.image.get_rect())
button.rect.x = 100
button.rect.y = 200
all_sp.add(button)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            get_event(button, event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    all_sp.draw(display)
    pygame.display.update()
