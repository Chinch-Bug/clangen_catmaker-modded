from __future__ import annotations
import os.path

from scripts.utility import *
from scripts.game_structure.game_essentials import *
from scripts.cat.pelts import Pelt
from .phenotype import Phenotype
from scripts.cat.sprites import sprites
from random import choice, randint, sample, shuffle, random


class Cat():

    def __init__(self):

        # Private attributes
        self._moons = 0
        
        # Public attributes

        self.age = "adult"
        self.pelt = Pelt()
        self.dead = False
        self.df = False
        self.ur = False
        self.shading = False
        self.cat_sprites = {
            "newborn": 0,
            "kitten": 3,
            "adolescent": 6,
            "adult": 11,
            "senior": 15,
        }
        self.platform = "None"
        self.permanent_condition = []

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
        self.phenotype = Phenotype()
        self.chimerapheno = Phenotype()

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
        self.age = choice(list(self.pelt.current_poses.keys()))
        length = choice(['Short', 'Long', 'Short Rexed', 'Long Rexed', 'Short', 'Long', 'Short Rexed', 'Long Rexed', 'Hairless', "Patchy Brush SH", "Patchy Brush LH", "Fur-point"])
        self.pelt.set_pelt_length(length)
        self.phenotype.SetFurLength(length.lower())

        

        self.phenotype.SetEarType(choice(['normal', 'folded', 'curled', 'folded curl']))
        self.phenotype.SetTailType(choice(['full', '3/4', '1/2', '1/3', 'stubby', 'none']))
        
        def SubRandomize(phenotype):
            phenotype.SetPoints(choice(['Normal', 'Colourpoint', 'Mink', 'Sepia', 'Point-Albino', 'Sepia-Albino', 'Siamocha', 'Burmocha', 'Mocha', 'Mocha-Albino']))
            phenotype.chimerapattern = choice(list(tortie_patches_shapes.keys()))
            if phenotype.sexgene is not ['O', 'O']:
                phenotype.sexgene = choice([['o', 'o'], ['o', 'o'], ['O', 'o']])
                if 'O' in phenotype.sexgene:
                    phenotype.tortie = True
                else:
                    phenotype.tortie = False
            phenotype.SetBaseColour(choice(['Black', 'Blue', 'Red', 'Cream', 'White', 'Albino', 'Chocolate', 'Lilac', 'Cinnamon', 'Fawn', 'Dove', 'Platinum', 
            'Honey', 'Ivory', 'Champagne', 'Lavender', 'Buff', 'Beige']).lower())

            if random() < 0.1:
                phenotype.specialred = choice(['cameo', 'cameo', 'cameo', 'cameo', 'cameo', 'cameo', 'cameo', 'pseudo-cinnamon', 'blue-red', 'blue-tipped', 'blue-tipped'])
            else:
                phenotype.specialred = "none"

            phenotype.dilutemd[0] = choice(['dm', 'dm', 'dm', 'dm', 'dm', 'Dm'])
            phenotype.bleach[0] = choice(['Lb', 'Lb', 'Lb', 'Lb', 'Lb', 'lb'])
            phenotype.ghosting[0] = choice(['gh', 'gh', 'gh', 'gh', 'gh', 'Gh'])
            phenotype.satin[0] = choice(['St', 'St', 'St', 'St', 'St', 'st'])

            phenotype.karp = choice([['k', 'k'], ['k', 'k'], ['k', 'k'], ['k', 'k'], ['k', 'k'], ['k', 'k'], ['K', 'k'], ['K', 'k'], ['K', 'k'], ['K', 'K']])
            if global_vars.CREATED_CAT.phenotype.karp == ['k', 'k']:
                global_vars.CREATED_CAT.phenotype.fade = 'None'
            elif global_vars.CREATED_CAT.phenotype.karp == ['K', 'k']:
                global_vars.CREATED_CAT.phenotype.fade = 'Heterozygous'
            else:
                global_vars.CREATED_CAT.phenotype.fade = 'Homozygous'

            phenotype.fur_shade = choice([0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6])

            phenotype.refone = 'R' + str(randint(1, 11))
            phenotype.refext = 'R' + str(randint(1, 11))
            phenotype.pigone = choice(['P11', 'P10', 'P9', 'P8', 'P7', 'P6', 'P5', 'P4', 'P3', 'P2', 'P1', 'blue'])
            phenotype.pigext = choice(['P11', 'P10', 'P9', 'P8', 'P7', 'P6', 'P5', 'P4', 'P3', 'P2', 'P1', 'blue'])

            if random() < 0.1:
                phenotype.reftwo = 'R' + str(randint(1, 11))
                phenotype.pigtwo = choice(['P11', 'P10', 'P9', 'P8', 'P7', 'P6', 'P5', 'P4', 'P3', 'P2', 'P1', 'blue'])
            else:
                phenotype.reftwo = phenotype.refone
                if random() < 0.25:
                    phenotype.pigtwo = 'blue'
                else:    
                    phenotype.pigtwo = phenotype.pigone
            phenotype.UpdateEyes()

            if random() < 0.1:
                phenotype.extraeye = 'sectoral' + str(randint(1, 6))
            else:
                phenotype.extraeye = None
            
            tabbies = {"agouti" : "Agouti", "redbarc" : "Reduced Ticked (Blotched)", "redbar" : "Reduced Ticked", "fullbarc" : "Ticked (Blotched)", 
                  "fullbar" : "Ticked", "broken pinstripe" : "Broken Pinstripe", "pinstripe" : "Pinstripe", "servaline" : "Servaline", 
                  "broken pinstripe braided" : "Broken Pinstripe-Braided", "pinstripe braided" : "Pinstripe-Braided", 
                  "leopard" : "Servaline-Rosseted", "blotched" : "Blotched", "marbled" : "Marbled", "broken mackerel" : "Broken Mackerel", 
                  "mackerel" : "Mackerel", "spotted" : "Spotted", "brokenbraid" : "Broken Braided", "braided" : "Braided", 
                  "rosetted" : "Rosetted", "partial braided": "Partial Braided", "partial broken braided": "Partial Broken Braided", 
                  "partial rosetted": "Partial Rosettes", "partial marble": "Partial Marbled", "sheetmarble": "Sheet Marble", 
                  "sheetblotched": "Dense Blotched"}
            phenotype.SetTabbyPattern(choice(list(tabbies.keys())))

            phenotype.SetTabbyType(choice(['Solid', 'Solid', 'Solid', 'Agouti', 'Agouti', 'Agouti', 'Midnight Charcoal', 'Twilight Charcoal']))

            phenotype.soktype = choice(['normal markings', 'normal markings', 'normal markings', 'normal markings','normal markings' , 'full sokoke', 'mild fading', 'mild fading'])

            phenotype.fevercoat = random() < 0.1
            phenotype.silver[0] = choice(['I', 'i', 'i'])
            if phenotype.silver[0] == 'I':
                phenotype.pseudomerle = random() < 0.1
            else:
                phenotype.pseudomerle = False
            phenotype.wideband = choice(list(range(16)))
            phenotype.rufousing = choice(list(range(9)))
            phenotype.poly_eval()

            phenotype.ext[0] = choice(['E', 'E', 'E', 'E', choice(['Eg', 'ea', 'ea', 'er', 'ea', 'ec'])])
            phenotype.corin[0] = choice(['N', 'N', 'N', 'N', choice(['sh', 'sh', 'sg', 'fg'])])

            vitiligo = ['MOON', 'PHANTOM', 'POWDER', 'BLEACHED', 'VITILIGO', 'VITILIGOTWO', 'SMOKEY']
            phenotype.vitiligo = choice([True, False, False, False, False, False, False, False])
            self.pelt.rusting = {choice(sprites.rusting_sprites): randint(1, 5)*5} if random() < 0.25 else None

            #white patterns

            if phenotype.white[0] != 'W':
                for i in range(2):

                    if randint(1, 25) == 1:
                        phenotype.white[i] = "wg"
                    elif randint(1, 25) == 1:
                        phenotype.white[i] = "wt"
                    elif randint(1, 2) == 1:
                        phenotype.white[i] = "ws"
                    else:
                        phenotype.white[i] = "w"
                
                if phenotype.white[0] == "wg":
                    phenotype.white[0] = phenotype.white[1]
                    phenotype.white[1] = "wg"
                elif phenotype.white[0] == "w" and phenotype.white[1] != "wg":
                    phenotype.white[0] = phenotype.white[1]
                    phenotype.white[1] = "w"
                elif phenotype.white[0] == "wt" and phenotype.white[1] != "wg" and phenotype.white[1] != "w":
                    phenotype.white[0] = phenotype.white[1]
                    phenotype.white[1] = "wt"

            white_pattern = None
            
            def GenerateWhite(KIT, KITgrade, vit, white_pattern):
                pax3 = ["NoDBE", "NoDBE"]
                def clean_white(white_pattern):
                    white_pattern = list(set(white_pattern))
                    while None in white_pattern:
                        white_pattern.remove(None)
                    return white_pattern

                if white_pattern is None and (KIT[0] != "W" and KIT[0] != "w"):
                    white_pattern = []
                    if 'wt' in KIT:
                        if KIT[1] not in ['ws', 'wt'] and KITgrade < 3:
                            white_pattern.append(choice(["dorsal1", "STRIPE_SMALL"]))
                        elif KIT[1] not in ['ws', 'wt'] and KITgrade < 5:
                            white_pattern.append(choice(["dorsal1", "STRIPE_SMALL", "dorsal2"]))
                        else:
                            white_pattern.append(choice(["dorsal2", "STRIPE_SMALL", "STRIPE_MID"]))
                        white_pattern.append("thai tail")
                    
                    if KIT[0] == "wg":
                        if random() < 0.33:
                            white_pattern.append("PAWS")
                        else:
                            white_pattern.extend(["left front mitten", "left back mitten", "right front mitten", "right back mitten"])
                    elif (KIT[0] in ["ws", "wt"] or pax3[0] != 'NoDBE') and KIT[1] not in ["ws", "wt"] and 'NoDBE' in pax3:
                        if not KIT[0] in ["ws", "wt"]:
                            if 'DBEre' in pax3[0]:
                                KITgrade = min(KITgrade, 3)
                            else:
                                KITgrade = randint(1, 2)

                        if(randint(1, 4) == 1):
                            white_pattern.append(choice(Pelt.maingame_white["low"].get(str(KITgrade))))

                        elif KITgrade == 1:
                            if random () < 0.95:
                                white_pattern.append(choice(['chest tuft', 'belly tuft', 'belly tuft', 'belly tuft', "CHEST_MIN", "LOCKET"]))
                            
                        elif KITgrade == 2:
                            while len(white_pattern) == 0:
                                #chest
                                if random () < 0.5:
                                    white_pattern.append(choice(['chest tuft', 'locket', 'chest tuft', 'locket', 'bib', "BIB_SMALL", "CHEST_MIN", "CHEST_SMALL", "LOCKET", "CHEST_STREAK", "NECKBEARD"]))
                                #belly
                                elif random () < 0.5:
                                    white_pattern.append(choice(['belly tuft', 'belly spot', 'belly tuft', 'belly spot', 'belly', "BELLY_SMALL", "BELLY_MIN"]))

                                #toes
                                nropaws = choice([4, 3, 2, 1, 0, 0])
                                order = ['right front', 'left front', 'right back', 'left back']
                                shuffle(order)

                                for i in range(nropaws):
                                    white_pattern.append(order[i] + choice([' toes', ' toes', ' toes', ' mitten']))
                        elif KITgrade == 3:
                            while len(white_pattern) < 4:
                                #chest
                                if random () < 0.8:
                                    white_pattern.append(choice(['chest', 'chest', 'beard', 'chest', 'bib', 
                                    "BIB", "CHEST_BROKEN", "CHEST_MID", "DAMIEN_REDUCED", "NECKBEARD"]))

                                # belly
                                if random() < 0.8:
                                    white_pattern.append(choice(['belly spot', 'belly', 'belly spot', 'belly', 'belly spot', 'BELLY_SMALL', "BELLY_MIN"]))

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
                                if 'beard' in white_pattern or "NECKBEARD" in white_pattern:
                                    if random() < 0.5:
                                        white_pattern.append(choice(['chin', 'mustache', "MUSTACHE", "MUZZLE", 'chin', 'BEARD_SMALL']))

                                #tail
                                if random() < 0.2:
                                    white_pattern.append(choice(['tail tip', "TAILTIP"]))
                                white_pattern.append(choice([None, None, None, choice(['break/nose1', 'break/nose2'])]))

                        elif KITgrade == 4:
                            while len(white_pattern) < 6:
                                #chest
                                white_pattern.append(choice(
                                    ['underbelly1', 'underbelly1', 'underbelly1', 
                                    'beard', 'chest', 
                                    "CHEST_BROKEN", "BELLY", "CHEST_MID"]))

                                #belly
                                if 'underbelly1' not in white_pattern:
                                    white_pattern.append('belly')
                                white_pattern.append(choice(['belt', 'belt', 'pants'] + [None] * 7))

                                #paws
                                nropaws = choice([4, 4, 4, 4, 3, 3, 2, 2, 1])
                                order = ['right front', 'left front', 'right back', 'left back']
                                shuffle(order)
                                pawtype = choice(['same', 'mixed'])

                                for i in range(nropaws):
                                    if pawtype == 'same':
                                        pawtype = choice([' mitten', ' low sock', ' low sock', ' high sock'])
                                        white_pattern.append(order[i] + pawtype)
                                    else:
                                        white_pattern.append(order[i] + choice([' mitten', ' low sock', ' high sock']))

                                if random() < 0.2:
                                    nropaws = choice([4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1])
                                    order = ['right front', 'left front', 'right back', 'left back']
                                    shuffle(order)
                                    for i in range(nropaws):
                                        white_pattern.append("break/"+ order[i] + choice([' toes', ' mitten']))
                                
                                for i in range(randint(0, 2)):
                                    white_pattern.append(choice(['break/bracelet left', 'break/bracelet right'] + [None] * 5))

                                #face
                                if 'beard' or 'underbelly1' in white_pattern:
                                    if random() < 0.75:
                                        white_pattern.append(choice(['chin', 'chin', 'muzzle1', 'muzzle1', 'muzzle2', 'blaze', "MUSTACHE", "MUZZLE"]))

                                    if random() < 0.25:
                                        white_pattern.append(choice(["BEARD_MID", "BEARD_HIGH"]))
                                if random () < 0.1:
                                    white_pattern.append(choice(['break/chin', "break/CHIN"]))

                                #tail
                                if random() < 0.2:
                                    white_pattern.append(choice(['tail tip', "TAILTIP"]))
                                white_pattern.append(choice([None, None, None, choice(['break/nose1', 'break/nose2'])]))
                        else:
                            while len(white_pattern) < 6:
                                #chest
                                white_pattern.append('underbelly1')
                                white_pattern.append(choice(['belt', 'belt', 'pants'] + [None] * 7))

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

                                if random() < 0.2:
                                    nropaws = choice([4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1])
                                    order = ['right front', 'left front', 'right back', 'left back']
                                    shuffle(order)
                                    pawtype = choice(['same', 'mixed'])
                                    for i in range(nropaws):
                                        white_pattern.append("break/" + order[i] + choice([' toes', ' mitten', ' mitten']))

                                for i in range(randint(0, 2)):
                                    white_pattern.append(choice(['break/bracelet left', 'break/bracelet right'] + [None] * 5))
                                #face
                                white_pattern.append(choice(['chin', 'muzzle1', 'muzzle1', 'muzzle1', 'muzzle2', 'blaze', "MUSTACHE", "MUZZLE"]))

                                if random() < 0.25:
                                    white_pattern.append(choice(["BEARD_MID", "BEARD_HIGH"]))

                                if random() < 0.1:
                                    white_pattern.append(
                                        choice(['break/chin', "break/CHIN"]))

                                # tail
                                if random() < 0.2:
                                    white_pattern.append(
                                        choice(['tail tip', "TAILTIP"]))
                                white_pattern.append(choice([None, None, None, choice(['break/nose1', 'break/nose2'])]))
                    else:
                        if "NoDBE" not in pax3 and (random() < 0.75):
                            white_pattern = [choice(["REVERSEPANTS", "FULLWHITE", "van3"])]

                        if(randint(1, 4) == 1):
                            white_pattern.append(choice(Pelt.maingame_white["high"].get(str(KITgrade))))

                        elif KITgrade == 1:
                            while len(white_pattern) < 6:
                                #chest
                                white_pattern.append('underbelly1')
                                white_pattern.append(choice(['belt', 'belt', 'pants'] + [None] * 7))

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

                                if random() < 0.2:
                                    nropaws = choice([4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1])
                                    order = ['right front', 'left front', 'right back', 'left back']
                                    shuffle(order)
                                    for i in range(nropaws):
                                        white_pattern.append("break/"+ order[i] + choice([' toes', ' mitten', ' mitten', ' low sock']))

                                for i in range(randint(0, 2)):
                                    white_pattern.append(choice(['break/bracelet left', 'break/bracelet right'] + [None] * 5))
                                #face
                                white_pattern.append(choice(['chin', 'muzzle1', 'muzzle1', 'muzzle1', 'muzzle2', 'blaze', 'blaze']))
                                white_pattern.append(choice(['break/chin'] + [None] * 5))

                                if random() < 0.25:
                                    white_pattern.append(choice(["BEARD_FULL", "BEARD_HIGH", "BEARD_MID"]))

                                #tail
                                if random() < 0.2:
                                    white_pattern.append(choice(['tail tip', "TAILTIP"]))
                                white_pattern.append(choice([None, None, None, choice(['break/nose1', 'break/nose2'])]))

                        elif KITgrade == 2:
                            #body
                            white_pattern.append(choice(['underbelly1', 'mask n mantle']))

                            white_pattern.append(choice(['break/right no', 'break/left no'] + [None] * 14))
                            white_pattern.append(choice(['break/pants'] + [None] * 9))

                            #paws
                            nropaws = 4
                            order = ['right front', 'left front', 'right back', 'left back']

                            for i in range(nropaws):
                                white_pattern.append(order[i] + ' bicolour2')

                            if random() < 0.15:
                                nropaws = choice([4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1])
                                order = ['right front', 'left front', 'right back', 'left back']
                                shuffle(order)
                                for i in range(nropaws):
                                    white_pattern.append("break/"+ order[i] + choice([' toes', ' mitten', ' mitten', ' low sock']))

                            for i in range(randint(0, 2)):
                                white_pattern.append(choice(['break/bracelet left', 'break/bracelet right'] + [None] * 5))
                            
                            # face
                            if random() < 0.1:
                                white_pattern.append(choice(["MASK_FULL", "MASK_HIGH"]))
                            else:
                                white_pattern.append(choice(['muzzle1', 'muzzle1', 'muzzle2', 'blaze', 'blaze']))
                            

                            if random() < 0.25:
                                white_pattern.append(choice(["BEARD_FULL", "BEARD_HIGH", "BEARD_MID"]))

                            if random () < 0.2:
                                white_pattern.append(choice(['break/nose1', 'break/nose2']))
                            if random () < 0.1:
                                white_pattern.append(choice(['break/chin', "BLAZE_FULL", "FOREHEAD_MID", "break/CHIN"]))

                            #tail
                            if random() < 0.2:
                                white_pattern.append(choice(['tail tip', "TAILTIP"]))
                        elif KITgrade == 3:
                            white_pattern.append(choice(['van1', 'van2', 'van3']))

                            if random() < 0.25:
                                white_pattern.append(choice(['FOREHEAD_STRIPE']))
                            
                            if random() < 0.1:
                                nropaws = choice([4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1])
                                order = ['right front', 'left front',
                                        'right back', 'left back']
                                shuffle(order)
                                for i in range(nropaws):
                                    white_pattern.append("break/" + order[i] + choice(
                                        [' toes', ' toes', ' mitten', ' mitten', ' mitten', ' low sock', ' high sock']))
                            for i in range(randint(0, 2)):
                                white_pattern.append(
                                    choice(['break/bracelet left', 'break/bracelet right'] + [None] * 9))

                            if random() < 0.25:
                                white_pattern.append(choice(["break/BACKSPOT", "break/SADDLE_SMALL"]))
                            white_pattern.append(choice(['break/piebald1', 'break/piebald2', 'break/piebald3']))
                            
                            if random() < 0.1:
                                white_pattern.append(choice(['break/pants']))
                            if random() < 0.05:
                                white_pattern.append(choice(['break/right no', 'break/left no']))
                            
                            if random() < 0.9:
                                for i in range(randint(1, 2)):
                                    white_pattern.append(choice([
                                        choice(['break/LEFTEAR', 'break/LEFTEAR_MID', 'break/LEFTEAR_MOSTLY', 'break/LEFTEAR_TIP']), 
                                        choice(['break/RIGHTEAR', 'break/RIGHTEAR_MID', 'break/RIGHTEAR_MOSTLY', 'break/RIGHTEAR_TIP']), 
                                        'break/left face', 'break/right face', 'break/bowl cut', 
                                        'break/EYESPOT_L', 'break/EYESPOT_R', "break/FOREHEAD_MIN"]))
                            if random() < 0.25:
                                white_pattern.append(choice(['break/nose1', 'break/nose2']))
                            if random() < 0.1:
                                white_pattern.append(choice(['break/chin', "break/CHIN", "break/FOREHEAD_MID"]))
                        elif KITgrade == 4:
                            white_pattern.append(choice(['van1', 'van2', 'van3', 'van1', 'van2', 'van3', 'FULLWHITE']))

                            if random() < 0.25:
                                white_pattern.append(choice(["break/BACKSPOT", "break/SADDLE_SMALL"]))

                            if random() < 0.05:
                                nropaws = choice([4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1])
                                order = ['right front', 'left front', 'right back', 'left back']
                                shuffle(order)
                                for i in range(nropaws):
                                    white_pattern.append("break/"+ order[i] + choice([' toes', ' toes', ' mitten', ' mitten', ' mitten', ' low sock', ' high sock']))

                            for i in range(randint(0, 2)):
                                white_pattern.append(choice(['break/bracelet left', 'break/bracelet right'] + [None] * 9))
                            white_pattern.append(choice(['break/right no', 'break/left no'] + [None] * 14))
                            white_pattern.append(choice(['break/pants'] + [None] * 14))
                            if random() < 0.66:
                                for i in range(randint(1, 2)):
                                    white_pattern.append(choice([
                                        choice(['break/LEFTEAR', 'break/LEFTEAR_MID', 'break/LEFTEAR_MOSTLY', 'break/LEFTEAR_TIP']), 
                                        choice(['break/RIGHTEAR', 'break/RIGHTEAR_MID', 'break/RIGHTEAR_MOSTLY', 'break/RIGHTEAR_TIP']), 
                                        'break/left face', 'break/tail tip', 'break/TAILTIP', 'break/tail band',
                                        'break/tail rings', 'break/right face', 'EYESPOT_REVERSE_L', 'EYESPOT_REVERSE_R', 
                                        'break/EYESPOT_L', 'break/EYESPOT_R', "break/FOREHEAD_MIN", "break/FOREHEAD_STRIPE"]))
                            if random() < 0.2:
                                white_pattern.append(choice([
                                    choice(['break/LEFTEAR', 'break/LEFTEAR_MID', 'break/LEFTEAR_MOSTLY', 'break/LEFTEAR_TIP']), 
                                    choice(['break/RIGHTEAR', 'break/RIGHTEAR_MID', 'break/RIGHTEAR_MOSTLY', 'break/RIGHTEAR_TIP']), 
                                    'break/left face', 'break/right face', 'break/bowl cut']))
                            white_pattern.append(choice([None, None, None, None, choice(['break/nose1', 'break/nose2'])]))
                            
                            if random () < 0.1:
                                white_pattern.append(choice(['break/chin', "break/CHIN"]))
                        else:
                            white_pattern.append(choice(["FULLWHITE", 'van3']))
                            if random() < 0.05:
                                for i in range(randint(0, 2)):
                                    white_pattern.append(choice(['break/bracelet left', 'break/bracelet right']))
                                

                            if random() < 0.01:
                                nropaws = choice([4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1])
                                order = ['right front', 'left front', 'right back', 'left back']
                                shuffle(order)
                                for i in range(nropaws):
                                    white_pattern.append("break/"+ order[i] + choice([' toes', ' toes', ' mitten', ' mitten', ' mitten', ' low sock', ' high sock']))

                            if random() < 0.25:
                                white_pattern.append(choice(["break/BACKSPOT", "break/SADDLE_SMALL"]))
                            
                            if random() < 0.9:
                                for i in range(randint(1, 2)):
                                    white_pattern.append(choice([
                                    choice(['break/LEFTEAR', 'break/LEFTEAR_MID', 'break/LEFTEAR_MOSTLY', 'break/LEFTEAR_TIP']), 
                                    choice(['break/RIGHTEAR', 'break/RIGHTEAR_MID', 'break/RIGHTEAR_MOSTLY', 'break/RIGHTEAR_TIP']), 
                                    'break/tail tip', "break/TAILTIP", 'break/tail band', 
                                    "break/FOREHEAD_MIN", "break/FOREHEAD_STRIPE"]))
                            elif random() < 0.2:
                                white_pattern.append(choice(['break/left face', 'break/right face', 'break/bowl cut', "break/EYESPOT_R", "break/EYESPOT_L", 'break/chin']))

                            if random() < 0.01:
                                white_pattern = ["FULLWHITE", "break/dorsal stripe"]

                    if random() < 0.25:
                        if "blaze" in white_pattern:
                            white_pattern.append("BLAZE")
                        if "muzzle1" in white_pattern:
                            white_pattern.append(choice(["BLAZE_MID", "ESTRELLA"]))

                    if "NoDBE" not in pax3:
                        white_pattern.append(choice(["MASK_HIGH", "MASK_MID", "MASK_FACE", "MASK_REVERSE_BROWS"]))
                    elif pax3[0] != "NoDBE" and random() < 0.5:
                        white_pattern.append(choice(["BLAZE", "BLAZE_MID", "BLAZE_SMALL", "EYESPOT_L", "EYESPOT_R", "MUZZLE"]))
                    if KIT[0] != "wg" and random() < 0.2:
                        valid_legs = []
                        for w in white_pattern:
                            if w and ("bicolour2" in w or "low sock" in w or "toes" in w or "mitten" in w):
                                valid_legs.append(w)
                        if valid_legs:
                            count = choice(range(len(valid_legs)))
                            shuffle(valid_legs)
                            for i in range(count):
                                leg = valid_legs[i]
                                white_pattern.remove(leg)
                                split = leg.removeprefix("break/").split(" ", 2)
                                white_pattern.append(f"{"break/" if "break/" in leg else ""}LEG_{split[1].upper()}_{split[0].upper()}_{split[2].replace("bicolour2", "HIGH").replace("low sock", "MID").replace("mitten", "SMALL").replace("toes", "MIN")}")
                    
                    white_pattern = clean_white(white_pattern)
                elif white_pattern is None and vit:
                    white_pattern = [choice(vitiligo)]
                else:
                    white_pattern = []
                return white_pattern

            phenotype.white_pattern = GenerateWhite(phenotype.white, phenotype.whitegrade, phenotype.vitiligo, white_pattern)
            if len(phenotype.white_pattern) == 0:
                phenotype.white_pattern = [None]
            elif phenotype.white_pattern[0] not in vitiligo:
                phenotype.white_pattern = [None] + phenotype.white_pattern

        SubRandomize(self.phenotype)
        SubRandomize(self.chimerapheno)
        if random() < 0.1:
            self.phenotype.chimera = True
        else:
            self.phenotype.chimera = False

    def generate_large_image(self):
        return

    def generate_save_file(self):
        """Generates a basic save file dictionary with all the looks-based info filled in. """

        save = {
            "ID": self.ID,
            "name_prefix": "Prefix",
            "name_suffix": "suffix",
            "specsuffix_hidden": False,
            "gender_align": "sam",
            "pronouns": None,
            "birth_cooldown": 0,
            "status": {
                "group_history": [
                    {
                        "group": "1",
                        "rank": "warrior",
                        "moons_as": 0
                    }
                ],
                "standing_history": [
                    {
                        "group": "1",
                        "standing": [
                            "member"
                        ],
                        "near": True
                    }
                ]
            },
            "dark_forest_affinity": 0,
            "starclan_affinity": 0,
            "backstory": self.backstory,
            "moons": self.moons,
            "trait": self.trait,
            "parent1": None,
            "parent2": None,
            "parent3": None,
            "adoptive_parents": [],
            "surrogate_parents": [],
            "affair_parents": [],
            "mentor": None,
            "former_mentor": [],
            "patrol_with_mentor": 0,
            "mate": [],
            "previous_mates": [],
            "paralyzed": self.pelt.paralyzed,
            "no_kits": False,
            "no_retire": False,
            "no_mates": False,
            "genotype": self.phenotype.export(),
            "chimerageno": self.chimerapheno.export() if self.phenotype.chimera else None,
            "chimera_pattern": [self.chimerapheno.chimerapattern] if self.phenotype.chimera else None,
            "passes_genotype" : 1,
            "white_pattern" : self.phenotype.white_pattern[1:] if len(self.phenotype.white_pattern) > 1 else "No",
            "chim_white" : self.chimerapheno.white_pattern[1:] if self.phenotype.chimera and len(self.chimerapheno.white_pattern) > 1 else "No",
            "sprite_newborn": self.pelt.cat_sprites["newborn"],
            "sprite_kitten": self.pelt.cat_sprites['kitten'],
            "sprite_adolescent": self.pelt.cat_sprites['adolescent'],
            "sprite_adult": self.pelt.cat_sprites['adult'],
            "sprite_senior": self.pelt.cat_sprites['senior'],
            "sprite_para_adult": self.pelt.cat_sprites['para_adult'],
            "reverse": self.pelt.reverse,
            "rusting": self.pelt.rusting,
            "tint": None,
            "white_tint": None,
            "skill_dict": {
                "primary": "FIGHTER,0,False",
                "secondary": None,
                "hidden": None
            },
            "scars": [x for x in self.pelt.scar_slot_list if x],
            "accessory": [x for x in self.pelt.acc_slot_list if x],
            "experience": 0,
            "current_apprentice": [],
            "former_apprentices": [],
            "faded_offspring": [],
            "opacity": 100,
            "prevent_fading": False,
            "favourite": 0,
        }

        return save

# ---------------------------------------------------------------------------- #
#                               END OF CAT CLASS                               #
# ---------------------------------------------------------------------------- #
