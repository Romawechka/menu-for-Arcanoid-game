import pygame
import Image_creator


def settings(write=False):
    width_height = list()
    # print(write)
    with open("settings\display_settings.txt", 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        # print(file.readline())
        counter = 0
        for line in lines:
            if write == True:
                arg = str(line.split('=')[0]).replace('\n', '').replace(' ', '')
                # print(line, display_width)
                if arg == 'display_width':
                    # print('q')
                    file.seek(counter)
                    file.writelines('display_width = {}\n'.format(display_width))
                if arg == 'display_height':
                    file.writelines('display_height = {}\n'.format(display_height))

            arg = int(str(line.split('=')[1]).replace('\n', '').replace(' ', ''))
            width_height.append(arg)
            counter += 1
    return width_height


def display_create(args):
    global display
    global display_width
    global display_height

    display_width = args[0]
    display_height = args[1]
    if len(args) == 4:
        write = args[3]
        background = args[2]
    else:
        write = False
        background = args[2]

    Image_creator.resize_image(background, background, (display_width, display_height))
    new_background = pygame.image.load(background)


    if write:
        settings(True)



    display = pygame.display.set_mode((display_width, display_height))
    display.fill((255, 255, 255))
    display.blit(new_background, (0, 0))



class Text:
    def __init__(self, display):
        self.display = display

    def print_text(self, message, x, y, font_color=(0, 0, 0), font_type='fonts\Meamury.ttf', font_size=30):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.display.blit(text, (x, y))


class Button(Text):
    def __init__(self, width, height, inactive_color, active_color, display):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.button_sound = pygame.mixer.Sound("sounds\click_sound.WAV")
        self.display = display

    def draw_button(self, x, y, message='', action=None, args=None, size=30):
        mouse_cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x <= mouse_cursor[0]) and (x + self.width >= mouse_cursor[0]):
            if (y <= mouse_cursor[1]) and (y + self.height >= mouse_cursor[1]):
                pygame.draw.rect(self.display, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    pygame.mixer.Sound.play(self.button_sound)
                    pygame.time.delay(100)

                    if action is not None:
                        if args is not None:
                            action(args)
                        else:
                            action()
            else:
                pygame.draw.rect(self.display, self.inactive_color, (x, y, self.width, self.height))
        else:
            pygame.draw.rect(self.display, self.inactive_color, (x, y, self.width, self.height))
        self.print_text(message, x + 10, y + 10, font_size=size)
