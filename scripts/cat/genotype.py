from random import choice, randint, random
import json
from operator import xor


class Genotype:
    def __init__(self):
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

        self.saturation = 3

        self.bengal = ""
        self.bengtype = "normal markings"
        self.bengsum = 0

        self.sokoke = ""
        self.soktype = "normal markings"
        self.soksum = 0

        self.spotted = ""
        self.spottype = ""
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