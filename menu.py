import pygame
import Image_creator as ic
import Toolbox
from Toolbox import Button, Text

display_width, display_height = Toolbox.settings()

pygame.init()

display = pygame.display.set_mode((display_width, display_height))
display.fill((255, 255, 255))


def main_menu():
    ic.resize_image("resourse\main_menu.jpg", "resourse\main_menu.jpg", (display_width, display_height))
    menu_background = pygame.image.load('resourse\main_menu.jpg')
    show = True
    button = Button(110, 50, (13, 162, 58), (23, 204, 58), display)
    button1 = Button(200, 50, (13, 162, 58), (23, 204, 58), display)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        display.blit(menu_background, (0, 0))
        button.draw_button(display_width / 2 - 55, display_height / 2 + 100, 'Выход', quit)
        button1.draw_button(display_width / 2 - 100, display_height / 2, 'Настройки', settings_menu)


def display_settings(settings_background):
    global display_width
    global display_height

    button10 = Button(350, 50, (13, 162, 58), (23, 204, 58), display)
    button11 = Button(350, 50, (13, 162, 58), (23, 204, 58), display)
    button12 = Button(350, 50, (13, 162, 58), (23, 204, 58), display)
    Toolbox.display_create((display_width, display_height, settings_background))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

        button10.draw_button(
            display_width / 2 - 175, display_height / 2 - 100, 'Экран 800 на 600',
            Toolbox.display_create, (800, 600, settings_background, True)
        )
        button11.draw_button(
            display_width / 2 - 175, display_height / 2 - 180, 'Экран 450 на 400',
            Toolbox.display_create, (450, 400, settings_background, True)
        )
        button12.draw_button(
            display_width / 2 - 175, display_height / 2, 'Полный экран',
            Toolbox.display_create, (450, 400, settings_background, True)
        )


def settings_menu():
    global display_width
    global display_height
    settings_background = 'resourse\settings.jpg'

    Toolbox.display_create((display_width, display_height, settings_background, False))

    button3 = Button(200, 25, (13, 162, 58), (23, 204, 58), display)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

        button3.draw_button(
            display_width / 20, display_height / 2 - 100, 'Настройки экрана',
            display_settings, settings_background, size=18
        )


def start():
    pygame.time.set_timer(pygame.USEREVENT, 1300)
    counter = 8
    path = pygame.mixer.Sound("sounds\loading.WAV")
    path.set_volume(1)
    pygame.mixer.Sound.play(path)
    text = Text(display)

    srart_background = 'resourse\scale.jpg'

    Toolbox.display_create((display_width, display_height, srart_background))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                counter -= 1
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if counter == 0:
            break
        pygame.display.update()
        text.print_text("Arcanoid", display_width / 2 - 100, 5, (0, 255, 1), 'fonts\Start.ttf', 50)


#start()
main_menu()
