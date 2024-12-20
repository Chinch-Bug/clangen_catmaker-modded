import pygame
import pygame_gui
from bidict import bidict

# Start PyGame
pygame.init()
screen_x, screen_y = 800, 700
SCREEN = pygame.display.set_mode((screen_x, screen_y))
MANAGER = pygame_gui.ui_manager.UIManager((screen_x, screen_y), 'resources/defaults.json', enable_live_theme_updates=False)

MANAGER.get_theme().load_theme('resources/defaults.json')
MANAGER.get_theme().load_theme('resources/buttons.json')
MANAGER.get_theme().load_theme('resources/text_boxes.json')
MANAGER.get_theme().load_theme('resources/text_boxes.json')


import scripts.cat.cats

CREATED_CAT = scripts.cat.cats.Cat()


def sort_bidict(d: bidict, first_element=None):
    """Sorts Dictionary alphbetically. If None if in the dictionary, always have that first. """

    temp = bidict({})
    if first_element in d:
        temp[first_element] = d[first_element]
        del d[first_element]

    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    temp.update(sorted_dict)
    return temp


tabbies = bidict({"agouti" : "Agouti", "redbarc" : "Reduced Ticked (Classic)", "redbar" : "Reduced Ticked", "fullbarc" : "Ticked (Classic)", 
                  "fullbar" : "Ticked", "brokenpins" : "Broken Pinstripe", "pinstripe" : "Pinstripe", "servaline" : "Servaline", 
                  "brokenpinsbraid" : "Broken Pinstripe-Braided", "pinsbraided" : "Pinstripe-Braided", 
                  "leopard" : "Servaline-Rosseted", "classic" : "Blotched", "marbled" : "Marbled", "brokenmack" : "Broken Mackerel", 
                  "mackerel" : "Mackerel", "spotted" : "Spotted", "brokenbraid" : "Broken Braided", "braided" : "Braided", 
                  "rosetted" : "Rosetted"})
tabbies = sort_bidict(tabbies)

corin = bidict({"N": "None", "sh": "Sunshine", "sg": "Extreme Sunshine", "fg": "Flaxen Gold"})
extention = bidict({"E": "Normal", "ea": "Amber", "er": "Russet", "ec": "Carnelian",
                    "Eg": "Chausie Grizzle", 'ecc': 'Carnelian Carrier'})


white_patches = bidict({None: 'None', 'MAO': 'Mao', 'LUNA': 'Luna', 'CHESTSPECK': 'Chest Speck', 'WINGS': 'Wings',
                        'PAINTED': 'Painted', 'BLACKSTAR': 'Blackstar', 'LITTLE': 'Little', 'TUXEDO': 'Tuxedo',
                        'LIGHTTUXEDO': 'Light Tuxedo', 'BUZZARDFANG': 'Buzzardfang', 'TIP': 'Tip', 'BLAZE': 'Blaze',
                        'BIB': 'Bib', 'VEE': 'Vee', 'PAWS': 'Paws', 'BELLY': 'Belly', 'TAILTIP': 'Tail Tip',
                        'TOES': 'Toes', 'BROKENBLAZE': 'Broken Blaze', 'LILTWO': 'Lil Two', 'SCOURGE': 'Scourge',
                        'TOESTAIL': 'Toes Tail', 'RAVENPAW': 'Ravenpaw', 'HONEY': 'Honey', 'FANCY': 'Fancy',
                        'UNDERS': 'Unders', 'DAMIEN': 'Damien', 'SKUNK': 'Skunk', 'MITAINE': 'Mitaine',
                        'SQUEAKS': 'Squeaks', 'STAR': 'Star', 'ANY': 'Any', 'ANYTWO': 'Any Two', 'BROKEN': 'Broken',
                        'FRECKLES': 'Freckles', 'RINGTAIL': 'Ringtail', 'HALFFACE': 'Half Face', 'PANTSTWO': 'Pants 2',
                        'GOATEE': 'Goatee', 'PRINCE': 'Prince', 'FAROFA': 'Farofa', 'MISTER': 'Mister',
                        'PANTS': 'Pants', 'REVERSEPANTS': 'Reverse Pants', 'HALFWHITE': 'Half White',
                        'APPALOOSA': 'Appaloosa', 'PIEBALD': 'Piebald', 'CURVED': 'Curved', 'GLASS': 'Glass',
                        'MASKMANTLE': 'Mask Mantle', 'VAN': 'Van', 'ONEEAR': 'One Ear', 'LIGHTSONG': 'Lightsong',
                        'TAIL': 'Tail', 'HEART': 'Heart', 'HEARTTWO': 'Heart 2', 'MOORISH': 'Moorish', 'APRON': 'Apron',
                        'CAPSADDLE': 'Cap Saddle', 'FULLWHITE': 'Full White', "EXTRA": "Extra", 'PETAL': 'Petal',
                        "DIVA": "Diva", "SAVANNAH": "Savannah", "FADESPOTS": "Fadespots", "SHIBAINU": "Shiba Inu", 
                        "TOPCOVER": "Top Cover", "DAPPLEPAW": "Dapplepaw", "BEARD": "Beard", "PEBBLESHINE": "Pebbleshine", 
                        "OWL": "Owl", "WOODPECKER": "Woodpecker", "MISS": "Miss", "BOOTS": "Boots", "COW": "Cow", 
                        "COWTWO": "Cow 2", "BUB": "Bub", "BOWTIE": "Bowtie", "MUSTACHE" : "Mustache", "REVERSEHEART": "Reverse Heart", 
                        "SPARROW": "Sparrow", "VEST": "Vest", "LOVEBUG" : "Lovebug", "TRIXIE": "Trixie", "SPARKLE": "Sparkle", 
                        "RIGHTEAR" : "Right Ear", "LEFTEAR": "Left Ear", "ESTRELLA": "Estrella", "REVERSEEYE" : "Reverse Eye", 
                        "BACKSPOT": "Back spot", "EYEBAGS": "Eye Bags", "FADEBELLY": "Fade Belly", "SAMMY": "Sammy", "FRONT" : "Front", 
                        "BLOSSOMSTEP": "Blossomstep", "BULLSEYE": "Bullseye", "SHOOTINGSTAR" : "Shooting Star", "EYESPOT" : "Eye Spot", 
                        "PEBBLE": "Pebble", "TAILTWO": "Tail Two", "BUDDY": "Buddy", "FCONE": "FC One", "FCTWO": "FC Two", 
                        "MIA": "Mia", "DIGIT": "Digit", "SCAR": "Scar", "BUSTER": "Buster", "FINN": "Finn", "KROPKA": "Kropka", 
                        "HAWKBLAZE": "Hawkblaze", "LOCKET": "Locket", "PRINCESS": "Princess", "ROSINA" : "Rosina", "CAKE" : "Cake", "BLAZEMASK" : 'Blazemask', "TEARS" : "Tears", "DOUGIE" : 'Dougie'})
white_patches = sort_bidict(white_patches, None)
tortie_patches_shapes = bidict({"ONE": "One", "TWO": "Two", "THREE": "Three", "FOUR": "Four",  'REDTAIL': "Redtail",
                                'DELILAH': "Delilah", 'MINIMALONE': "Minimal 1", 'MINIMALTWO': "Minimal 2",
                                'MINIMALTHREE': "Minimal 3", 'MINIMALFOUR': "Minimal 4", 'OREO': "Oreo", 'SWOOP': "Swoop",
                                'MOTTLED': "Mottled", 'SIDEMASK': "Sidemask", 'EYEDOT': "Eye dot",
                                'BANDANA': "Bandana", 'PACMAN': "Pacman", 'STREAMSTRIKE': "Streamstrike",
                                'ORIOLE': "Oriole", 'ROBIN': "Robin", 'BRINDLE': "Brindle", 'PAIGE': "Paige", 
                                "ROSETAIL": "Rosetail", "SAFI": "Safi", "HALF": "Half", "CHIMERA": "Chimera", 
                                "SMUDGED": "Smudged", "DAUB": "Daub", "DAPPLENIGHT": "Dapplenight", "STREAK": "Streak", 
                                "MASK": "Mask", "CHEST": "Chest", "ARMTAIL": "Armtail", "EMBER": "Ember", "SMOKE": "Smoke", 
                                "GRUMPYFACE": "Grumpy Face", "BRIE": "Brie", "BELOVED": "Beloved", "SHILOH" : "Shiloh", 
                                "BODY" : "Body"})
tortie_patches_shapes = sort_bidict(tortie_patches_shapes)
tortie_patches_shapes.update(white_patches)

merle_patches_shapes = bidict({None: 'None', 'DELILAH' : "Delilah", 'MOTTLED' : "Mottled", 'EYEDOT' : "Eye dot", 'BANDANA' : "Bandana", 
                               'SMUDGED' : "Smudged", 'EMBER' : "Ember", 'BRINDLE' : "Brindle", 'SAFI' : "Safi", 'BELOVED' : "Beloved", 
                               'BODY' : "Body", 'SHILOH' : "Shiloh", 'FRECKLED' : "Freckled", "BACKSPOT" : "Backspot", "BEARD" : "Beard", 
                               "BELLY" : "Belly", "BIB" : "Bib", "revBLACKSTAR" : "Blackstar", "BLAZE" : "Blaze", "BLAZEMASK" : "Blaze mask", 
                               "revBOOTS" : "Boots", "revCHESTSPECK" : "Chest speck", "ESTRELLA" : "Estrelle", 'ONE' : "One", 'TWO' : "Two", 
                               'SMOKE' : "Smoke", 'MINIMALONE': "Minimal 1", 'MINIMALTWO': "Minimal 2", 'MINIMALTHREE': "Minimal 3", 
                               'MINIMALFOUR': "Minimal 4", 'OREO' : "Oreo", 'CHIMERA' : "Chimera", 'CHEST' : "Chest", 'GRUMPYFACE' : "Grumpyface", 
                               'SIDEMASK' : "Sidemask", 'PACMAN' : "Pacman", 'BRIE' : "Brie" ,'ORIOLE' : "Oriole", 'ROBIN' : "Robin", 
                               'PAIGE' : "Paige", 'HEARTBEAT' : "Heartbeat", "EYEBAGS" : "Eyebags", "revEYESPOT": "Eye spot", 
                               "revHEART": "Heart", "HONEY" : "Honey", "LEFTEAR": "Left ear", "LITTLE" : "Little", "PAWS" : "Paws", 
                               "REVERSEEYE" : "Reverse eye", "REVERSEHEART" : "Reverse heart", "RIGHTEAR" : "Right ear", "SCOURGE" : "Scourge", 
                               "SPARKLE" : "Sparkle", "revTAIL" : "Tail", 'revTAILTWO': "Tail 2", "TAILTIP": "Tailtip", "TEARS": "Tears", 
                               "TIP": "Tip", "TOES": "Toes", "TOESTAIL": "Toes & Tail", "VEE" : "Vee"})
merle_patches_shapes = sort_bidict(merle_patches_shapes)

eye_colors = bidict( {'YELLOW': "Yellow", 'AMBER': "Amber", 'HAZEL': "Hazel", 'PALEGREEN': "Pale Green",
                      'GREEN': "Green", 'BLUE': "Blue", 'DARKBLUE': "Dark Blue", 'GREY': "Grey", 'CYAN': "Cyan",
                      'EMERALD': "Emerald", 'PALEBLUE': "Pale Blue", 'PALEYELLOW': "Pale Yellow", 'GOLD': "Gold",
                      'HEATHERBLUE': "Heather Blue", 'SAGE': "Sage", 'COBALT': "Cobalt",
                      'SUNLITICE': "Sunlit Ice", "GREENYELLOW": "Green-Yellow", 'COPPER': 'Copper', 'BRONZE': 'Bronze',
                      'SILVER': 'Silver'})
eye_colors = sort_bidict(eye_colors)

tints = bidict({"none": "None", "pink": "Pink", "gray": "Gray", "red": "Red", "black": "Black", "orange": "Orange",
                "yellow": "Yellow", "purple": "Purple", "blue": "Blue"})
tints = sort_bidict(tints, 'none')

white_patches_tint = bidict({"none": "None", "darkcream": "Dark Cream", "cream": "Cream", "offwhite": "Blue",
                             "gray": "Gray", "pink": "Pink"})

skin_colors = bidict({'BLACK': "Black", 'RED': "Red", 'PINK': "Pink", 'DARKBROWN': "Dark Brown", 'BROWN': "Brown",
                      'LIGHTBROWN': "Light Brown", 'DARK': "Dark", 'DARKGREY': "Dark Gray", 'GREY': "Gray",
                      'DARKSALMON': "Dark Salmon", 'SALMON': 'Salmon', 'PEACH': 'Peach', 'DARKMARBLED': 'Dark Marbled',
                      'MARBLED': 'Marbled', 'LIGHTMARBLED': 'Light Marbled', 'DARKBLUE': 'Dark Blue', 'BLUE': 'Blue',
                      'LIGHTBLUE': 'Light Blue'})
skin_colors = sort_bidict(skin_colors)

colors = ['Black', 'Blue', 'Red', 'Cream', 'White', 'Albino', 'Chocolate', 'Lilac', 'Cinnamon', 'Fawn', 'Dove', 'Platinum', 
          'Honey', 'Ivory', 'Champagne', 'Lavender', 'Buff', 'Beige']

genemod_white = bidict({None: 'None',
                        'None1': '-Right Front Leg-',
                        'right front toes' : 'RF Toes', 'right front mitten' : 'RF Mitten', 'right front low sock' : 'RF Low Sock', 'right front high sock' : 'RF High Sock', 'right front bicolour1' : 'RF Bicolour1', 'right front bicolour2' : 'RF Bicolour2', 'break/right front mitten' : 'RF No Mitten', 'break/bracelet right' : 'RF Dark Band',
                        'None2' : '-Left Front Leg-',
                        'left front toes' : 'LF Toes', 'left front mitten' : 'LF Mitten', 'left front low sock' : 'LF Low Sock', 'left front high sock' : 'LF High Sock', 'left front bicolour1' : 'LF Bicolour1', 'left front bicolour2' : 'LF Bicolour2', 'break/left front mitten' : 'LF No Mitten', 'break/bracelet left' : 'LF Dark Band',
                        'None3' : '-Right Back Leg-',
                        'right back toes' : 'RB Toes', 'right back mitten' : 'RB Mitten', 'right back low sock' : 'RB Low Sock', 'right back high sock' : 'RB High Sock', 'right back bicolour1' : 'RB Bicolour1', 'right back bicolour2' : 'RB Bicolour2', 'break/right back mitten' : 'RB No Mitten',
                        'None4' : '-Left Back Leg-',
                        'left back toes' : 'LB Toes', 'left back mitten' : 'LB Mitten', 'left back low sock' : 'LB Low Sock', 'left back high sock' : 'LB High Sock', 'left back bicolour1' : 'LB Bicolour1', 'left back bicolour2' : 'LB Bicolour2', 'break/left back mitten' : 'LB No Mitten',
                        'None5' : '-Underbelly-',
                        'belly tuft' : 'Belly Tuft', 'chest tuft' : 'Chest Tuft', 'belly spot' : 'Belly Spot', 'locket' : 'Locket', 'belly' : 'Belly', 'bib' : 'Bib', 'chest' : 'Chest', 'beard' : 'Beard', 'underbelly1' : 'Underbelly', 'mask n mantle' : 'Underbelly2',
                        'None6' : '-Head-',
                        'chin' : 'White Chin', 'break/chin' : 'Dark Chin', 'mustache' : 'Mustache', 'muzzle': 'Muzzle', 'blaze' : 'Blaze', 'break/nose1' : 'Coloured Nose Patch', 'break/nose2' : 'Coloured Nose', 'break/left ear' : 'No Left Ear', 'break/right ear' : 'No Right Ear', 'break/left face' : 'No Left Mask', 'break/right face' : 'No Right Mask', 'break/bowl cut' : 'Head Patch',
                        'None7' : '-Dorsal-', 
                        'dorsal1': 'Thin Stripe', 'dorsal2' : 'Thick Stripe', 'break/inverse thai' : 'Coloured Stripe',
                        'None8' : '-Full-',
                        'van1' : 'Van 1', 'van2' : 'Van 2', 'van3' : 'Van 3', 'full white' : 'Full White', 'break/piebald1' : 'Piebald Patches 1', 'break/piebald2' : 'Piebald Patches 2', 'break/left no' : 'Left \'No\'', 'break/right no' : 'Right \'No\'', 
                        'None9' : '-Body-',
                        'belt' : 'White Belt', 'pants' : 'White Pants', 'break/pants' : 'Dark Pants',
                        'None10' : '-Tail-',
                        'tail tip' : 'Tail Tip', 'break/tail tip' : 'No Tail Tip', 'break/tail band': 'Colour Band', 'break/tail rings' : 'Colour Rings', 'thai tail' : 'Partial Tail'
                        })

points = ['Normal', 'Colourpoint', 'Mink', 'Sepia', 'Point-Albino', 'Sepia-Albino', 'Siamocha', 'Burmocha', 'Mocha', 'Mocha-Albino']

vit = bidict({None: 'None', 'VITILIGO': 'Vitiligo 1', 'VITILIGOTWO': 'Vitiligo 2',
              'MOON': 'Moon', 'PHANTOM': 'Phantom', 'POWDER': 'Powder', 'BLEACHED': 'Bleached', "SMOKEY": "Smokey"})
#vit = sort_bidict(vit, None)

scars = bidict({None: "None", "ONE": "Chest", "TWO": "Shoulder", "THREE": "Over Eye", "TAILSCAR": "Tail",
                "SNOUT": "Snout", "CHEEK": "Cheek",
                "SIDE": "Side", "THROAT": "Throat", "TAILBASE": "Tail Base", "BELLY": "Belly", "LEGBITE": "Bite: Leg",
                "NECKBITE": "Bite: Neck", "FACE": "Face", "MANLEG": "Mangled Leg", "BRIGHTHEART": "Mangled Face",
                "MANTAIL": "Mangled Tail", "BRIDGE": "Bridge", "RIGHTBLIND": "Right Eye Blind",
                "LEFTBLIND": "Left Eye Blind", "BOTHBLIND": "Both Eyes Blind", "BEAKCHEEK": "Beak: Cheek",
                "BEAKLOWER": "Beak: Lower", "CATBITE": "Cat Bite", "RATBITE": "Rat Bite", "QUILLCHUNK": "Quill Chunk",
                "QUILLSCRATCH": "Quill Scratch", "LEFTEAR": "Left Ear Notch", "RIGHTEAR": "Right Ear Notch",
                "NOLEFTEAR": "No Left Ear", "NORIGHTEAR": "No Right Ear", "NOEAR": "No Ears", "NOTAIL": "No Tail",
                "HALFTAIL": "Half Tail", "NOPAW": "Missing Leg",
                "SNAKE": "Bite: Snake", "TOETRAP": "Toe Trap", "BURNPAWS": "Burnt Paws", "BURNTAIL": "Burnt Tail",
                "BURNBELLY": "Burnt Belly", "BURNRUMP": "Burnt Rump", "FROSTFACE": "Frostbitten Face",
                "FROSTTAIL": "Frostbitten Tail", "FROSTMITT": "Frostbitten Paw1", "FROSTSOCK": "Frostbitten Paw2"})
scars = sort_bidict(scars, None)

accessories = bidict({None: "None", "MAPLE LEAF": "Maple Leaf", "HOLLY": "Holly", "BLUE BERRIES": "Blue Berries",
                      "FORGET ME NOTS": "Forget-me-nots", "RYE STALK": "Rye Stalk", "LAUREL": "Laurel",
                      "BLUEBELLS": "Bluebells", "NETTLE": "Nettle", "POPPY": "Poppy", "LAVENDER": "Lavender",
                      "HERBS": "Herbs", "PETALS": "Petals", "DRY HERBS": "Dry Herbs", "OAK LEAVES": "Oak Leaves",
                      "CATMINT": "Catmint", "MAPLE SEED": "Maple Seed", "JUNIPER": "Juniper",
                      "RED FEATHERS": "Red Feathers", "BLUE FEATHERS": "Blue Feathers", "JAY FEATHERS": "Jay Feathers",
                      "MOTH WINGS": "Moth Wings", "CICADA WINGS": "Cicada Wings", "CRIMSON": "Crimson Collar",
                      "BLUE": "Blue Collar", "YELLOW": "Yellow Collar", "CYAN": "Cyan Collar", "RED": "Red Collar",
                      "LIME": "Lime Collar", "GREEN": "Green Collar", "RAINBOW": "Rainbow Collar",
                      "BLACK": "Black Collar", "SPIKES": "Spiked Collar", "PINK": "Pink Collar",
                      "PURPLE": "Purple Collar", "MULTI": "Mulicolored Collar", "CRIMSONBELL": "Crimson Bell Collar",
                      "BLUEBELL": "Blue Bell Collar", "YELLOWBELL": "Yellow Bell Collar",
                      "CYANBELL": "Cyan Bell Collar", "REDBELL": "Red Bell Collar", "LIMEBELL": "Lime Bell Collar",
                      "GREENBELL": "Green Bell Collar", "RAINBOWBELL": "Rainbow Bell Color",
                      "BLACKBELL": "Black Bell Collar", "SPIKESBELL": "Spiked Bell Collar",
                      "PINKBELL": "Pine Bell Collar", "PURPLEBELL": "Purple Bell Collar",
                      "MULTIBELL": "Mulitcolored Bell Color", "CRIMSONBOW": "Crimson Bow", "BLUEBOW": "Blue Bow",
                      "YELLOWBOW": "Yellow Bow", "CYANBOW": "Cyan Bow", "REDBOW": "Red Bow", "LIMEBOW": "Lime Bow",
                      "GREENBOW": "Green Bow", "RAINBOWBOW": "Rainbow Bow", "BLACKBOW": "Black Bow",
                      "SPIKESBOW": "Spiked Bow", "PINKBOW": "Pink Bow", "PURPLEBOW": "Purple Bow",
                      "MULTIBOW": "Multicolored Bow", "WHITEBOW": "White Bow", "INDIGOBOW": "Indigo Bow",
                      "INDIGO": "Indigo Collar", "WHITE": "White Collar", "WHITEBELL": "White Bell Collar",
                      "INDIGOBELL": "Indigo Bell Collar", "CRIMSONNYLON": "Crimson Nylon Collar",
                      "BLUENYLON": "Blue Nylon Collar", "YELLOWNYLON": "Yellow Nylon Collar",
                      "CYANNYLON": "Cyan Nylon Collar", "REDNYLON": "Red Nylon Collar",
                      "LIMENYLON": "Line Nylon Collar", "GREENNYLON": "Green Nylon Collar",
                      "RAINBOWNYLON": "Rainbow Nylon Collar", "BLACKNYLON": "Black Nylon Collar",
                      "SPIKESNYLON": "Spiked Nylon Collar", "WHITENYLON": "White Nylon Collar",
                      "PINKNYLON": "Pink Nylon Collar", "PURPLENYLON": "Purple Nylon Collar",
                      "MULTINYLON": "Mulicolored Nylon Collar", "INDIGONYLON": "Indigo Nylon Collar"})
accessories = sort_bidict(accessories, None)

platforms = {"None": None,
             "Greenleaf Plains - Day": "resources/images/platforms/plains/greenleaf_light.png",
             "Leaf-fall Plains - Day": "resources/images/platforms/plains/leaffall_light.png",
             "Leaf-bare Plains - Day": "resources/images/platforms/plains/leafbare_light.png",
             "Newleaf Plains - Day": "resources/images/platforms/plains/newleaf_light.png",
             "Greenleaf Plains - Night": "resources/images/platforms/plains/greenleaf_dark.png",
             "Leaf-fall Plains - Night": "resources/images/platforms/plains/leaffall_dark.png",
             "Leaf-bare Plains - Night": "resources/images/platforms/plains/leafbare_dark.png",
             "Newleaf Plains - Night": "resources/images/platforms/plains/newleaf_dark.png",
             "Greenleaf Forest - Day": "resources/images/platforms/forest/greenleaf_light.png",
             "Leaf-fall Forest - Day": "resources/images/platforms/forest/leaffall_light.png",
             "Leaf-bare Forest - Day": "resources/images/platforms/forest/leafbare_light.png",
             "Newleaf Forest - Day": "resources/images/platforms/forest/newleaf_light.png",
             "Greenleaf Forest - Night": "resources/images/platforms/forest/greenleaf_dark.png",
             "Leaf-fall Forest - Night": "resources/images/platforms/forest/leaffall_dark.png",
             "Leaf-bare Forest - Night": "resources/images/platforms/forest/leafbare_dark.png",
             "Newleaf Forest - Night": "resources/images/platforms/forest/newleaf_dark.png",
             "Greenleaf Mountains - Day": "resources/images/platforms/mountainous/greenleaf_light.png",
             "Leaf-fall Mountains - Day": "resources/images/platforms/mountainous/leaffall_light.png",
             "Leaf-bare Mountains - Day": "resources/images/platforms/mountainous/leafbare_light.png",
             "Newleaf Mountains - Day": "resources/images/platforms/mountainous/newleaf_light.png",
             "Greenleaf Mountains - Night": "resources/images/platforms/mountainous/greenleaf_dark.png",
             "Leaf-fall Mountains - Night": "resources/images/platforms/mountainous/leaffall_dark.png",
             "Leaf-bare Mountains - Night": "resources/images/platforms/mountainous/leafbare_dark.png",
             "Newleaf Mountains - Night": "resources/images/platforms/mountainous/newleaf_dark.png",
             "Greenleaf Beach - Day": "resources/images/platforms/beach/greenleaf_light.png",
             "Leaf-fall Beach - Day": "resources/images/platforms/beach/leaffall_light.png",
             "Leaf-bare Beach - Day": "resources/images/platforms/beach/leafbare_light.png",
             "Newleaf Beach - Day": "resources/images/platforms/beach/newleaf_light.png",
             "Greenleaf Beach - Night": "resources/images/platforms/beach/greenleaf_dark.png",
             "Leaf-fall Beach - Night": "resources/images/platforms/beach/leaffall_dark.png",
             "Leaf-bare Beach - Night": "resources/images/platforms/beach/leafbare_dark.png",
             "Newleaf Beach - Night": "resources/images/platforms/beach/newleaf_dark.png",
             "Dark Forest - Light": "resources/images/platforms/darkforestplatform_light.png",
             "Dark Forest - Dark": "resources/images/platforms/darkforestplatform_dark.png",
             "StarClan": "resources/images/platforms/starclanplatform_dark.png"}

lineart = ["Normal", "StarClan", "Dark Forest"]

poses = {
    "short": {
        "newborn": {
            "1": 20,
            "2": 20,
            "3": 20
        },
        "kitten": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "adolescent": {
            "1": 3,
            "2": 4,
            "3": 5
        },
        "adult": {
            "1": 6,
            "2": 7,
            "3": 8
        },
        "senior": {
            "1": 12,
            "2": 13,
            "3": 14
        }
    },
    "hairless": {
        "newborn": {
            "1": 20,
            "2": 20,
            "3": 20
        },
        "kitten": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "adolescent": {
            "1": 3,
            "2": 4,
            "3": 5
        },
        "adult": {
            "1": 6,
            "2": 7,
            "3": 8
        },
        "senior": {
            "1": 12,
            "2": 13,
            "3": 14
        }
    },
    "long": {
        "newborn": {
            "1": 20,
            "2": 20,
            "3": 20
        },
        "kitten": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "adolescent": {
            "1": 3,
            "2": 4,
            "3": 5
        },
        "adult": {
            "1": 9,
            "2": 10,
            "3": 11
        },
        "senior": {
            "1": 12,
            "2": 13,
            "3": 14
        }
    }
}