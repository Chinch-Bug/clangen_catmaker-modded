from scripts.game_structure.image_button import UIImageButton
import pygame
from pygame_gui.elements import UIWindow
import pygame_gui
import datetime
import os
import subprocess
from platform import system
import logging

logger = logging.getLogger(__name__)
screen_x, screen_y = 800, 700

def scale(rect):
    rect[0] = round(rect[0] / 1600 * screen_x) if rect[0] > 0 else rect[0]
    rect[1] = round(rect[1] / 1400 * screen_y) if rect[1] > 0 else rect[1]
    rect[2] = round(rect[2] / 1600 * screen_x) if rect[2] > 0 else rect[2]
    rect[3] = round(rect[3] / 1400 * screen_y) if rect[3] > 0 else rect[3]

    return rect


def scale_dimentions(dim):
    dim = list(dim)
    dim[0] = round(dim[0] / 1600 * screen_x) if dim[0] > 0 else dim[0]
    dim[1] = round(dim[1] / 1400 * screen_y) if dim[1] > 0 else dim[1]
    dim = tuple(dim)

    return dim

class SaveAsImage(UIWindow):
    def __init__(self, image_to_save):
        super().__init__(scale(pygame.Rect((400, 350), (800, 550))),
                         object_id="#game_over_window",
                         resizable=False)

        self.set_blocking(True)
        #game.switches['window_open'] = True

        self.image_to_save = image_to_save
        self.file_name = f'{datetime.datetime.now():%Y-%m-%d}'
        self.scale_factor = 1

        button_layout_rect = scale(pygame.Rect((0, 10), (44, 44)))
        button_layout_rect.topright = scale_dimentions((-2, 10))

        self.save_as_image = UIImageButton(
            scale(pygame.Rect((0, 180), (270, 60))),
            "",
            object_id="#save_image_button",
            starting_height=2,
            container=self,
            anchors={'centerx': 'centerx'}
        )

        self.open_data_directory_button = UIImageButton(
            scale(pygame.Rect((0, 350), (356, 60))),
            "",
            object_id="#open_data_directory_button",
            container=self,
            starting_height=2,
            tool_tip_text="Opens the data directory. "
                          "This is where save files, images, "
                          "and logs are stored.",
            anchors={'centerx': 'centerx'}
        )

        self.small_size_button = UIImageButton(
            scale(pygame.Rect((109, 100), (194, 60))),
            "",
            object_id="#image_small_button",
            container=self,
            starting_height=2
        )
        self.small_size_button.disable()

        self.medium_size_button = UIImageButton(
            scale(pygame.Rect((303, 100), (194, 60))),
            "",
            object_id="#image_medium_button",
            container=self,
            starting_height=2
        )

        self.large_size_button = UIImageButton(
            scale(pygame.Rect((497, 100), (194, 60))),
            "",
            object_id="#image_large_button",
            container=self,
            starting_height=2
        )

        self.confirm_text = pygame_gui.elements.UITextBox(
            "",
            scale(pygame.Rect((10, 250), (780, 90))),
            object_id="#text_box_26_horizcenter_vertcenter_spacing_95",
            container=self,
            starting_height=2
        )

    def save_image(self):
        file_name = self.file_name
        file_number = ""
        i = 0
        
        while True:
            if os.path.isfile(f"{'./saved_images'}/{file_name + file_number}.png"):
                i += 1
                file_number = f"_{i}"
            else:
                break

        scaled_image = pygame.transform.scale_by(
            self.image_to_save, self.scale_factor)
        pygame.image.save(
            scaled_image, f"{'./saved_images'}/{file_name + file_number}.png")
        return f"{file_name + file_number}.png"

    def process_event(self, event) -> bool:
        super().process_event(event)

        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.open_data_directory_button:
                if system() == 'Darwin':
                    subprocess.Popen(["open", "-R", './saved_images'])
                elif system() == 'Windows':
                    os.startfile('.\\saved_images')  # pylint: disable=no-member
                elif system() == 'Linux':
                    try:
                        subprocess.Popen(['xdg-open', './saved_images'])
                    except OSError:
                        logger.exception("Failed to call to xdg-open.")
                return
            elif event.ui_element == self.save_as_image:
                file_name = self.save_image()
                self.confirm_text.set_text(
                    f"Saved as {file_name} in the saved_images folder")
            elif event.ui_element == self.small_size_button:
                self.scale_factor = 1
                self.small_size_button.disable()
                self.medium_size_button.enable()
                self.large_size_button.enable()
            elif event.ui_element == self.medium_size_button:
                self.scale_factor = 4
                self.small_size_button.enable()
                self.medium_size_button.disable()
                self.large_size_button.enable()
            elif event.ui_element == self.large_size_button:
                self.scale_factor = 6
                self.small_size_button.enable()
                self.medium_size_button.enable()
                self.large_size_button.disable()
