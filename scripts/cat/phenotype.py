from .genotype import *
from random import choice, randint


class Phenotype(Genotype):

    def __init__(self):
        super().__init__()
        self.length = ""
        self.furtype = ['', '']

        self.fade = "None"
        self.colour = "black"
        self.tortie = False
        self.silvergold = ''
        self.tabby = ""
        self.sheeted = False
        self.tabtype = "Solid"
        self.point = "Normal"

        self.eartype = ""
        self.tailtype = ""
        self.bobtailnr = 0

        self.vitiligo = ""

        self.pigone = 'P11'
        self.pigtwo = 'P11'
        self.refone = 'R11'
        self.reftwo = 'R11'
        self.pigext = 'P11'
        self.refext = 'R1'

        tortie_patches_shapes = {"ONE": "One", "TWO": "Two", "THREE": "Three", "FOUR": "Four",  'REDTAIL': "Redtail",
                                 'DELILAH': "Delilah", 'MINIMALONE': "Minimal 1", 'MINIMALTWO': "Minimal 2",
                                 'MINIMALTHREE': "Minimal 3", 'MINIMALFOUR': "Minimal 4", 'OREO': "Oreo", 'SWOOP': "Swoop",
                                 'MOTTLED': "Mottled", 'SIDEMASK': "Sidemask", 'EYEDOT': "Eye dot",
                                 'BANDANA': "Bandana", 'PACMAN': "Pacman", 'STREAMSTRIKE': "Streamstrike",
                                 'ORIOLE': "Oriole", 'ROBIN': "Robin", 'BRINDLE': "Brindle", 'PAIGE': "Paige",
                                 "ROSETAIL": "Rosetail", "SAFI": "Safi", "HALF": "Half", "CHIMERA": "Chimera",
                                 "SMUDGED": "Smudged", "DAUB": "Daub", "DAPPLENIGHT": "Dapplenight", "STREAK": "Streak",
                                 "MASK": "Mask", "CHEST": "Chest", "ARMTAIL": "Armtail", "EMBER": "Ember", "SMOKE": "Smoke",
                                 "GRUMPYFACE": "Grumpy Face", "BRIE": "Brie", "BELOVED": "Beloved", "SHILOH": "Shiloh",
                                 "BODY": "Body"}
        if not self.chimerapattern:
            self.chimerapattern = choice(
                list(tortie_patches_shapes.keys()))

    def SilverGoldFinder(self):
        self.silvergold = ""

        if (self.agouti[0] == 'a' and 'o' in self.sexgene):
            if (self.silver[0] == 'I'):
                if (self.wbtype == 'chinchilla'):
                    self.silvergold = 'masked silver '
                else:
                    if (self.wbtype in ['shaded', 'high']):
                        self.silvergold = 'light '
                    self.silvergold += 'smoke '
        else:
            if (self.silver[0] == 'I'):
                if (self.corin[0] in ['sg', 'sh']):
                    self.silvergold = 'bimetallic '
                elif (self.corin[0] == 'fg'):
                    self.silvergold = 'silver copper '
                elif ('o' not in self.sexgene):
                    self.silvergold = 'cameo '
                else:
                    self.silvergold = 'silver '
            elif (self.corin[0] == 'sg' or self.wbtype in ['shaded', 'chinchilla']):
                self.silvergold = 'golden '
            elif (self.corin[0] == 'sh'):
                self.silvergold = 'sunshine '
            elif (self.corin[0] == 'fg'):
                self.silvergold = 'flaxen gold '

    def ExtFinder(self):
        if('o' in self.sexgene):
            if(self.ext[0] == 'ec'):
                if(self.colour == ''):
                    self.tortie = " " + self.tortie
                self.colour = 'agouti carnelian'
                if(self.agouti[0] == 'a'):
                    self.colour = "non" + self.colour
                if(self.dilute[0] == 'd' or self.pinkdilute[0] == 'dp'):
                    self.colour = "light " + self.colour
            
            elif(self.ext[0] == 'er'):
                self.colour += ' russet'
            elif(self.ext[0] == 'ea'):
                if(self.dilute[0] == 'd' or self.pinkdilute[0] == 'dp'):
                    self.colour += " light"
                self.colour += ' amber'
    
    def GetTabbySprite(self, special=None):
        all_patterns = []

        if (special == 'redbar'):
            all_patterns = ['redbaralt']
        elif(special == 'ghost'):
            all_patterns = ['fullbaralt']
        elif (self.wbtype == 'chinchilla' or self.ticked[1] == "Ta" or ((not self.breakthrough or self.mack[0] == "mc") and self.ticked[0] == "Ta")):
            if (self.ticktype == "agouti" or self.wbtype == 'chinchilla'):
                all_patterns = ['agouti']
            elif (self.ticktype == 'reduced barring'):
                all_patterns = ['redbar']
            else:
                all_patterns = ['fullbar']
        elif (self.ticked[0] == "Ta"):
            if (self.bengtype == "normal markings"):
                if (self.spotsum == 4):
                    all_patterns = ['brokenpins', 'pinsbar']
                elif (self.spotsum < 6):
                    all_patterns = ['pinstripe', 'pinsbar']
                else:
                    all_patterns = ['servaline', 'pinsbar']
            else:
                if (self.spotsum == 4):
                    all_patterns = ['brokenpinsbraid', 'pinsbar']
                elif (self.spotsum < 6):
                    all_patterns = ['pinsbraided', 'pinsbar']
                else:
                    all_patterns = ['leopard', 'pinsbar']
        elif (self.mack[0] == "mc"):
            if (self.bengtype == "normal markings"):
                all_patterns = ['blotched', 'blotchbar']
            elif self.bengtype == "mild bengal":
                all_patterns = ["marbled", "marbled", 'blotchbar']
            else:
                all_patterns = ['marbled', 'blotchbar']
        else:
            if (self.bengtype == "normal markings"):
                if (self.spotsum == 4):
                    all_patterns = ['brokenmack', 'fullbar']
                elif (self.spotsum < 6):
                    all_patterns = ['mackerel', 'fullbar']
                else:
                    all_patterns = ['spotted', 'fullbar']
            elif (self.bengtype == "mild bengal"):
                if (self.spotsum == 4):
                    all_patterns = ['brokenbraid', 'fullbar']
                elif (self.spotsum < 6):
                    all_patterns = ['braided', 'fullbar']
                else:
                    all_patterns = ['partialrosetted', 'fullbar']
            else:
                if (self.spotsum == 4):
                    all_patterns = ['brokenbraid', 'fullbar']
                elif (self.spotsum < 6):
                    all_patterns = ['braided', 'fullbar']
                else:
                    all_patterns = ['rosetted', 'fullbar']

        if all_patterns[0] != "agouti":
            if self.bengtype != "normal markings":
                tail = "bengtail"
            else:
                if self.mack[0] == "mc":
                    tail = "blotchtail"
                else:
                    tail = "macktail"
            all_patterns.append(tail)

        return all_patterns

    def ChooseTortiePattern(self, spec=None):
        def_tortie_low_patterns = ['DELILAH', 'MOTTLED', 'EYEDOT', 'BANDANA', 'SMUDGED', 'EMBER', 'BRINDLE', 'SAFI', 'BELOVED', 'BODY',
                                   'SHILOH', 'FRECKLED']
        def_tortie_mid_patterns = ['ONE', 'TWO', 'SMOKE', 'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'OREO', 'CHIMERA',
                                   'CHEST', 'GRUMPYFACE', 'SIDEMASK', 'PACMAN', 'BRIE', 'ORIOLE', 'ROBIN', 'PAIGE', 'HEARTBEAT']
        def_tortie_high_patterns = ['THREE', 'FOUR', 'REDTAIL', 'HALF', 'STREAK', 'MASK', 'SWOOP', 'ARMTAIL', 'STREAMSTRIKE', 'DAUB',
                                    'ROSETAIL', 'DAPPLENIGHT', 'BLANKET']
        tortie_low_patterns = def_tortie_low_patterns
        tortie_mid_patterns = def_tortie_mid_patterns
        tortie_high_patterns = def_tortie_high_patterns
        tiny_patches = ["BACKSPOT", "BEARD", "BELLY", "BIB", "revBLACKSTAR", "BLAZE", "BLAZEMASK", "revBOOTS", "revCHESTSPECK", "ESTRELLA",
                        "EYEBAGS", "revEYESPOT", "revHEART", "HONEY", "LEFTEAR", "LITTLE", "PAWS", "REVERSEEYE", "REVERSEHEART", "RIGHTEAR",
                        "SCOURGE", "SPARKLE", "revTAIL", 'revTAILTWO', "TAILTIP", "TEARS", "TIP", "TOES", "TOESTAIL", "VEE"]

        chosen = []

        if spec == 'merle':
            chosen.append(choice([choice(tortie_low_patterns), choice(tortie_low_patterns), choice(tortie_mid_patterns), choice(tortie_mid_patterns), choice(
                tiny_patches), choice(tiny_patches), choice(tiny_patches), choice(tiny_patches), choice(tiny_patches), choice(tiny_patches)]))

        elif spec:
            chosen.append(choice([choice(tortie_high_patterns), choice(tortie_high_patterns), choice(
                tortie_mid_patterns), choice(tortie_mid_patterns), choice(tortie_low_patterns)]))

        elif randint(1, 10) == 1:
            chosen.append('CRYPTIC')

        else:
            for i in range(choice([1, 1, 1, 1, 1, 2, 2, 3])):
                tortie_low_patterns = def_tortie_low_patterns
                tortie_mid_patterns = def_tortie_mid_patterns
                tortie_high_patterns = def_tortie_high_patterns

                if randint(1, 15) == 1 or (i > 0 and randint(1, 10) == 1):
                    tortie_low_patterns = ["BOWTIE", "BROKENBLAZE", "BUZZARDFANG", "revCOWTWO", "FADEBELLY", "FADESPOTS", "revLOVEBUG", "MITAINE",
                                           "revPEBBLESHINE", "revPIEBALD", "SAVANNAH",
                                           choice(tiny_patches)]
                    tortie_mid_patterns = ["revAPPALOOSA", "BLOSSOMSTEP", "BOWTIE", "revBROKEN", "revBUB", "BULLSEYE", "revBUSTER", "BUZZARDFANG",
                                           "revCOW", "revCOWTWO", "DAMIEN", "DAPPLEPAW", "DIVA", "FCTWO", "revFINN", "FRECKLES", "revGLASS", "HAWKBLAZE",
                                           "revLOVEBUG", "MITAINE", "PAINTED", "PANTSTWO", "revPEBBLE", "revPIEBALD", "ROSINA", "revSHOOTINGSTAR", "SPARROW",
                                           "WOODPECKER",
                                           choice(tiny_patches)]
                    tortie_high_patterns = ["revANY", "revANYTWO", "BLOSSOMSTEP", "revBUB", "revBUDDY", "revBUSTER", "revCAKE", "revCOW", "revCURVED",
                                            "DAPPLEPAW", "FCTWO", "FAROFA", "revGOATEE", "revHALFFACE", "HAWKBLAZE", "LILTWO", "MISS", "MISTER", "revMOORISH",
                                            "OWL", "PANTS", "revPRINCE", "REVERSEPANTS", "RINGTAIL", "SAMMY", "SKUNK", "SPARROW", "TOPCOVER", "VEST", "WINGS",
                                            choice(tiny_patches)]
                elif i > 0 and randint(1, 3) == 1:
                    tortie_low_patterns = tiny_patches
                    tortie_mid_patterns = tiny_patches
                    tortie_high_patterns = tiny_patches

                if (self.white[1] == "ws" or self.white[1] == "wt"):
                    if self.whitegrade > 2:
                        if (randint(1, 10) == 1):
                            chosen.append(choice(tortie_low_patterns))
                        elif (randint(1, 5) == 1):
                            chosen.append(choice(tortie_mid_patterns))
                        else:
                            chosen.append(choice(tortie_high_patterns))
                    else:
                        if (randint(1, 7) == 1):
                            chosen.append(choice(tortie_low_patterns))
                        elif (randint(1, 3) == 1):
                            chosen.append(choice(tortie_mid_patterns))
                        else:
                            chosen.append(choice(tortie_high_patterns))
                elif (self.white[0] == 'ws' or self.white[0] == 'wt'):
                    if self.whitegrade > 3:
                        if (randint(1, 7) == 1):
                            chosen.append(choice(tortie_high_patterns))
                        elif (randint(1, 3) == 1):
                            chosen.append(choice(tortie_mid_patterns))
                        else:
                            chosen.append(choice(tortie_low_patterns))
                    else:
                        if (randint(1, 10) == 1):
                            chosen.append(choice(tortie_high_patterns))
                        elif (randint(1, 5) == 1):
                            chosen.append(choice(tortie_mid_patterns))
                        else:
                            chosen.append(choice(tortie_low_patterns))
                else:
                    if (randint(1, 15) == 1):
                        chosen.append(choice(tortie_high_patterns))
                    elif (randint(1, 7) == 1):
                        chosen.append(choice(tortie_mid_patterns))
                    else:
                        chosen.append(choice(tortie_low_patterns))

        return chosen

    def SetFurLength(self, type):
        if 'long' in type or 'lh' in type:
            self.furLength = ['l', 'l']
            self.length = 'longhaired'
        else:
            self.furLength = ['L', 'L']
            self.length = 'shorthaired'

        if 'rexed' in type:
            self.wirehair = ['Wh', 'Wh']
        else:
            self.wirehair = ['wh', 'wh']

        if type == 'fur-point':
            self.sedesp = ['hr', 're']
        else:
            self.sedesp[0] = "Hr"
        if 'patchy' in type:
            self.furtype[0] = 'patchy '
        else:
            self.furtype[0] = ''

    def SetEarType(self, type):
        if type == 'folded curl':
            self.fold[0] = 'Fd'
            self.curl[0] = 'Cu'
        elif 'fold' in type:
            self.fold[0] = 'Fd'
            self.curl[0] = 'cu'
        elif 'curl' in type:
            self.fold[0] = 'fd'
            self.curl[0] = 'Cu'
        if 'normal' in type:
            self.fold[0] = 'fd'
            self.curl[0] = 'cu'

    def GetEarType(self):
        # ["Normal", "Folded", "Curled", "Folded Curl"]
        if self.fold[0] == 'Fd':
            if (self.curl[0] == 'Cu'):
                return 'Folded Curl'
            else:
                return 'Folded'
        elif self.curl[0] == 'Cu':
            return 'Curled'
        else:
            return 'Normal'

    def SetTailType(self, type):
        taildict = {
            'full': 0,
            '3/4': 5,
            '1/2': 4,
            '1/3': 3,
            'stubby': 2,
            'none': 1
        }

        self.bobtailnr = taildict[type]

    def GetTailType(self):
        taildict = {
            0: 'Full',
            5: '3/4',
            4: '1/2',
            3: '1/3',
            2: 'Stubby',
            1: 'None'
        }

        return taildict[self.bobtailnr]

    def UpdateEyes(self):
        self.lefteyetype = self.refone + " ; " + self.pigone
        self.righteyetype = self.reftwo + " ; " + self.pigtwo
        self.extraeyetype = self.refext + " ; " + self.pigext

    def SetBaseColour(self, base):
        self.colour = base

        if base == 'white':
            self.white[0] = 'W'
        else:
            self.white[0] = 'w'

        if base == 'albino':
            self.pointgene[0] = 'c'
        else:
            self.SetPoints(self.point)

        if base in ['red', 'cream', 'honey', 'ivory']:
            self.sexgene = ['O', 'O']
        else:
            if self.tortie:
                self.sexgene = ['O', 'o']
            else:
                self.sexgene = ['o', 'o']

        if base in ['black', 'blue', 'dove', 'platinum']:
            self.eumelanin[0] = 'B'
        elif base in ['chocolate', 'lilac', 'champagne', 'lavender']:
            self.eumelanin[0] = 'b'
        else:
            self.eumelanin[0] = 'bl'

        if base in ['blue', 'platinum', 'lilac', 'lavender', 'fawn', 'beige', 'cream', 'ivory']:
            self.dilute[0] = 'd'
        else:
            self.dilute[0] = 'D'

        if base in ['dove', 'platinum', 'champagne', 'lavender', 'buff', 'beige', 'honey', 'ivory']:
            self.pinkdilute[0] = 'dp'
        else:
            self.pinkdilute[0] = 'Dp'

    def SetPoints(self, input):
        self.point = input

        value = input.lower()
        gene = ['C', 'C']

        if self.colour == 'albino':
            gene = ['c', 'c']
        elif value == 'normal':
            gene = ['C', 'C']
        elif value == 'colourpoint':
            gene = ['cs', 'cs']
        elif value == 'mink':
            gene = ['cb', 'cs']
        elif value == 'sepia':
            gene = ['cb', 'cb']
        elif value == 'point-albino':
            gene = ['cs', 'c']
        elif value == 'sepia-albino':
            gene = ['cb', 'c']
        elif value == 'siamocha':
            gene = ['cs', 'cm']
        elif value == 'burmocha':
            gene = ['cb', 'cm']
        elif value == 'mocha':
            gene = ['cm', 'cm']
        elif value == 'mocha-albino':
            gene = ['cm', 'c']

        self.pointgene = gene

    def TabbyFinder(self):
        self.tabby = ""

        def FindPattern():
            if (self.ticked[0] != 'ta' or self.wbsum > 13):
                if (self.wbsum > 13):
                    self.tabby = 'chinchilla'
                elif (self.ticked[1] == 'Ta' or not self.breakthrough):
                    if (self.wbsum > 11):
                        self.tabby = 'shaded'
                    elif (self.ticksum > 7):
                        self.tabby = 'agouti'
                    else:
                        self.tabby = 'ticked'
                else:
                    if (self.mack[0] == 'mc'):
                        self.tabby = 'ghost-patterned'
                    elif (self.spotsum > 5):
                        self.tabby = 'servaline'
                    else:
                        if (self.spotsum > 2):
                            self.tabby = 'broken '
                        self.tabby += 'pinstripe'
            elif (self.mack[0] == 'mc'):
                self.tabby = 'blotched'
            elif (self.spotsum > 5):
                self.tabby = 'spotted'
            else:
                if (self.spotsum > 2):
                    self.tabby = 'broken '
                self.tabby += 'mackerel'

            if (self.tabby != "" and (self.bengsum > 3 or self.soksum > 5)):
                if (self.bengsum > 3):
                    if (self.tabby == "spotted"):
                        self.tabby = "rosetted"
                    elif (self.tabby == "broken mackerel"):
                        self.tabby = "broken braided"
                    elif (self.tabby == "mackerel"):
                        self.tabby = "braided"
                    elif (self.tabby == "blotched"):
                        self.tabby = "marbled"

                    elif (self.tabby == "servaline"):
                        self.tabby += "-rosetted"
                    elif ('pinstripe' in self.tabby):
                        self.tabby += "-braided"
                    elif (self.tabby == "ghost-patterned"):
                        self.tabby = "ghost marble"
                elif (self.tabby == 'blotched'):
                    self.tabby = 'sokoke'

        if ('o' not in self.sexgene or self.agouti[0] != 'a' or self.tabtype != '' or ('smoke' in self.silvergold and self.length == 'shorthaired') or self.ext[0] not in ['Eg', 'E']):
            FindPattern()

        if (self.tortie != '' and self.tabby != '' and self.tortie != "brindled bicolour "):
            self.tortie = ' torbie '
        elif (self.tabby != '' and self.point not in ['point ', 'mink ', 'siamocha ']):
            self.tabby += ' tabby '
        elif (self.tabby != '' and self.point in ['point ', 'mink ', 'siamocha ']):
            if (self.colour == 'seal' or self.colour == 'chocolate'):
                self.tabby += ' lynx '
            elif ('o' not in self.sexgene):
                self.tabby = ''
            else:
                self.tabby = ' lynx '

    def SetTabbyPattern(self, input):

        if input == 'agouti':
            self.ticked = ['Ta', 'Ta']
            self.ticktype = 'agouti'
        elif input in ['redbarc', 'redbar', 'fullbarc', 'fullbar']:
            self.ticked = ['Ta', 'ta']
            self.breakthrough = False
            if 'red' in input:
                self.ticktype = 'reduced barring'
            else:
                self.ticktype = 'full barring'
        elif input in ['brokenpins', 'pinstripe', 'servaline', 'brokenpinsbraid', 'pinsbraided', 'leopard']:
            self.ticked = ['Ta', 'ta']
            self.breakthrough = True
        else:
            self.ticked = ['ta', 'ta']

        if input in ['redbarc', 'fullbarc', 'blotched', 'marbled', "partialmarble", "sheetmarble", "sheetblotched"]:
            self.mack = ['mc', 'mc']
        else:
            self.mack = ['Mc', 'Mc']

        if input in ['servaline', 'leopard', 'spotted', 'rosetted', "partialrosetted"]:
            self.spotsum = 8
        elif 'broken' in input:
            self.spotsum = 4
        else:
            self.spotsum = 0

        if input in ['brokenpinsbraid', 'pinsbraided', 'leopard', 'marbled', 'braided', 'brokenbraid', 'rosetted', "sheetmarble"]:
            self.bengtype = 'bengal'
        elif input in ["partialmarble", "partialbraided", "partialbrokenbraided", "partialrosetted"]:
            self.bengtype = "mild bengal"
        else:
            self.bengtype = 'normal markings'

        if "sheet" in input:
            self.sheeted = True
        else:
            self.sheeted = False

        self.TabbyFinder()

    def SetTabbyType(self, input):
        self.tabtype = input

        if input == 'Solid':
            self.agouti = ['a', 'a']
        elif input == 'Twilight Charcoal':
            self.agouti = ['Apb', 'Apb']
        elif input == 'Midnight Charcoal':
            self.agouti = ['Apb', 'a']
        else:
            self.agouti = ['A', 'A']

    def SpriteInfo(self, moons):
        self.maincolour = ""
        self.mainunders = []
        self.spritecolour = ""
        self.caramel = ""
        self.patchmain = ""
        self.patchunders = []
        self.patchcolour = ""

        if (self.pseudomerle):
            if not self.merlepattern:
                self.merlepattern = self.ChooseTortiePattern(
                    spec='merle')

        if self.white[0] == "W" or self.pointgene[0] == "c" or ('DBEalt' not in self.pax3 and 'NoDBE' not in self.pax3) or (self.brindledbi and (('o' not in self.sexgene) or (self.ext[0] == 'ea' and ((moons > 11 and self.agouti[0] != 'a') or (moons > 23))) or (self.ext[0] == 'er' and moons > 23) or (self.ext[0] == 'ec' and (self.agouti[0] != 'a' or moons > 5)))):
            self.spritecolour = "white"
            self.maincolour = self.spritecolour
        elif ('o' not in self.sexgene) or (self.ext[0] == 'ea' and ((moons > 11 and self.agouti[0] != 'a') or (moons > 23))) or (self.ext[0] == 'er' and moons > 23) or (self.ext[0] == 'ec' and moons > 0 and (self.agouti[0] != 'a' or moons > 5)):
            if self.specialred == 'blue-tipped':
                self.tortiepattern = ['BLUE-TIPPED']
                main = self.FindRed(self, moons)
                self.maincolour = main[0]
                self.spritecolour = main[1]
                self.mainunders = [main[2], main[3]]
                main = self.FindRed(self, moons, 'blue-tipped')
                self.patchmain = main[0]
                self.patchcolour = main[1]
                self.patchunders = [main[2], main[3]]
            else:
                main = self.FindRed(self, moons, special=self.ext[0])
                self.maincolour = main[0]
                self.spritecolour = main[1]
                self.mainunders = [main[2], main[3]]
        elif ('O' not in self.sexgene):
            main = self.FindBlack(self, moons)
            self.maincolour = main[0]
            self.spritecolour = main[1]
            self.mainunders = [main[2], main[3]]
        else:
            if not self.tortiepattern:
                self.tortiepattern = self.ChooseTortiePattern()
                for i in range(len(self.tortiepattern)):
                    if randint(1, round(10/((i+1)*2))) == 1:
                        if 'rev' in self.tortiepattern[i]:
                            self.tortiepattern[i] = self.tortiepattern[i].replace(
                                'rev', '')
                        else:
                            self.tortiepattern[i] = 'rev' + \
                                self.tortiepattern[i]

            main = self.FindBlack(self, moons)
            self.maincolour = main[0]
            self.spritecolour = main[1]
            self.mainunders = [main[2], main[3]]
            if (self.brindledbi):
                self.patchmain = "white"
                self.patchcolour = "white"
            else:
                main = self.FindRed(self, moons)
                self.patchmain = main[0]
                self.patchcolour = main[1]
                self.patchunders = [main[2], main[3]]

    def FindEumUnders(self, genes, wideband, rufousing, unders_ruf):
        if(genes.dilute[0] == "d"):
            if(genes.pinkdilute[0] == "dp"):
                colour = "ivory"
            else:
                colour = "cream"
        else:
            if(genes.pinkdilute[0] == "dp"):
                colour = "honey"
            else:
                colour = "red"
        

        if wideband in ["chinchilla", "shaded"]:
            colour = "lightbasecolours0"
        elif unders_ruf == "rufoused":
            colour = rufousing + colour + "3"
        elif unders_ruf == "low":
            colour = colour + "low" + "shaded" + "0"
        elif rufousing != "rufoused":
            colour = colour + "low" + wideband + "0"
        else:
            colour = colour + "medium" + wideband + "0"
        
        return colour

    def GetSilverUnders(self, wideband):
        if wideband == "low":
            return 20
        elif wideband == "medium":
            return 40
        elif wideband == "high":
            return 60
        elif wideband == "shaded":
            return 80
        else:
            return 100

    def GetRedUnders(self, wideband):
        if wideband == "low":
            return 20
        elif wideband == "medium":
            return 30
        elif wideband == "high":
            return 40
        elif wideband == "shaded":
            return 50
        else:
            return 60

    def FindBlack(self, genes, moons, special=None):
        unders_colour = ""
        unders_opacity = 0
        if special == 'er':
            return self.FindRed(genes, moons, special)
        else:
            if genes.eumelanin[0] == "bl":
                if genes.dilutemd[0] == 'Dm':
                    self.caramel = 'caramel'

                if genes.dilute[0] == "d":
                    if (genes.pinkdilute[0] == "dp"):
                        colour = "beige"
                    else:
                        colour = "fawn"
                else:
                    if (genes.pinkdilute[0] == "dp"):
                        colour = "buff"
                    else:
                        colour = "cinnamon"
                        self.caramel = ""
            elif genes.eumelanin[0] == "b":
                if genes.dilutemd[0] == 'Dm':
                    self.caramel = 'caramel'

                if genes.dilute[0] == "d":
                    if (genes.pinkdilute[0] == "dp"):
                        colour = "lavender"
                    else:
                        colour = "lilac"
                else:
                    if (genes.pinkdilute[0] == "dp"):
                        colour = "champagne"
                    else:
                        colour = "chocolate"
                        self.caramel = ""
            else:
                if (genes.dilutemd[0] == 'Dm'):
                    self.caramel = 'caramel'

                if (genes.dilute[0] == "d"):
                    if (genes.pinkdilute[0] == "dp"):
                        colour = "platinum"
                    else:
                        colour = "blue"
                else:
                    if (genes.pinkdilute[0] == "dp"):
                        colour = "dove"
                    else:
                        colour = "black"
                        self.caramel = ""

            maincolour = colour + str(self.saturation)

            if self.saturation < 3 and colour in ['blue', 'lilac', 'fawn', 'dove']:
                colour = "pale_" + colour

            rufousing = ""
            banding = ""

            if ('masked' in self.silvergold) or (genes.agouti[0] != "a" and genes.ext[0] != "Eg") or (genes.ext[0] not in ['Eg', 'E']):
                if genes.silver[0] == "I" or genes.brindledbi or (moons < 3 and genes.karp[0] == "K"):
                    rufousing = "silver"
                elif genes.pointgene[0] != "C" or genes.agouti[0] == "Apb":
                    rufousing = "low"
                else:
                    rufousing = genes.ruftype

                if genes.corin[0] == "sg" or genes.wbtype == "chinchilla":
                    banding = "chinchilla"
                elif genes.wbtype == "shaded" or genes.corin[0] == "sh" or genes.corin[0] == "fg" or genes.ext[0] == 'ec' or (genes.ext[0] == 'ea' and moons > 3):
                    banding = "shaded"
                else:
                    banding = genes.wbtype

                if rufousing == "silver":
                    unders_colour = "lightbasecolours0"
                    unders_opacity = self.GetSilverUnders(banding)
                else:
                    unders_colour = self.FindEumUnders(genes, banding, rufousing, self.unders_ruftype)
                    if self.unders_ruftype == "rufoused" and banding not in ["chinchilla", "shaded"]:
                        unders_opacity = 30
                    else:
                        unders_opacity = 20

                colour = colour + rufousing + banding + "0"
                self.banding = banding

            else:
                colour = maincolour

            return [maincolour, colour, unders_colour, unders_opacity]

    def FindRed(self, genes, moons, special=None):
        unders_colour = 'lightbasecolours0'
        unders_opacity = 0
        maincolour = genes.ruftype
        if special == 'er':
            if (genes.eumelanin[0] == 'B'):
                maincolour = 'rufoused'
            elif (genes.eumelanin[0] == 'b'):
                maincolour = 'medium'
            else:
                maincolour = 'low'
        if (genes.dilute[0] == "d" or (genes.specialred == 'cameo' or self.pseudomerle) and genes.silver[0] == 'I'):
            if (genes.pinkdilute[0] == "dp"):
                if genes.dilutemd[0] == "Dm":
                    colour = "ivory-apricot"
                else:
                    colour = "ivory"
            else:
                if genes.dilutemd[0] == "Dm" and not (genes.specialred == 'cameo' or self.pseudomerle):
                    colour = "apricot"
                else:
                    colour = "cream"
        else:
            if (genes.pinkdilute[0] == "dp"):
                if genes.dilutemd[0] == "Dm":
                    colour = "honey-apricot"
                else:
                    colour = "honey"
            else:
                colour = "red"

        maincolour += colour + str(self.saturation)

        rufousing = ""
        banding = ""
        if genes.silver[0] == "I" and special != 'nosilver' or (moons < 3 and genes.karp[0] == "K"):
            rufousing = "silver"
        elif genes.pointgene[0] not in ["C", "cm"] or special == 'low':
            rufousing = "low"
        else:
            rufousing = genes.ruftype

        if genes.corin[0] == "sg" or genes.wbtype == "chinchilla":
            banding = "chinchilla"
        elif genes.corin[0] == "sh" or genes.corin[0] == "fg" or genes.wbtype == "shaded":
            banding = "shaded"
        else:
            banding = genes.wbtype
        
        self.banding = banding

        if colour == "apricot":
            if genes.ruftype == "low":
                colour = "cream"
                if rufousing != "silver":
                    rufousing = "medium"
            elif genes.ruftype == "medium":
                colour = "cream"
                if rufousing != "silver":
                    rufousing = "rufoused"
            else:
                colour = "red"
                if rufousing != "silver":
                    rufousing = "low"
        elif colour == "honey-apricot":
            if genes.ruftype == "low":
                colour = "honey"
                if rufousing != "silver":
                    rufousing = "medium"
            elif genes.ruftype == "medium":
                colour = "honey"
                if rufousing != "silver":
                    rufousing = "rufoused"
            else:
                colour = "red"
                if rufousing != "silver":
                    rufousing = "low"
        elif colour == "ivory-apricot":
            if genes.ruftype == "low":
                colour = "ivory"
                if rufousing != "silver":
                    rufousing = "medium"
            elif genes.ruftype == "medium":
                colour = "ivory"
                if rufousing != "silver":
                    rufousing = "rufoused"
            else:
                colour = "honey"
                if rufousing != "silver":
                    rufousing = "low"

        if (genes.ext[0] == "ec" and genes.agouti[0] == "a" and 'o' in genes.sexgene):
            unders_opacity = 0
        elif rufousing == "silver" or (genes.ext[0] == "ec" and genes.agouti[0] != "a" and 'o' in genes.sexgene):
            unders_opacity = self.GetSilverUnders(banding)
        else:
            unders_opacity = self.GetRedUnders(banding)
        colour = colour + rufousing + banding + "0"

        if (genes.specialred in ['blue-red', 'pseudo-cinnamon']) or special == 'blue-tipped':
            colour = colour.replace('red', 'blue')
            colour = colour.replace('cream', 'lilac')
            colour = colour.replace('honey', 'dove')
            colour = colour.replace('ivory', 'lavender')
            if (genes.specialred == 'pseudo-cinnamon'):
                if ('red' in maincolour):
                    maincolour = 'cinnamon3'
                elif ('cream' in maincolour or maincolour == 'apricot'):
                    maincolour = 'fawn3'
                elif ('honey' in maincolour):
                    maincolour = 'buff3'
                elif ('ivory' in maincolour):
                    maincolour = 'beige3'

                if ('apricot' in maincolour):
                    self.caramel = 'caramel'
            
            if rufousing != "silver":
                unders_colour = self.FindEumUnders(genes, banding, rufousing, self.unders_ruftype)
                if self.unders_ruftype == "rufoused":
                    unders_opacity = 45
                else:
                    unders_opacity = 25

        return [maincolour, colour, unders_colour, unders_opacity]
