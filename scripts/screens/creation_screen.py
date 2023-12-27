import scripts.screens.base_screens as base_screens
import pygame_gui
import pygame
import scripts.global_vars as global_vars
from scripts.utility import update_sprite, generate_sprite, set_current_season
from scripts.game_structure.image_cache import load_image
import scripts.game_structure.image_button as custom_buttons
from scripts.cat.cats import Cat
from scripts.game_structure.image_cache import load_image

class CreationScreen(base_screens.Screens):

    def __init__(self, name):
        self.general_tab = None
        self.pattern_tab = None
        self.extras_tab = None
        self.cat_image = None
        self.back = None
        self.randomize = None
        self.clear = None
        self.tab_background = None
        self.fur_length_select = None
        self.general_tab_button = None
        self.pattern_tab_button = None
        self.extras_tab_button = None
        self.color_select = None
        self.white_patches_select = None
        self.pose_select = None
        self.base_pelt_select = None
        self.cat_platform = None
        self.visable_tab = None
        self.dropdown_menus = {}
        self.checkboxes = {}
        self.labels = {}
        self.selectedbasegame = None
        self.selectedgenemod = None
        self.selectedwhite = 'None'

        super().__init__(name)

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.general_tab_button:
                self.show_tab(self.general_tab)
                self.handle_page_switching(0)
            elif event.ui_element == self.pattern_tab_button:
                self.show_tab(self.pattern_tab)
                self.handle_page_switching(0)
            elif event.ui_element == self.extras_tab_button:
                self.show_tab(self.extras_tab)
                self.handle_page_switching(0)
            elif event.ui_element == self.next_page:
                self.handle_page_switching(1)
            elif event.ui_element == self.last_page:
                self.handle_page_switching(-1)
            elif event.ui_element == self.clear:
                global_vars.CREATED_CAT = Cat()
                self.build_dropdown_menus()
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
                self.update_platform()
            elif event.ui_element == self.randomize:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    shift_click = True
                else:
                    shift_click = False
                
                global_vars.CREATED_CAT.randomize_looks(just_pattern=shift_click)
                self.build_dropdown_menus()
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
                self.update_platform()
            elif event.ui_element == self.back:
                self.change_screen('start screen')
            # Here is where the cat creation checkboxes start.
            elif event.ui_element == self.checkboxes["reverse"]:
                # This checkbox flips the car horizonally.
                global_vars.CREATED_CAT.pelt.reverse = not \
                    global_vars.CREATED_CAT.pelt.reverse
                    
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["shading"]:
                if global_vars.CREATED_CAT.shading:
                    global_vars.CREATED_CAT.shading = False
                else:
                    global_vars.CREATED_CAT.shading = True
                    
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["paralyzed"]:
                global_vars.CREATED_CAT.pelt.paralyzed = not \
                    global_vars.CREATED_CAT.pelt.paralyzed
                
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["sick"]:
                global_vars.CREATED_CAT.pelt.not_working = not \
                    global_vars.CREATED_CAT.pelt.not_working
                
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["carameltoggle"]:
                if global_vars.CREATED_CAT.genotype.dilutemd[0] == 'Dm':
                    global_vars.CREATED_CAT.genotype.dilutemd[0] = 'dm'
                else:
                    global_vars.CREATED_CAT.genotype.dilutemd[0] = 'Dm'
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["tortie"]:
                if global_vars.CREATED_CAT.genotype.sexgene == ['O', 'o']:
                    global_vars.CREATED_CAT.genotype.sexgene = ['o', 'o']
                    global_vars.CREATED_CAT.phenotype.tortie = False
                else:
                    global_vars.CREATED_CAT.genotype.sexgene = ['O', 'o']
                    global_vars.CREATED_CAT.phenotype.tortie = True
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["chimera"]:
                if global_vars.CREATED_CAT.genotype.chimera:
                    global_vars.CREATED_CAT.genotype.chimera = False
                else:
                    global_vars.CREATED_CAT.genotype.chimera = True
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["revtortie"]:
                if global_vars.CREATED_CAT.genotype.tortiepattern and 'rev' in global_vars.CREATED_CAT.genotype.tortiepattern:
                    global_vars.CREATED_CAT.genotype.tortiepattern = global_vars.CREATED_CAT.genotype.tortiepattern.replace('rev', '')
                else:
                    global_vars.CREATED_CAT.genotype.tortiepattern = 'rev' + global_vars.CREATED_CAT.genotype.tortiepattern
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["brindled_bicolour"]:
                global_vars.CREATED_CAT.genotype.brindledbi = not \
                    global_vars.CREATED_CAT.genotype.brindledbi
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["bleaching"]:
                if global_vars.CREATED_CAT.genotype.bleach[0] == 'lb':
                    global_vars.CREATED_CAT.genotype.bleach[0] = 'Lb'
                else:
                    global_vars.CREATED_CAT.genotype.bleach[0] = 'lb'
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["ghosting"]:
                if global_vars.CREATED_CAT.genotype.ghosting[0] == 'Gh':
                    global_vars.CREATED_CAT.genotype.ghosting[0] = 'gh'
                else:
                    global_vars.CREATED_CAT.genotype.ghosting[0] = 'Gh'
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.checkboxes["satin"]:
                if global_vars.CREATED_CAT.genotype.satin[0] == 'st':
                    global_vars.CREATED_CAT.genotype.satin[0] = 'St'
                else:
                    global_vars.CREATED_CAT.genotype.satin[0] = 'st'
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            
            elif event.ui_element == self.checkboxes["silver_checkbox"]:
                if global_vars.CREATED_CAT.genotype.silver[0] == 'I':
                    global_vars.CREATED_CAT.genotype.silver[0] = 'i'
                else:
                    global_vars.CREATED_CAT.genotype.silver[0] = 'I'

                global_vars.CREATED_CAT.phenotype.SilverGoldFinder()
                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["add_basegame"]:

                global_vars.CREATED_CAT.genotype.white_pattern.append(self.selectedbasegame)

                self.build_dropdown_menus()
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["add_genemod"]:

                if 'None' not in self.selectedgenemod:
                    global_vars.CREATED_CAT.genotype.white_pattern.append(self.selectedgenemod)

                self.build_dropdown_menus()
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["remove_white"]:

                while self.selectedwhite in global_vars.CREATED_CAT.genotype.white_pattern:
                    global_vars.CREATED_CAT.genotype.white_pattern.remove(self.selectedwhite)
                
                self.selectedwhite = 'None'

                self.build_dropdown_menus()
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["clear_white"]:

                global_vars.CREATED_CAT.genotype.white_pattern = [global_vars.CREATED_CAT.genotype.white_pattern[0]]
                
                self.selectedwhite = 'None'

                self.build_dropdown_menus()
                self.update_cat_image()
        
        # Here if where all the dropdown menu actions are handled. ---------------------------------------------
        elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.dropdown_menus["color_select"]:
                global_vars.CREATED_CAT.phenotype.SetBaseColour(event.text.lower())

                if global_vars.CREATED_CAT.genotype.pinkdilute[0] == 'dp' or global_vars.CREATED_CAT.genotype.pointgene[0] == 'c' or (global_vars.CREATED_CAT.genotype.pointgene[0] != 'C' and global_vars.CREATED_CAT.genotype.pointgene[1] == 'c'):
                    global_vars.CREATED_CAT.phenotype.pigone = 'albino'
                    global_vars.CREATED_CAT.phenotype.pigtwo = 'albino'
                    global_vars.CREATED_CAT.phenotype.pigext = 'albino'
                else:
                    if global_vars.CREATED_CAT.phenotype.pigone == 'albino':
                        global_vars.CREATED_CAT.phenotype.pigone = 'P1'
                    if global_vars.CREATED_CAT.phenotype.pigtwo == 'albino':
                        global_vars.CREATED_CAT.phenotype.pigtwo = 'P1'
                    if global_vars.CREATED_CAT.phenotype.pigext == 'albino':
                        global_vars.CREATED_CAT.phenotype.pigext = 'P1'
                global_vars.CREATED_CAT.phenotype.UpdateEyes()

                self.update_checkboxes_and_disable_dropdowns()

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["pelt_length_select"]:
                global_vars.CREATED_CAT.pelt.set_pelt_length(event.text)
                global_vars.CREATED_CAT.phenotype.SetFurLength(event.text.lower())
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["ear_type_select"]:
                global_vars.CREATED_CAT.phenotype.SetEarType(event.text.lower())
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["tail_type_select"]:
                global_vars.CREATED_CAT.phenotype.SetTailType(event.text.lower())
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["pose_select"]:
                global_vars.CREATED_CAT.pelt.set_pose(
                    global_vars.CREATED_CAT.age,
                    event.text[-1]
                )
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["age_select"]:
                global_vars.CREATED_CAT.age = event.text.lower()
                # We need to rebuild some dropdowns in order for the pose
                # to update correctly. 
                self.build_dropdown_menus()
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["tabby_pattern_select"]:

                global_vars.CREATED_CAT.phenotype.SetTabbyPattern(global_vars.tabbies.inverse[event.text])

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["agouti_select"]:

                global_vars.CREATED_CAT.phenotype.SetTabbyType(event.text)

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["sokoke_select"]:

                global_vars.CREATED_CAT.genotype.soktype = event.text.lower()

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["wideband_select"]:

                global_vars.CREATED_CAT.genotype.wbtype = event.text.lower()
                global_vars.CREATED_CAT.phenotype.SilverGoldFinder()
                
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["rufousing_select"]:

                global_vars.CREATED_CAT.genotype.ruftype = event.text.lower()

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["corin_select"]:

                global_vars.CREATED_CAT.genotype.sunshine[0] = global_vars.corin.inverse[event.text]
                global_vars.CREATED_CAT.genotype.sunshine[1] = global_vars.corin.inverse[event.text]
                global_vars.CREATED_CAT.phenotype.SilverGoldFinder()
                
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["extention_select"]:

                global_vars.CREATED_CAT.genotype.ext[0] = global_vars.extention.inverse[event.text]
                global_vars.CREATED_CAT.genotype.ext[1] = global_vars.extention.inverse[event.text]

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["specred_select"]:

                global_vars.CREATED_CAT.genotype.specialred = event.text.lower()

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["vitiligo_select"]:

                global_vars.CREATED_CAT.genotype.white_pattern[0] = global_vars.vit.inverse[event.text]

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["basegame_select"]:

                self.selectedbasegame = global_vars.white_patches.inverse[event.text]
            elif event.ui_element == self.dropdown_menus["genemod_select"]:

                self.selectedgenemod = global_vars.genemod_white.inverse[event.text]
            elif event.ui_element == self.dropdown_menus["white_select"]:

                self.selectedwhite = event.text
            elif event.ui_element == self.dropdown_menus["chimera_shape"]:

                global_vars.CREATED_CAT.genotype.chimerapattern = global_vars.tortie_patches_shapes.inverse[event.text]

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["torte_patches_shape"]:

                global_vars.CREATED_CAT.genotype.tortiepattern = global_vars.tortie_patches_shapes.inverse[event.text]
                if global_vars.CREATED_CAT.genotype.sexgene == ['o', 'o'] and event.text != 'None':    
                    global_vars.CREATED_CAT.genotype.sexgene = ['O', 'o']
                elif event.text == 'None':
                    global_vars.CREATED_CAT.genotype.tortiepattern = None
                    if global_vars.CREATED_CAT.genotype.sexgene == ['O', 'o']:
                        global_vars.CREATED_CAT.genotype.sexgene = ['o', 'o']

                self.update_checkboxes_and_disable_dropdowns()
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["scar_1"]:
                global_vars.CREATED_CAT.pelt.scar_slot_list[0] = global_vars.scars.inverse[event.text]
                
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["scar_2"]:
                global_vars.CREATED_CAT.pelt.scar_slot_list[1] = global_vars.scars.inverse[event.text]
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["scar_3"]:
                global_vars.CREATED_CAT.pelt.scar_slot_list[2] = global_vars.scars.inverse[event.text]
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["scar_4"]:
                global_vars.CREATED_CAT.pelt.scar_slot_list[3] = global_vars.scars.inverse[event.text]
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["accessory"]:
                global_vars.CREATED_CAT.pelt.accessory = global_vars.accessories.inverse[event.text]
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["lineart_select"]:
                if event.text == "StarClan":
                    global_vars.CREATED_CAT.dead = True
                    global_vars.CREATED_CAT.df = False
                elif event.text == "Dark Forest":
                    global_vars.CREATED_CAT.dead = True
                    global_vars.CREATED_CAT.df = True
                else:
                    global_vars.CREATED_CAT.dead = False
                    global_vars.CREATED_CAT.df = False
                
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["platform_select"]:
                global_vars.CREATED_CAT.platform = event.text
                set_current_season(global_vars.CREATED_CAT, event.text)
                self.update_cat_image()
                self.update_platform()
            elif event.ui_element == self.dropdown_menus["karpati_select"]:
                global_vars.CREATED_CAT.phenotype.fade = event.text

                if event.text == 'None':
                    global_vars.CREATED_CAT.genotype.karp = ['k', 'k']
                elif event.text == 'Homozygous':
                    global_vars.CREATED_CAT.genotype.karp = ['K', 'K']
                else:
                    global_vars.CREATED_CAT.genotype.karp = ['K', 'k']
                
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["points_select"]:
                global_vars.CREATED_CAT.phenotype.SetPoints(event.text)

                if global_vars.CREATED_CAT.genotype.pinkdilute[0] == 'dp' or 'c' in global_vars.CREATED_CAT.genotype.pointgene:
                    global_vars.CREATED_CAT.phenotype.pigone = 'albino'
                    global_vars.CREATED_CAT.phenotype.pigtwo = 'albino'
                    global_vars.CREATED_CAT.phenotype.pigext = 'albino'
                elif global_vars.CREATED_CAT.genotype.pointgene[0] == 'cs':
                    global_vars.CREATED_CAT.phenotype.pigone = 'blue'
                    global_vars.CREATED_CAT.phenotype.pigtwo = 'blue'
                    global_vars.CREATED_CAT.phenotype.pigext = 'blue'
                elif global_vars.CREATED_CAT.genotype.pointgene == ['cb', 'cs']:
                    if global_vars.CREATED_CAT.phenotype.pigone not in ['P1', 'blue']:
                        global_vars.CREATED_CAT.phenotype.pigone = 'P1'
                    if global_vars.CREATED_CAT.phenotype.pigtwo not in ['P1', 'blue']:
                        global_vars.CREATED_CAT.phenotype.pigtwo = 'P1'
                    if global_vars.CREATED_CAT.phenotype.pigext not in ['P1', 'blue']:
                        global_vars.CREATED_CAT.phenotype.pigext = 'P1'
                else:
                    if global_vars.CREATED_CAT.phenotype.pigone == 'albino':
                        global_vars.CREATED_CAT.phenotype.pigone = 'P1'
                    if global_vars.CREATED_CAT.phenotype.pigtwo == 'albino':
                        global_vars.CREATED_CAT.phenotype.pigtwo = 'P1'
                    if global_vars.CREATED_CAT.phenotype.pigext == 'albino':
                        global_vars.CREATED_CAT.phenotype.pigext = 'P1'

                global_vars.CREATED_CAT.phenotype.UpdateEyes()
                
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["ref1_select"]:
                global_vars.CREATED_CAT.phenotype.refone = event.text
                
                global_vars.CREATED_CAT.phenotype.UpdateEyes()

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["ref2_select"]:
                global_vars.CREATED_CAT.phenotype.reftwo = event.text
                
                global_vars.CREATED_CAT.phenotype.UpdateEyes()

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["ref3_select"]:
                global_vars.CREATED_CAT.phenotype.refext = event.text
                
                global_vars.CREATED_CAT.phenotype.UpdateEyes()

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["pig1_select"]:
                global_vars.CREATED_CAT.phenotype.pigone = event.text
                
                if global_vars.CREATED_CAT.genotype.pinkdilute[0] == 'dp' or 'c' in global_vars.CREATED_CAT.genotype.pointgene:
                    global_vars.CREATED_CAT.phenotype.pigone = 'albino'
                elif global_vars.CREATED_CAT.genotype.pointgene[0] == 'cs':
                    global_vars.CREATED_CAT.phenotype.pigone = 'blue'
                elif global_vars.CREATED_CAT.genotype.pointgene == ['cb', 'cs']:
                    if global_vars.CREATED_CAT.phenotype.pigone not in ['P1', 'blue']:
                        global_vars.CREATED_CAT.phenotype.pigone = 'P1'
                else:
                    if global_vars.CREATED_CAT.phenotype.pigone == 'albino':
                        global_vars.CREATED_CAT.phenotype.pigone = 'P1'
                global_vars.CREATED_CAT.phenotype.UpdateEyes()

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["pig2_select"]:
                global_vars.CREATED_CAT.phenotype.pigtwo = event.text
                
                if global_vars.CREATED_CAT.genotype.pinkdilute[0] == 'dp' or 'c' in global_vars.CREATED_CAT.genotype.pointgene:
                    global_vars.CREATED_CAT.phenotype.pigtwo = 'albino'
                elif global_vars.CREATED_CAT.genotype.pointgene[0] == 'cs':
                    global_vars.CREATED_CAT.phenotype.pigtwo = 'blue'
                elif global_vars.CREATED_CAT.genotype.pointgene == ['cb', 'cs']:
                    if global_vars.CREATED_CAT.phenotype.pigtwo not in ['P1', 'blue']:
                        global_vars.CREATED_CAT.phenotype.pigtwo = 'P1'
                else:
                    if global_vars.CREATED_CAT.phenotype.pigtwo == 'albino':
                        global_vars.CREATED_CAT.phenotype.pigtwo = 'P1'
                global_vars.CREATED_CAT.phenotype.UpdateEyes()

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["pig3_select"]:
                global_vars.CREATED_CAT.phenotype.pigext = event.text
                
                if global_vars.CREATED_CAT.genotype.pinkdilute[0] == 'dp' or 'c' in global_vars.CREATED_CAT.genotype.pointgene:
                    global_vars.CREATED_CAT.phenotype.pigext = 'albino'
                elif global_vars.CREATED_CAT.genotype.pointgene[0] == 'cs':
                    global_vars.CREATED_CAT.phenotype.pigext = 'blue'
                elif global_vars.CREATED_CAT.genotype.pointgene == ['cb', 'cs']:
                    if global_vars.CREATED_CAT.phenotype.pigext not in ['P1', 'blue']:
                        global_vars.CREATED_CAT.phenotype.pigext = 'P1'
                else:
                    if global_vars.CREATED_CAT.phenotype.pigext == 'albino':
                        global_vars.CREATED_CAT.phenotype.pigext = 'P1'
                global_vars.CREATED_CAT.phenotype.UpdateEyes()

                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["sectype_select"]:
                if event.text != 'N/A':    
                    global_vars.CREATED_CAT.genotype.extraeye = 'sectoral' + event.text
                else:
                    global_vars.CREATED_CAT.genotype.extraeye = None

                self.update_cat_image()

    def show_tab(self, container):
        for x in [self.pattern_tab, self.pattern_tab2, self.pattern_tab3, self.general_tab, self.extras_tab]:
            if x == container:
                x.show()
                self.visable_tab = x
            else:
                x.hide()
                
        tab_buttons = [((self.pattern_tab, self.pattern_tab2, self.pattern_tab3), self.pattern_tab_button),
                       ([self.general_tab], self.general_tab_button),
                       ([self.extras_tab], self.extras_tab_button)]
        
        for x in tab_buttons:
            if self.visable_tab in x[0]:
                x[1].disable()
            else:
                x[1].enable()
                    
    def handle_page_switching(self, direction: 1): 
        """Direction is next vs last page. 1 is next page, -1 is last page. 0 is no change (just update the buttons)  """
        if direction not in (1, 0, -1):
            return
        
        pages = [
            [self.pattern_tab, self.pattern_tab2, self.pattern_tab3]
        ]
        
        for x in pages:
            if self.visable_tab in x:    
                index = x.index(self.visable_tab)
                new_index = index + direction
                self.page_indicator.set_text(f"{new_index + 1} / {len(x)}")
                
                if 0 <= new_index < len(x):
                    self.show_tab(x[new_index])
                    
                    if new_index == len(x) - 1:
                        self.last_page.enable()
                        self.next_page.disable()
                    elif new_index == 0:
                        self.next_page.enable()
                        self.last_page.disable()
                    else:
                        self.next_page.enable()
                        self.last_page.enable()
                            
                    return
                
                
        self.page_indicator.set_text(f"1 / 1")
        self.next_page.disable()
        self.last_page.disable()

    def update_platform(self):
        path = global_vars.platforms[
            global_vars.CREATED_CAT.platform
        ]

        if path:
            self.cat_platform.set_image(pygame.transform.scale(load_image(path), (480, 420)))
            self.cat_platform.show()
        else:
            self.cat_platform.hide()

    def screen_switches(self):
        update_sprite(global_vars.CREATED_CAT)

        if global_vars.CREATED_CAT.platform != "None":
            self.cat_platform = pygame_gui.elements.UIImage(pygame.Rect((160, 25), (480, 420)),
                                                            pygame.transform.scale(load_image(
                                                                global_vars.platforms[
                                                                    global_vars.CREATED_CAT.platform
                                                                ]),(480, 420)))
        else:
            self.cat_platform = pygame_gui.elements.UIImage(pygame.Rect((160, 25), (480, 420)),
                                                            global_vars.MANAGER.get_universal_empty_surface(),
                                                            visible=False)

        self.cat_image = pygame_gui.elements.UIImage(pygame.Rect((250, 25), (300, 300)),
                                                     pygame.transform.scale(global_vars.CREATED_CAT.sprite,
                                                                            (300, 300)))

        self.back = custom_buttons.UIImageButton(pygame.Rect((50, 25), (105, 30)), "",
                                                 object_id="#back_button")

        self.randomize = custom_buttons.UIImageButton(pygame.Rect((630, 291), (50, 50)), "",
                                                      object_id="#random_dice_button")

        self.clear = custom_buttons.UIImageButton(pygame.Rect((690, 291), (50, 50)), "",
                                                  object_id="#clear_button")

        # -----------------------------------------------------------------------------------------------------------
        # TAB BUTTONS -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------------
        self.general_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 365), (100, 88)), "",
                                                               object_id="#general_tab_button")
        self.general_tab_button.disable()

        self.pattern_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 456), (100, 88)), "",
                                                               object_id="#pattern_tab_button")

        self.extras_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 547), (100, 88)), "",
                                                               object_id="#extra_tab_button")

        self.tab_background = pygame_gui.elements.UIImage(pygame.Rect((150, 350), (600, 300)),
                                                          load_image("resources/images/options.png"))
        
        # -----------------------------------------------------------------------------------------------------------
        # TAB CONTAINERS --------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------------
        self.general_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                    global_vars.MANAGER)

        self.pattern_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                    global_vars.MANAGER,
                                                                    visible=False)
        
        self.pattern_tab2 = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                    global_vars.MANAGER,
                                                                    visible=False)
        
        self.pattern_tab3 = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                    global_vars.MANAGER,
                                                                    visible=False)

        self.extras_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                   global_vars.MANAGER,
                                                                   visible=False)
        
        self.visable_tab = self.general_tab

        # ------------------------------------------------------------------------------------------------------------
        # Page Buttons -----------------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------------------------------
        self.last_page = custom_buttons.UIImageButton(pygame.Rect((334, 640), (34, 34)), "",
                                                      object_id="#last_page_button")
        self.next_page = custom_buttons.UIImageButton(pygame.Rect((534, 640), (34, 34)), "",
                                                      object_id="#next_page_button")
        self.page_indicator = pygame_gui.elements.UITextBox("", pygame.Rect((370, 647), (162, 30)),
                                                            object_id="#page_number")
        
        # Updates the page indicator and disabling the page buttons
        self.handle_page_switching(0)


        # ------------------------------------------------------------------------------------------------------------
        # General Tab Labels -----------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------------------------------

        self.labels["Age"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Age:",
                                                         container=self.general_tab,
                                                         object_id="#dropdown_label")

        self.labels["pose"] = pygame_gui.elements.UILabel(pygame.Rect((180, 15), (150, 25)), "Pose:",
                                                          container=self.general_tab,
                                                          object_id="#dropdown_label")

        self.labels["pelt_length"] = pygame_gui.elements.UILabel(pygame.Rect((20, 80), (150, 25)), "Pelt Length:",
                                                                 container=self.general_tab,
                                                                 object_id="#dropdown_label")

        self.labels["ear_type"] = pygame_gui.elements.UILabel(pygame.Rect((180, 80), (150, 25)), "Ear Type:",
                                                                 container=self.general_tab,
                                                                 object_id="#dropdown_label")

        self.labels["tail_type"] = pygame_gui.elements.UILabel(pygame.Rect((340, 80), (150, 25)), "Tail Length:",
                                                                 container=self.general_tab,
                                                                 object_id="#dropdown_label")

        self.labels["reversed"] = pygame_gui.elements.UILabel(pygame.Rect((55, 164), (-1, 25)), "Reversed",
                                                              container=self.general_tab,
                                                              object_id="#dropdown_label")

        self.labels["shading"] = pygame_gui.elements.UILabel(pygame.Rect((226, 164), (-1, 25)), "Shading",
                                                              container=self.general_tab,
                                                              object_id="#dropdown_label")

        self.labels["lineart"] = pygame_gui.elements.UILabel(pygame.Rect((340, 15), (150, 25)), "Lineart:",
                                                              container=self.general_tab,
                                                              object_id="#dropdown_label")
        
        self.labels["paralyzed"] = pygame_gui.elements.UILabel(pygame.Rect((55, 229), (-1, 25)), "Paralyzed",
                                                               container=self.general_tab,
                                                               object_id="#dropdown_label")
        
        self.labels["sick"] = pygame_gui.elements.UILabel(pygame.Rect((226, 229), (-1, 25)), "Sick",
                                                               container=self.general_tab,
                                                               object_id="#dropdown_label")
        
        self.labels["Chimera shape"] = pygame_gui.elements.UILabel(pygame.Rect((340, 145), (165, 25)),
                                                                          "Chimera Pattern:",
                                                                          container=self.general_tab,
                                                                          object_id="#dropdown_label")
        self.labels["Chimera"] = pygame_gui.elements.UILabel(pygame.Rect((397, 229), (-1, 25)), "Chimera?",
                                                               container=self.general_tab,
                                                               object_id="#dropdown_label")

        # -------------------------------------------------------------------------------------------------------------
        # Pattern Tab Labels ------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        self.labels["color"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Base Color:",
                                                           container=self.pattern_tab,
                                                           object_id="#dropdown_label")

        #self.labels["base pattern"] = pygame_gui.elements.UILabel(pygame.Rect((185, 15), (150, 25)), "Base Pattern:",
        #                                                          container=self.pattern_tab,
        #                                                          object_id="#dropdown_label")
        self.labels["Tortie Patches shape"] = pygame_gui.elements.UILabel(pygame.Rect((185, 15), (165, 25)),
                                                                          "Tortie Patches Pattern:",
                                                                          container=self.pattern_tab,
                                                                          object_id="#dropdown_label")

        #self.labels["white_patches"] = pygame_gui.elements.UILabel(pygame.Rect((375, 15), (150, 25)), "White Patches:",
        #                                                           container=self.pattern_tab,
        #                                                           object_id="#dropdown_label")
        
        self.labels["points"] = pygame_gui.elements.UILabel(pygame.Rect((375, 15), (-1, 25)), "Colour Restriction:",
                                                                   container=self.pattern_tab,
                                                                   object_id="#dropdown_label")
        
        #self.labels["vit"] = pygame_gui.elements.UILabel(pygame.Rect((220, 70), (-1, 25)), "Vitiligo:",
        #                                                           container=self.pattern_tab,
        #                                                           object_id="#dropdown_label")

        self.labels["caramel"] = pygame_gui.elements.UILabel(pygame.Rect((54, 80), (150, 25)), "Caramel",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")

        self.labels["revtort"] = pygame_gui.elements.UILabel(pygame.Rect((159, 80), (150, 25)), "Reverse Tortie",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")
        
        self.labels["brindlebi"] = pygame_gui.elements.UILabel(pygame.Rect((304, 80), (150, 25)), "Brindled Bicolour",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")

        self.labels["bleach"] = pygame_gui.elements.UILabel(pygame.Rect((54, 125), (150, 25)), "Bleaching",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")

        self.labels["ghost"] = pygame_gui.elements.UILabel(pygame.Rect((159, 125), (150, 25)), "Ghosting",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")
        
        self.labels["sat"] = pygame_gui.elements.UILabel(pygame.Rect((304, 125), (150, 25)), "Satin",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")
        self.labels["karp"] = pygame_gui.elements.UILabel(pygame.Rect((375, 100), (150, 25)), "Karpati:",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")
        self.labels["tortie"] = pygame_gui.elements.UILabel(pygame.Rect((500, 80), (150, 25)), "Tortie",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")
        
        
        self.labels["left"] = pygame_gui.elements.UILabel(pygame.Rect((20, 160), (150, 25)), "Left Eye:",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")
        self.labels["right"] = pygame_gui.elements.UILabel(pygame.Rect((185, 160), (150, 25)), "Right Eye:",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")
        self.labels["sec"] = pygame_gui.elements.UILabel(pygame.Rect((375, 160), (150, 25)), "Sectoral:",
                                                                 container=self.pattern_tab,
                                                                 object_id="#dropdown_label")

        #self.labels["eye color 1"] = pygame_gui.elements.UILabel(pygame.Rect((20, 125), (150, 25)), "Eye Color:",
        #                                                         container=self.pattern_tab,
        #                                                         object_id="#dropdown_label")

        #self.labels["eye color 2"] = pygame_gui.elements.UILabel(pygame.Rect((385, 125), (150, 25)), "Second Eye Color:",
        #                                                         container=self.pattern_tab,
        #                                                         object_id="#dropdown_label")

        #self.labels["tint"] = pygame_gui.elements.UILabel(pygame.Rect((200, 180), (150, 25)), "Tint:",
        #                                                  container=self.pattern_tab,
        #                                                  object_id="#dropdown_label")

        #self.labels["white_patches_tint"] = pygame_gui.elements.UILabel(pygame.Rect((360, 180), (-1, 25)),
        #                                                                "White Patches/Points Tint:",
        #                                                                container=self.pattern_tab,
        #                                                                object_id="#dropdown_label")

        #self.labels["Skin Color"] = pygame_gui.elements.UILabel(pygame.Rect((20, 180), (150, 25)), "Skin Color:",
        #                                                        container=self.pattern_tab,
        #                                                        object_id="#dropdown_label")

        #self.labels["hetero"] = pygame_gui.elements.UILabel(pygame.Rect((244, 145), (150, 25)), "Heterochromia",
        #                                                    container=self.pattern_tab,
        #                                                    object_id="#dropdown_label")

        
        
        # -------------------------------------------------------------------------------------------------------------
        # Pattern 2 Tab Labels ----------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        self.labels["tabby"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Tabby Pattern:",
                                                            container=self.pattern_tab2,
                                                            object_id="#dropdown_label")
        self.labels["agouti"] = pygame_gui.elements.UILabel(pygame.Rect((210, 15), (150, 25)), "Agouti:",
                                                            container=self.pattern_tab2,
                                                            object_id="#dropdown_label")
        self.labels["sokoke"] = pygame_gui.elements.UILabel(pygame.Rect((400, 15), (150, 25)), "Sokoke:",
                                                            container=self.pattern_tab2,
                                                            object_id="#dropdown_label")
        self.labels["wideband"] = pygame_gui.elements.UILabel(pygame.Rect((210, 70), (150, 25)), "Wideband:",
                                                            container=self.pattern_tab2,
                                                            object_id="#dropdown_label")
        self.labels["rufous"] = pygame_gui.elements.UILabel(pygame.Rect((400, 70), (150, 25)), "Rufousing:",
                                                            container=self.pattern_tab2,
                                                            object_id="#dropdown_label")
        self.labels["silver"] = pygame_gui.elements.UILabel(pygame.Rect((54, 80), (150, 25)), "Silver",
                                                            container=self.pattern_tab2,
                                                            object_id="#dropdown_label")
        self.labels["corin"] = pygame_gui.elements.UILabel(pygame.Rect((20, 125), (150, 25)), "CORIN gold:",
                                                            container=self.pattern_tab2,
                                                            object_id="#dropdown_label")
        self.labels["extention"] = pygame_gui.elements.UILabel(pygame.Rect((210, 125), (150, 25)), "Extention:",
                                                            container=self.pattern_tab2,
                                                            object_id="#dropdown_label")
        self.labels["specred"] = pygame_gui.elements.UILabel(pygame.Rect((400, 125), (150, 25)), "Special Red:",
                                                            container=self.pattern_tab2,
                                                            object_id="#dropdown_label")
        
        #self.labels["Tortie Patches Color"] = pygame_gui.elements.UILabel(pygame.Rect((70, 15), (150, 25)),
        #                                                                  "Tortie Patches Color",
        #                                                                  container=self.pattern_tab2,
        #                                                                  object_id="#dropdown_label")

        #self.labels["Tortie Patches pattern"] = pygame_gui.elements.UILabel(pygame.Rect((230, 15), (190, 25)),
        #                                                                  "Tortie Patches Pattern",
        #                                                                  container=self.pattern_tab2,
        #                                                                  object_id="#dropdown_label")

        #self.labels["Tortie Patches shape"] = pygame_gui.elements.UILabel(pygame.Rect((420, 15), (190, 25)),
        #                                                                  "Tortie Patches Shape",
        #                                                                  container=self.pattern_tab2,
        #                                                                  object_id="#dropdown_label")

        # -------------------------------------------------------------------------------------------------------------
        # Pattern 3 Tab Labels ----------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------
        
        self.labels["basegame"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Basegame White:",
                                                            container=self.pattern_tab3,
                                                            object_id="#dropdown_label")
        self.labels["remwhite"] = pygame_gui.elements.UILabel(pygame.Rect((240, 15), (150, 25)), "Remove White:",
                                                            container=self.pattern_tab3,
                                                            object_id="#dropdown_label")
        self.labels["genemod"] = pygame_gui.elements.UILabel(pygame.Rect((20, 70), (150, 25)), "Added White:",
                                                            container=self.pattern_tab3,
                                                            object_id="#dropdown_label")
        self.labels["vitiligo"] = pygame_gui.elements.UILabel(pygame.Rect((20, 125), (150, 25)), "Vitiligo:",
                                                            container=self.pattern_tab3,
                                                            object_id="#dropdown_label")

        # -------------------------------------------------------------------------------------------------------------
        # EXTRAS Tab Labels -------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        self.labels["scar_1"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Scar 1:",
                                                            container=self.extras_tab,
                                                            object_id="#dropdown_label")

        self.labels["scar_2"] = pygame_gui.elements.UILabel(pygame.Rect((300, 15), (150, 25)), "Scar 2:",
                                                            container=self.extras_tab,
                                                            object_id="#dropdown_label")

        self.labels["scar_3"] = pygame_gui.elements.UILabel(pygame.Rect((20, 70), (150, 25)), "Scar 3:",
                                                            container=self.extras_tab,
                                                            object_id="#dropdown_label")

        self.labels["scar_4"] = pygame_gui.elements.UILabel(pygame.Rect((300, 70), (150, 25)), "Scar 4:",
                                                            container=self.extras_tab,
                                                            object_id="#dropdown_label")

        self.labels["accessory"] = pygame_gui.elements.UILabel(pygame.Rect((20, 125), (150, 25)), "Accessory:",
                                                               container=self.extras_tab,
                                                               object_id="#dropdown_label")

        self.labels["platform"] = pygame_gui.elements.UILabel(pygame.Rect((270, 125), (150, 25)), "Platform:",
                                                               container=self.extras_tab,
                                                               object_id="#dropdown_label")


        self.build_dropdown_menus()
        self.update_checkboxes_and_disable_dropdowns()        
        
    def update_cat_image(self):
        """ Updates the cat images and displays it. """
        update_sprite(global_vars.CREATED_CAT)
        self.cat_image.set_image(pygame.transform.scale(global_vars.CREATED_CAT.sprite, (300, 300)))

    def build_dropdown_menus(self):
        """ Creates all the dropdown menus. """

        for ele in self.dropdown_menus:
            self.dropdown_menus[ele].kill()
        self.dropdown_menus = {}

        # -------------------------------------------------------------------------------------------------------------
        # General Tab Contents ----------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        self.dropdown_menus["pelt_length_select"] = pygame_gui.elements.UIDropDownMenu(["Short", "Long", "Short Rexed", "Long Rexed"],
                                                                                       global_vars.CREATED_CAT.pelt.type,
                                                                                       pygame.Rect((20, 100), (150, 30)),
                                                                                       container=self.general_tab)

        self.dropdown_menus["ear_type_select"] = pygame_gui.elements.UIDropDownMenu(["Normal", "Folded", "Curled", "Folded Curl"],
                                                                                       global_vars.CREATED_CAT.phenotype.GetEarType(),
                                                                                       pygame.Rect((180, 100), (150, 30)),
                                                                                       container=self.general_tab)

        self.dropdown_menus["tail_type_select"] = pygame_gui.elements.UIDropDownMenu(["Full", "3/4", "1/2", "1/3", "Stubby", "None"],
                                                                                       global_vars.CREATED_CAT.phenotype.GetTailType(),
                                                                                       pygame.Rect((340, 100), (150, 30)),
                                                                                       container=self.general_tab)

        self.dropdown_menus["pose_select"] = pygame_gui.elements.UIDropDownMenu(["Pose " + i for i in global_vars.poses[global_vars.CREATED_CAT.pelt.length][global_vars.CREATED_CAT.age]],
                                                                                 "Pose " +
                                                                                 global_vars.CREATED_CAT.pelt.current_poses[
                                                                                 global_vars.CREATED_CAT.age
                                                                                 ],
                                                                                 pygame.Rect((180, 35), (140, 30)),
                                                                                 container=self.general_tab)

        self.dropdown_menus["age_select"] = pygame_gui.elements.UIDropDownMenu(["Newborn", "Kitten", "Adolescent", "Adult", "Senior"],
                                                                               global_vars.CREATED_CAT.age.capitalize(),
                                                                               pygame.Rect((20, 35), (140, 30)),
                                                                               container=self.general_tab)

        if global_vars.CREATED_CAT.dead:
            if global_vars.CREATED_CAT.df:
                lineart = global_vars.lineart[2]
            else:
                lineart = global_vars.lineart[1]
        else:
            lineart = global_vars.lineart[0]

        self.dropdown_menus["lineart_select"] = pygame_gui.elements.UIDropDownMenu(global_vars.lineart,
                                                                                   lineart,
                                                                                   pygame.Rect((340, 35), (150, 30)),
                                                                                   container=self.general_tab)
        self.dropdown_menus["chimera_shape"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.tortie_patches_shapes.values(),
                                               global_vars.tortie_patches_shapes.get(
                                                  global_vars.CREATED_CAT.genotype.chimerapattern.replace('rev', '')
                                               ),
                                               pygame.Rect((340, 165), (180, 30)),
                                               container=self.general_tab)

        
        # -------------------------------------------------------------------------------------------------------------
        # Pattern Tab Contents ----------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        self.dropdown_menus["color_select"] = pygame_gui.elements.UIDropDownMenu(global_vars.colors,
                                                                                 global_vars.CREATED_CAT.phenotype.colour.capitalize(),
                                                                                 pygame.Rect((20, 35), (155, 30)),
                                                                                 container=self.pattern_tab)


        self.dropdown_menus["torte_patches_shape"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.tortie_patches_shapes.values(),
                                               global_vars.tortie_patches_shapes.get(
                                                  global_vars.CREATED_CAT.genotype.tortiepattern.replace('rev', '')
                                               ),
                                               pygame.Rect((185, 35), (180, 30)),
                                               container=self.pattern_tab)

        self.dropdown_menus["points_select"] = pygame_gui.elements.UIDropDownMenu(global_vars.points,
                                                                                  global_vars.CREATED_CAT.phenotype.point,
                                                                           pygame.Rect((375, 35), (190, 30)),
                                                                           container=self.pattern_tab)
        
        self.dropdown_menus["karpati_select"] = pygame_gui.elements.UIDropDownMenu(['None', 'Heterozygous', 'Homozygous'],
                                                                                  global_vars.CREATED_CAT.phenotype.fade,
                                                                           pygame.Rect((375, 120), (190, 30)),
                                                                           container=self.pattern_tab)
        
        if global_vars.CREATED_CAT.genotype.pinkdilute[0] == 'dp' or 'c' in global_vars.CREATED_CAT.genotype.pointgene:
            global_vars.CREATED_CAT.phenotype.pigone = 'albino'
            global_vars.CREATED_CAT.phenotype.pigtwo = 'albino'
            global_vars.CREATED_CAT.phenotype.pigext = 'albino'
        elif global_vars.CREATED_CAT.genotype.pointgene[0] == 'cs':
            global_vars.CREATED_CAT.phenotype.pigone = 'blue'
            global_vars.CREATED_CAT.phenotype.pigtwo = 'blue'
            global_vars.CREATED_CAT.phenotype.pigext = 'blue'
        elif global_vars.CREATED_CAT.genotype.pointgene == ['cb', 'cs']:
            if global_vars.CREATED_CAT.phenotype.pigone not in ['P1', 'blue']:
                global_vars.CREATED_CAT.phenotype.pigone = 'P1'
            if global_vars.CREATED_CAT.phenotype.pigtwo not in ['P1', 'blue']:
                global_vars.CREATED_CAT.phenotype.pigtwo = 'P1'
            if global_vars.CREATED_CAT.phenotype.pigext not in ['P1', 'blue']:
                global_vars.CREATED_CAT.phenotype.pigext = 'P1'
        else:
            if global_vars.CREATED_CAT.phenotype.pigone == 'albino':
                global_vars.CREATED_CAT.phenotype.pigone = 'P1'
            if global_vars.CREATED_CAT.phenotype.pigtwo == 'albino':
                global_vars.CREATED_CAT.phenotype.pigtwo = 'P1'
            if global_vars.CREATED_CAT.phenotype.pigext == 'albino':
                global_vars.CREATED_CAT.phenotype.pigext = 'P1'
        global_vars.CREATED_CAT.phenotype.UpdateEyes()
        self.dropdown_menus["ref1_select"] = pygame_gui.elements.UIDropDownMenu(['R11', 'R10', 'R9', 'R8', 'R7', 'R6', 'R5', 'R4', 'R3', 'R2', 'R1'],
                                                                                  global_vars.CREATED_CAT.phenotype.refone,
                                                                           pygame.Rect((20, 180), (75, 30)),
                                                                           container=self.pattern_tab)
        self.dropdown_menus["ref2_select"] = pygame_gui.elements.UIDropDownMenu(['R11', 'R10', 'R9', 'R8', 'R7', 'R6', 'R5', 'R4', 'R3', 'R2', 'R1'],
                                                                                  global_vars.CREATED_CAT.phenotype.reftwo,
                                                                           pygame.Rect((185, 180), (75, 30)),
                                                                           container=self.pattern_tab)
        self.dropdown_menus["ref3_select"] = pygame_gui.elements.UIDropDownMenu(['R11', 'R10', 'R9', 'R8', 'R7', 'R6', 'R5', 'R4', 'R3', 'R2', 'R1'],
                                                                                  global_vars.CREATED_CAT.phenotype.refext,
                                                                           pygame.Rect((375, 180), (75, 30)),
                                                                           container=self.pattern_tab)
        self.dropdown_menus["pig1_select"] = pygame_gui.elements.UIDropDownMenu(['P11', 'P10', 'P9', 'P8', 'P7', 'P6', 'P5', 'P4', 'P3', 'P2', 'P1', 'blue'],
                                                                                  global_vars.CREATED_CAT.phenotype.pigone,
                                                                           pygame.Rect((95, 180), (75, 30)),
                                                                           container=self.pattern_tab)
        self.dropdown_menus["pig2_select"] = pygame_gui.elements.UIDropDownMenu(['P11', 'P10', 'P9', 'P8', 'P7', 'P6', 'P5', 'P4', 'P3', 'P2', 'P1', 'blue'],
                                                                                  global_vars.CREATED_CAT.phenotype.pigtwo,
                                                                           pygame.Rect((260, 180), (75, 30)),
                                                                           container=self.pattern_tab)
        self.dropdown_menus["pig3_select"] = pygame_gui.elements.UIDropDownMenu(['P11', 'P10', 'P9', 'P8', 'P7', 'P6', 'P5', 'P4', 'P3', 'P2', 'P1', 'blue'],
                                                                                  global_vars.CREATED_CAT.phenotype.pigext,
                                                                           pygame.Rect((450, 180), (75, 30)),
                                                                           container=self.pattern_tab)
        self.dropdown_menus["sectype_select"] = pygame_gui.elements.UIDropDownMenu(['N/A', '1', '2', '3', '4', '5', '6'],
                                                                                  global_vars.CREATED_CAT.genotype.extraeye.replace('sectoral', '') if global_vars.CREATED_CAT.genotype.extraeye else 'N/A',
                                                                           pygame.Rect((450, 155), (100, 25)),
                                                                           container=self.pattern_tab)
        
        #------------------------------------------------------------------------------------------------------------
        # PATTERN TAB CONTENTS Page 2 -------------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------------ 
        
         # Tabby Pattern
        self.dropdown_menus["tabby_pattern_select"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.tabbies.values(),
                                               global_vars.tabbies[global_vars.CREATED_CAT.phenotype.GetTabbySprite()],
                                               pygame.Rect((20, 35), (175, 30)),
                                               container=self.pattern_tab2)
        self.dropdown_menus["agouti_select"] = \
            pygame_gui.elements.UIDropDownMenu(['Solid', 'Agouti', 'Midnight Charcoal', 'Twilight Charcoal'],
                                               global_vars.CREATED_CAT.phenotype.tabtype,
                                               pygame.Rect((210, 35), (175, 30)),
                                               container=self.pattern_tab2)
        self.dropdown_menus["sokoke_select"] = \
            pygame_gui.elements.UIDropDownMenu(['Normal markings', 'Mild fading', 'Full sokoke'],
                                               global_vars.CREATED_CAT.genotype.soktype.capitalize(),
                                               pygame.Rect((400, 35), (175, 30)),
                                               container=self.pattern_tab2)
        self.dropdown_menus["wideband_select"] = \
            pygame_gui.elements.UIDropDownMenu(['Low', 'Medium', 'High', 'Shaded', 'Chinchilla'],
                                               global_vars.CREATED_CAT.genotype.wbtype.capitalize(),
                                               pygame.Rect((210, 90), (175, 30)),
                                               container=self.pattern_tab2)
        self.dropdown_menus["rufousing_select"] = \
            pygame_gui.elements.UIDropDownMenu(['Low', 'Medium', 'Rufoused'],
                                               global_vars.CREATED_CAT.genotype.ruftype.capitalize(),
                                               pygame.Rect((400, 90), (175, 30)),
                                               container=self.pattern_tab2)
        self.dropdown_menus["corin_select"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.corin.values(),
                                               global_vars.corin[global_vars.CREATED_CAT.genotype.sunshine[0]],
                                               pygame.Rect((20, 145), (175, 30)),
                                               container=self.pattern_tab2)
        self.dropdown_menus["extention_select"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.extention.values(),
                                               global_vars.extention[global_vars.CREATED_CAT.genotype.ext[0]],
                                               pygame.Rect((210, 145), (175, 30)),
                                               container=self.pattern_tab2)
        self.dropdown_menus["specred_select"] = \
            pygame_gui.elements.UIDropDownMenu(['None', 'Merle', 'Cameo', 'Pseudo-cinnamon', 'Blue-red', 'Blue-tipped'],
                                               global_vars.CREATED_CAT.genotype.specialred.capitalize(),
                                               pygame.Rect((400, 145), (175, 30)),
                                               container=self.pattern_tab2)

        #------------------------------------------------------------------------------------------------------------
        # PATTERN TAB CONTENTS Page 3 -------------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------------ 
        
        self.dropdown_menus["basegame_select"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.white_patches.values(),
                                               global_vars.white_patches[self.selectedbasegame],
                                               pygame.Rect((20, 35), (175, 30)),
                                               container=self.pattern_tab3)
        
        self.dropdown_menus['add_basegame'] = custom_buttons.UIImageButton(pygame.Rect((200, 35), (30, 30)), "",
                                                    object_id="#add_button",
                                                    container=self.pattern_tab3)

        self.dropdown_menus["genemod_select"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.genemod_white.values(),
                                               global_vars.genemod_white[self.selectedgenemod],
                                               pygame.Rect((20, 90), (175, 30)),
                                               container=self.pattern_tab3)
        
        self.dropdown_menus['add_genemod'] = custom_buttons.UIImageButton(pygame.Rect((200, 90), (30, 30)), "",
                                                    object_id="#add_button",
                                                    container=self.pattern_tab3)
        self.dropdown_menus["white_select"] = \
            pygame_gui.elements.UIDropDownMenu(['None'] + global_vars.CREATED_CAT.genotype.white_pattern[1:] if len(global_vars.CREATED_CAT.genotype.white_pattern) > 1 else ['None'],
                                               self.selectedwhite,
                                               pygame.Rect((240, 35), (175, 30)),
                                               container=self.pattern_tab3)
        self.dropdown_menus['remove_white'] = custom_buttons.UIImageButton(pygame.Rect((420, 35), (30, 30)), "",
                                                    object_id="#minus_button",
                                                    container=self.pattern_tab3)
        self.dropdown_menus['clear_white'] = custom_buttons.UIImageButton(pygame.Rect((450, 35), (30, 30)), "",
                                                    object_id="#clear_button",
                                                    container=self.pattern_tab3)

        self.dropdown_menus["vitiligo_select"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.vit.values(),
                                               global_vars.vit[global_vars.CREATED_CAT.genotype.white_pattern[0]],
                                               pygame.Rect((20, 145), (175, 30)),
                                               container=self.pattern_tab3)

        #------------------------------------------------------------------------------------------------------------
        # EXTRAS TAB CONTENTS ---------------------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------------ 

        self.dropdown_menus["scar_1"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.scars.values(),
                                               global_vars.scars[
                                                   global_vars.CREATED_CAT.pelt.scar_slot_list[0]
                                               ],
                                               pygame.Rect((20, 35), (270, 30)),
                                               container=self.extras_tab)

        self.dropdown_menus["scar_2"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.scars.values(),
                                               global_vars.scars[
                                                   global_vars.CREATED_CAT.pelt.scar_slot_list[1]
                                               ],
                                               pygame.Rect((300, 35), (270, 30)),
                                               container=self.extras_tab)

        self.dropdown_menus["scar_3"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.scars.values(),
                                               global_vars.scars[
                                                   global_vars.CREATED_CAT.pelt.scar_slot_list[2]
                                               ],
                                               pygame.Rect((20, 90), (270, 30)),
                                               container=self.extras_tab)

        self.dropdown_menus["scar_4"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.scars.values(),
                                               global_vars.scars[
                                                   global_vars.CREATED_CAT.pelt.scar_slot_list[3]
                                               ],
                                               pygame.Rect((300, 90), (270, 30)),
                                               container=self.extras_tab)

        self.dropdown_menus["accessory"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.accessories.values(),
                                               global_vars.accessories[
                                                   global_vars.CREATED_CAT.pelt.accessory
                                               ],
                                               pygame.Rect((20, 145), (240, 30)),
                                               container=self.extras_tab)

        self.dropdown_menus["platform_select"] = \
            pygame_gui.elements.UIDropDownMenu(global_vars.platforms.keys(),
                                               global_vars.CREATED_CAT.platform,
                                               pygame.Rect((270, 145), (270, 30)),
                                               container=self.extras_tab)

    def update_checkboxes_and_disable_dropdowns(self):
        """ This function updates the state of the checkboxes, and also disables any dropdown menus that
            need to be disabled. """
        for ele in self.checkboxes:
            self.checkboxes[ele].kill()
        self.checkboxes = {}
        
        # -------------------------------------------------------------------------------------------------------------
        # General Tab -------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------
        
        #Shading
        if global_vars.CREATED_CAT.shading:
            self.checkboxes["shading"] = custom_buttons.UIImageButton(pygame.Rect((190, 160), (34, 34)),
                                                                      "",
                                                                      object_id="#checked_checkbox",
                                                                      container=self.general_tab)
        else:
            self.checkboxes["shading"] = custom_buttons.UIImageButton(pygame.Rect((190, 160), (34, 34)),
                                                                      "",
                                                                      object_id="#unchecked_checkbox",
                                                                      container=self.general_tab)
            
        # Reversed
        if global_vars.CREATED_CAT.pelt.reverse:
            self.checkboxes["reverse"] = custom_buttons.UIImageButton(pygame.Rect((20, 160), (34, 34)),
                                                                      "",
                                                                      object_id="#checked_checkbox",
                                                                      container=self.general_tab)
        else:
            self.checkboxes["reverse"] = custom_buttons.UIImageButton(pygame.Rect((20, 160), (34, 34)),
                                                                      "",
                                                                      object_id="#unchecked_checkbox",
                                                                      container=self.general_tab)
        
        # Paralyzed
        if global_vars.CREATED_CAT.pelt.paralyzed:
            self.checkboxes["paralyzed"] = custom_buttons.UIImageButton(pygame.Rect((20, 225), (34, 34)),
                                                                        "",
                                                                        object_id="#checked_checkbox",
                                                                        container=self.general_tab)
        else:
            self.checkboxes["paralyzed"] = custom_buttons.UIImageButton(pygame.Rect((20, 225), (34, 34)),
                                                                        "",
                                                                        object_id="#unchecked_checkbox",
                                                                        container=self.general_tab)
            
        # Sick
        if global_vars.CREATED_CAT.pelt.not_working:
            self.checkboxes["sick"] = custom_buttons.UIImageButton(pygame.Rect((190, 225), (34, 34)),
                                                                   "",
                                                                   object_id="#checked_checkbox",
                                                                   container=self.general_tab)
        else:
            self.checkboxes["sick"] = custom_buttons.UIImageButton(pygame.Rect((190, 225), (34, 34)),
                                                                   "",
                                                                   object_id="#unchecked_checkbox",
                                                                   container=self.general_tab)
        # Chimera
        if global_vars.CREATED_CAT.genotype.chimera:
            self.checkboxes["chimera"] = custom_buttons.UIImageButton(pygame.Rect((360, 225), (34, 34)),
                                                                   "",
                                                                   object_id="#checked_checkbox",
                                                                   container=self.general_tab)
        else:
            self.checkboxes["chimera"] = custom_buttons.UIImageButton(pygame.Rect((360, 225), (34, 34)),
                                                                   "",
                                                                   object_id="#unchecked_checkbox",
                                                                   container=self.general_tab)

        # -------------------------------------------------------------------------------------------------------------
        # Pattern Tab -------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        # Caramel
        
        if global_vars.CREATED_CAT.genotype.dilutemd[0] == 'Dm':
            self.checkboxes["carameltoggle"] = custom_buttons.UIImageButton(pygame.Rect((20, 75), (34, 34)),
                                                                          "",
                                                                          object_id="#checked_checkbox",
                                                                          container=self.pattern_tab)
        else:
            self.checkboxes["carameltoggle"] = custom_buttons.UIImageButton(pygame.Rect((20, 75), (34, 34)),
                                                                          "",
                                                                          object_id="#unchecked_checkbox",
                                                                          container=self.pattern_tab)
            
        # Tortie
        if global_vars.CREATED_CAT.genotype.sexgene == ['O', 'o']:
            self.checkboxes["tortie"] = custom_buttons.UIImageButton(pygame.Rect((466, 75), (34, 34)),
                                                                      "",
                                                                      object_id="#checked_checkbox",
                                                                      container=self.pattern_tab)
        else:
            self.checkboxes["tortie"] = custom_buttons.UIImageButton(pygame.Rect((466, 75), (34, 34)),
                                                                      "",
                                                                      object_id="#unchecked_checkbox",
                                                                      container=self.pattern_tab)
        if global_vars.CREATED_CAT.genotype.sexgene[1] == 'O':
            self.checkboxes['tortie'].disable()
        else:
            self.checkboxes['tortie'].enable()

        # Reverse tortie
        if global_vars.CREATED_CAT.genotype.tortiepattern and 'rev' in global_vars.CREATED_CAT.genotype.tortiepattern:
            self.checkboxes["revtortie"] = custom_buttons.UIImageButton(pygame.Rect((125, 75), (34, 34)),
                                                                      "",
                                                                      object_id="#checked_checkbox",
                                                                      container=self.pattern_tab)
        else:
            self.checkboxes["revtortie"] = custom_buttons.UIImageButton(pygame.Rect((125, 75), (34, 34)),
                                                                      "",
                                                                      object_id="#unchecked_checkbox",
                                                                      container=self.pattern_tab)
            
        # Brindled Bicolour
        if global_vars.CREATED_CAT.genotype.brindledbi:
            self.checkboxes["brindled_bicolour"] = custom_buttons.UIImageButton(pygame.Rect((270, 75), (34, 34)),
                                                                      "",
                                                                      object_id="#checked_checkbox",
                                                                      container=self.pattern_tab)
        else:
            self.checkboxes["brindled_bicolour"] = custom_buttons.UIImageButton(pygame.Rect((270, 75), (34, 34)),
                                                                      "",
                                                                      object_id="#unchecked_checkbox",
                                                                      container=self.pattern_tab)

        if global_vars.CREATED_CAT.phenotype.tortie:
            self.checkboxes["brindled_bicolour"].enable()
        else:
            self.checkboxes["brindled_bicolour"].disable()

        # Bleaching
        
        if global_vars.CREATED_CAT.genotype.bleach[0] == 'lb':
            self.checkboxes["bleaching"] = custom_buttons.UIImageButton(pygame.Rect((20, 120), (34, 34)),
                                                                          "",
                                                                          object_id="#checked_checkbox",
                                                                          container=self.pattern_tab)
        else:
            self.checkboxes["bleaching"] = custom_buttons.UIImageButton(pygame.Rect((20, 120), (34, 34)),
                                                                          "",
                                                                          object_id="#unchecked_checkbox",
                                                                          container=self.pattern_tab)
            
        # Ghosting
        if global_vars.CREATED_CAT.genotype.ghosting[0] == 'Gh':
            self.checkboxes["ghosting"] = custom_buttons.UIImageButton(pygame.Rect((125, 120), (34, 34)),
                                                                      "",
                                                                      object_id="#checked_checkbox",
                                                                      container=self.pattern_tab)
        else:
            self.checkboxes["ghosting"] = custom_buttons.UIImageButton(pygame.Rect((125, 120), (34, 34)),
                                                                      "",
                                                                      object_id="#unchecked_checkbox",
                                                                      container=self.pattern_tab)
            
        # Satin/glitter
        if global_vars.CREATED_CAT.genotype.satin[0] == 'st':
            self.checkboxes["satin"] = custom_buttons.UIImageButton(pygame.Rect((270, 120), (34, 34)),
                                                                      "",
                                                                      object_id="#checked_checkbox",
                                                                      container=self.pattern_tab)
        else:
            self.checkboxes["satin"] = custom_buttons.UIImageButton(pygame.Rect((270, 120), (34, 34)),
                                                                      "",
                                                                      object_id="#unchecked_checkbox",
                                                                      container=self.pattern_tab)
            
        # Heterochromia
        #if global_vars.CREATED_CAT.pelt.eye_colour2:
        #    self.checkboxes["hetero_eyes"] = custom_buttons.UIImageButton(pygame.Rect((210, 140), (34, 34)),
        #                                                                  "",
        #                                                                  object_id="#checked_checkbox",
        #                                                                  container=self.pattern_tab)
        #    self.dropdown_menus["eye_color_2"].enable()
        #else:
        #    self.checkboxes["hetero_eyes"] = custom_buttons.UIImageButton(pygame.Rect((210, 140), (34, 34)),
        #                                                                  "",
        #                                                                  object_id="#unchecked_checkbox",
        #                                                                  container=self.pattern_tab)
        #    self.dropdown_menus["eye_color_2"].disable()
            
        # -------------------------------------------------------------------------------------------------------------
        # Pattern 2 Tab -----------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------
        
         # Silver Checkbox
        if global_vars.CREATED_CAT.genotype.silver[0] == 'I':
            self.checkboxes["silver_checkbox"] = custom_buttons.UIImageButton(pygame.Rect((20, 75), (34, 34)),
                                                                              "",
                                                                              object_id="#checked_checkbox",
                                                                              container=self.pattern_tab2)
        else:
            self.checkboxes["silver_checkbox"] = custom_buttons.UIImageButton(pygame.Rect((20, 75), (34, 34)),
                                                                              "",
                                                                              object_id="#unchecked_checkbox",
                                                                              container=self.pattern_tab2)
        
        # -------------------------------------------------------------------------------------------------------------
        # Extras Tab --------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

    def exit_screen(self):
        self.back.kill()
        self.back = None

        self.next_page.kill()
        self.next_page = None
        
        self.last_page.kill()
        self.last_page = None
        
        self.page_indicator.kill()
        self.page_indicator = None

        self.cat_platform.kill()
        self.cat_platform = None

        self.randomize.kill()
        self.randomize = None

        self.clear.kill()
        self.clear = None

        self.cat_image.kill()
        self.cat_image = None

        # Tabs
        self.general_tab_button.kill()
        self.general_tab_button = None

        self.pattern_tab_button.kill()
        self.pattern_tab_button = None

        self.extras_tab_button.kill()
        self.pattern_tab_button = None

        self.tab_background.kill()
        self.tab_background = None

        # TAB CONTAINERS
        self.general_tab.kill()
        self.general_tab = None

        self.pattern_tab.kill()
        self.pattern_tab = None
        
        self.pattern_tab2.kill()
        self.pattern_tab2 = None
        
        self.pattern_tab3.kill()
        self.pattern_tab3 = None

        self.extras_tab.kill()
        self.extras_tab = None

        self.labels = {}
        self.dropdown_menus = {}
        self.checkboxes = {}



class MoreDetailScreen(base_screens.Screens):

    def __init__(self, name):
        self.save_dict = {}
        self.labels = {}
        self.number_selects = {}
        self.cat_images = {}
        self.stored_status = None
        super().__init__(name)

    def handle_event(self, event):
        pass

    def screen_switches(self):
        update_sprite(global_vars.CREATED_CAT)

        self.draw_age_stage()
        
        self.back = custom_buttons.UIImageButton(pygame.Rect((50, 25), (105, 30)), "",
                                                 object_id="#back_button")

        # -----------------------------------------------------------------------------------------------------------
        # TAB BUTTONS -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------------
        self.general_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 365), (100, 88)), "",
                                                               object_id="#general_info_tab_button")
        self.general_tab_button.disable()

        self.trait_skill_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 456), (100, 88)), "",
                                                               object_id="#pattern_tab_button")

        self.tab_background = pygame_gui.elements.UIImage(pygame.Rect((150, 350), (600, 300)),
                                                          load_image("resources/images/options.png"))
        
        # -----------------------------------------------------------------------------------------------------------
        # TAB CONTAINERS --------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------------
        self.general_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                    global_vars.MANAGER)

        self.trait_skill_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                    global_vars.MANAGER,
                                                                    visible=False)
        
        self.trait_skill_tab2 = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                         global_vars.MANAGER,
                                                                         visible=False)
        
        self.visable_tab = self.general_tab

        # ------------------------------------------------------------------------------------------------------------
        # Page Buttons -----------------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------------------------------
        self.last_page = custom_buttons.UIImageButton(pygame.Rect((334, 640), (34, 34)), "",
                                                      object_id="#last_page_button")
        self.next_page = custom_buttons.UIImageButton(pygame.Rect((534, 640), (34, 34)), "",
                                                      object_id="#next_page_button")
        self.page_indicator = pygame_gui.elements.UITextBox("", pygame.Rect((370, 647), (162, 30)),
                                                            object_id="#page_number")
        
        # Updates the page indicator and disabling the page buttons
        self.handle_page_switching(0)


        # ------------------------------------------------------------------------------------------------------------
        # General Tab Labels -----------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------------------------------

        self.labels["prefix"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Prefix:",
                                                            container=self.general_tab,
                                                            object_id="#dropdown_label")
        
        self.prefix_enter = pygame_gui.elements.UITextEntryLine(pygame.Rect((20, 35),(180, 30)), 
                                                                container=self.general_tab,
                                                                placeholder_text="Fire")
        
        self.labels["suffix"] = pygame_gui.elements.UILabel(pygame.Rect((210, 15), (150, 25)), "Suffix:",
                                                            container=self.general_tab,
                                                            object_id="#dropdown_label")
        
        self.suffix_enter = pygame_gui.elements.UITextEntryLine(pygame.Rect((210, 35),(180, 30)), 
                                                                container=self.general_tab,
                                                                placeholder_text="heart")
        
        self.labels["status"] = pygame_gui.elements.UILabel(pygame.Rect((400, 15), (150, 25)), "Status (Rank):",
                                                            container=self.general_tab,
                                                            object_id="#dropdown_label")
        
        self.labels["sex"] = pygame_gui.elements.UILabel(pygame.Rect((20, 80), (150, 25)), "Sex:",
                                                            container=self.general_tab,
                                                            object_id="#dropdown_label")
        
        self.labels["gender"] = pygame_gui.elements.UILabel(pygame.Rect((20, 145), (150, 25)), "Gender Alignment:",
                                                            container=self.general_tab,
                                                            object_id="#dropdown_label")
        
        self.labels["experience"] = pygame_gui.elements.UILabel(pygame.Rect((210, 80), (150, 25)), "Experience Level:",
                                                                container=self.general_tab,
                                                                object_id="#dropdown_label")
        
        self.labels["age"] = pygame_gui.elements.UILabel(pygame.Rect((400, 80), (150, 25)), "Age (in moons):",
                                                                container=self.general_tab,
                                                                object_id="#dropdown_label")
        
        self.age_enter = pygame_gui.elements.UITextEntryLine(pygame.Rect((400, 100),(180, 30)), 
                                                             container=self.general_tab)
        self.age_enter.set_allowed_characters('numbers')
        
        
        """self.gender_alignment_other = pygame_gui.elements.UITextEntryLine(pygame.Rect((), ()), 
                                                                          container=self.general_tab,
                                                                          placeholder_text="Gender Here")
        
        self.labels["status"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Status (Rank):",
                                                            container=self.general_tab,
                                                            object_id="#dropdown_label")
        
        self.labels["age"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Age (in moons):",
                                                            container=self.general_tab,
                                                            object_id="#dropdown_label")
        
        self.labels["id"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Cat ID:",
                                                            container=self.general_tab,
                                                            object_id="#dropdown_label")
        
        self.labels["experience"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Experience Level:",
                                                                container=self.general_tab,
                                                                object_id="#dropdown_label")"""

        # -------------------------------------------------------------------------------------------------------------
        # Trait Skill Labels ------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        self.labels["trait"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Trait:",
                                                           container=self.trait_skill_tab,
                                                           object_id="#dropdown_label")
        self.labels["lawfulness"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Lawfulness:",
                                                           container=self.trait_skill_tab,
                                                           object_id="#dropdown_label")
        self.labels["aggression"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Aggression:",
                                                           container=self.trait_skill_tab,
                                                           object_id="#dropdown_label")
        self.labels["sociability"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Sociability:",
                                                           container=self.trait_skill_tab,
                                                           object_id="#dropdown_label")
        self.labels["stablity"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Stablity:",
                                                           container=self.trait_skill_tab,
                                                           object_id="#dropdown_label")
        
        """# Also create the facet select options, since those can be changes and don't need to be rebuild later
        self.lawfulness_enter = custom_buttons.UIFacetSelect()
        self.aggression_enter = custom_buttons.UIFacetSelect()
        self.sociability_enter = custom_buttons.UIFacetSelect()
        self.stablity_enter = custom_buttons.UIFacetSelect()"""
        
        
        # -------------------------------------------------------------------------------------------------------------
        # Trait Skill Labels 2 Tab Labels -----------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        self.labels["primary_path"] = pygame_gui.elements.UILabel(pygame.Rect((20, 15), (150, 25)), "Primary Skill Path:",
                                                            container=self.trait_skill_tab2,
                                                            object_id="#dropdown_label")
        
        self.labels["secondary_path"] = pygame_gui.elements.UILabel(pygame.Rect((70, 15), (150, 25)),
                                                               "Secondary Skill Path:",
                                                               container=self.trait_skill_tab2,
                                                               object_id="#dropdown_label")

        self.labels["primary_tier"] = pygame_gui.elements.UILabel(pygame.Rect((230, 15), (190, 25)),
                                                                          "Primary Skill Tier:",
                                                                          container=self.trait_skill_tab2,
                                                                          object_id="#dropdown_label")

        self.labels["secondary_tier"] = pygame_gui.elements.UILabel(pygame.Rect((420, 15), (190, 25)),
                                                                          "Secondary Skill Tier:",
                                                                          container=self.trait_skill_tab2,
                                                                          object_id="#dropdown_label")
        
        self.labels["hidden"] = pygame_gui.elements.UILabel(pygame.Rect((420, 15), (190, 25)),
                                                                        "Hidden Skill: ",
                                                                        container=self.trait_skill_tab2,
                                                                        object_id="#dropdown_label")
        
        """self.number_selects["primary_tier"] = custom_buttons.UIFacetSelect()
        self.number_selects["secondary_tier"] = custom_buttons.UIFacetSelect()"""
        

        #self.build_dropdown_menus()
        #self.update_checkboxes_and_disable_dropdowns()

    def handle_page_switching(self, direction: 1): 
        """Direction is next vs last page. 1 is next page, -1 is last page. 0 is no change (just update the buttons)  """
        if direction not in (1, 0, -1):
            return
        
        pages = []
        
        for x in pages:
            if self.visable_tab in x:    
                index = x.index(self.visable_tab)
                new_index = index + direction
                self.page_indicator.set_text(f"{new_index + 1} / {len(x)}")
                
                if 0 <= new_index < len(x):
                    self.show_tab(x[new_index])
                    
                    if new_index == len(x) - 1:
                        self.last_page.enable()
                        self.next_page.disable()
                    elif new_index == 0:
                        self.next_page.enable()
                        self.last_page.disable()
                    else:
                        self.next_page.enable()
                        self.last_page.enable()
                            
                    return
                
                
        self.page_indicator.set_text(f"1 / 1")
        self.next_page.disable()
        self.last_page.disable()
    
    def exit_screen(self):
        pass

    
    def draw_age_stage(self):
        for ele in self.cat_images:
            self.cat_images[ele].kill()
        self.cat_images = {}
        
        x_pos = 130
        for age in ["newborn", "kitten", "adolescent", "adult", "senior"]:
            self.cat_images[age] = pygame_gui.elements.UIImage(
                pygame.Rect((x_pos, 140), (100, 100)),
                pygame.transform.scale(generate_sprite(
                    global_vars.CREATED_CAT,
                    life_state=age,
                    no_not_working=True,
                    no_para=True
                ), (100, 100))
            )
            x_pos += 110
    
    def save_png(self, path):
        pass
    
    def update_status_from_moons(self):
        entered = int(self.age_enter.get_text())



class SaveCodeScreen(base_screens.Screens):

    def __init__(self, name):

        super().__init__(name)
        
        


