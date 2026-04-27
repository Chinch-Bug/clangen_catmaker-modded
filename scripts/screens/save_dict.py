import os

import pygame
import pygame_gui

from scripts.game_structure.image_button import UIImageButton
from pygame_gui.elements import UIWindow
import datetime
from platform import system
import logging
import json

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

class SaveAsDict(UIWindow):
    def __init__(self, cat_data):
        super().__init__(scale(pygame.Rect((400, 350), (800, 350))),
                         object_id="#game_over_window",
                         resizable=False)

        self.cat_data = cat_data
        self.file_name = f'{datetime.datetime.now():%Y-%m-%d}'

        self.open_data_directory_button = UIImageButton(
            scale(pygame.Rect((0, 215), (356, 60))),
            "",
            object_id="#open_data_directory_button",
            container=self,
            starting_height=2,
            tool_tip_text="Opens the data directory. "
                          "This is where save files, images, "
                          "and logs are stored.",
            anchors={'centerx': 'centerx'}
        )

        self.confirm_button = UIImageButton(
            scale(pygame.Rect((0, 150), (150, 60))),
            "",
            object_id="#save_cat_button",
            container=self,
            starting_height=2,
            anchors={'centerx': 'centerx'}
        )

        self.confirm_text = pygame_gui.elements.UITextEntryLine(
            scale(pygame.Rect((0, 55), (390, -1))),
            placeholder_text=self.file_name,
            object_id="#text_box_26_horizcenter_vertcenter_spacing_95",
            container=self,
            anchors={"centerx": "centerx"}
        )

    def save_text(self):
        if t := self.confirm_text.get_text():
            self.file_name = t
        file_number = ""
        i = 0
        while True:
            if os.path.isfile(f"{'./saved_cats'}/{self.file_name + file_number}.json"):
                i += 1
                file_number = f"_{i}"
            else:
                break
        
        with open(f"{'./saved_cats'}/{self.file_name + file_number}.json", "w") as f:
            json.dump(self.cat_data, f, indent=4)
        self.confirm_text.set_text(f"{self.file_name + file_number}")

    def process_event(self, event) -> bool:
        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.open_data_directory_button:
                if system() == 'Darwin':
                    subprocess.Popen(["open", "-R", './saved_cats'])
                elif system() == 'Windows':
                    os.startfile('.\\saved_cats')  # pylint: disable=no-member
                elif system() == 'Linux':
                    try:
                        subprocess.Popen(['xdg-open', './saved_cats'])
                    except OSError:
                        logger.exception("Failed to call to xdg-open.")
                return
            elif event.ui_element == self.confirm_button:
                self.save_text()
                self.confirm_button.disable()

        return super().process_event(event)
