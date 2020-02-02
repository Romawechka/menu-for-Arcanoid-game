import pygame
import Toolbox
from Toolbox import Button, Text
import threading

display_width, display_height = Toolbox.settings()


def display_updeate():
    global display_width
    global display_height
    while True:
        display_width, display_height = Toolbox.settings()


def display_tread():
    tread1 = threading.Thread(target=display_updeate, daemon=True)
    tread1.start()


pygame.init()

display = pygame.display.set_mode((display_width, display_height))
display.fill((255, 255, 255))

back_trigger = True


def back():
    global back_trigger
    back_trigger = True
    return back_trigger


def main_menu():
    global back_trigger
    main_menu_background = 'resourse\main_menu.jpg'
    show = True
    button = Button(display, 150, 50)
    button1 = Button(display, 200, 44)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        if back_trigger == True:
            Toolbox.display_create((display_width, display_height, main_menu_background))
            back_trigger = False
        button.draw_button(display_width / 2 - 55, display_height / 2 + 100, 'Выход', quit)
        button1.draw_button(display_width / 2 - int(button.width / 2), display_height / 2, 'Настройки', settings_menu)


def display_settings(settings_background):
    global display_width
    global display_height
    global back_trigger

    display_tread()

    button10 = Button(display, 400, 40)
    button11 = Button(display, 360, 40)
    button12 = Button(display, 240, 40)
    button13 = Button(display, 240, 40)
    Toolbox.display_create((display_width, display_height, settings_background))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

        button10.draw_button(
            display_width / 2 - button10.width / 2, display_height * 0.65, 'Экран 800 на 600',
            Toolbox.display_create, (800, 600, settings_background, True)
        )
        button11.draw_button(
            display_width / 2 - button11.width / 2, display_height * 0.8, 'Экран 450 на 400',
            Toolbox.display_create, (450, 400, settings_background, True)
        )
        button12.draw_button(
            display_width / 2 - button12.width / 2, display_height * 0.5, 'Полный экран',
            Toolbox.display_create, (450, 400, settings_background, True)
        )
        button13.draw_button(display_width * 0.02, display_height * 0.02, 'Главное меню', back, size=18)
        if back_trigger:
            back_trigger = False
            return


def volume_settings(settings_background):
    pass


def settings_menu():
    global display_width
    global display_height
    global back_trigger

    settings_background = 'resourse\settings.jpg'
    Toolbox.display_create((display_width, display_height, settings_background, False))

    button3 = Button(display, 210, 35)
    button4 = Button(display, 180, 35)
    button5 = Button(display, 180, 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

        button3.draw_button(
            display_width * 0.02, display_height * 0.2, 'Настройки экрана',
            display_settings, settings_background, size=18
        )
        button5.draw_button(
            display_width * 0.02, display_height * 0.3, 'Настройки звука',
            volume_settings, settings_background, size=18
        )

        button4.draw_button(display_width * 0.02, display_height * 0.02, 'Главное меню', back, size=18)
        if back_trigger:
            break


def start():
    pygame.time.set_timer(pygame.USEREVENT, 1300)
    counter = 8
    path = pygame.mixer.Sound("sounds\loading.WAV")
    path.set_volume(0.01)
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


# start()
main_menu()
