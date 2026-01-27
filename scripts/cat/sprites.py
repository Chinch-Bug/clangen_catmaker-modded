import pygame

import ujson
import os

from scripts.game_structure.game_essentials import game

class Sprites():
    cat_tints = {}
    white_patches_tints = {}
    clan_symbols = []

    with open(
        "sprites/dicts/pose_sprite_data.json", "r", encoding="utf-8"
    ) as read_file:
        POSE_DATA = ujson.loads(read_file.read())

    with open(
        "sprites/dicts/collar_sprite_data.json", "r", encoding="utf-8"
    ) as read_file:
        COLLAR_DATA = ujson.loads(read_file.read())

    with open(
        "sprites/dicts/wild_sprite_data.json", "r", encoding="utf-8"
    ) as read_file:
        WILD_DATA = ujson.loads(read_file.read())

    with open(
        "sprites/dicts/plant_sprite_data.json", "r", encoding="utf-8"
    ) as read_file:
        PLANT_DATA = ujson.loads(read_file.read())

    with open(
        "sprites/dicts/scar_sprite_data.json", "r", encoding="utf-8"
    ) as read_file:
        SCAR_DATA = ujson.loads(read_file.read())

    with open(
        "sprites/dicts/scar_missing_sprite_data.json", "r", encoding="utf-8"
    ) as read_file:
        SCAR_MISSING_PART_DATA = ujson.loads(read_file.read())

    with open(
        "sprites/dicts/tortie_patches_sprite_data.json", "r", encoding="utf-8"
    ) as read_file:
        TORTIE_DATA = ujson.loads(read_file.read())

    with open(
        "sprites/dicts/white_patches_sprite_data.json", "r", encoding="utf-8"
    ) as read_file:
        WHITE_DATA = ujson.loads(read_file.read())

    with open(
        "sprites/dicts/eye_colour_data.json", "r", encoding="utf-8"
    ) as read_file:
        EYE_DATA = ujson.loads(read_file.read())

    def __init__(self):
        """Class that handles and hold all spritesheets.
        Size is normally automatically determined by the size
        of the lineart. If a size is passed, it will override
        this value."""
        self.symbol_dict = None
        self.size = None
        self.spritesheets = {}
        self.images = {}
        self.sprites = {}

        # Shared empty sprite for placeholders
        self.blank_sprite = None

        self.load_tints()

        self.sheet_layout = self.POSE_DATA["sheet_layout"]

    def load_tints(self):
        try:
            with open("sprites/dicts/tint.json", 'r') as read_file:
                Sprites.cat_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading Tints")

        try:
            with open("sprites/dicts/white_patches_tint.json", 'r') as read_file:
                Sprites.white_patches_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading White Patches Tints")
            
    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def make_group(
        self,
        spritesheet,
        pos,
        name,
        sprites_x=None,
        sprites_y=None,
        no_index=False,
        palettes: list = None,
    ):  # pos = ex. (2, 3), no single pixels
        """
        Divide sprites on a spritesheet into groups of sprites that are easily accessible
        :param spritesheet: Name of spritesheet file
        :param pos: (x,y) tuple of offsets. NOT pixel offset, but offset of other sprites
        :param name: Name of group being made
        :param sprites_x: default 3, number of sprites horizontally
        :param sprites_y: default 7, number of sprites vertically
        :param no_index: default False, set True if sprite name does not require cat pose index:
        :param palettes: list of palette names
        """
        # pulls the defaults from the pose_sprite_data.json file
        if not sprites_x:
            sprites_x = self.sheet_layout[0]
        if not sprites_y:
            sprites_y = self.sheet_layout[1]

        group_x_ofs = pos[0] * sprites_x * self.size
        group_y_ofs = pos[1] * sprites_y * self.size
        i = 0

        # splitting group into singular sprites and storing into self.sprites section
        for y in range(sprites_y):
            for x in range(sprites_x):
                if no_index:
                    full_name = f"{name}"
                else:
                    full_name = f"{name}{i}"

                try:
                    new_sprite = pygame.Surface.subsurface(
                        self.spritesheets[spritesheet],
                        group_x_ofs + x * self.size,
                        group_y_ofs + y * self.size,
                        self.size,
                        self.size,
                    )

                except ValueError:
                    # Fallback for non-existent sprites
                    print(f"WARNING: nonexistent sprite - {full_name}")
                    if not self.blank_sprite:
                        self.blank_sprite = pygame.Surface(
                            (self.size, self.size), pygame.HWSURFACE | pygame.SRCALPHA
                        )
                    new_sprite = self.blank_sprite

                if palettes:
                    self.apply_palettes(i, name, new_sprite, palettes)
                else:
                    self.sprites[full_name] = new_sprite
                i += 1

    def apply_palettes(
        self, sprite_index: int, name: str, new_sprite, palette_names: list
    ):
        """
        Creates sprites for each color palette variation
        :param sprite_index: index of sprite
        :param name: name of sprite
        :param new_sprite: the sprite object to create variations of
        :param palette_names: list of palette names
        """
        # first we create an array of our palette map
        full_map = pygame.image.load(f"sprites/palettes/{name}_palette.png")
        map_array = pygame.PixelArray(full_map)
        # then create a dictionary associating the palette name with its row of the array
        color_palettes = {}
        palette_names = palette_names.copy()
        palette_names.insert(0, "BASE")
        for row in range(
            0, map_array.shape[1]  # pylint: disable=unsubscriptable-object
        ):
            color_name = palette_names[row]
            color_palettes.update(
                {color_name: [full_map.unmap_rgb(px) for px in map_array[::, row]]}
            )

        base_palette = color_palettes["BASE"]

        # now we recolor the sprite
        for color_name, palette in color_palettes.items():
            if color_name == "BASE":
                continue
            recolor_sprite = pygame.PixelArray(new_sprite.copy())
            # we replace each base_palette color with it's matching index from the color_palette
            for color_i, color in enumerate(palette):
                recolor_sprite.replace(base_palette[color_i], color)
            # convert back into a surface
            _sprite = recolor_sprite.make_surface()
            # add it to our sprite dict!
            self.sprites[f"{name}_{color_name}{sprite_index}"] = _sprite
            # close the pixel array now that we're done
            recolor_sprite.close()

        map_array.close()

    def load_all(self):
        # get the width and height of the spritesheet
        lineart = pygame.image.load('sprites/lineart.png')
        width, height = lineart.get_size()
        del lineart # unneeded

        # if anyone changes lineart for whatever reason update this
        if isinstance(self.size, int):
            pass
        elif width / 3 == height / 8:
            self.size = width / 3
        else:
            self.size = 50 # default, what base clangen uses
            print(f"lineart.png is not 3x7, falling back to {self.size}")
            print(f"if you are a modder, please update scripts/cat/sprites.py and do a search for 'if width / 3 == height / 7:'")

        del width, height # unneeded

        for x in [
            "lineart", "lineartdf", "lineartdead", "lineartur", 
            "line_sc_overlay", "line_ur_underlay", "line_ur_overlay",
            "gradient_ur",
            'whitepatches', 'tortiepatchesmasks', 
            'scars', 'missingscars',
            'medcatherbs', 'wild',
            'collars', 'bellcollars', 'bowcollars', 'nyloncollars',
            'shadersnewwhite', 'lightingnew', 
            'fademask', 'fadestarclan', 'fadedarkforest', "fadeunknownresidence",

        ]:
            self.spritesheet(f"sprites/{x}.png", x)

        for x in os.listdir("sprites/genemod/borders"):
            sprites.spritesheet("sprites/genemod/borders/"+x, 'genemod/'+x.replace('.png', ""))
        for x in os.listdir("sprites/genemod/Base Colours"):
            sprites.spritesheet("sprites/genemod/Base Colours/"+x, 'base/'+x.replace('.png', ""))
        for x in os.listdir("sprites/genemod/points"):
            sprites.spritesheet("sprites/genemod/points/"+x, x.replace('.png', ""))
        for x in os.listdir("sprites/genemod/New Tabbies"):
            sprites.spritesheet("sprites/genemod/New Tabbies/"+x, 'Tabby/'+x.replace('.png', ""))
        for x in os.listdir("sprites/genemod/extra"):
            sprites.spritesheet("sprites/genemod/extra/"+x, 'Other/'+x.replace('.png', ""))
        for x in os.listdir("sprites/genemod/effects"):
            sprites.spritesheet("sprites/genemod/effects/"+x, 'Other/'+x.replace('.png', ""))
        
        
        for x in os.listdir("sprites/genemod/white"):
            sprites.spritesheet("sprites/genemod/white/"+x, 'White/'+x.replace('.png', ""))
            self.make_group('White/'+x.replace('.png', ""), (0, 0), x.replace('.png', ""))
        for x in os.listdir("sprites/genemod/break white"):
            sprites.spritesheet("sprites/genemod/break white/"+x, 'Break/'+x.replace('.png', ""))
            self.make_group('Break/'+x.replace('.png', ""), (0, 0), 'break/'+x.replace('.png', ""))

        # ...idk what to call these

        self.make_group('genemod/normal border', (0, 0), 'normbord')
        self.make_group('genemod/foldborder', (0, 0), 'foldbord')
        self.make_group('genemod/curlborder', (0, 0), 'curlbord')
        self.make_group('genemod/foldlineart', (0, 0), 'foldlines')
        self.make_group('genemod/fold_curllineart', (0, 0), 'fold_curllines')
        self.make_group('genemod/curllineart', (0, 0), 'curllines')
        self.make_group('genemod/foldlineartdf', (0, 0), 'foldlineartdf')
        self.make_group('genemod/fold_curllineartdf', (0, 0), 'fold_curllineartdf')
        self.make_group('genemod/curllineartdf', (0, 0), 'curllineartdf')
        self.make_group('genemod/foldlineartdead', (0, 0), 'foldlineartdead')
        self.make_group('genemod/fold_curllineartdead', (0, 0), 'fold_curllineartdead')
        self.make_group('genemod/curllineartdead', (0, 0), 'curllineartdead')

        self.make_group('genemod/isolateears', (0, 0), 'isolateears', sprites_y=7)
        self.make_group('genemod/noears', (0, 0), 'noears', sprites_y=7)
        
        self.make_group('genemod/rexlines', (0, 0), 'rexlineart')
        self.make_group('genemod/rexlinesdead', (0, 0), 'rexlineartdead')
        self.make_group('genemod/rexlinesdf', (0, 0), 'rexlineartdf')
        self.make_group('genemod/rexborder', (0, 0), 'rexbord')

        for a, x in enumerate(range(1, 6)):
            self.make_group('genemod/bobtails', (a, 0), f'bobtail{x}')

        # genemod base colours

        for i, x in enumerate(["black", "chocolate", "cinnamon", 
                               "blue", "lilac", "fawn", 
                               "dove", "champagne", "buff", 
                               "platinum", "lavender", "beige"]):
            self.make_group('base/eumelanin', (0, i), f'{x}', sprites_x=7, sprites_y=1)
        for i, x in enumerate(["rufousedred", "mediumred", "lowred", 
                               "rufousedcream", "mediumcream", "lowcream", 
                               "rufousedhoney", "mediumhoney", "lowhoney", 
                               "rufousedivory", "mediumivory", "lowivory"]):
            self.make_group('base/pheomelanin', (0, i), f'{x}', sprites_x=7, sprites_y=1)
        self.make_group('base/lightbases', (0, 0), 'lightbasecolours', sprites_x=4, sprites_y=1)

        
        # genemod tabby bases

        for x in ["black", "blue", "pale_blue", "dove", "pale_dove", "platinum",
                  "chocolate", "lilac", "pale_lilac", "champagne", "lavender",
                  "cinnamon", "fawn", "pale_fawn", "buff", "beige",
                  "red", "cream", "honey", "ivory"]:
            for a, i in enumerate(['rufousedlow', 'rufousedmedium', 'rufousedhigh', 'rufousedshaded', 'rufousedchinchilla']):
                self.make_group('Tabby/'+x, (a, 0), f'{x}{i}', sprites_x=1, sprites_y=1)
            for a, i in enumerate(['mediumlow', 'mediummedium', 'mediumhigh', 'mediumshaded', 'mediumchinchilla']):
                self.make_group('Tabby/'+x, (a, 1), f'{x}{i}', sprites_x=1, sprites_y=1)
            for a, i in enumerate(['lowlow', 'lowmedium', 'lowhigh', 'lowshaded', 'lowchinchilla']):
                self.make_group('Tabby/'+x, (a, 2), f'{x}{i}', sprites_x=1, sprites_y=1)
            for a, i in enumerate(['silverlow', 'silvermedium', 'silverhigh', 'silvershaded', 'silverchinchilla']):
                self.make_group('Tabby/'+x, (a, 3), f'{x}{i}', sprites_x=1, sprites_y=1)
        for a, x in enumerate(['low', 'medium', 'high', 'shaded', 'chinchilla']):
            self.make_group('Tabby/shading', (a, 0), f'{x}shading')
        self.make_group('Tabby/unders', (0, 0), f'Tabby_unders')

        # genemod tabby patterns

        for a, i in enumerate(['mackerel', 'brokenmack', 'spotted', 'blotched', 'fullbar', 'fullbaralt']):
            self.make_group('Other/tabbypatterns', (a, 0), f'{i}')
        for a, i in enumerate(['braided', 'brokenbraid', 'rosetted', 'marbled', 'redbar', 'redbaralt']):
            self.make_group('Other/tabbypatterns', (a, 1), f'{i}')
        for a, i in enumerate(['pinstripe', 'brokenpins', 'servaline', 'blotchtail', 'agouti']):
            self.make_group('Other/tabbypatterns', (a, 2), f'{i}')
        for a, i in enumerate(['pinsbraided', 'brokenpinsbraid', 'leopard', 'blotchbar', 'pinsbar', 'charcoal']):
            self.make_group('Other/tabbypatterns', (a, 3), f'{i}')
        for a, i in enumerate(['macktail', 'bengtail', 'partialrosetted', 'sheeted', 'goldengradient', 'tabbypads']):
            self.make_group('Other/tabbypatterns', (a, 4), f'{i}')
        
        #genemod point markings

        self.make_group('points_spring', (0, 0), 'pointsm')
        self.make_group('points_summer', (0, 0), 'pointsl')
        self.make_group('points_winter', (0, 0), 'pointsd')
        self.make_group('mocha_spring', (0, 0), 'mocham')
        self.make_group('mocha_summer', (0, 0), 'mochal')
        self.make_group('mocha_winter', (0, 0), 'mochad')

        #genemod karpati
        for a, x in enumerate(['hetkarpatiwinter', 'hetkarpatispring', 'hetkarpatisummer']):
            self.make_group('Other/karpati', (a, 0), x)
        for a, x in enumerate(['homokarpatiwinter', 'homokarpatispring', 'homokarpatisummer']):
            self.make_group('Other/karpati', (a, 1), x)

        #genemod effects
        self.make_group('Other/bimetal', (0, 0), 'bimetal')
        self.make_group('Other/ghosting', (0, 0), 'ghost')
        self.make_group('Other/grizzle', (0, 0), 'grizzle')
        self.make_group('Other/bleach', (0, 0), 'bleach')
        self.make_group('Other/caramel', (0, 0), 'caramel', 1, 1)
        self.make_group('Other/satin', (0, 0), 'satin', 1, 1)
        self.make_group('Other/salmiak', (0, 0), 'salmiak')
        self.make_group('Other/nosebridge', (0, 0), 'rednose')
        self.make_group('Other/blue-tipped', (0, 0), 'BLUE-TIPPED')

        self.make_group('Other/lykoi', (0, 0), 'lykoi')
        self.make_group('Other/hairless', (0, 0), 'hairless')
        self.make_group('Other/donskoy', (0, 0), 'donskoy')
        self.make_group('Other/furpoint', (0, 0), 'furpoint')

        #genemod extra
        self.make_group('Other/ears', (0, 0), 'ears')
        self.make_group('Other/noses', (0, 0), 'nose')
        self.make_group('Other/nose_colours', (0, 0), 'nosecolours', sprites_y=5)
        self.make_group('Other/paw_pads', (0, 0), 'pads')

        #genemod eyes

        for i, x in enumerate(['left', 'right', 'sectoral1', 'sectoral2', 'sectoral3', 'sectoral4', 'sectoral5', 'sectoral6']):
            self.make_group('Other/eyebase', (i, 0), x, sprites_y=6)
        
        for i, x in enumerate(['outer', 'inner', 'pupil']):
            self.make_group('Other/eyesections', (i, 0), f"eye{x}", sprites_y=6)
        
        data_jsons = (
            self.WHITE_DATA,
            self.TORTIE_DATA,
            self.SCAR_DATA,
            self.SCAR_MISSING_PART_DATA,
            self.PLANT_DATA,
            self.WILD_DATA,
            self.COLLAR_DATA,
        )

        # data jsons that have multiple associated spritesheets
        multi_sheet_data = [
            x for x in data_jsons if isinstance(x["spritesheet"], (list, dict))
        ]

        # COMPILING SPRITESHEETS
        spritesheets = [
            "fademask",
            "fadestarclan",
            "fadedarkforest",
            "fadeunknownresidence",
            "symbols",
        ]

        # separate from data_json list bc we need to handle it differently later
        spritesheets.extend(self.POSE_DATA["spritesheet"])

        for data in data_jsons:
            if data in multi_sheet_data:
                spritesheets.extend(data["spritesheet"])
            else:
                spritesheets.append(data["spritesheet"])

        for x in spritesheets:
            self.spritesheet(f"sprites/{x}.png", x)

        # Line art
        for sheet in self.POSE_DATA["spritesheet"]:
            self.make_group(sheet, (0, 0), sheet)

        # Fading Fog
        for i in range(0, 3):
            self.make_group("fademask", (i, 0), f"fademask{i}")
            self.make_group("fadestarclan", (i, 0), f"fadestarclan{i}")
            self.make_group("fadedarkforest", (i, 0), f"fadedf{i}")
            self.make_group("fadeunknownresidence", (i, 0), f"fadeur{i}")

        for data in data_jsons:
            # collar accs
            # this guy is special since it uses palette mapping
            if data == self.COLLAR_DATA and self.COLLAR_DATA["palette_map"]:
                spritesheet = self.COLLAR_DATA["spritesheet"]
                for row, style_type in enumerate(self.COLLAR_DATA["style_data"]):
                    for col, style in enumerate(style_type):
                        self.make_group(
                            spritesheet=spritesheet,
                            pos=(col, row),
                            name=f"{spritesheet}{style}",
                            palettes=style_type[style],
                        )

            # these have multiple sprite sheets, so are handled differently from the others
            elif data in multi_sheet_data:
                for spritesheet in data["spritesheet"]:
                    self.load_sheet(spritesheet, data["sprite_list"])

            # everything else
            else:
                self.load_sheet(data["spritesheet"], data["sprite_list"])

    def load_sheet(self, spritesheet: str, sprite_names: list[list[str]]):
        """
        Loads sheet data and creates sprite groups.
        :param spritesheet: name of the spritesheet
        :param sprite_names: list containing lists of sprite names for this spritesheet, each list is a single row of the sheet
        """
        for row, sprite_names in enumerate(sprite_names):
            for col, sprite in enumerate(sprite_names):
                self.make_group(
                    spritesheet=spritesheet,
                    pos=(col, row),
                    name=f"{spritesheet if "patches" not in spritesheet else ""}{sprite}",
                )

           

# CREATE INSTANCE 
sprites = Sprites()
sprites.load_all()
