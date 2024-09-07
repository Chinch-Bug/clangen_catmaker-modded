from .genotype import *
from random import choice, randint

class Phenotype():

    def __init__(self, genotype):
        self.length = ""
        self.furtype = ['', '']

        self.fade = "None"
        self.colour = "black"
        self.tortie = False
        self.silvergold = ''
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

        self.genotype = genotype

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
            
        if not self.genotype.tortiepattern:
            self.genotype.tortiepattern = choice(list(tortie_patches_shapes.keys()))
        if not self.genotype.chimerapattern:
            self.genotype.chimerapattern = choice(list(tortie_patches_shapes.keys()))

    def SilverGoldFinder(self):
        self.silvergold = ""

        if(self.genotype.agouti[0] == 'a' and 'o' in self.genotype.sexgene):
            if(self.genotype.silver[0] == 'I'):
                if(self.genotype.wbtype == 'chinchilla'):
                    self.silvergold = 'masked silver '
                else:
                    if(self.genotype.wbtype in ['shaded', 'high']):
                        self.silvergold = 'light '
                    self.silvergold += 'smoke '
        else:
            if(self.genotype.silver[0] == 'I'):
                if(self.genotype.corin[0] in ['sg', 'sh']):
                    self.silvergold = 'bimetallic '
                elif(self.genotype.corin[0] == 'fg'):
                    self.silvergold = 'silver copper '
                elif ('o' not in self.genotype.sexgene):
                    self.silvergold = 'cameo '
                else:
                    self.silvergold = 'silver '
            elif(self.genotype.corin[0] == 'sg' or self.genotype.wbtype in ['shaded', 'chinchilla']):
                self.silvergold = 'golden '
            elif(self.genotype.corin[0] == 'sh'):
                self.silvergold = 'sunshine '
            elif(self.genotype.corin[0] == 'fg'):
                self.silvergold = 'flaxen gold '

    def GetTabbySprite(self, special = None):
        pattern = ""

        if(special == 'redbar'):
            if(self.genotype.mack[0] == "mc"):
                pattern = 'redbarc'
            else:
                pattern = 'redbar'
        elif(self.genotype.wbtype == 'chinchilla' or self.genotype.ticked[1] == "Ta" or ((not self.genotype.breakthrough or self.genotype.mack[0] == "mc") and self.genotype.ticked[0] == "Ta")):
            if(self.genotype.ticktype == "agouti" or self.genotype.wbtype == 'chinchilla'):
                pattern = 'agouti'
            elif(self.genotype.ticktype == 'reduced barring'):
                if(self.genotype.mack[0] == "mc"):
                    pattern = 'redbarc'
                else:
                    pattern = 'redbar'
            else:
                if(self.genotype.mack[0] == "mc"):
                    pattern = 'fullbarc'
                else:
                    pattern = 'fullbar'
        elif(self.genotype.ticked[0] == "Ta"):
            if(self.genotype.bengtype == "normal markings"):
                if(self.genotype.spotsum == 4):
                    pattern = 'brokenpins'
                elif(self.genotype.spotsum < 6):
                    pattern = 'pinstripe'
                else:
                    pattern = 'servaline'
            else:
                if(self.genotype.spotsum == 4):
                    pattern = 'brokenpinsbraid'
                elif(self.genotype.spotsum < 6):
                    pattern = 'pinsbraided'
                else:
                    pattern = 'leopard'
        elif(self.genotype.mack[0] == "mc"):
            if(self.genotype.bengtype == "normal markings"):
                pattern = 'classic'
            else:
                pattern = 'marbled'
        else:
            if(self.genotype.bengtype == "normal markings"):
                if(self.genotype.spotsum == 4):
                    pattern = 'brokenmack'
                elif(self.genotype.spotsum < 6):
                    pattern = 'mackerel'
                else:
                    pattern = 'spotted'
            else:
                if(self.genotype.spotsum == 4):
                    pattern = 'brokenbraid'
                elif(self.genotype.spotsum < 6):
                    pattern = 'braided'
                else:
                    pattern = 'rosetted'
                

        return pattern
      
    def ChooseTortiePattern(self, spec = None):
        tortie_low_patterns = ['DELILAH', 'MOTTLED', 'EYEDOT', 'BANDANA', 'SMUDGED', 'EMBER', 'BRINDLE', 'SAFI', 'BELOVED', 'BODY', 
                               'SHILOH', 'FRECKLED']
        tortie_mid_patterns = ['ONE', 'TWO', 'SMOKE', 'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'OREO', 'CHIMERA',
                                'CHEST', 'GRUMPYFACE', 'SIDEMASK', 'PACMAN', 'BRIE' ,'ORIOLE', 'ROBIN', 'PAIGE', 'HEARTBEAT']
        tortie_high_patterns = ['THREE', 'FOUR', 'REDTAIL', 'HALF', 'STREAK', 'MASK', 'SWOOP', 'ARMTAIL', 'STREAMSTRIKE', 'DAUB',
                                'ROSETAIL', 'DAPPLENIGHT', 'BLANKET']
        
        chosen = ""

        if spec:
            chosen = choice([choice(tortie_high_patterns), choice(tortie_high_patterns), choice(tortie_mid_patterns), choice(tortie_mid_patterns), choice(tortie_low_patterns)])

        elif(self.genotype.white[1] == "ws" or self.genotype.white[1] == "wt"):
            if self.genotype.whitegrade > 2:
                if(randint(1, 10) == 1):
                    chosen = choice(tortie_low_patterns)
                elif(randint(1, 5) == 1):
                    chosen = choice(tortie_mid_patterns)
                else:
                    chosen = choice(tortie_high_patterns)
            else:
                if(randint(1, 7) == 1):
                    chosen = choice(tortie_low_patterns)
                elif(randint(1, 3) == 1):
                    chosen = choice(tortie_mid_patterns)
                else:
                    chosen = choice(tortie_high_patterns)
        elif(self.genotype.white[0] == 'ws' or self.genotype.white[0] == 'wt'):
            if self.genotype.whitegrade > 3:
                if(randint(1, 7) == 1):
                    chosen = choice(tortie_high_patterns)
                elif(randint(1, 3) == 1):
                    chosen = choice(tortie_mid_patterns)
                else:
                    chosen = choice(tortie_low_patterns)
            else:
                if(randint(1, 10) == 1):
                    chosen = choice(tortie_high_patterns)
                elif(randint(1, 5) == 1):
                    chosen = choice(tortie_mid_patterns)
                else:
                    chosen = choice(tortie_low_patterns)
        else:
            if(randint(1, 15) == 1):
                chosen = choice(tortie_high_patterns)
            elif(randint(1, 7) == 1):
                chosen = choice(tortie_mid_patterns)
            else:
                chosen = choice(tortie_low_patterns)

        return chosen        

    def SetFurLength(self, type):
        if 'long' in type or 'lh' in type:
            self.genotype.furLength = ['l', 'l']
        else:
            self.genotype.furLength = ['L', 'L']

        if 'rexed' in type:
            self.genotype.wirehair = ['Wh', 'Wh']
        else:
            self.genotype.wirehair = ['wh', 'wh']    

        if type == 'fur-point':
            self.genotype.sedesp = ['hr', 're']
        else:
            self.genotype.sedesp[0] = "Hr"
        if 'patchy' in type:
            self.furtype[0] = 'patchy ';
        else:
            self.furtype[0] = ''

    def SetEarType(self, type):
        if type == 'folded curl':
            self.genotype.fold[0] = 'Fd'
            self.genotype.curl[0] = 'Cu'
        elif 'fold' in type:
            self.genotype.fold[0] = 'Fd'
            self.genotype.curl[0] = 'cu'
        elif 'curl' in type:
            self.genotype.fold[0] = 'fd'
            self.genotype.curl[0] = 'Cu'
        if 'normal' in type:
            self.genotype.fold[0] = 'fd'
            self.genotype.curl[0] = 'cu'
    
    def GetEarType(self):
        #["Normal", "Folded", "Curled", "Folded Curl"]
        if self.genotype.fold[0] == 'Fd':
            if(self.genotype.curl[0] == 'Cu'):
                return 'Folded Curl'
            else:
                return 'Folded'
        elif self.genotype.curl[0] == 'Cu':
            return 'Curled'
        else:
            return 'Normal'

    def SetTailType(self, type):
        taildict = {
            'full' : 0,
            '3/4' : 5,
            '1/2' : 4,
            '1/3' : 3,
            'stubby' : 2,
            'none' : 1
        }

        self.bobtailnr = taildict[type]

    def GetTailType(self):
        taildict = {
            0 : 'Full',
            5 : '3/4',
            4 : '1/2',
            3 : '1/3',
            2 : 'Stubby',
            1 : 'None'
        }
        
        return taildict[self.bobtailnr]

    def UpdateEyes(self):
        self.genotype.lefteyetype = self.refone + " ; " + self.pigone
        self.genotype.righteyetype = self.reftwo + " ; " + self.pigtwo
        self.genotype.extraeyetype = self.refext + " ; " + self.pigext

    def SetBaseColour(self, base):
        self.colour = base

        if base == 'white':
            self.genotype.white[0] = 'W'
        else:
            self.genotype.white[0] = 'w'
        
        if base == 'albino':
            self.genotype.pointgene[0] = 'c'
        else:
            self.SetPoints(self.point)
        

        if base in ['red', 'cream', 'honey', 'ivory']:
            self.genotype.sexgene = ['O', 'O']
        else:
            if self.tortie:
                self.genotype.sexgene = ['O', 'o']
            else:
                self.genotype.sexgene = ['o', 'o']
        
        if base in ['black', 'blue', 'dove', 'platinum']:
            self.genotype.eumelanin[0] = 'B'
        elif base in ['chocolate', 'lilac', 'champagne', 'lavender']:
            self.genotype.eumelanin[0] = 'b'
        else:
            self.genotype.eumelanin[0] = 'bl'
        
        if base in ['blue', 'platinum', 'lilac', 'lavender', 'fawn', 'beige', 'cream', 'ivory']:
            self.genotype.dilute[0] = 'd'
        else:
            self.genotype.dilute[0] = 'D'
        
        if base in ['dove', 'platinum', 'champagne', 'lavender', 'buff', 'beige', 'honey', 'ivory']:
            self.genotype.pinkdilute[0] = 'dp'
        else:
            self.genotype.pinkdilute[0] = 'Dp'
        
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

        self.genotype.pointgene = gene
            
    def SetTabbyPattern(self, input):
        """{"agouti" : "Agouti", "redbarc" : "Reduced Ticked (Classic)", "redbar" : "Reduced Ticked", "fullbarc" : "Ticked (Classic)", 
                  "fullbar" : "Ticked", "brokenpins" : "Broken Pinstripe", "pinstripe" : "Pinstripe", "servaline" : "Servaline", 
                  "brokenpinsbraid" : "Broken Pinstripe-Braided", "pinsbraided" : "Pinstripe-Braided", 
                  "leopard" : "Servaline-Rosseted", "classic" : "Blotched", "marbled" : "Marbled", "brokenmack" : "Broken Mackerel", 
                  "mackerel" : "Mackerel", "spotted" : "Spotted", "brokenbraid" : "Broken Braided", "braided" : "Braided", 
                  "rosetted" : "Rosetted"}"""
        
        if input == 'agouti':
            self.genotype.ticked = ['Ta', 'Ta']
            self.genotype.ticktype = 'agouti'
        elif input in ['redbarc', 'redbar', 'fullbarc', 'fullbar']:
            self.genotype.ticked = ['Ta', 'ta']
            self.genotype.breakthrough = False
            if 'red' in input:
                self.genotype.ticktype = 'reduced barring'
            else:
                self.genotype.ticktype = 'full barring'
        elif input in ['brokenpins', 'pinstripe', 'servaline', 'brokenpinsbraid', 'pinsbraided', 'leopard']:
            self.genotype.ticked = ['Ta', 'ta']
            self.genotype.breakthrough = True
        else:
            self.genotype.ticked = ['ta', 'ta']

        if input in ['redbarc', 'fullbarc', 'classic', 'marbled']:
            self.genotype.mack = ['mc', 'mc']
        else:
            self.genotype.mack = ['Mc', 'Mc']
        
        if input in ['servaline', 'leopard', 'spotted', 'rosetted']:
            self.genotype.spotsum = 8
        elif 'broken' in input:
            self.genotype.spotsum = 4
        else:
            self.genotype.spotsum = 0

        if input in ['brokenpinsbraid', 'pinsbraided', 'leopard', 'marbled', 'braided', 'brokenbraid', 'rosetted']:
            self.genotype.bengtype = 'bengal'
        else:
            self.genotype.bengtype = 'normal markings'

    def SetTabbyType(self, input):
        self.tabtype = input

        if input == 'Solid':
            self.genotype.agouti = ['a', 'a']
        elif input == 'Twilight Charcoal':
            self.genotype.agouti = ['Apb', 'Apb']
        elif input == 'Midnight Charcoal':
            self.genotype.agouti = ['Apb', 'a']
        else:
            self.genotype.agouti = ['A', 'A']

    def SpriteInfo(self, moons):
        self.maincolour = ""
        self.mainunders = []
        self.spritecolour = ""
        self.caramel = ""
        self.tortpattern = ""
        self.patchmain = ""
        self.patchunders = []
        self.patchcolour = ""

        if self.genotype.pointgene[0] == "c":
            self.spritecolour = "albino"
            self.maincolour = self.spritecolour
        elif self.genotype.white[0] == "W" or (self.genotype.brindledbi and (('o' not in self.genotype.sexgene) or (self.genotype.ext[0] == 'ea' and ((moons > 11 and self.genotype.agouti[0] != 'a') or (moons > 23))) or (self.genotype.ext[0] == 'er' and moons > 23 and 'O' not in self.genotype.sexgene) or (self.genotype.ext[0] == 'ec' and (self.genotype.agouti[0] != 'a' or moons > 5)))):
            self.spritecolour = "white"
            self.maincolour = self.spritecolour
        elif('o' not in self.genotype.sexgene and self.genotype.silver[0] == 'I' and self.genotype.specialred == 'merle'):
            if self.genotype.tortiepattern is not None:
                self.tortpattern = self.genotype.tortiepattern
                main = self.FindRed(self.genotype, moons, 'merle')
                self.maincolour = main[0]
                self.spritecolour = main[1]
                self.mainunders = [main[2], main[3]]
                main = self.FindRed(self.genotype, moons)
                self.patchmain = main[0]
                self.patchcolour = main[1]
                self.patchunders = [main[2], main[3]]
            else:
                self.tortpattern = self.ChooseTortiePattern()
                main = self.FindRed(self.genotype, moons, 'merle')
                self.maincolour = main[0]
                self.spritecolour = main[1]
                self.mainunders = [main[2], main[3]]
                main = self.FindRed(self.genotype, moons)
                self.patchmain = main[0]
                self.patchcolour = main[1]
                self.patchunders = [main[2], main[3]]

                self.genotype.tortiepattern = self.tortpattern
        elif('o' not in self.genotype.sexgene and self.genotype.specialred == 'blue-tipped'):
            self.tortpattern = 'BLUE-TIPPED'
            main = self.FindRed(self.genotype, moons)
            self.maincolour = main[0]
            self.spritecolour = main[1]
            self.mainunders = [main[2], main[3]]
            main = self.FindRed(self.genotype, moons, 'blue-tipped')
            self.patchmain = main[0]
            self.patchcolour = main[1]
            self.patchunders = [main[2], main[3]]

            self.genotype.tortiepattern = self.tortpattern
        elif ('o' not in self.genotype.sexgene) or (self.genotype.ext[0] == 'ea' and ((moons > 11 and self.genotype.agouti[0] != 'a') or (moons > 23))) or (self.genotype.ext[0] == 'er' and moons > 23 and 'O' not in self.genotype.sexgene) or (self.genotype.ext[0] == 'ec' and moons > 0 and (self.genotype.agouti[0] != 'a' or moons > 5)):
            main = self.FindRed(self.genotype, moons, special=self.genotype.ext[0])
            self.maincolour = main[0]
            self.spritecolour = main[1]
            self.mainunders = [main[2], main[3]]
        elif('O' not in self.genotype.sexgene):
            main = self.FindBlack(self.genotype, moons)
            self.maincolour = main[0]
            self.spritecolour = main[1]
            self.mainunders = [main[2], main[3]]
        else:
            if self.genotype.tortiepattern is not None:
                self.tortpattern = self.genotype.tortiepattern
            else:
                self.tortpattern = self.ChooseTortiePattern()
                if randint(1, 10) == 1:
                    self.tortpattern = 'rev'+self.tortpattern

                self.genotype.tortiepattern = self.tortpattern
            
            if 'rev' in self.tortpattern:
                if(self.genotype.brindledbi):
                    self.maincolour = "white"
                    self.spritecolour = "white"
                else:
                    main = self.FindRed(self.genotype, moons)
                    self.maincolour = main[0]
                    self.spritecolour = main[1]
                    self.mainunders = [main[2], main[3]]
                main = self.FindBlack(self.genotype, moons, self.genotype.ext[0])
                self.patchmain = main[0]
                self.patchcolour = main[1]
                self.patchunders = [main[2], main[3]]
            else:
                main = self.FindBlack(self.genotype, moons)
                self.maincolour = main[0]
                self.spritecolour = main[1]
                self.mainunders = [main[2], main[3]]
                if(self.genotype.brindledbi):
                    self.patchmain = "white"
                    self.patchcolour = "white"
                else:
                    main = self.FindRed(self.genotype, moons)
                    self.patchmain = main[0]
                    self.patchcolour = main[1]
                    self.patchunders = [main[2], main[3]]

    def FindEumUnders(self, genes, wideband, rufousing):
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
        if special=='er':
            return self.FindRed(genes, moons, special)
        else:
            if genes.eumelanin[0] == "bl":
                if genes.dilutemd[0] == 'Dm':
                    self.caramel = 'caramel'
                
                if genes.dilute[0] == "d":
                    if(genes.pinkdilute[0] == "dp"):
                        colour = "beige"
                    else:
                        colour = "fawn"
                else:
                    if(genes.pinkdilute[0] == "dp"):
                        colour = "buff"
                    else:
                        colour = "cinnamon"
                        self.caramel = ""
            elif genes.eumelanin[0] == "b":
                if genes.dilutemd[0] == 'Dm':
                    self.caramel = 'caramel'
                
                if genes.dilute[0] == "d":
                    if(genes.pinkdilute[0] == "dp"):
                        colour = "lavender"
                    else:
                        colour = "lilac"
                else:
                    if(genes.pinkdilute[0] == "dp"):
                        colour = "champagne"
                    else:
                        colour = "chocolate"
                        self.caramel = ""
            else:
                if(genes.dilutemd[0] == 'Dm'):
                    self.caramel = 'caramel'
                
                if(genes.dilute[0] == "d"):
                    if(genes.pinkdilute[0] == "dp"):
                        colour = "platinum"
                    else:
                        colour = "blue"
                else:
                    if(genes.pinkdilute[0] == "dp"):
                        colour = "dove"
                    else:
                        colour = "black"
                        self.caramel = ""
            
            maincolour = colour + str(self.genotype.saturation)

            rufousing = ""
            banding = ""
            
            if ('masked' in self.silvergold and genes.wbsum > 15) or (genes.agouti[0] != "a" and genes.ext[0] != "Eg") or (genes.ext[0] not in ['Eg', 'E']):
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
                    unders_colour = self.FindEumUnders(genes, banding, rufousing)
                    unders_opacity = 33
                
                colour = colour + rufousing + banding + "0"
                
            else:
                colour = maincolour        


            return [maincolour, colour, unders_colour, unders_opacity]
    def FindRed(self, genes, moons, special = None):
        unders_colour = 'lightbasecolours0'
        unders_opacity = 0
        maincolour = genes.ruftype
        if special == 'er':
            if(genes.eumelanin[0] == 'B'):
                maincolour = 'rufoused'
            elif(genes.eumelanin[0] == 'b'):
                maincolour = 'medium'
            else:
                maincolour = 'low'
        if(genes.dilute[0] == "d" or (genes.specialred == 'cameo' and genes.silver[0] == 'I') or special == 'merle'):
            if(genes.pinkdilute[0] == "dp"):
                if genes.dilutemd[0] == "Dm":
                    colour = "ivory-apricot"
                else:
                    colour = "ivory"
            else:
                if genes.dilutemd[0] == "Dm" and not(genes.specialred == 'cameo' or special == 'merle'):
                    colour = "apricot"
                else:
                    colour = "cream"
        else:
            if(genes.pinkdilute[0] == "dp"):
                if genes.dilutemd[0] == "Dm":
                    colour = "honey-apricot"
                else:
                    colour = "honey"
            else:
                colour = "red"
        
        maincolour += colour + '0'
        
        rufousing = ""
        banding = ""
        if genes.silver[0] == "I" and special != 'nosilver' or (moons < 3 and genes.karp[0] == "K"):
            rufousing = "silver"
        elif genes.pointgene[0] not in ["C", "cm"] or special=='low':
            rufousing = "low"
        else:
            rufousing = genes.ruftype

        if genes.corin[0] == "sg" or genes.wbtype == "chinchilla":
            banding = "chinchilla"
        elif genes.corin[0] == "sh" or genes.corin[0] == "fg" or genes.wbtype == "shaded":
            banding = "shaded"
        else:
            banding = genes.wbtype


        if colour == "apricot":
            if rufousing == "low":
                colour = "cream"
                rufousing = "medium"
            elif rufousing == "medium":
                colour = "cream"
                rufousing = "rufoused"
            else:
                colour = "red"
                rufousing = "low"
        elif colour == "honey-apricot":
            if rufousing == "low":
                colour = "honey"
                rufousing = "medium"
            elif rufousing == "medium":
                colour = "honey"
                rufousing = "rufoused"
            else:
                colour = "red"
                rufousing = "low"
        elif colour == "ivory-apricot":
            if rufousing == "low":
                colour = "ivory"
                rufousing = "medium"
            elif rufousing == "medium":
                colour = "ivory"
                rufousing = "rufoused"
            else:
                colour = "honey"
                rufousing = "low"
        
        if (genes.ext[0] == "ec" and genes.agouti[0] == "a" and 'o' in genes.sexgene):
            unders_opacity = 0
        elif rufousing == "silver" or (genes.ext[0] == "ec" and genes.agouti[0] != "a" and 'o' in genes.sexgene):
            unders_opacity = self.GetSilverUnders(banding)
        else:
            unders_opacity = self.GetRedUnders(banding)
        colour = colour + rufousing + banding + "0"
        
        if(genes.specialred in ['blue-red', 'cinnamon']) or special == 'blue-tipped':
            colour = colour.replace('cream', 'lilac')
            colour = colour.replace('red', 'blue')
            colour = colour.replace('honey', 'dove')
            colour = colour.replace('ivory', 'lavender')
            if(genes.specialred == 'cinnamon'):
                if('red' in maincolour):
                    maincolour = 'cinnamon3'
                elif('cream' in maincolour or maincolour == 'apricot'):
                    maincolour = 'fawn3'
                elif('honey' in maincolour):
                    maincolour = 'buff3'
                elif('ivory' in maincolour):
                    maincolour = 'beige3'
                
                if('apricot' in maincolour):
                    self.caramel = 'caramel'
            if rufousing != "silver":
                unders_colour = self.FindEumUnders(genes, banding, rufousing)
                unders_opacity = 33
        
        return [maincolour, colour, unders_colour, unders_opacity]
    