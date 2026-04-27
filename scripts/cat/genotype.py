from random import choice, randint, random
import json
from operator import xor
import tomllib
import os

maingame_white = {
    'low': {
        '1': [None, 'SCOURGE', 'BLAZE', 'TAILTIP', 'TOES', 'LUNA', 'LOCKET', "RIGHTEAR", "LEFTEAR", "ESTRELLA", "BACKSPOT", "EYEBAGS"],
        '2': ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'PAWS', 'BROKENBLAZE', 'BEARD', 'BIB', 'VEE', 'HONEY', 'TOESTAIL',
                'RAVENPAW', 'DAPPLEPAW', 'LILTWO', 'MUSTACHE', 'REVERSEHEART', 'SPARKLE', 'REVERSEEYE', "EXTRA", "BLAZEMASK", "TEARS"],
        '3': ['TUXEDO', 'SAVANNAH', 'FANCY', 'DIVA', 'BEARD', 'DAMIEN', 'BELLY', 'SQUEAKS', 'STAR', 'MISS', 'BOWTIE',
                'FCTWO', 'FCONE', 'MIA', 'PRINCESS', 'DOUGIE', "TOPCOVER", "WINGS", "WOODPECKER", "FADEBELLY", "ROSINA"],
        '4': ['TUXEDO', 'SAVANNAH', 'OWL', 'RINGTAIL', 'UNDERS', 'FAROFA', 'VEST', 'FRONT', 'BLOSSOMSTEP', 'DIGIT',
                'HAWKBLAZE', "FADESPOTS", "MITAINE", "SKUNK", "BULLSEYE"],
        '5': ['ANY', 'SHIBAINU', 'FAROFA', 'MISTER', 'PANTS', 'TRIXIE', "SPARROW"]
    },
    'high': {
        '1': ['ANY', 'SHIBAINU', 'PANTSTWO', 'MAO', 'TRIXIE'],
        '2': ['ANY', 'FRECKLES', 'PANTSTWO', 'MASKMANTLE', 'MAO', 'PAINTED', 'BUB', 'SCAR'],
        '3': ['ANYTWO', 'PEBBLESHINE', 'BROKEN', 'PIEBALD', 'FRECKLES', 'HALFFACE', 'GOATEE', 'PRINCE', 'CAPSADDLE',
                'REVERSEPANTS', 'GLASS', 'PAINTED', 'COWTWO', 'SAMMY', 'FINN', 'BUSTER', 'CAKE'],
        '4': ['VAN', 'PEBBLESHINE', 'LIGHTSONG', 'CURVED', 'GOATEE', 'TAIL', 'APRON', 'HALFWHITE', 'APPALOOSA', 'HEART',
                'MOORISH', 'COW', 'SHOOTINGSTAR', 'PEBBLE', 'TAILTWO', 'BUDDY', 'KROPKA'],
        '5': ['ONEEAR', 'LIGHTSONG', 'PETAL', 'CHESTSPECK', 'HEARTTWO', 'BOOTS', 'SHOOTINGSTAR', 'EYESPOT',
                'KROPKA', "BLACKSTAR", "LOVEBUG", "FULLWHITE"]
    }
}
genemod_white = {
    'low': {
        '1': ['chest tuft', 'belly tuft', "left back toes", "right back toes", "left front toes", "right front toes", 'tail tip'],
        '2': ['locket', 'belly spot', 'mustache', "left back mitten", "right back mitten", "left front mitten", "right front mitten", 'chin'],
        '3': ['belly', 'bib', "left back low sock", "right back low sock", "left front low sock", "right front low sock", 'muzzle1', 'muzzle1', 'muzzle2', 'blaze', 'blaze'],
        '4': ['beard', 'chest', "left back high sock", "right back high sock", "left front high sock", "right front high sock", 'belt'],
        '5': ["left back bicolour1", "right back bicolour1", "left front bicolour1", "right front bicolour1", 'underbelly1']
    },
    'high': {
        '1': ['pants'],
        '2': ["left back bicolour2", "right back bicolour2", "left front bicolour2", "right front bicolour2"],
        '3': ['mask n mantle'],
        '4': ['van1', 'van2', 'van3'],
        '5': ["full white"]
    }
}

class Genotype:
    def __init__(self):
        self.odds = {}
        with open("resources/gene_config.toml", "r", encoding="utf-8") as read_file:
            self.odds = tomllib.loads(read_file.read())

        self.furLength = ["L", "L"]
        self.eumelanin = ["B", "B"]
        self.sexgene = ["o", "o"]
        self.specialred = "none"
        self.tortiepattern = []
        self.brindledbi = False
        self.chimera = False
        self.chimerapattern = None
        self.pseudomerle = False
        self.merlepattern = []
        self.gender = ""
        self.dilute = ["D", "D"]
        self.white = ["w", "w"]
        self.whitegrade = randint(1, 5)
        self.white_pattern = [None]
        self.vitiligo = True
        self.deaf = False
        self.fevercoat = False
        self.pointgene = ["C", "C"]
        self.silver = ["i", "i"]
        self.agouti = ["a", "a"]
        self.pangere = None
        self.mack = ["Mc", "Mc"]
        self.ticked = ["ta", "ta"]
        self.breakthrough = False

        self.york = ["yuc", "yuc"]
        self.wirehair = ["wh", "wh"]
        self.laperm = ["lp", "lp"]
        self.cornish = ["R", "R"]
        self.urals = ["Ru", "Ru"]
        self.tenn = ["Tr", "Tr"]
        self.fleece = ["Fc", "Fc"]
        self.sedesp = ["Hr", "Hr"]
        self.ruhr = ["hrbd", "hrbd"]
        self.ruhrmod = ""
        self.lykoi = ["Ly", "Ly"]

        self.pinkdilute = ["Dp", "Dp"]
        self.dilutemd = ["dm", "dm"]
        self.ext = ["E", "E"]
        self.corin = ["N", "N"]
        self.karp = ["k", "k"]
        self.bleach = ["Lb", "Lb"]
        self.ghosting = ["gh", "gh"]
        self.satin = ["St", "St"]
        self.glitter = ["Gl", "Gl"]

        self.curl = ["cu", "cu"]
        self.fold = ["fd", "fd"]
        self.fourear = ["Dup", "Dup"]
        self.manx = ["ab", "ab"]
        self.manxtype = choice(["long", "most", "most", "stubby", "stubby", "stubby", "stubby", "stubby", "stubby", "stumpy", "stumpy", "stumpy", "stumpy", "stumpy", "stumpy", "stumpy", "stumpy", "riser", "riser", "riser", "riser", "riser", "riser", "riser", "riser", "riser", "rumpy", "rumpy", "rumpy", "rumpy", "rumpy", "rumpy", "rumpy", "rumpy", "rumpy", "rumpy"])
        self.kab = ["Kab", "Kab"]
        self.toybob = ["tb", "tb"]
        self.jbob = ["Jb", "Jb"]
        self.kub = ["kub", "kub"]
        self.ring = ["Rt", "Rt"]
        self.munch = ["mk", "mk"]
        self.poly = ["pd", "pd"]
        self.pax3 = ["NoDBE", "NoDBE"]

        self.wideband = ""
        self.wbtype = "medium"
        self.wbsum = 7

        self.rufousing = ""
        self.ruftype = "medium"
        self.rufsum = 4

        self.unders_ruf = ""
        self.unders_ruftype = "medium"
        self.unders_rufsum = 4

        self.rednose = False
        self.blacknose = False

        self.saturation = 3

        self.bengal = ""
        self.bengtype = "normal markings"
        self.bengsum = 0

        self.sokoke = ""
        self.soktype = "normal markings"
        self.soksum = 0

        self.spotted = ""
        self.spottype = "broken stripes"
        self.spotsum = 4

        self.tickgenes = ""
        self.ticktype = "full barring"
        self.ticksum = 0

        self.refraction = ""
        self.refgrade = ""
        self.refsum = 0

        self.pigmentation = ""
        self.piggrade = ""
        self.pigsum = 0

        self.lefteye = ""
        self.righteye = ""
        self.lefteyetype = "R11 ; P11"
        self.righteyetype = "R11 ; P11"

        self.extraeye = None
        self.extraeyetype = ""
        self.extraeyecolour = ""

    def __getitem__(self, name):
        return getattr(self, name)

    def toJSON(self):
        return {
            "fevercoat" : self.fevercoat,
            "furLength": self.furLength,
            "longtype": self.longtype,
            "eumelanin": self.eumelanin,
            "sexgene" : self.sexgene,
            "specialred" : self.specialred,
            "tortiepattern" : self.tortiepattern,
            "brindledbi" : self.brindledbi,

            "pseudomerle" : self.pseudomerle,
            "merlepattern" : self.merlepattern,

            "sex": self.sex,
            "dilute": self.dilute,
            "white" : self.white,
            "whitegrade" : self.whitegrade,
            "vitiligo" : self.white_pattern[0] is not None,
            "pointgene" : self.pointgene,
            "silver" : self.silver,
            "agouti" : self.agouti,
            "pangere" : self.pangere,
            "blacknose" : self.blacknose,
            "rednose" : self.rednose,
            "mack" : self.mack,
            "ticked" : self.ticked,
            "breakthrough" : self.breakthrough,
            "sheeted" : self.sheeted,

            "wirehair" : self.wirehair,
            "laperm" : self.laperm,
            "cornish" : self.cornish,
            "urals" : self.urals,
            "tenn" : self.tenn,
            "fleece" : self.fleece,
            "sedesp" : self.sedesp,
            "ruhr" : self.ruhr,
            "ruhrmod" : self.ruhrmod,
            "lykoi" : self.lykoi,

            "pinkdilute" : self.pinkdilute,
            "dilutemd" : self.dilutemd,
            "ext" : self.ext,
            "corin" : self.corin,
            "karp" : self.karp,
            "bleach" : self.bleach,
            "ghosting" : self.ghosting,
            "satin" : self.satin,
            "glitter" : self.glitter,

            "curl" : self.curl,
            "fold" : self.fold,
            "fourear": self.fourear,
            "manx" : self.manx,
            "manxtype" : self.manxtype,
            "kab" : self.kab,
            "toybob" : self.toybob,
            "jbob" : self.jbob,
            "kub" : self.kub,
            "ring" : self.ring,
            "munch" : self.munch,
            "poly" : self.poly,
            "pax3" : self.pax3,

            "wideband" : self.wideband,
            "saturation" : self.saturation,
            "rufousing" : self.rufousing,
            "unders_ruf": self.unders_ruf,
            "bengal" : self.bengal,
            "sokoke" : self.sokoke,
            "spotted" : self.spotted,
            "tickgenes" : self.tickgenes,
            "refraction" :self.refraction,
            "pigmentation" : self.pigmentation,
            
            "lefteye" : self.lefteye,
            "righteye" : self.righteye,
            "lefteyetype" :self.lefteyetype,
            "righteyetype" : self.righteyetype,
            
            "extraeye" : self.extraeye,
            "extraeyetype" :self.extraeyetype,
            "extraeyecolour" : self.extraeyecolour,

            "body_type" : self.body_value,
            "height" : self.height_value,
            "growth_pattern": "average",

            "breeds" : {},
            "somatic" : {},
            "april_fools" : {}
        }

    def fill(self):

        self.body_value = randint(1, sum(self.odds["body_ranges"]))
        self.height_value = randint(1, sum(self.odds["height_ranges"]))

        # FUR
        a = randint(1, 4)

        if a == 1:
            self.ruhrmod = ["hi", "hi"]
        elif a == 4:
            self.ruhrmod = ["ha", "ha"]
        else:
            self.ruhrmod = ["hi", "ha"]

        if self.ruhr[0] == "Hrbd":
            self.ruhrmod = ["hi", "ha"]

        is_hairless = self.sedesp == ["hr", "hr"]
            
        if self.furLength[0] == "L":
            self.furLength[1] = "l" if random() < 1/self.odds["longhair"] else "L"
            self.longtype = choice(self.odds["longtype"])
        else:
            self.longtype = "long"

        if self.sedesp == ["hr", "hr"] and random() < 0.4:
            self.ruhr = ["Hrbd", "hrbd" if self.ruhrmod == ["ha", "ha"] and random() < 0.5 else "Hrbd"]
        elif self.sedesp == ["hr", "hr"]:
            for i in range(2):
                self.ruhr[i] = "Hrbd" if random() < 1/self.odds["russian hairless"] else "hrbd"

        if self.lykoi[0] != "ly":
            for i in range(2):
                self.lykoi[i] = "ly" if random() < 1/self.odds["lykoi"] else "Ly"
            if self.lykoi == ["ly", "ly"]:
                self.lykoi[0] == "Ly"

        if self.sedesp[0] == "hr":
            for i in range(2):
                self.furLength[i] = "l" if random() < 1/self.odds["longhair"] else "L"

                self.wirehair[i] = "Wh" if random() < 1/self.odds["wirehair"] else "wh"
                self.laperm[i] = "Lp" if random() < 1/self.odds["laperm"] else "lp"
                self.cornish[i] = "r" if random() < 1/self.odds["cornish"] else "R"
                self.urals[i] = "ru" if random() < 1/self.odds["urals"] else "Ru"
                self.tenn[i] = "tr" if random() < 1/self.odds["tenn"] else "Tr"
                self.fleece[i] = "fc" if random() < 1/self.odds["fleece"] else "Fc"
                self.ruhr[i] = "Hrbd" if random() < 1/self.odds["russian hairless"] else "hrbd"
            if self.sedesp[0] == "Hr":
                for i in range(2):
                    if random() < 1/self.odds["canadian hairless"]:
                        self.sedesp[i] = "hr"
                    elif random() < 1/self.odds["selkirk"]:
                        self.sedesp[i] = "Se"
                    elif random() < 1/self.odds["devon"]:
                        self.sedesp[i] = "re"
            self.longtype = choice(self.odds["longtype"])
        elif self.wirehair[0] == "Wh":
            if self.furLength[0] == "l":
                main = choice(["wirehair", "laperm", "urals", "tenn", "fleece", "selkirk"])
            else:
                main = choice(["wirehair", "laperm", "cornish", "urals", "tenn", "fleece", "devon", "selkirk"])

            for i in range(2):
                self.wirehair[i] = "Wh" if random() < 1/self.odds["wirehair"] or (main == "wirehair" and "Wh" not in self.wirehair) else "wh"
                self.laperm[i] = "Lp" if random() < 1/self.odds["laperm"] or (main == "laperm" and "Lp" not in self.laperm) else "lp"
                self.cornish[i] = "r" if random() < 1/self.odds["cornish"] or main == "cornish" else "R"
                self.urals[i] = "ru" if random() < 1/self.odds["urals"] or main == "urals" else "Ru"
                self.tenn[i] = "tr" if random() < 1/self.odds["tenn"] or main == "tenn" else "Tr"
                self.fleece[i] = "fc" if random() < 1/self.odds["fleece"] or main == "fleece" else "Fc"
                if random() < 1/self.odds["devon"] or main == "devon":
                    self.sedesp[i] = "re"
                elif random() < 1/self.odds["selkirk"] or (main == "selkirk" and "Se" not in self.sedesp):
                    self.sedesp[i] = "Se"
                elif random() < 1/self.odds["canadian hairless"] and i == 1 and "re" not in self.sedesp:
                    self.sedesp[i] = "hr"
                if self.ruhrmod == ["hi", "hi"] and self.furLength[0] == "L":
                    self.ruhr[i] = "Hrbd" if random() < 1/self.odds["russian hairless"] else "hrbd"
            
            if self.furLength[0] == "l":
                if self.cornish == ["r", "r"]:
                    self.cornish[0] == "R"
                if self.sedesp == ["re", "re"]:
                    self.sedesp[0] == "Hr"
        else:
            for i in range(2):
                self.cornish[i] = "r" if random() < 1/self.odds["cornish"] else "R"
                self.urals[i] = "ru" if random() < 1/self.odds["urals"] else "Ru"
                self.tenn[i] = "tr" if random() < 1/self.odds["tenn"] else "Tr"
                self.fleece[i] = "fc" if random() < 1/self.odds["fleece"] else "Fc"
                if random() < 1/self.odds["devon"]:
                    self.sedesp[i] = "re"
                elif random() < 1/self.odds["canadian hairless"]:
                    self.sedesp[i] = "hr"

            if self.cornish == ["r", "r"]:
                self.cornish[0] == "R"
            if self.tenn == ["tr", "tr"]:
                self.tenn[0] == "Tr"
            if self.fleece == ["fc", "fc"]:
                self.fleece[0] == "Fc"
            if self.urals == ["ru", "ru"]:
                self.urals[0] == "Ru"
            if "Hr" not in self.sedesp[0]:
                self.sedesp[0] == "Hr"

        # BODY

        if self.curl[0] == "Cu":
            self.curl[1] = "Cu" if random() < 1/self.odds["curl"] else "cu"
        self.fourear[1] = "dup" if random() < 1/self.odds["four_ears"] else "Dup"
        for i in range(2):
            self.munch[i] = "Mk" if random() < 1/self.odds["munchkin"] and "Mk" not in self.munch else "mk"
            self.ring[i] = "rt" if random() < 1/self.odds["ringtail"] else "Rt"
            self.poly[i] = "Pd" if random() < 1/self.odds["polydactyl"] else "pd"

        if self.bobtailnr > 0:
            for i in range(2):
                self.kab[i] = "kab" if random() < 1/self.odds["karelian bobtail"] else "Kab"
            if self.kab == ["kab", "kab"]:
                self.kab[0] == "Kab"
            if self.bobtailnr < 3:
                for i in range(2):
                    self.kub[i] = "Kub" if random() < 1/self.odds["kurilian bobtail"] else "kub"
                    self.jbob[i] = "jb" if random() < 1/self.odds["japanese bobtail"] else "Jb"
                    self.toybob[i] = "Tb" if random() < 1/self.odds["toybob"] else "tb"
                    if "M" not in self.manx and "Ab" not in self.manx:
                        if random() < 1/self.odds["manx"]:
                            self.manx[i] = "M"
                        elif random() < 1/self.odds["american bobtail"]:
                            self.manx[i] = "Ab"

            if self.bobtailnr == 1:
                self.manx = ["M", "m"]
                self.manxtype = choice(["rumpy", "riser"])
            elif self.bobtailnr == 2:
                if "M" in self.manx:
                    self.manx = ["ab", "ab"]
                if "Kab" in self.kab and "tb" in self.toybob and "Kub" not in self.kub and "Jb" in self.jbob and (self.manxtype not in ["rumpy", "riser"] or "Ab" not in self.manx):
                    main = choice(["karel", "toybob", "kuril", "jbob", "am"])
                    if main == "am":
                        self.manxtype = choice(["rumpy", "riser"])
                    for i in range(2):
                        self.kab[i] = "kab" if random() < 1/self.odds["karelian bobtail"] or main == "karel" else "Kab"
                        self.kub[i] = "Kub" if random() < 1/self.odds["kurilian bobtail"] or (main == "kuril" and "Kub" not in self.kub) else "kub"
                        self.jbob[i] = "jb" if random() < 1/self.odds["japanese bobtail"] or main == "jbob" else "Jb"
                        self.toybob[i] = "Tb" if random() < 1/self.odds["toybob"] or main == "toybob" else "tb"
                        self.manx[i] = "Ab" if "Ab" not in self.manx and (random() < 1/self.odds["american bobtail"] or main == "am") else "ab"
            elif self.bobtailnr == 3:
                main = choice(["am", "manx", "toybob", "jbob"])
                for i in range(2):
                    self.jbob[i] = "jb" if "jb" not in self.jbob and ((random() < 1/self.odds["japanese bobtail"]) or main == "jbob") else "Jb"
                    self.toybob[i] = "Tb" if "Tb" not in self.toybob and (random() < 1/self.odds["toybob"] or main == "toybob") else "tb"
                    if main == "am" or random() < 1/self.odds["american bobtail"] and self.manx == ["ab", "ab"]:
                        self.manx[i] = "Ab"
                        self.manxtype = choice(["stubby", "stubby", "stubby", "stumpy", "stumpy", "stumpy", "stumpy"])
                    if main == "manx" or random() < 1/self.odds["manx"] and self.manx == ["ab", "ab"]:
                        self.manx[i] = "M"
                        self.manxtype = "stumpy" if main == "manx" else choice(["long", "most", "most", "stubby", "stubby", "stubby", "stubby", "stubby", "stubby", "stumpy", "stumpy", "stumpy", "stumpy", "stumpy", "stumpy", "stumpy", "stumpy"])
            elif self.bobtailnr == 4:
                main = choice(["am", "manx", "toybob", "jbob"])
                self.manxtype = choice(["long", "most"])
                for i in range(2):
                    self.jbob[i] = "jb" if "jb" not in self.jbob and ((random() < 1/self.odds["japanese bobtail"]) or main == "jbob") else "Jb"
                    self.toybob[i] = "Tb" if "Tb" not in self.toybob and (random() < 1/self.odds["toybob"] or main == "toybob") else "tb"
                    if (main == "am" or random() < 1/self.odds["american bobtail"]) and self.manx == ["ab", "ab"]:
                        self.manx[i] = "Ab"
                    if (main == "manx" or random() < 1/self.odds["manx"]) and self.manx == ["ab", "ab"]:
                        self.manx[i] = "M"
                        self.manxtype = "stubby" if main == "manx" else choice(["long", "most", "most", "stubby", "stubby", "stubby", "stubby", "stubby", "stubby"])
            elif self.bobtailnr == 5:
                self.manx = ["M", "m"]
                self.manxtype = "most"

        # EYES
        self.refraction = int(self.lefteyetype.split(" ; ")[0][1:])
        pig = None
        if "blue" not in self.lefteyetype and "albino" not in self.lefteyetype:
            pig = int(self.lefteyetype.split(" ; ")[1][1:])
        elif "blue" not in self.righteyetype and "albino" not in self.righteyetype:
            pig = int(self.lefteyetype.split(" ; ")[1][1:])

        if pig and (self.pointgene == ["cb", "cs"] or self.pointgene[0] == "cm"):
            pig *= 2
        if not pig:
            pig = randint(1, 11)
        self.pigmentation = pig

        if self.odds["DBE"] > 0 and randint(1, self.odds["DBE"] ** 2) == 1:
            self.pax3 = ['DBEalt', choice(['DBEcel', 'DBEcel', 'DBEre', 'DBEalt', 'DBEalt'])]
        elif self.odds["DBE"] > 0 and randint(1, self.odds["DBE"]) == 1:
            self.pax3[0] = choice(['DBEcel', 'DBEcel', 'DBEre', 'DBEalt', 'DBEalt'])

        # COLOURS
        if self.white[0] == "W" or self.pointgene[0] == "c":
            for i in range(2):
                if self.odds["cinnamon"] > 0 and randint(1, self.odds["cinnamon"]) == 1:
                    self.eumelanin[i] = "bl"
                elif self.odds["chocolate"] > 0 and randint(1, self.odds["chocolate"]) == 1:
                    self.eumelanin[i] = "b"
                else:
                    self.eumelanin[i] = "B"

                self.dilute[i] = "d" if randint(1, self.odds["dilute"]) == 1 else "D"
                self.pinkdilute[i] = "dp" if randint(1, self.odds["pink-eyed dilute"]) == 1 else "Dp"

                if self.white[0] != "W" or i == 1:
                    if self.odds["birman gloving"] > 0 and randint(1, self.odds["birman gloving"]) == 1:
                        self.white[i] = "wg"
                    elif self.odds["thai white"] > 0 and randint(1, self.odds["thai white"]) == 1:
                        self.white[i] = "wt"
                    elif self.odds["salmiak"] > 0 and randint(1, self.odds["salmiak"]) == 1:
                        self.white[i] = "wsal"
                    elif self.odds["dominant white"] > 0 and randint(1, self.odds["dominant white"]) == 1:
                        self.white[i] = "W"
                    elif self.odds["white spotting"] > 0 and randint(1, self.odds["white spotting"]) == 1:
                        self.white[i] = "ws"
                    else:
                        self.white[i] = "w"

            if self.odds['X monosomy'] > 0 and randint(1, self.odds['X monosomy']) == 1:
                self.sexgene = [""]
            elif self.odds['XXX/XXY'] > 0 and randint(1, self.odds['XXX/XXY']) == 1:
                self.sexgene = ["", "", ""]
            else:
                self.sexgene = ["", ""]

            for i in range(len(self.sexgene)):
                if self.odds["red"] > 0 and randint(1, self.odds["red"]) == 1:
                    self.sexgene[i] = "O"
                else:
                    self.sexgene[i] = "o"
        else:
            if self.sexgene == ["O", "O"]:
                for i in range(2):
                    if self.odds["cinnamon"] > 0 and randint(1, self.odds["cinnamon"]) == 1:
                        self.eumelanin[i] = "bl"
                    elif self.odds["chocolate"] > 0 and randint(1, self.odds["chocolate"]) == 1:
                        self.eumelanin[i] = "b"
                    else:
                        self.eumelanin[i] = "B"
            else:
                if self.eumelanin[0] == "B":
                    for i in range(2):
                        if self.odds["cinnamon"] > 0 and randint(1, self.odds["cinnamon"]) == 1:
                            self.eumelanin[i] = "bl"
                        elif self.odds["chocolate"] > 0 and randint(1, self.odds["chocolate"]) == 1:
                            self.eumelanin[i] = "b"
                        else:
                            self.eumelanin[i] = "B"
                    if "B" not in self.eumelanin:
                        self.eumelanin[0] = "B"
                elif self.eumelanin[0] == "b":
                    for i in range(2):
                        self.eumelanin[i] = "bl" if self.odds["cinnamon"] > 0 and randint(1, self.odds["cinnamon"]) == 1 else "b"
                    if "b" not in self.eumelanin:
                        self.eumelanin[0] = "b"
                else:
                    self.eumelanin = ["bl", "bl"]
            if self.sexgene == ["O", "o"]:
                if self.odds['XXX/XXY'] > 0 and randint(1, self.odds['XXX/XXY']) == 1:
                    self.sexgene.append(choice(["Y", "Y", "O", "o"]))
            else:      
                first = self.sexgene[0]  
                if self.odds['X monosomy'] > 0 and randint(1, self.odds['X monosomy']) == 1:
                    self.sexgene = [""]
                elif self.odds['XXX/XXY'] > 0 and randint(1, self.odds['XXX/XXY']) == 1:
                    self.sexgene = ["", "", ""]
                else:
                    self.sexgene = ["", ""]

                for i in range(len(self.sexgene)):
                    self.sexgene[i] = first
            
            if self.dilute[0] == "D":
                self.dilute[1] = "d" if self.odds["dilute"] > 0 and randint(1, self.odds["dilute"]) == 1 else "D"
            else:
                self.dilute[1] = "d"
            if self.pinkdilute[0] == "Dp":
                for i in range(2):
                    self.pinkdilute[i] = "dp" if self.odds["pink-eyed dilute"] > 0 and randint(1, self.odds["pink-eyed dilute"]) == 1 else "Dp"
                if "Dp" not in self.pinkdilute:
                    self.pinkdilute[0] = "Dp"
            else:
                self.pinkdilute[1] = "dp"

            if self.pointgene[0] == "C":
                for i in range(2):
                    if self.odds["albino"] > 0 and randint(1, self.odds["albino"]) == 1:
                        self.pointgene[i] = "c"
                    elif self.odds["mocha"] > 0 and randint(1, self.odds["mocha"]) == 1:
                        self.pointgene[i] = "cm"
                    elif self.odds["sepia"] > 0 and randint(1, self.odds["sepia"]) == 1:
                        self.pointgene[i] = "cb"
                    elif self.odds["colourpoint"] > 0 and randint(1, self.odds["colourpoint"]) == 1:
                        self.pointgene[i] = "cs"
                    else:
                        self.pointgene[i] = "C"
                if "C" not in self.pointgene:
                    self.pointgene[0] = "C"

            is_thai = False
            if self.white[0] == "wsal":
                self.white = ["wsal", "wsal"]
            elif self.white_pattern == ["left front mitten", "right front mitten", "left back mitten", "right back mitten"] and random() < 0.1:
                self.white = "wg", "wg"
            else:
                if "dorsal1" in self.white_pattern or "dorsal2" in self.white_pattern:
                    is_thai = True

                no_breaks = [pat for pat in self.white_pattern[1:] if "break/" not in pat]
                if not no_breaks:
                    if random() < 0.05:
                        self.white = ["ws", "w"]
                        self.whitegrade = 1
                    else:
                        self.white = ["w", "w"]

                else:
                    highest = 0
                    for pat in no_breaks:
                        for i, l in enumerate(["high", "low"]):
                            for k in range(5, 0, -1):
                                if pat in maingame_white[l][str(k)] and k + 5 - (i*5) > highest:
                                    highest = k + 5 - (i*5)
                                    break
                                if pat in genemod_white[l][str(k)] and k + 5 - (i*5) > highest:
                                    highest = k + 5 - (i*5)
                                    break
                    self.whitegrade = highest % 5 + 1
                    if highest < 5:
                        self.white = ["wt", "w"] if is_thai else ["ws", "w"]
                    else:
                        self.white = ["wt", "ws"] if is_thai else ["ws", "ws"]
                        if is_thai and self.odds["thai white"] > 0 and randint(1, self.odds["thai white"]) == 1:
                            self.white[1] = ["wt"]

                if "w" in self.white:
                    self.white[1] = "wg" if self.odds["birman gloving"] > 0 and randint(1, self.odds["birman gloving"]) == 1 else "w"
        
        if random() < 0.5 and len(self.sexgene) > 1:
            self.sexgene[-1] = "Y"
            self.sex = "tom"
        else:
            self.sex = "molly"

        if self.ext[0] != "E":
            self.ext[1] = self.ext[0]
        elif self.ext == ["E", "ec"]:
            pass
        else:
            is_grizzle = self.ext[0] == "Eg"
            for i in range(2):
                if self.odds["grizzle"] > 0 and randint(1, self.odds["grizzle"]) == 1:
                    self.ext[i] = "Eg"
                elif self.odds["carnelian"] > 0 and randint(1, self.odds["carnelian"]) == 1:
                    self.ext[i] = "ec"
                elif self.odds["russet"] > 0 and randint(1, self.odds["russet"]) == 1:
                    self.ext[i] = "er"
                elif self.odds["amber"] > 0 and randint(1, self.odds["amber"]) == 1:
                    self.ext[i] = "ea"
            if "Eg" not in self.ext and is_grizzle:
                self.ext[0] = "Eg"
            if "E" not in self.ext and not is_grizzle:
                self.ext[0] = "E"

        if self.dilutemd[0] == "Dm":
            self.dilutemd[1] = "Dm" if self.odds["dilute modifier"] > 0 and randint(1, self.odds["dilute modifier"]) == 1 else "dm"
        else:
            self.dilutemd[1] = "dm"

        if self.bleach[0] == "Lb":
            self.bleach[1] = "lb" if self.odds["bleaching"] > 0 and randint(1, self.odds["bleaching"]) == 1 else "Lb"
        else:
            self.bleach[1] = "lb"

        if self.ghosting[0] == "Gh":
            self.ghosting[1] = "Gh" if self.odds["ghosting"] > 0 and randint(1, self.odds["ghosting"]) == 1 else "gh"
        else:
            self.ghosting[1] = "gh"

        if self.satin[0] == "St":
            self.satin[1] = "st" if self.odds["satin"] > 0 and randint(1, self.odds["satin"]) == 1 else "St"
        else:
            if self.agouti[0] == "A":
                if random() < 0.5:
                    self.glitter = ["gl", "gl"]
                else:
                    self.satin[1] = "st"
            else:
                self.satin[1] = "st"

        # TABBY

        if self.silver[0] == "I":
            self.silver[1] = "I" if self.odds["silver"] > 0 and randint(1, self.odds["silver"]) == 1 else "i"
        else:
            self.silver[1] = "i"

        if self.agouti[0] == "A":
            if self.corin[0] == "sh2":
                self.agouti[1] = "a"
            elif self.odds["charcoal"] > 0 and randint(1, self.odds["charcoal"]) == 1:
                self.agouti[1] = "Apb"
            elif self.odds["solid"] > 0 and randint(1, self.odds["solid"]) == 1:
                self.agouti[1] = "a"
            else:
                self.agouti[1] = "A"

        if "sh2" in self.corin:
            self.corin = ["sh", "sh"]
        if self.odds["sunshine"] > 0 and randint(1, self.odds["sunshine"]) == 1 and self.corin[0] != "fg":
            self.corin[1] = "sh"
        elif self.odds["extreme sunshine"] > 0 and randint(1, self.odds["extreme sunshine"]) == 1 and self.corin[0] in ["N", "sg"]:
            self.corin[1] = "sg"
        elif self.odds["copper"] > 0 and randint(1, self.odds["copper"]) == 1:
            self.corin[1] = "fg"
        else:
            self.corin[1] = "N"
        
        if self.ticked[0] == "Ta":
            self.sheeted = self.odds["dense_blotched"] > 0 and randint(1, self.odds["dense_blotched"]) == 1
            if self.breakthrough:
                self.ticked[1] = "ta"
                if self.mack[0] == "Mc":
                    self.mack[1] = "mc" if self.odds["blotched"] > 0 and randint(1, self.odds["blotched"]) == 1 else "Mc"
            else:
                for i in range(2):
                    self.mack[i] = "mc" if self.odds["blotched"] > 0 and randint(1, self.odds["blotched"]) == 1 else "Mc"
            if self.odds["ticked"] > 0 and randint(1, self.odds["ticked"]) == 1:
                self.ticked[1] = "Ta"
                self.breakthrough = self.odds["breakthrough"] > 0 and randint(1, self.odds["breakthrough"]) == 1
        else:
            self.breakthrough = self.odds["breakthrough"] > 0 and randint(1, self.odds["breakthrough"]) == 1
            if self.mack[0] == "Mc":
                self.sheeted = self.odds["dense_blotched"] > 0 and randint(1, self.odds["dense_blotched"]) == 1
                self.mack[1] = "mc" if self.odds["blotched"] > 0 and randint(1, self.odds["blotched"]) == 1 else "Mc"

        # POLYGENES

        wbtypes = ["low", "medium", "high", "shaded", "chinchilla"]
        ruftypes = ["low", "medium", "rufoused"]    
        spottypes = ["fully striped", "slightly broken", "broken stripes", "mostly broken", "spotted"]
        ticktypes = ["full barring", "reduced barring", "agouti"]
        bengtypes = ["normal markings", "mild bengal", "full bengal"]
        soktypes = ["normal markings", "mild fading", "full sokoke"]
            

        for i in range(0, 8):
            self.wideband += choice(self.odds["wideband"])
            self.wbsum += int(self.wideband[i])
        ranges = [6, 10, 12, 14, 17]
        index = wbtypes.index(self.wbtype)
        matched = False
        while not matched:
            matched = True
            if index == 0:
                if self.wbsum < ranges[0]:
                    matched = False
            else:
                if ranges[index]-1 < self.wbsum < ranges[index]:
                    matched = False

            if not matched:
                self.wideband = ""
                for i in range(0, 8):
                    self.wideband += choice(self.odds["wideband"])
                    self.wbsum += int(self.wideband[i])

        for i in range(0, 4):
            self.rufousing += choice(self.odds["rufousing"])
            self.rufsum += int(self.rufousing[i])
        ranges = [3, 6, 9]
        index = ruftypes.index(self.ruftype)
        matched = False
        while not matched:
            matched = True
            if index == 0:
                if self.rufsum < ranges[0]:
                    matched = False
            else:
                if ranges[index]-1 < self.rufsum < ranges[index]:
                    matched = False

            if not matched:
                self.rufousing = ""
                for i in range(0, 4):
                    self.rufousing += choice(self.odds["rufousing"])
                    self.rufsum += int(self.rufousing[i])

        for i in range(0, 4):
            self.unders_ruf += choice(self.odds["rufousing"])
            self.unders_rufsum += int(self.unders_ruf[i])
        ranges = [3, 6, 9]
        index = ruftypes.index(self.ruftype)
        matched = False
        while not matched:
            matched = True
            if index == 0:
                if self.unders_rufsum < ranges[0]:
                    matched = False
            else:
                if ranges[index]-1 < self.unders_rufsum < ranges[index]:
                    matched = False

            if not matched:
                self.unders_ruf = ""
                for i in range(0, 4):
                    self.unders_ruf += choice(self.odds["rufousing"])
                    self.unders_rufsum += int(self.rufousing[i])

        for i in range(0, 4):
            self.spotted += choice(self.odds["spotted"])
            self.spotsum += int(self.spotted[i])
        ranges = [3, 6, 9]
        index = spottypes.index(self.spottype)
        matched = self.ticked[0] != "Ta" or not self.breakthrough or self.mack[0] != "mc"
        while not matched:
            matched = True
            if index == 0:
                if self.spotsum < ranges[0]:
                    matched = False
            else:
                if ranges[index]-1 < self.spotsum < ranges[index]:
                    matched = False

            if not matched:
                self.spotted = ""
                for i in range(0, 4):
                    self.spotted += choice(self.odds["spotted"])
                    self.spotsum += int(self.spotted[i])

        for i in range(0, 4):
            self.tickgenes += choice(self.odds["tickmod"])
            self.ticksum += int(self.tickgenes[i])
        ranges = [3, 6, 9]
        index = ticktypes.index(self.ticktype)
        matched = self.ticked[0] != "Ta"
        while not matched:
            matched = True
            if index == 0:
                if self.ticksum < ranges[0]:
                    matched = False
            else:
                if ranges[index]-1 < self.ticksum < ranges[index]:
                    matched = False

            if not matched:
                self.tickgenes = ""
                for i in range(0, 4):
                    self.tickgenes += choice(self.odds["tickmod"])
                    self.ticksum += int(self.tickgenes[i])

        for i in range(0, 4):
            self.bengal += choice(self.odds["bengal"])
            self.bengsum += int(self.bengal[i])
        ranges = [3, 6, 9]
        index = bengtypes.index(self.bengtype)
        matched = self.ticked[0] != "Ta" or not self.breakthrough
        while not matched:
            matched = True
            if index == 0:
                if self.bengsum < ranges[0]:
                    matched = False
            else:
                if ranges[index]-1 < self.bengsum < ranges[index]:
                    matched = False

            if not matched:
                self.bengal = ""
                for i in range(0, 4):
                    self.bengal += choice(self.odds["bengal"])
                    self.bengsum += int(self.bengal[i])

        for i in range(0, 4):
            self.sokoke += choice(self.odds["sokoke"])
            self.soksum += int(self.sokoke[i])
        ranges = [3, 6, 9]
        index = soktypes.index(self.soktype)
        matched = False
        while not matched:
            matched = True
            if index == 0:
                if self.soksum < ranges[0]:
                    matched = False
            else:
                if ranges[index]-1 < self.soksum < ranges[index]:
                    matched = False
            if not matched:
                self.sokoke = ""
                for i in range(0, 4):
                    self.sokoke += choice(self.odds["sokoke"])
                    self.soksum += int(self.sokoke[i])

    def genesort(self):
        for gene in ["furLength", "dilute", 'silver', 'mack', 'ticked',
                     'wirehair', 'laperm', 'cornish', 'urals', 'tenn', 'fleece', 'ruhr', 'lykoi',
                     'pinkdilute', 'dilutemd', 'karp', 'bleach', 'ghosting', 'satin', 'glitter',
                     'curl', 'fold', "fourear", 'kab', 'toybob', 'jbob', 'kub', 'ring', 'munch', 'poly']:
            self[gene].sort()

        if self.eumelanin[0] == "bl":
            self.eumelanin[0] = self.eumelanin[1]
            self.eumelanin[1] = "bl"
        elif self.eumelanin[0] == "b" and self.eumelanin[1] == "B":
            self.eumelanin[0] = "B"
            self.eumelanin[1] = "b"

        self.sexgene.sort(key=lambda s: (s.lower(), s))

        if self.white[0] == "wsal":
            self.white[0] = self.white[1]
            self.white[1] = "wsal"
        elif self.white[0] == "wg" and self.white[1] != "wsal":
            self.white[0] = self.white[1]
            self.white[1] = "wg"
        elif self.white[0] == "w" and self.white[1] not in ["wsal", "wg"]:
            self.white[0] = self.white[1]
            self.white[1] = "w"
        elif self.white[0] == "wt" and self.white[1] not in ["wsal", "wg", "w"]:
            self.white[0] = self.white[1]
            self.white[1] = "wt"
        elif self.white[1] == "W":
            self.white[1] = self.white[0]
            self.white[0] = "W"

        if self.pointgene[0] == "c":
            self.pointgene[0] = self.pointgene[1]
            self.pointgene[1] = "c"
        elif self.pointgene[0] == "cm" and self.pointgene[1] != "c":
            self.pointgene[0] = self.pointgene[1]
            self.pointgene[1] = "cm"
        elif self.pointgene[0] == "cs" and self.pointgene[1] not in ["c", "cm"]:
            self.pointgene[0] = self.pointgene[1]
            self.pointgene[1] = "cs"
        elif self.pointgene[1] == "C":
            self.pointgene[1] = self.pointgene[0]
            self.pointgene[0] = "C"

        if self.agouti[0] == "a":
            self.agouti[0] = self.agouti[1]
            self.agouti[1] = "a"
        elif self.agouti[0] == "Apb" and self.agouti[1] != "a":
            self.agouti[0] = self.agouti[1]
            self.agouti[1] = "Apb"

        if self.sedesp[0] == "re":
            self.sedesp[0] = self.sedesp[1]
            self.sedesp[1] = "re"
        elif self.sedesp[0] == "hr" and self.sedesp[1] != "re":
            self.sedesp[0] = self.sedesp[1]
            self.sedesp[1] = "hr"
        elif self.sedesp[1] == "Se":
            self.sedesp[1] = self.sedesp[0]
            self.sedesp[0] = "Se"

        if self.ext[0] == "ec":
            self.ext[0] = self.ext[1]
            self.ext[1] = "ec"
        elif self.ext[0] == "er" and self.ext[1] != "ec":
            self.ext[0] = self.ext[1]
            self.ext[1] = "er"
        elif self.ext[1] == "Eg":
            self.ext[1] = self.ext[0]
            self.ext[0] = "Eg"
        elif self.ext[1] == "E" and self.ext[0] != "Eg":
            self.ext[1] = self.ext[0]
            self.ext[0] = "E"

        if self.corin[0] == "fg":
            self.corin[0] = self.corin[1]
            self.corin[1] = "fg"
        elif self.corin[0] == "sh" and self.corin[1] != "fg":
            self.corin[0] = self.corin[1]
            self.corin[1] = "sh"
        elif self.corin[0] == "sg" and self.corin[1] not in ["sh", "fg"]:
            self.corin[0] = self.corin[1]
            self.corin[1] = "sg"

        if self.manx[1] == "M":
            self.manx[1] = self.manx[0]
            self.manx[0] = "M"
        elif self.manx[1] == "Ab":
            self.manx[1] = self.manx[0]
            self.manx[0] = "Ab"

        if self.pax3[0] == 'NoDBE':
            self.pax3[0] = self.pax3[1]
            self.pax3[1] = 'NoDBE'