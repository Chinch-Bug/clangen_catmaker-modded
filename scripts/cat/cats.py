from __future__ import annotations
from random import choice, randint, sample, shuffle
import os.path

from scripts.utility import *
from scripts.game_structure.game_essentials import *
from scripts.cat.pelts import Pelt
from .genotype import Genotype
from .phenotype import Phenotype


class Cat():

    def __init__(self):

        # Private attributes
        self._moons = 0
        
        # Public attributes

        self.age = "adult"
        self.pelt = Pelt()
        self.dead = False
        self.df = False
        self.shading = False
        self.cat_sprites = {
            "newborn": 20,
            "kitten": 0,
            "adolescent": 3,
            "adult": 8,
            "senior": 12,
        }
        self.platform = "None"

        # Used only for export
        self.ID = "2"
        self.gender = "female"
        self.gender_align = "female"
        self.status = "warrior"
        self.skill = "???"
        self.trait = "troublesome"
        self.backstory = "clan_founder"
        self.moons = 0
        self.season = 'Newleaf'
        self.genotype = Genotype()
        self.phenotype = Phenotype(self.genotype)
        self.chimpheno = Phenotype(self.genotype.chimerageno)

        # Sprite sizes
        self.sprite = None

    def randomize_looks(self, just_pattern=False):
        
        tortie_patches_shapes = {"ONE": "One", "TWO": "Two", "THREE": "Three", "FOUR": "Four",  'REDTAIL': "Redtail",
                                'DELILAH': "Delilah", 'MINIMALONE': "Minimal 1", 'MINIMALTWO': "Minimal 2",
                                'MINIMALTHREE': "Minimal 3", 'MINIMALFOUR': "Minimal 4", 'OREO': "Oreo", 'SWOOP': "Swoop",
                                'MOTTLED': "Mottled", 'SIDEMASK': "Sidemask", 'EYEDOT': "Eye dot",
                                'BANDANA': "Bandana", 'PACMAN': "Pacman", 'STREAMSTRIKE': "Streamstrike",
                                'ORIOLE': "Oriole", 'ROBIN': "Robin", 'BRINDLE': "Brindle", 'PAIGE': "Paige", 
                                "ROSETAIL": "Rosetail", "SAFI": "Safi", "HALF": "Half", "CHIMERA": "Chimera", 
                                "SMUDGED": "Smudged", "DAUB": "Daub", "DAPPLENIGHT": "Dapplenight", "STREAK": "Streak", 
                                "MASK": "Mask", "CHEST": "Chest", "ARMTAIL": "Armtail", "EMBER": "Ember", "SMOKE": "Smoke", 
                                "GRUMPYFACE": "Grumpy Face", "BRIE": "Brie", "BELOVED": "Beloved", "SHILOH" : "Shiloh", 
                                "BODY" : "Body"}
        self.age = random.choice(list(self.pelt.current_poses.keys()))
        length = choice(['Short', 'Long', 'Short Rexed', 'Long Rexed', 'Short', 'Long', 'Short Rexed', 'Long Rexed', 'Hairless', "Patchy Brush SH", "Patchy Brush LH", "Fur-point"])
        self.pelt.set_pelt_length(length)
        self.phenotype.SetFurLength(length.lower())

        

        self.phenotype.SetEarType(choice(['normal', 'folded', 'curled', 'folded curl']))
        self.phenotype.SetTailType(choice(['full', '3/4', '1/2', '1/3', 'stubby', 'none']))
        
        def SubRandomize(genotype, phenotype):
            phenotype.SetPoints(choice(['Normal', 'Colourpoint', 'Mink', 'Sepia', 'Point-Albino', 'Sepia-Albino', 'Siamocha', 'Burmocha', 'Mocha', 'Mocha-Albino']))
            genotype.tortiepattern = choice(list(tortie_patches_shapes.keys()))
            genotype.chimerapattern = choice(list(tortie_patches_shapes.keys()))
            if genotype.sexgene is not ['O', 'O']:
                genotype.sexgene = choice([['o', 'o'], ['o', 'o'], ['O', 'o']])
                if 'O' in genotype.sexgene:
                    phenotype.tortie = True
                else:
                    phenotype.tortie = False
            phenotype.SetBaseColour(choice(['Black', 'Blue', 'Red', 'Cream', 'White', 'Albino', 'Chocolate', 'Lilac', 'Cinnamon', 'Fawn', 'Dove', 'Platinum', 
            'Honey', 'Ivory', 'Champagne', 'Lavender', 'Buff', 'Beige']).lower())
            genotype.dilutemd[0] = choice(['dm', 'dm', 'dm', 'dm', 'dm', 'Dm'])
            genotype.bleach[0] = choice(['Lb', 'Lb', 'Lb', 'Lb', 'Lb', 'lb'])
            genotype.ghosting[0] = choice(['gh', 'gh', 'gh', 'gh', 'gh', 'Gh'])
            genotype.satin[0] = choice(['St', 'St', 'St', 'St', 'St', 'st'])
            genotype.brindledbi = (random.random() < 0.1)
            if (random.random() < 0.1 and genotype.tortiepattern):
                genotype.tortiepattern = 'rev' + genotype.tortiepattern
            elif genotype.tortiepattern:
                genotype.tortiepattern = genotype.tortiepattern.replace('rev', '')

            genotype.karp = choice([['k', 'k'], ['k', 'k'], ['k', 'k'], ['k', 'k'], ['k', 'k'], ['k', 'k'], ['K', 'k'], ['K', 'k'], ['K', 'k'], ['K', 'K']])
            if global_vars.CREATED_CAT.genotype.karp == ['k', 'k']:
                global_vars.CREATED_CAT.phenotype.fade = 'None'
            elif global_vars.CREATED_CAT.genotype.karp == ['K', 'k']:
                global_vars.CREATED_CAT.phenotype.fade = 'Heterozygous'
            else:
                global_vars.CREATED_CAT.phenotype.fade = 'Homozygous'


            phenotype.refone = 'R' + str(randint(1, 11))
            phenotype.refext = 'R' + str(randint(1, 11))
            phenotype.pigone = choice(['P11', 'P10', 'P9', 'P8', 'P7', 'P6', 'P5', 'P4', 'P3', 'P2', 'P1', 'blue'])
            phenotype.pigext = choice(['P11', 'P10', 'P9', 'P8', 'P7', 'P6', 'P5', 'P4', 'P3', 'P2', 'P1', 'blue'])

            if random.random() < 0.1:
                phenotype.reftwo = 'R' + str(randint(1, 11))
                phenotype.pigtwo = choice(['P11', 'P10', 'P9', 'P8', 'P7', 'P6', 'P5', 'P4', 'P3', 'P2', 'P1', 'blue'])
            else:
                phenotype.reftwo = phenotype.refone
                if random.random() < 0.25:
                    phenotype.pigtwo = 'blue'
                else:    
                    phenotype.pigtwo = phenotype.pigone
            phenotype.UpdateEyes()

            if random.random() < 0.1:
                genotype.extraeye = 'sectoral' + str(randint(1, 6))
            else:
                genotype.extraeye = None
            
            tabbies = {"agouti" : "Agouti", "redbarc" : "Reduced Ticked (Classic)", "redbar" : "Reduced Ticked", "fullbarc" : "Ticked (Classic)", 
                    "fullbar" : "Ticked", "brokenpins" : "Broken Pinstripe", "pinstripe" : "Pinstripe", "servaline" : "Servaline", 
                    "brokenpinsbraid" : "Broken Pinstripe-Braided", "pinsbraided" : "Pinstripe-Braided", 
                    "leopard" : "Servaline-Rosseted", "classic" : "Blotched", "marbled" : "Marbled", "brokenmack" : "Broken Mackerel", 
                    "mackerel" : "Mackerel", "spotted" : "Spotted", "brokenbraid" : "Broken Braided", "braided" : "Braided", 
                    "rosetted" : "Rosetted"}
            phenotype.SetTabbyPattern(choice(list(tabbies.keys())))

            phenotype.SetTabbyType(choice(['Solid', 'Solid', 'Solid', 'Agouti', 'Agouti', 'Agouti', 'Midnight Charcoal', 'Twilight Charcoal']))

            genotype.soktype = choice(['normal markings', 'normal markings', 'normal markings', 'normal markings','normal markings' , 'full sokoke', 'mild fading', 'mild fading'])

            genotype.silver[0] = choice(['I', 'i', 'i'])
            genotype.wbtype = choice(['low', 'medium', 'high', 'shaded', 'chinchilla'])
            genotype.ruftype = choice(['low', 'medium', 'rufoused'])

            genotype.ext[0] = choice(['E', 'E', 'E', 'E', choice(['Eg', 'ea', 'ea', 'er', 'ea', 'ec'])])
            genotype.sunshine[0] = choice(['N', 'N', 'N', 'N', choice(['sh', 'sh', 'sg', 'fg'])])

            maingame_white = {
                'low':{
                    '1': [None, 'SCOURGE', 'BLAZE', 'TAILTIP', 'TOES', 'LUNA', 'LOCKET'],
                    '2': ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'PAWS', 'BROKENBLAZE', 'BEARD', 'BIB', 'VEE', 'HONEY', 'TOESTAIL',
                        'RAVENPAW', 'DAPPLEPAW', 'LILTWO', 'MUSTACHE', 'REVERSEHEART', 'SPARKLE', 'REVERSEEYE'],
                    '3': ['TUXEDO', 'SAVANNAH', 'FANCY', 'DIVA', 'BEARD', 'DAMIEN', 'BELLY', 'SQUEAKS', 'STAR', 'WINGS', 'MISS', 'BOWTIE',
                        'FCTWO', 'FCONE', 'MIA', 'PRINCESS', 'DOUGIE'],
                    '4': ['TUXEDO', 'SAVANNAH', 'OWL', 'RINGTAIL', 'UNDERS', 'FAROFA', 'WINGS', 'VEST', 'FRONT', 'BLOSSOMSTEP', 'DIGIT',
                        'HAWKBLAZE'],
                    '5': ['ANY', 'SHIBAINU', 'FAROFA', 'MISTER', 'PANTS', 'TRIXIE']
                },
                'high':{
                    '1': ['ANY', 'SHIBAINU', 'PANTSTWO', 'MAO', 'TRIXIE'],
                    '2': ['ANY', 'FRECKLES', 'PANTSTWO', 'MASKMANTLE', 'MAO', 'PAINTED', 'BUB', 'SCAR'],
                    '3': ['ANYTWO', 'PEBBLESHINE', 'BROKEN', 'PIEBALD', 'FRECKLES', 'HALFFACE', 'GOATEE', 'PRINCE', 'CAPSADDLE', 
                        'REVERSEPANTS', 'GLASS', 'PAINTED', 'COWTWO', 'SAMMY', 'FINN', 'BUSTER', 'CAKE'],
                    '4': ['VAN', 'PEBBLESHINE', 'LIGHTSONG', 'CURVED', 'GOATEE', 'TAIL', 'APRON', 'HALFWHITE', 'APPALOOSA', 'HEART',
                        'MOORISH', 'COW', 'SHOOTINGSTAR', 'PEBBLE', 'TAILTWO', 'BUDDY', 'KROPKA'],
                    '5': ['ONEEAR', 'LIGHTSONG', 'BLACKSTAR', 'PETAL', 'CHESTSPECK', 'HEARTTWO', 'BOOTS', 'SHOOTINGSTAR', 'EYESPOT', 
                        'KROPKA']
                }
            }

            vitiligo = ['MOON', 'PHANTOM', 'POWDER', 'BLEACHED', 'VITILIGO', 'VITILIGOTWO', 'SMOKEY']
            genotype.vitiligo = choice([True, False, False, False, False, False, False, False])

            #white patterns

            if genotype.white[0] != 'W':
                for i in range(2):

                    if randint(1, 25) == 1:
                        genotype.white[i] = "wg"
                    elif randint(1, 25) == 1:
                        genotype.white[i] = "wt"
                    elif randint(1, 2) == 1:
                        genotype.white[i] = "ws"
                    else:
                        genotype.white[i] = "w"
                
                if genotype.white[0] == "wg":
                    genotype.white[0] = genotype.white[1]
                    genotype.white[1] = "wg"
                elif genotype.white[0] == "w" and genotype.white[1] != "wg":
                    genotype.white[0] = genotype.white[1]
                    genotype.white[1] = "w"
                elif genotype.white[0] == "wt" and genotype.white[1] != "wg" and genotype.white[1] != "w":
                    genotype.white[0] = genotype.white[1]
                    genotype.white[1] = "wt"

            white_pattern = None
            
            def GenerateWhite(KIT, KITgrade, vit, white_pattern):
                def clean_white():
                    while None in white_pattern:
                        white_pattern.remove(None)

                if white_pattern is None and (KIT[0] != "W" and KIT[0] != "w"):
                    white_pattern = []
                    if(vit):
                        white_pattern.append(choice(vitiligo))
                    if "wt" in KIT:
                        if KIT[1] not in ['ws', 'wt'] and KITgrade < 3:
                            white_pattern.append("dorsal1")
                        elif KIT[1] not in ['ws', 'wt'] and KITgrade < 5:
                            white_pattern.append(choice(["dorsal1", "dorsal2"]))
                        else:
                            white_pattern.append("dorsal2")
                    
                    if KIT[0] == "wg":
                        for mark in ["left front mitten", "left back mitten", "right front mitten", "right back mitten"]:
                            white_pattern.append(mark)
                    elif KIT[0] in ["ws", "wt"] and KIT[1] not in ["ws", "wt"]:
                        
                        if(randint(1, 4) == 1):
                            white_pattern.append(choice(maingame_white["low"].get(str(KITgrade))))
                            clean_white()

                        elif KITgrade == 1:
                            grade1list = ['chest tuft', 'belly tuft', 'chest tuft', 'belly tuft', None]
                            white_pattern.append(choice(grade1list))
                            clean_white()
                        elif KITgrade == 2:
                            while len(white_pattern) == 0:
                                #chest
                                white_pattern.append(choice(['chest tuft', 'locket', None, 'chest tuft', 'locket', None, 'bib']))
                                #belly
                                white_pattern.append(choice(['belly tuft', 'belly spot', None, 'belly tuft', 'belly spot', None, 'belly']))

                                #toes
                                nropaws = choice([4, 3, 2, 1, 0, 0])
                                order = ['right front', 'left front', 'right back', 'left back']
                                shuffle(order)

                                for i in range(nropaws):
                                    white_pattern.append(order[i] + choice([' toes', ' toes', ' toes', ' mitten']))
                            clean_white()
                        elif KITgrade == 3:
                            while len(white_pattern) < 4:
                                #chest
                                white_pattern.append(choice(['chest', 'beard', 'chest', 'bib', None]))

                                #belly
                                white_pattern.append(choice(['belly spot', 'belly', 'belly spot', 'belly', 'belly spot', 'belly', None]))

                                #paws
                                nropaws = choice([4, 4, 3, 2, 1, 0])
                                order = ['right front', 'left front', 'right back', 'left back']
                                shuffle(order)
                                pawtype = choice(['same', 'mixed'])

                                for i in range(nropaws):
                                    if pawtype == 'same':
                                        pawtype = choice([' toes', ' mitten', ' mitten', ' mitten', ' low sock'])
                                        white_pattern.append(order[i] + pawtype)
                                    else:
                                        white_pattern.append(order[i] + choice([' toes', ' mitten', ' mitten', ' low sock']))

                                #face
                                if 'beard' in white_pattern:
                                    white_pattern.append(choice(['chin', 'mustache', 'chin', 'chin', None, None, None, None]))

                                #tail
                                white_pattern.append(choice(['tail tip', None, None, None, None]))
                                white_pattern.append(choice([None, None, None, 'break/nose1']))

                                clean_white()
                        elif KITgrade == 4:
                            while len(white_pattern) < 4:
                                #chest
                                white_pattern.append(choice(['underbelly1', 'beard', 'chest', 'underbelly1']))

                                #belly
                                if 'underbelly1' not in white_pattern:
                                    white_pattern.append('belly')

                                #paws
                                nropaws = choice([4, 4, 4, 4, 3, 3, 2, 2, 1, 0])
                                order = ['right front', 'left front', 'right back', 'left back']
                                shuffle(order)
                                pawtype = choice(['same', 'mixed'])

                                for i in range(nropaws):
                                    if pawtype == 'same':
                                        pawtype = choice([' mitten', ' low sock', ' low sock', ' high sock'])
                                        white_pattern.append(order[i] + pawtype)
                                    else:
                                        white_pattern.append(order[i] + choice([' mitten', ' low sock', ' high sock']))

                                #face
                                if 'beard' or 'underbelly1' in white_pattern:
                                    white_pattern.append(choice(['chin', 'chin', 'muzzle', 'muzzle', 'blaze', None, None]))

                                #tail
                                white_pattern.append(choice(['tail tip', None, None, None, None]))
                                white_pattern.append(choice([None, None, None, 'break/nose1']))

                                clean_white()
                        else:
                            while len(white_pattern) < 4:
                                #chest
                                white_pattern.append('underbelly1')

                                #paws
                                nropaws = 4
                                order = ['right front', 'left front', 'right back', 'left back']
                                shuffle(order)
                                pawtype = choice(['same', 'mixed'])

                                for i in range(nropaws):
                                    if pawtype == 'same':
                                        pawtype = choice([' high sock', ' bicolour1', ' bicolour1', ' bicolour2'])
                                        white_pattern.append(order[i] + pawtype)
                                    else:
                                        white_pattern.append(order[i] + choice([' high sock', ' bicolour1', ' bicolour1', ' bicolour2']))

                                #face
                                white_pattern.append(choice(['chin', 'muzzle', 'muzzle', 'muzzle', 'blaze']))

                                #tail
                                white_pattern.append(choice(['tail tip', None, None, None, None]))
                                white_pattern.append(choice([None, None, None, 'break/nose1']))

                                clean_white()
                    else:
                        
                        if(randint(1, 4) == 1):
                            white_pattern.append(choice(maingame_white["high"].get(str(KITgrade))))

                        elif KITgrade == 1:
                            while len(white_pattern) < 4:
                                #chest
                                white_pattern.append('underbelly1')

                                #paws
                                nropaws = 4
                                order = ['right front', 'left front', 'right back', 'left back']
                                shuffle(order)
                                pawtype = choice(['same', 'mixed'])

                                for i in range(nropaws):
                                    if pawtype == 'same':
                                        pawtype = choice([' bicolour1', ' bicolour2', ' bicolour2'])
                                        white_pattern.append(order[i] + pawtype)
                                    else:
                                        white_pattern.append(order[i] + choice([' bicolour1', ' bicolour2', ' bicolour2']))

                                #face
                                white_pattern.append(choice(['chin', 'muzzle', 'muzzle', 'muzzle', 'blaze', 'blaze']))

                                #tail
                                white_pattern.append(choice(['tail tip', None, None, None, None]))
                                white_pattern.append(choice([None, None, None, 'break/nose1']))

                                clean_white()
                        elif KITgrade == 2:
                            #chest
                            white_pattern.append(choice(['underbelly1', 'mask n mantle']))

                            #paws
                            nropaws = 4
                            order = ['right front', 'left front', 'right back', 'left back']
                            shuffle(order)
                            pawtype = choice(['same', 'mixed'])

                            for i in range(nropaws):
                                white_pattern.append(order[i] + ' bicolour2')

                            #face
                            white_pattern.append(choice(['muzzle', 'muzzle', 'blaze', 'blaze']))

                            #tail
                            white_pattern.append(choice(['tail tip', None, None, None, None]))
                            white_pattern.append(choice([None, None, None, 'break/nose1']))
                            clean_white()
                        elif KITgrade == 3:
                            white_pattern.append(choice(['van1', 'van2', 'van3', 'van1', 'van2', 'van3', 'full white']))
                            white_pattern.append(choice(['break/piebald1', 'break/piebald2']))
                            white_pattern.append(choice([None, 'break/left ear', 'break/right ear', 'break/tail tip', 'break/tail band', 'break/tail rings', 'break/left face', 'break/right face']))
                            clean_white()
                        elif KITgrade == 4:
                            white_pattern.append(choice(['van1', 'van2', 'van3']))
                            white_pattern.append(choice([None, None, choice(['break/left ear', 'break/right ear', 'break/tail tip', 'break/tail band', 'break/left face', 'break/right face'])]))
                            white_pattern.append(choice([None, None, None, None, None, choice(['break/left ear', 'break/right ear', 'break/tail tip', 'break/tail band', 'break/left face', 'break/right face'])]))

                            clean_white()
                        else:
                            white_pattern.append(choice(["full white", 'van3']))

                            white_pattern.append(choice([None, 'break/left ear', 'break/right ear', 'break/tail tip', 'break/tail band', 'break/left face', 'break/right face']))
                            white_pattern.append(choice([None, choice(['break/left ear', 'break/right ear', 'break/tail tip', 'break/tail band', 'break/left face', 'break/right face'])]))

                            clean_white()
                    
                elif white_pattern is None and vit:
                    white_pattern = [choice(vitiligo)]
                else:
                    white_pattern = []
                return white_pattern

            genotype.white_pattern = GenerateWhite(genotype.white, genotype.whitegrade, genotype.vitiligo, white_pattern)
            if len(genotype.white_pattern) == 0:
                genotype.white_pattern = [None]
            elif genotype.white_pattern[0] not in vitiligo:
                genotype.white_pattern = [None] + genotype.white_pattern

        SubRandomize(self.genotype, self.phenotype)
        SubRandomize(self.genotype.chimerageno, self.chimpheno)
        if random.random() < 0.1:
            self.genotype.chimera = True
        else:
            self.genotype.chimera = False

    def generate_large_image(self):
        return

    def generate_save_file(self):
        """Generates a basic save file dictionary with all the looks-based info filled in. """
        pelt_name = self.pelt.name
        if pelt_name == "SingleColour" and self.white_patches:
            pelt_name = "TwoColour"
        if pelt_name == "Tortie" and self.white_patches:
            pelt_name = "Calico"

        save = {
            "ID": self.ID,
            "name_prefix": "Prefix",
            "name_suffix": "Suffix",
            "gender": self.gender,
            "gender_align": self.gender_align,
            "birth_cooldown": 0,
            "status": self.status,
            "backstory": self.backstory,
            "age": self.age,
            "moons": self.moons,
            "trait": "wise",
            "parent1": None,
            "parent2": None,
            "mentor": None,
            "former_mentor": [],
            "patrol_with_mentor": 0,
            "mentor_influence": [],
            "mate": None,
            "dead": False,
            "died_by": [],
            "paralyzed": self.paralyzed,
            "no_kits": False,
            "exiled": False,
            "pelt_name": pelt_name,
            "pelt_color": self.pelt.colour,
            "pelt_white": bool(self.white_patches),
            "pelt_length": self.pelt.length,
            "spirit_kitten": self.age_sprites["kitten"],
            "spirit_adolescent": self.age_sprites["adolescent"],
            "spirit_young_adult": self.age_sprites["adult"],
            "spirit_adult": self.age_sprites["adult"],
            "spirit_senior_adult": self.age_sprites["adult"],
            "spirit_elder": self.age_sprites["elder"],
            "spirit_dead": None,
            "eye_colour": self.eye_colour,
            "eye_colour2": self.eye_colour2,
            "reverse": self.reverse,
            "white_patches": self.white_patches,
            "vitiligo": self.vitiligo,
            "points": self.points,
            "white_patches_tint": self.white_patches_tint,
            "pattern": self.pattern if self.pelt.name == "Tortie" else None,
            "tortie_base": self.tortiebase if self.pelt.name == "Tortie" else None,
            "tortie_color": self.tortiecolour if self.pelt.name == "Tortie" else None,
            "tortie_pattern": self.tortiepattern if self.pelt.name == "Tortie" else None,
            "skin": self.skin,
            "tint": self.tint,
            "skill": self.skill,
            "scars": [x for x in self.scar_slot_list if x],
            "accessory": self.accessory,
            "experience": 0,
            "dead_moons": 0,
            "current_apprentice": [],
            "former_apprentices": [],
            "possible_scar": None,
            "scar_event": [],
            "df": False,
            "outside": False,
            "corruption": 0,
            "life_givers": [],
            "known_life_givers": [],
            "virtues": [],
            "retired": False,
            "faded_offspring": [],
            "opacity": 100,
            "prevent_fading": False
        }

        return save

# ---------------------------------------------------------------------------- #
#                               END OF CAT CLASS                               #
# ---------------------------------------------------------------------------- #
