import pygame
from scripts.game_structure import image_cache

from scripts.cat.sprites import *
from scripts.cat.pelts import *
from scripts.game_structure.game_essentials import *
import traceback
from scripts.cat.phenotype import Phenotype
import logging
logger = logging.getLogger(__name__)


def update_sprite(cat):
    # First, check if the cat is faded.
    cat.sprite = generate_sprite(cat)


def set_current_season(cat, platform=None):
    if platform:
        if 'Greenleaf' in platform:
            cat.season = 'Greenleaf'
        elif 'Leaf-bare' in platform:
            cat.season = 'Leaf-bare'
        elif 'Leaf-fall' in platform:
            cat.season = 'Leaf-fall'
        else:
            cat.season = 'Newleaf'
    else:
        cat.season = 'Newleaf'


def generate_sprite(cat, life_state=None, scars_hidden=False, acc_hidden=False, always_living=False,
                    no_not_working=False, no_para=False) -> pygame.Surface:
    """Generates the sprite for a cat, with optional arugments that will override certain things. 
        life_stage: sets the age life_stage of the cat, overriding the one set by it's age. Set to string. 
        scar_hidden: If True, doesn't display the cat's scars. If False, display cat scars. 
        acc_hidden: If True, hide the accessory. If false, show the accessory.
        always_living: If True, always show the cat with living lineart
        no_not_working: If true, never use the not_working lineart.
                        If false, use the cat.not_working() to determine the no_working art. 
        """

    if life_state is not None:
        age = life_state
    else:
        age = cat.age

    if always_living:
        dead = False
    else:
        dead = cat.dead

    cat_scars = []
    for x in cat.pelt.scar_slot_list:
        if x:
            cat_scars.append(x)

    # setting the cat_sprite (bc this makes things much easier)
    if not no_not_working and cat.pelt.not_working and age != 'newborn':
        if age in ['kitten', 'adolescent']:
            cat_sprite = str(19)
        else:
            cat_sprite = str(18)
    elif cat.pelt.paralyzed and age != 'newborn' and not no_para:
        if age in ['kitten', 'adolescent']:
            cat_sprite = str(17)
        else:
            if cat.pelt.length == 'long':
                cat_sprite = str(16)
            else:
                cat_sprite = str(15)
    else:
        if age == 'elder':
            age = 'senior'

        cat_sprite = str(cat.pelt.cat_sprites[age])

    new_sprite = pygame.Surface(
        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

    vitiligo = ['PHANTOM', 'POWDER', 'BLEACHED',
                'VITILIGO', 'VITILIGOTWO', 'SMOKEY', "MOON"]

    if cat_sprite == '20':
        cat.moons = 0
    elif cat.age == 'kitten':
        cat.moons = 3
    elif cat.age == 'adolescent':
        cat.moons = 9
    elif cat.age == 'senior':
        cat.moons = 150
    else:
        cat.moons = 60

    try:
        stripecolourdict = {
            'rufousedapricot': 'lowred',
            'mediumapricot': 'rufousedcream',
            'lowapricot': 'mediumcream',

            'rufousedhoney-apricot': 'lowred',
            'mediumhoney-apricot': 'rufousedhoney',
            'lowhoney-apricot': 'mediumhoney',

            'rufousedivory-apricot': 'lowhoney',
            'mediumivory-apricot': 'rufousedivory',
            'lowivory-apricot': 'mediumivory'
        }
        gensprite = pygame.Surface(
            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

        def get_current_season():
            return cat.season

        def GenSprite(genotype, phenotype, sprite_age, merle=False):
            phenotype.SpriteInfo(sprite_age)
            if (genotype.pseudomerle and not merle and 'rev' in genotype.merlepattern[0]):
                old_silver = genotype.silver
                phenotype.genotype.silver = ['i', 'i']
                phenotype.SpriteInfo(sprite_age)
                phenotype.genotype.silver = old_silver

            def CreateStripes(stripecolour, whichbase, coloursurface=None, pattern=None, special=None):
                stripebase = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

                if not pattern and not special and 'solid' not in whichbase:
                    if ('chinchilla' in whichbase):
                        stripebase.blit(
                            sprites.sprites['chinchillashading' + cat_sprite], (0, 0))
                    elif ('shaded' in whichbase):
                        stripebase.blit(
                            sprites.sprites['shadedshading' + cat_sprite], (0, 0))
                    else:
                        stripebase.blit(
                            sprites.sprites[genotype.wbtype + 'shading' + cat_sprite], (0, 0))

                if pattern:
                    stripebase.blit(
                        sprites.sprites[pattern + cat_sprite], (0, 0))
                elif 'ghost' in phenotype.tabby:
                    ghoststripes = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    ghoststripes.blit(
                        sprites.sprites[phenotype.GetTabbySprite() + cat_sprite], (0, 0))
                    ghoststripes.set_alpha(25)
                    stripebase.blit(ghoststripes, (0, 0))
                    stripebase.blit(sprites.sprites[phenotype.GetTabbySprite(
                        special='ghost') + cat_sprite], (0, 0))
                else:
                    stripebase.blit(
                        sprites.sprites[phenotype.GetTabbySprite() + cat_sprite], (0, 0))

                charc = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                charc_shading = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                if (genotype.agouti[0] == "Apb" and ('red' not in stripecolour and 'cream' not in stripecolour and 'honey' not in stripecolour and 'ivory' not in stripecolour and 'apricot' not in stripecolour)):
                    charc_shading.blit(
                        sprites.sprites['lightbasecolours0'], (0, 0))
                    modifiers = {
                        "chinchilla": 2,
                        "shaded": 3,
                        "high": 5,
                        "medium": 6,
                        "low": 7
                    }
                    opacity = int(
                        25 * (modifiers.get(phenotype.banding, 5) / (1 * (int("silver" in whichbase) + 1))))
                    charc_shading.set_alpha(opacity)
                    charc.blit(charc_shading, (0, 0))
                    charc.blit(
                        sprites.sprites['charcoal' + cat_sprite], (0, 0))

                if (genotype.agouti == ["Apb", "Apb"]):
                    charc.set_alpha(125)
                stripebase.blit(charc, (0, 0))

                if coloursurface:
                    stripebase.blit(coloursurface, (0, 0),
                                    special_flags=pygame.BLEND_RGBA_MULT)
                elif 'basecolours' in stripecolour:
                    stripebase.blit(
                        sprites.sprites[stripecolour], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                else:
                    surf = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    surf.blit(sprites.sprites[stripecolourdict.get(
                        stripecolour[:-1], stripecolour[:-1])+stripecolour[-1]], (0, 0))
                    if phenotype.caramel == 'caramel' and not ('red' in stripecolour or 'cream' in stripecolour or 'honey' in stripecolour or 'ivory' in stripecolour or 'apricot' in stripecolour):
                        surf.blit(sprites.sprites['caramel0'], (0, 0))

                    stripebase.blit(
                        surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                middle = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                if (genotype.soktype == "full sokoke" and not pattern and 'agouti' not in phenotype.tabby):
                    middle.blit(stripebase, (0, 0))
                    stripebase = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    middle.set_alpha(150)
                    stripebase.blit(middle, (0, 0))
                    middle = CreateStripes(
                        stripecolour, whichbase, coloursurface, pattern=phenotype.GetTabbySprite(special='redbar'))
                    stripebase.blit(middle, (0, 0))
                elif (genotype.soktype == "mild fading" and not pattern and 'agouti' not in phenotype.tabby):
                    middle.blit(stripebase, (0, 0))
                    stripebase = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    middle.set_alpha(204)
                    stripebase.blit(middle, (0, 0))
                    middle = CreateStripes(
                        stripecolour, whichbase, coloursurface, pattern=phenotype.GetTabbySprite(special='redbar'))
                    stripebase.blit(middle, (0, 0))

                if 'chinchilla' in whichbase:
                    stripebase.set_alpha(50)
                if 'shaded' in whichbase:
                    stripebase.set_alpha(150)

                # if cat.genotype.furLength[0] == 'l':
                #     stripebase = pygame.transform.box_blur(stripebase, 1)

                return stripebase

            def TabbyBase(whichcolour, whichbase, cat_unders, special=None):
                is_red = (
                    'red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour)
                whichmain = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                whichmain.blit(sprites.sprites[whichbase], (0, 0))
                if special != 'copper' and sprite_age > 12 and (genotype.silver[0] == 'I' and genotype.corin[0] == 'fg' and (get_current_season() == 'Leaf-fall' or get_current_season() == 'Leaf-bare')):
                    sunshine = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

                    colours = phenotype.FindRed(
                        genotype, sprite_age, special='low')
                    sunshine = MakeCat(sunshine, colours[0], colours[1], [
                                       colours[2], colours[3]], special='copper')

                    sunshine.set_alpha(150)
                    whichmain.blit(sunshine, (0, 0))

                unders = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                unders.blit(
                    sprites.sprites["Tabby_unders" + cat_sprite], (0, 0))
                unders.blit(
                    sprites.sprites[cat_unders[0]], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                unders.set_alpha(int(cat_unders[1] * 2.55))
                whichmain.blit(unders, (0, 0))

                if phenotype.caramel == 'caramel' and not is_red:
                    whichmain.blit(sprites.sprites['caramel0'], (0, 0))

                return whichmain

            def AddStripes(whichmain, whichcolour, whichbase, coloursurface=None):
                stripebase = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                if ((genotype.corin[0] != 'N' and genotype.wbtype == "shaded") or genotype.wbtype == 'chinchilla'):
                    stripebase = CreateStripes(
                        whichcolour, whichbase, coloursurface=coloursurface)
                    stripebase.set_alpha(100)
                elif (genotype.wbtype == "shaded" or genotype.corin[0] != 'N'):
                    stripebase = CreateStripes(
                        phenotype.FindRed(genotype, sprite_age, special='red')[0], phenotype.FindRed(genotype, sprite_age, special='red')[1], coloursurface=coloursurface)
                    stripebase.set_alpha(50)
                    whichmain.blit(stripebase, (0, 0))
                    stripebase = CreateStripes(
                        whichcolour, whichbase, coloursurface=coloursurface)
                    stripebase.set_alpha(100)
                    whichmain.blit(stripebase, (0, 0))
                    stripebase = CreateStripes(
                        whichcolour, whichbase, pattern="agouti", coloursurface=coloursurface)
                    stripebase.set_alpha(150)
                elif ('ec' in genotype.ext and 'Eg' not in genotype.ext and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour)):
                    stripebase = CreateStripes(
                        whichcolour, whichbase, coloursurface=coloursurface)
                    stripebase.set_alpha(200)
                    whichmain.blit(stripebase, (0, 0))
                    stripebase = CreateStripes(
                        whichcolour, whichbase, coloursurface=coloursurface, pattern='agouti')
                else:
                    stripebase.blit(CreateStripes(
                        whichcolour, whichbase, coloursurface=coloursurface), (0, 0))

                whichmain.blit(stripebase, (0, 0))

                return whichmain

            def ApplySmokeEffects(whichmain):
                white = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                white.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                smokeUnders = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                smokeUnders.blit(
                    sprites.sprites["Tabby_unders" + cat_sprite], (0, 0))
                smokeUnders.blit(
                    white, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                smokeUnders.set_alpha(10)
                white.set_alpha(10)
                smokeLayer = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                smokeLayer.blit(white, (0, 0))
                if (genotype.ext[0] == 'Eg' and genotype.agouti[0] != 'a'):
                    whichmain.blit(
                        sprites.sprites['grizzle' + cat_sprite], (0, 0))
                if genotype.ghosting[0] == 'Gh' and not (genotype.silver[0] == 'I' and cat.pelt.length == 'long'):
                    ghostingbase = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    ghostingbase.blit(
                        sprites.sprites['ghost' + cat_sprite], (0, 0))
                    if (sprite_age < 4):
                        ghostingbase.set_alpha(150)

                    whichmain.blit(ghostingbase, (0, 0))
                if (genotype.silver[0] == 'I'):
                    ghostingbase = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    ghostingbase.blit(
                        sprites.sprites['ghost' + cat_sprite], (0, 0))
                    if cat.pelt.length != 'long':
                        ghostingbase.set_alpha(100)
                    elif genotype.wbtype == 'low':
                        ghostingbase.set_alpha(150)

                    whichmain.blit(ghostingbase, (0, 0))
                if (genotype.silver[0] == 'I'):
                    smokeLayer.set_alpha(255)
                    if cat.pelt.length != 'long':
                        smokeLayer.blit(smokeUnders, (0, 0))
                    if genotype.wbtype == 'low' and cat.pelt.length == 'long':
                        smokeLayer.set_alpha(75)
                    elif genotype.wbtype == 'low' or cat.pelt.length == 'long':
                        smokeLayer.set_alpha(150)
                    else:
                        smokeLayer.set_alpha(200)
                    whichmain.blit(smokeLayer, (0, 0))
                if ('light smoke' in phenotype.silvergold):
                    smokeLayer.set_alpha(255)
                    if cat.pelt.length != 'long':
                        smokeLayer.blit(smokeUnders, (0, 0))
                    if genotype.wbtype == 'high':
                        smokeLayer.set_alpha(100)
                    elif cat.pelt.length == 'long':
                        smokeLayer.set_alpha(200)
                    whichmain.blit(smokeLayer, (0, 0))

                return whichmain

            def AddPads(sprite, whichcolour, is_red=False, override=None):
                pads = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                pads.blit(sprites.sprites['pads' + cat_sprite], (0, 0))

                pad_dict = {
                    'red': 0,
                    'whit': 1,
                    'tabby': 2,
                    'black': 3,
                    'chocolate': 4,
                    'cinnamon': 5,
                    'blue': 6,
                    'lilac': 7,
                    'fawn': 8,
                    'dove': 9,
                    'champagne': 10,
                    'buff': 11,
                    'platinum': 12,
                    'lavender': 13,
                    'beige': 14
                }

                if (genotype.white[0] == 'W' or genotype.pointgene[0] == 'c' or genotype.white_pattern == ['full white'] or override == "white"):
                    pads.blit(
                        sprites.sprites['nosecolours1'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                elif ('amber' not in phenotype.colour or genotype.agouti[0] != 'a') and ('russet' in phenotype.colour or 'carnelian' in phenotype.colour or is_red):
                    pads.blit(
                        sprites.sprites['nosecolours0'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                elif 'amber' in phenotype.colour:
                    phenotype.SpriteInfo(10)
                    whichcolour = phenotype.maincolour
                    pads.blit(sprites.sprites['nosecolours' + str(pad_dict.get(
                        whichcolour[:-1], 0))], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    phenotype.SpriteInfo(sprite_age)
                else:
                    pads.blit(sprites.sprites['nosecolours' + str(pad_dict.get(
                        whichcolour[:-1]))], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                sprite.blit(pads, (0, 0))

                return sprite

            def AddNose(sprite, override=None):
                nose = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                nose.blit(sprites.sprites['nose' + cat_sprite], (0, 0))

                nose_dict = {
                    'red': 0,
                    'whit': 1,
                    'tabby': 2,
                    'black': 3,
                    'chocolate': 4,
                    'cinnamon': 5,
                    'blue': 6,
                    'lilac': 7,
                    'fawn': 8,
                    'dove': 9,
                    'champagne': 10,
                    'buff': 11,
                    'platinum': 12,
                    'lavender': 13,
                    'beige': 14
                }

                if phenotype.maincolour == "white" or override == 'white':
                    nose.blit(
                        sprites.sprites['nosecolours1'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                elif ('amber' not in phenotype.colour or genotype.agouti[0] != 'a') and ('red' in phenotype.maincolour or 'cream' in phenotype.maincolour or 'honey' in phenotype.maincolour or 'ivory' in phenotype.maincolour or 'apricot' in phenotype.maincolour):
                    nose.blit(
                        sprites.sprites['nosecolours0'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                elif 'amber' in phenotype.colour:
                    phenotype.SpriteInfo(10)
                    nose.blit(sprites.sprites['nosecolours' + str(nose_dict.get(
                        phenotype.maincolour[:-1]))], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    phenotype.SpriteInfo(sprite_age)
                elif phenotype.maincolour != phenotype.spritecolour:
                    nose.blit(
                        sprites.sprites['nosecolours2'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    nose.set_alpha(200)
                else:
                    nose.blit(sprites.sprites['nosecolours' + str(nose_dict.get(
                        phenotype.maincolour[:-1]))], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                sprite.blit(nose, (0, 0))
                return sprite

            def MakeCat(whichmain, whichcolour, whichbase, cat_unders, special=None):
                is_red = (
                    'red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour)

                if (genotype.white[0] == 'W' or genotype.pointgene[0] == 'c' or whichcolour == 'white' or genotype.white_pattern == ['full white']):
                    whichmain.blit(
                        sprites.sprites['lightbasecolours0'], (0, 0))
                elif (whichcolour != whichbase and special != 'masked silver'):
                    if (genotype.pointgene[0] == "C"):
                        whichmain = TabbyBase(
                            whichcolour, whichbase, cat_unders, special)

                        whichmain = AddStripes(
                            whichmain, whichcolour, whichbase)
                    else:
                        # create base
                        colourbase = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        if ("black" in whichcolour and genotype.pointgene[0] == "cm"):
                            colourbase.blit(
                                sprites.sprites[whichbase.replace("black", "cinnamon")], (0, 0))
                        else:
                            colourbase = TabbyBase(
                                whichcolour, whichbase, cat_unders, special)

                            if ((genotype.pointgene == ["cb", "cb"] and cat_sprite != "20") or (((("cb" in genotype.pointgene or genotype.pointgene[0] == "cm") and cat_sprite != "20") or genotype.pointgene == ["cb", "cb"]) and get_current_season() == 'Leaf-bare')):
                                colourbase.set_alpha(100)
                            elif ((("cb" in genotype.pointgene or genotype.pointgene[0] == "cm") and cat_sprite != "20") or genotype.pointgene == ["cb", "cb"] or ((cat_sprite != "20" or ("cb" in genotype.pointgene or genotype.pointgene[0] == "cm")) and get_current_season() == 'Leaf-bare')):
                                colourbase.set_alpha(50)
                            elif (("cb" in genotype.pointgene or genotype.pointgene[0] == "cm")):
                                colourbase.set_alpha(15)
                            else:
                                colourbase.set_alpha(0)

                        whichmain.blit(
                            sprites.sprites['lightbasecolours0'], (0, 0))
                        whichmain.blit(colourbase, (0, 0))

                        # add base stripes
                        if ("cm" in genotype.pointgene):
                            if ("black" in whichcolour and genotype.pointgene[0] == "cm"):
                                whichmain = AddStripes(
                                    whichmain, 'lightbasecolours2', whichbase)
                            else:
                                if ("cb" in genotype.pointgene or genotype.pointgene[0] == "cm"):
                                    if ("black" in whichcolour and cat_sprite != "20"):
                                        whichmain = AddStripes(
                                            whichmain, 'lightbasecolours2', whichbase)
                                    elif (("chocolate" in whichcolour and cat_sprite != "20") or "black" in whichcolour):
                                        whichmain = AddStripes(
                                            whichmain, 'lightbasecolours1', whichbase)
                                    elif ("cinnamon" in whichcolour or "chocolate" in whichcolour):
                                        whichmain = AddStripes(
                                            whichmain, 'lightbasecolours0', whichbase)
                                    else:
                                        pointbase = pygame.Surface(
                                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                        pointbase.blit(sprites.sprites[stripecolourdict.get(
                                            whichcolour[:-1], whichcolour[:-1])+whichcolour[-1]], (0, 0))
                                        if phenotype.caramel == 'caramel' and not is_red:
                                            pointbase.blit(
                                                sprites.sprites['caramel0'], (0, 0))
                                        pointbase.set_alpha(102)
                                        pointbase2 = pygame.Surface(
                                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                        pointbase2.blit(
                                            sprites.sprites['lightbasecolours0'], (0, 0))
                                        pointbase2.blit(pointbase, (0, 0))
                                        whichmain = AddStripes(
                                            whichmain, whichcolour, whichbase, coloursurface=pointbase2)
                                else:
                                    if ("black" in whichcolour and cat_sprite != "20"):
                                        stripecolour = pygame.Surface(
                                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                        stripecolour = AddStripes(
                                            stripecolour, 'lightbasecolours1', whichbase)
                                        stripecolour.set_alpha(102)
                                        whichmain.blit(stripecolour, (0, 0))
                                    else:
                                        whichmain = AddStripes(
                                            whichmain, 'lightbasecolours0', whichbase)

                        else:
                            if ("black" in whichcolour and genotype.pointgene == ["cb", "cb"] and cat_sprite != "20"):
                                whichmain = AddStripes(
                                    whichmain, 'lightbasecolours3', whichbase)
                            elif ((("chocolate" in whichcolour and genotype.pointgene == ["cb", "cb"]) or ("black" in whichcolour and "cb" in genotype.pointgene)) and cat_sprite != "20" or ("black" in whichcolour and genotype.pointgene == ["cb", "cb"])):
                                whichmain = AddStripes(
                                    whichmain, 'lightbasecolours2', whichbase)
                            elif ((("cinnamon" in whichcolour and genotype.pointgene == ["cb", "cb"]) or ("chocolate" in whichcolour and "cb" in genotype.pointgene) or ("black" in whichcolour and genotype.pointgene == ["cs", "cs"])) and cat_sprite != "20" or (("chocolate" in whichcolour and genotype.pointgene == ["cb", "cb"]) or ("black" in whichcolour and "cb" in genotype.pointgene))):
                                whichmain = AddStripes(
                                    whichmain, 'lightbasecolours1', whichbase)

                            elif (genotype.pointgene == ["cb", "cb"]) and cat_sprite != "20":
                                pointbase = pygame.Surface(
                                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                pointbase.blit(sprites.sprites[stripecolourdict.get(
                                    whichcolour[:-1], whichcolour[:-1])+whichcolour[-1]], (0, 0))
                                if phenotype.caramel == 'caramel' and not is_red:
                                    pointbase.blit(
                                        sprites.sprites['caramel0'], (0, 0))
                                pointbase.set_alpha(204)
                                pointbase2 = pygame.Surface(
                                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                pointbase2.blit(
                                    sprites.sprites['lightbasecolours0'], (0, 0))
                                pointbase2.blit(pointbase, (0, 0))
                                whichmain = AddStripes(
                                    whichmain, whichcolour, whichbase, coloursurface=pointbase2)
                            elif ("cb" in genotype.pointgene) and (cat_sprite != "20" or genotype.pointgene == ["cb", "cb"]):
                                pointbase = pygame.Surface(
                                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                pointbase.blit(sprites.sprites[stripecolourdict.get(
                                    whichcolour[:-1], whichcolour[:-1])+whichcolour[-1]], (0, 0))
                                if phenotype.caramel == 'caramel' and not is_red:
                                    pointbase.blit(
                                        sprites.sprites['caramel0'], (0, 0))
                                if (genotype.eumelanin[0] == "bl"):
                                    pointbase.set_alpha(25)
                                else:
                                    pointbase.set_alpha(102)
                                pointbase2 = pygame.Surface(
                                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                pointbase2.blit(
                                    sprites.sprites['lightbasecolours0'], (0, 0))
                                pointbase2.blit(pointbase, (0, 0))
                                whichmain = AddStripes(
                                    whichmain, whichcolour, whichbase, coloursurface=pointbase2)
                            else:
                                whichmain = AddStripes(
                                    whichmain, 'lightbasecolours0', whichbase)

                        # mask base
                        colourbase = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        if ("black" in whichcolour and genotype.pointgene[0] == "cm"):
                            colourbase2 = pygame.Surface(
                                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            colourbase.blit(
                                sprites.sprites['lightbasecolours0'], (0, 0))
                            colourbase2.blit(
                                sprites.sprites[whichbase.replace("black", "cinnamon")], (0, 0))
                            colourbase2.set_alpha(150)
                            colourbase.blit(colourbase2, (0, 0))
                        else:
                            colourbase = TabbyBase(
                                whichcolour, whichbase, cat_unders, special)
                        pointbase = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        pointbase2 = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        pointbase2.blit(
                            sprites.sprites['lightbasecolours0'], (0, 0))
                        if ("cm" in genotype.pointgene):
                            if ("black" in whichcolour and genotype.pointgene[0] == "cm"):
                                pointbase.blit(colourbase, (0, 0))
                            else:
                                if ((("cb" in genotype.pointgene or genotype.pointgene[0] == "cm") and cat_sprite != "20") or ((cat_sprite != "20" or ("cb" in genotype.pointgene or genotype.pointgene[0] == "cm")) and get_current_season() == "Leaf-bare")):
                                    colourbase.set_alpha(180)
                                elif (cat_sprite != "20" or ("cb" in genotype.pointgene or genotype.pointgene[0] == "cm")):
                                    colourbase.set_alpha(50)
                                else:
                                    colourbase.set_alpha(0)

                                pointbase2.blit(colourbase, (0, 0))

                                if (get_current_season() == "Greenleaf"):
                                    pointbase.blit(
                                        sprites.sprites['mochal' + cat_sprite], (0, 0))
                                    pointbase.blit(pointbase2, (0, 0),
                                                   special_flags=pygame.BLEND_RGBA_MULT)
                                elif (get_current_season() == "Leaf-bare"):
                                    pointbase.blit(
                                        sprites.sprites['mochad' + cat_sprite], (0, 0))
                                    pointbase.blit(pointbase2, (0, 0),
                                                   special_flags=pygame.BLEND_RGBA_MULT)
                                else:
                                    pointbase.blit(
                                        sprites.sprites['mocham' + cat_sprite], (0, 0))
                                    pointbase.blit(pointbase2, (0, 0),
                                                   special_flags=pygame.BLEND_RGBA_MULT)

                        else:
                            if ((genotype.pointgene == ["cb", "cb"] and cat_sprite != "20") or ("cb" in genotype.pointgene and cat_sprite != "20" and get_current_season() == 'Leaf-bare')):
                                colourbase.set_alpha(180)
                            elif (("cb" in genotype.pointgene and cat_sprite != "20") or genotype.pointgene == ["cb", "cb"] or ((cat_sprite != "20" or "cb" in genotype.pointgene) and get_current_season() == 'Leaf-bare')):
                                colourbase.set_alpha(120)
                            elif (cat_sprite != "20" or "cb" in genotype.pointgene):
                                colourbase.set_alpha(50)
                            else:
                                colourbase.set_alpha(15)

                            pointbase2.blit(colourbase, (0, 0))

                            if (get_current_season() == "Greenleaf"):
                                pointbase.blit(
                                    sprites.sprites['pointsl' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0),
                                               special_flags=pygame.BLEND_RGBA_MULT)
                            elif (get_current_season() == "Leaf-bare"):
                                pointbase.blit(
                                    sprites.sprites['pointsd' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0),
                                               special_flags=pygame.BLEND_RGBA_MULT)
                            else:
                                pointbase.blit(
                                    sprites.sprites['pointsm' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0),
                                               special_flags=pygame.BLEND_RGBA_MULT)

                        # add mask stripes

                        stripebase = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        stripebase2 = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

                        if ("black" in whichcolour and genotype.pointgene[0] == "cm"):
                            colour = whichcolour.replace("black", "cinnamon")
                        else:
                            colour = whichcolour

                        stripebase.blit(CreateStripes(
                            colour, whichbase), (0, 0))

                        if (get_current_season() == "Greenleaf"):
                            stripebase2.blit(
                                sprites.sprites['mochal' + cat_sprite], (0, 0))
                            stripebase2.blit(stripebase, (0, 0),
                                             special_flags=pygame.BLEND_RGBA_MULT)
                        elif (get_current_season() == "Leaf-bare"):
                            stripebase2.blit(
                                sprites.sprites['mochad' + cat_sprite], (0, 0))
                            stripebase2.blit(stripebase, (0, 0),
                                             special_flags=pygame.BLEND_RGBA_MULT)
                        else:
                            stripebase2.blit(
                                sprites.sprites['mocham' + cat_sprite], (0, 0))
                            stripebase2.blit(stripebase, (0, 0),
                                             special_flags=pygame.BLEND_RGBA_MULT)

                        pointbase.blit(stripebase2, (0, 0))

                        whichmain.blit(pointbase, (0, 0))

                else:
                    if (genotype.pointgene[0] == "C"):
                        whichmain.blit(sprites.sprites[stripecolourdict.get(
                            whichcolour[:-1], whichcolour[:-1])+whichcolour[-1]], (0, 0))
                        if phenotype.caramel == 'caramel' and not is_red:
                            whichmain.blit(sprites.sprites['caramel0'], (0, 0))

                        whichmain = ApplySmokeEffects(whichmain)

                        if phenotype.length != "longhaired":
                            stripebase = pygame.Surface(
                                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            stripebase.blit(CreateStripes(
                                whichcolour, "solid"), (0, 0))
                            whichmain.blit(stripebase, (0, 0))
                    elif ("cm" in genotype.pointgene):
                        colour = None
                        coloursurface = None
                        if ("black" in whichcolour and genotype.pointgene[0] == "cm"):
                            whichmain.blit(
                                sprites.sprites['lightbasecolours2'], (0, 0))
                            overlay = pygame.Surface(
                                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            overlay.blit(sprites.sprites['cinnamon3'], (0, 0))
                            overlay.set_alpha(150)
                            whichmain.blit(overlay, (0, 0))
                            whichmain = ApplySmokeEffects(whichmain)

                            if phenotype.length != "longhaired":
                                stripebase = pygame.Surface(
                                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

                                stripebase.blit(CreateStripes(whichcolour.replace(
                                    "black", "cinnamon"), 'solid', pattern="fullbar"), (0, 0))
                                stripebase.set_alpha(150)

                                whichmain.blit(stripebase, (0, 0))
                        else:
                            stripebase = pygame.Surface(
                                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

                            if ("cb" in genotype.pointgene or genotype.pointgene[0] == "cm"):
                                if ("black" in whichcolour and cat_sprite != "20"):
                                    whichmain.blit(
                                        sprites.sprites['lightbasecolours2'], (0, 0))
                                    colour = 'lightbasecolours2'
                                    whichmain = ApplySmokeEffects(whichmain)

                                elif (("chocolate" in whichcolour and cat_sprite != "20") or "black" in whichcolour):
                                    whichmain.blit(
                                        sprites.sprites['lightbasecolours1'], (0, 0))
                                    colour = 'lightbasecolours1'
                                    whichmain = ApplySmokeEffects(whichmain)
                                elif ("chocolate" in whichcolour or "chocolate" in whichcolour):
                                    whichmain.blit(
                                        sprites.sprites['lightbasecolours0'], (0, 0))
                                    colour = 'lightbasecolours0'
                                else:
                                    pointbase = pygame.Surface(
                                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                    pointbase.blit(
                                        sprites.sprites[whichcolour], (0, 0))
                                    if phenotype.caramel == 'caramel' and not is_red:
                                        pointbase.blit(
                                            sprites.sprites['caramel0'], (0, 0))

                                    pointbase.set_alpha(102)
                                    if 'fawn' in whichcolour:
                                        pointbase.set_alpha(0)

                                    if 'blue' in whichcolour:
                                        if genotype.pointgene[0] == "cm":
                                            whichmain.blit(
                                                sprites.sprites[whichcolour.replace('blue', 'fawn')], (0, 0))
                                            whichmain.blit(pointbase, (0, 0))
                                            pointbase.blit(
                                                sprites.sprites['lightbasecolours2'], (0, 0))
                                            pointbase.set_alpha(50)
                                        else:
                                            whichmain.blit(
                                                sprites.sprites['lightbasecolours1'], (0, 0))
                                    else:
                                        whichmain.blit(
                                            sprites.sprites['lightbasecolours0'], (0, 0))
                                    whichmain.blit(pointbase, (0, 0))
                                    pointbase.blit(whichmain, (0, 0))
                                    coloursurface = pointbase
                                    colour = whichcolour

                                    whichmain = ApplySmokeEffects(whichmain)
                            else:
                                if ("black" in whichcolour and cat_sprite != "20"):
                                    whichmain.blit(
                                        sprites.sprites['lightbasecolours1'], (0, 0))
                                    colour = 'lightbasecolours1'
                                    whichmain = ApplySmokeEffects(whichmain)
                                else:
                                    whichmain.blit(
                                        sprites.sprites['lightbasecolours0'], (0, 0))
                                    colour = 'lightbasecolours0'

                            if phenotype.length != "longhaired":
                                stripebase = CreateStripes(
                                    colour, 'solid', coloursurface=coloursurface)
                                whichmain.blit(stripebase, (0, 0))

                            pointbase = pygame.Surface(
                                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            pointbase2 = pygame.Surface(
                                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

                            pointbase2.blit(
                                sprites.sprites[whichcolour], (0, 0))
                            if phenotype.caramel == 'caramel' and not is_red:
                                pointbase2.blit(
                                    sprites.sprites['caramel0'], (0, 0))

                            whichmain = ApplySmokeEffects(whichmain)

                            if phenotype.length != "longhaired":
                                stripebase = pygame.Surface(
                                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                stripebase.blit(CreateStripes(
                                    whichcolour, 'solid'), (0, 0))

                            pointbase2.blit(stripebase, (0, 0))

                            if (get_current_season() == "Greenleaf"):
                                pointbase.blit(
                                    sprites.sprites['mochal' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0),
                                               special_flags=pygame.BLEND_RGBA_MULT)
                            elif (get_current_season() == "Leaf-bare"):
                                pointbase.blit(
                                    sprites.sprites['mochad' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0),
                                               special_flags=pygame.BLEND_RGBA_MULT)
                            else:
                                pointbase.blit(
                                    sprites.sprites['mocham' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0),
                                               special_flags=pygame.BLEND_RGBA_MULT)

                            if genotype.pointgene[0] == "cm" and 'blue' in whichcolour:
                                pointbase.set_alpha(102)

                            whichmain.blit(pointbase, (0, 0))

                    else:
                        colour = whichcolour
                        coloursurface = None
                        stripebase = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        if ("black" in whichcolour and genotype.pointgene == ["cb", "cb"] and cat_sprite != "20"):
                            whichmain.blit(
                                sprites.sprites['lightbasecolours3'], (0, 0))
                            colour = 'lightbasecolours3'
                            whichmain = ApplySmokeEffects(whichmain)
                        elif ((("chocolate" in whichcolour and genotype.pointgene == ["cb", "cb"]) or ("black" in whichcolour and "cb" in genotype.pointgene)) and cat_sprite != "20") or ("black" in whichcolour and genotype.pointgene == ["cb", "cb"]):
                            whichmain.blit(
                                sprites.sprites['lightbasecolours2'], (0, 0))
                            colour = 'lightbasecolours2'
                            whichmain = ApplySmokeEffects(whichmain)
                        elif ((("chocolate" in whichcolour and genotype.pointgene == ["cb", "cb"]) or ("chocolate" in whichcolour and "cb" in genotype.pointgene) or ("black" in whichcolour and genotype.pointgene == ["cs", "cs"])) and cat_sprite != "20") or (("chocolate" in whichcolour and genotype.pointgene == ["cb", "cb"]) or ("black" in whichcolour and "cb" in genotype.pointgene)):
                            whichmain.blit(
                                sprites.sprites['lightbasecolours1'], (0, 0))
                            colour = 'lightbasecolours1'
                            whichmain = ApplySmokeEffects(whichmain)
                        elif (genotype.pointgene == ["cb", "cb"]) and cat_sprite != "20":
                            pointbase = pygame.Surface(
                                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            pointbase.blit(
                                sprites.sprites[whichcolour], (0, 0))
                            if phenotype.caramel == 'caramel' and not is_red:
                                pointbase.blit(
                                    sprites.sprites['caramel0'], (0, 0))

                            pointbase.set_alpha(204)
                            if 'lilac' in whichcolour:
                                pointbase.set_alpha(140)
                            if 'fawn' in whichcolour:
                                pointbase.set_alpha(50)

                            if 'blue' in whichcolour:
                                whichmain.blit(
                                    sprites.sprites['lightbasecolours1'], (0, 0))
                            else:
                                whichmain.blit(
                                    sprites.sprites['lightbasecolours0'], (0, 0))
                            whichmain.blit(pointbase, (0, 0))
                            pointbase.blit(whichmain, (0, 0))
                            coloursurface = pointbase
                            whichmain = ApplySmokeEffects(whichmain)
                        elif ("cb" in genotype.pointgene) and (cat_sprite != "20" or genotype.pointgene == ["cb", "cb"]):
                            pointbase = pygame.Surface(
                                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            pointbase.blit(
                                sprites.sprites[whichcolour], (0, 0))
                            if phenotype.caramel == 'caramel' and not is_red:
                                pointbase.blit(
                                    sprites.sprites['caramel0'], (0, 0))

                            if (genotype.eumelanin[0] == "bl"):
                                pointbase.set_alpha(25)
                            else:
                                pointbase.set_alpha(102)

                            if 'blue' in whichcolour:
                                whichmain.blit(
                                    sprites.sprites['lightbasecolours1'], (0, 0))
                            else:
                                whichmain.blit(
                                    sprites.sprites['lightbasecolours0'], (0, 0))
                            whichmain.blit(pointbase, (0, 0))
                            coloursurface = whichmain
                            whichmain = ApplySmokeEffects(whichmain)
                            colour = whichcolour

                        else:
                            whichmain.blit(
                                sprites.sprites['lightbasecolours0'], (0, 0))
                            colour = 'lightbasecolours0'

                        stripebase = CreateStripes(
                            colour, 'solid', coloursurface=coloursurface)

                        whichmain.blit(stripebase, (0, 0))

                        pointbase = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        pointbase2 = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

                        pointbase2.blit(sprites.sprites[whichcolour], (0, 0))
                        if phenotype.caramel == 'caramel' and not is_red:
                            pointbase2.blit(
                                sprites.sprites['caramel0'], (0, 0))
                        pointbase2 = ApplySmokeEffects(pointbase2)

                        if phenotype.length != "longhaired":
                            stripebase = CreateStripes(whichcolour, "solid")

                            pointbase2.blit(stripebase, (0, 0))

                        if (get_current_season() == "Greenleaf"):
                            pointbase.blit(
                                sprites.sprites['pointsl' + cat_sprite], (0, 0))
                            pointbase.blit(pointbase2, (0, 0),
                                           special_flags=pygame.BLEND_RGBA_MULT)
                        elif (get_current_season() == "Leaf-bare"):
                            pointbase.blit(
                                sprites.sprites['pointsd' + cat_sprite], (0, 0))
                            pointbase.blit(pointbase2, (0, 0),
                                           special_flags=pygame.BLEND_RGBA_MULT)
                        else:
                            pointbase.blit(
                                sprites.sprites['pointsm' + cat_sprite], (0, 0))
                            pointbase.blit(pointbase2, (0, 0),
                                           special_flags=pygame.BLEND_RGBA_MULT)

                        whichmain.blit(pointbase, (0, 0))

                seasondict = {
                    'Greenleaf': 'summer',
                    'Leaf-bare': 'winter'
                }

                if (genotype.karp[0] == 'K'):
                    if (genotype.karp[1] == 'K'):
                        whichmain.blit(sprites.sprites['homokarpati' + seasondict.get(
                            get_current_season(), "spring") + cat_sprite], (0, 0))
                    else:
                        whichmain.blit(sprites.sprites['hetkarpati' + seasondict.get(
                            get_current_season(), "spring") + cat_sprite], (0, 0))
                if (genotype.white[0] == 'wsal'):
                    whichmain.blit(
                        sprites.sprites['salmiak' + cat_sprite], (0, 0))

                whichmain = AddPads(whichmain, whichcolour, is_red)

                return whichmain

            gensprite = pygame.Surface(
                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

            def ApplyPatchEffects(sprite):
                if ('masked' in phenotype.silvergold):
                    masked = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    masked = MakeCat(masked, phenotype.maincolour, phenotype.spritecolour,
                                     phenotype.mainunders, special="masked silver")
                    masked2 = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    masked2.blit(
                        sprites.sprites["BLUE-TIPPED" + cat_sprite], (0, 0))
                    masked2.blit(masked, (0, 0),
                                 special_flags=pygame.BLEND_RGBA_MULT)
                    masked2.set_alpha(120)
                    sprite.blit(masked2, (0, 0))

                if (genotype.ext[0] == 'Eg' and genotype.agouti[0] != 'a') and genotype.satin[0] != "st" and genotype.tenn[0] != 'tr' and not ('red' in phenotype.maincolour or 'cream' in phenotype.maincolour or 'honey' in phenotype.maincolour or 'ivory' in phenotype.maincolour or 'apricot' in phenotype.maincolour):
                    sprite.blit(sprites.sprites['satin0'], (0, 0))
                elif (genotype.glitter[0] == 'gl' or genotype.ghosting[0] == 'Gh') and (genotype.agouti[0] != 'a' or ('red' in phenotype.maincolour or 'cream' in phenotype.maincolour or 'honey' in phenotype.maincolour or 'ivory' in phenotype.maincolour or 'apricot' in phenotype.maincolour)):
                    if genotype.satin[0] != "st" and genotype.tenn[0] != 'tr':
                        sprite.blit(sprites.sprites['satin0'], (0, 0))
                    if (genotype.ghosting[0] == 'Gh'):
                        fading = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        fading.blit(
                            sprites.sprites['tabbyghost'+cat_sprite], (0, 0))
                        fading.set_alpha(50)
                        sprite.blit(fading, (0, 0))
                        sprite.blit(sprites.sprites['satin0'], (0, 0))
                if not genotype.brindledbi and not ('red' in phenotype.maincolour or 'cream' in phenotype.maincolour or 'honey' in phenotype.maincolour or 'ivory' in phenotype.maincolour or 'apricot' in phenotype.maincolour) and (genotype.ext[0] != "Eg" and genotype.agouti[0] != 'a' and (genotype.corin[0] == 'sg' or genotype.corin[0] == 'sh' or ('ec' in genotype.ext and genotype.ext[0] != "Eg") or (genotype.ext[0] == 'ea' and sprite_age > 6) or (genotype.silver[0] == 'i' and genotype.corin[0] == 'fg'))):
                    sunshine = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    sunshine.blit(
                        sprites.sprites['bimetal' + cat_sprite], (0, 0))

                    colours = phenotype.FindRed(
                        genotype, sprite_age, special='nosilver')
                    underbelly = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    underbelly = MakeCat(underbelly, colours[0], colours[1], [
                                         colours[2], colours[3]], special='nounders')
                    sunshine.blit(underbelly, (0, 0),
                                  special_flags=pygame.BLEND_RGBA_MIN)
                    sunshine.set_alpha(75)
                    sprite.blit(sunshine, (0, 0))
                return sprite

            is_white = 'W' in genotype.white or genotype.pointgene[0] == 'c' or genotype.white_pattern == [
                'full white']
            if (phenotype.patchmain != "" and 'rev' in genotype.tortiepattern[0]):
                gensprite = MakeCat(
                    gensprite, phenotype.patchmain, phenotype.patchcolour, phenotype.patchunders)
            else:
                gensprite = MakeCat(
                    gensprite, phenotype.maincolour, phenotype.spritecolour, phenotype.mainunders)

            if not is_white:
                gensprite = ApplyPatchEffects(gensprite)

                if (phenotype.patchmain != ""):
                    for pattern in genotype.tortiepattern:
                        tortpatches = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        if 'rev' in pattern:
                            isred = not (
                                'red' in phenotype.maincolour or 'cream' in phenotype.maincolour or 'honey' in phenotype.maincolour or 'ivory' in phenotype.maincolour or 'apricot' in phenotype.maincolour)
                            tortpatches = MakeCat(
                                tortpatches, phenotype.maincolour, phenotype.spritecolour, phenotype.mainunders)
                        else:
                            isred = not (
                                'red' in phenotype.patchmain or 'cream' in phenotype.patchmain or 'honey' in phenotype.patchmain or 'ivory' in phenotype.patchmain or 'apricot' in phenotype.patchmain)
                            tortpatches = MakeCat(
                                tortpatches, phenotype.patchmain, phenotype.patchcolour, phenotype.patchunders)
                        if phenotype.caramel == 'caramel' and isred:
                            tortpatches.blit(
                                sprites.sprites['caramel0'], (0, 0))
                        tortpatches = ApplyPatchEffects(tortpatches)

                        tortpatches2 = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        tortpatches2.blit(
                            sprites.sprites[pattern.replace('rev', "") + cat_sprite], (0, 0))
                        tortpatches2.blit(tortpatches, (0, 0),
                                          special_flags=pygame.BLEND_RGBA_MULT)
                        gensprite.blit(tortpatches2, (0, 0))

                if (genotype.pseudomerle and not merle):
                    for pattern in genotype.merlepattern:
                        if 'rev' in pattern:
                            phenotype.SpriteInfo(sprite_age)
                            merlepatches = GenSprite(
                                genotype, phenotype, sprite_age, merle=True)
                        else:
                            old_silver = genotype.silver
                            phenotype.genotype.silver = ['i', 'i']
                            phenotype.SpriteInfo(sprite_age)
                            merlepatches = GenSprite(
                                genotype, phenotype, sprite_age, merle=True)
                            phenotype.genotype.silver = old_silver
                            phenotype.SpriteInfo(sprite_age)

                        merlepatches2 = pygame.Surface(
                            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        merlepatches2.blit(
                            sprites.sprites[pattern.replace('rev', "") + cat_sprite], (0, 0))
                        merlepatches2.blit(
                            merlepatches, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                        gensprite.blit(merlepatches2, (0, 0))

                if genotype.satin[0] == "st" or genotype.tenn[0] == 'tr':
                    gensprite.blit(sprites.sprites['satin0'], (0, 0))

                if (genotype.fevercoat and sprite_age < 5):
                    fevercoat = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    fevercoat.blit(
                        sprites.sprites['bleach' + cat_sprite], (0, 0))
                    fevercoat.blit(
                        sprites.sprites['bleach' + cat_sprite], (0, 0))
                    fevercoat.blit(
                        sprites.sprites['bleach' + cat_sprite], (0, 0))
                    fevercoat.blit(
                        sprites.sprites['bleach' + cat_sprite], (0, 0))
                    fevercoat.blit(
                        sprites.sprites['bleach' + cat_sprite], (0, 0))
                    fevercoat.blit(
                        sprites.sprites['lightbasecolours0'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    if (sprite_age > 2):
                        fevercoat.set_alpha(150)
                    gensprite.blit(fevercoat, (0, 0))

                elif (genotype.bleach[0] == "lb" and sprite_age > 3) or (genotype.wbtype == "shaded" and 'smoke' in phenotype.silvergold):
                    gensprite.blit(
                        sprites.sprites['bleach' + cat_sprite], (0, 0))

            gensprite = AddNose(gensprite)

            whitesprite = pygame.Surface(
                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
            tintedwhitesprite = pygame.Surface(
                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

            if (genotype.white_pattern != 'No' and genotype.white_pattern):
                for x in genotype.white_pattern:
                    if (x and 'dorsal' not in x and 'break/' not in x and x not in vitiligo):
                        whitesprite.blit(
                            sprites.sprites[x + cat_sprite], (0, 0))
            if (genotype.white_pattern != 'No' and genotype.white_pattern):
                for x in genotype.white_pattern:
                    if (x and 'break/' in x):
                        whitesprite.blit(
                            sprites.sprites[x + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
            tintedwhitesprite.blit(whitesprite, (0, 0))

            leathers = pygame.Surface(
                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
            leathers = AddPads(leathers, "white", override="white")
            leathers = AddNose(leathers, "white")
            white_leathers = pygame.Surface(
                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
            white_leathers.blit(whitesprite, (0, 0))

            if (genotype.vitiligo):
                for x in vitiligo:
                    if x in genotype.white_pattern:
                        white_leathers.blit(
                            sprites.sprites[x + cat_sprite], (0, 0))
                        tintedwhitesprite.blit(
                            sprites.sprites[x + cat_sprite], (0, 0))
            white_leathers.blit(
                leathers, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

            if genotype.white_pattern:
                if 'dorsal1' in genotype.white_pattern:
                    tintedwhitesprite.blit(
                        sprites.sprites['dorsal1' + cat_sprite], (0, 0))
                elif 'dorsal2' in genotype.white_pattern:
                    tintedwhitesprite.blit(
                        sprites.sprites['dorsal2' + cat_sprite], (0, 0))

            gensprite.blit(tintedwhitesprite, (0, 0))

            if cat.genotype.sedesp == ['hr', 're'] or (cat.genotype.sedesp[0] == 're' and sprite_age < 12) or (cat.genotype.laperm[0] == 'Lp' and sprite_age < 4):
                gensprite.blit(
                    sprites.sprites['furpoint' + cat_sprite], (0, 0))
                gensprite.blit(
                    sprites.sprites['furpoint' + cat_sprite], (0, 0))
            elif (cat.pelt.length == 'hairless'):
                gensprite.blit(
                    sprites.sprites['hairless' + cat_sprite], (0, 0))
                gensprite.blit(
                    sprites.sprites['furpoint' + cat_sprite], (0, 0))
            elif ('patchy ' in cat.phenotype.furtype):
                gensprite.blit(sprites.sprites['donskoy' + cat_sprite], (0, 0))

            if ('sparse' in cat.phenotype.furtype):
                gensprite.blit(sprites.sprites['satin0'], (0, 0))
                gensprite.blit(sprites.sprites['satin0'], (0, 0))
                gensprite.blit(sprites.sprites['lykoi' + cat_sprite], (0, 0))

            gensprite.blit(white_leathers, (0, 0))

            if (genotype.fold[0] != 'Fd' or genotype.curl[0] == 'Cu'):
                gensprite.blit(sprites.sprites['ears' + cat_sprite], (0, 0))

            if (int(cat_sprite) < 18):
                lefteye = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                righteye = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                special = pygame.Surface(
                    (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

                lefteye.blit(sprites.sprites['left' + cat_sprite], (0, 0))
                righteye.blit(sprites.sprites['right' + cat_sprite], (0, 0))

                lefteye.blit(sprites.sprites[genotype.lefteyetype + "/" +
                             cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                righteye.blit(sprites.sprites[genotype.righteyetype + "/" +
                              cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                gensprite.blit(lefteye, (0, 0))
                gensprite.blit(righteye, (0, 0))

                if sprite_age == 1:
                    lefteye.blit(sprites.sprites['left' + cat_sprite], (0, 0))
                    righteye.blit(
                        sprites.sprites['right' + cat_sprite], (0, 0))
                    lefteye.blit(sprites.sprites[genotype.lefteyetype.split(' ; ')[
                                 0] + ' ; blue' + "/" + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    righteye.blit(sprites.sprites[genotype.righteyetype.split(' ; ')[
                                  0] + ' ; blue' + "/" + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    lefteye.set_alpha(200)
                    righteye.set_alpha(200)
                    gensprite.blit(lefteye, (0, 0))
                    gensprite.blit(righteye, (0, 0))

                if (genotype.extraeye):
                    special.blit(
                        sprites.sprites[genotype.extraeye + cat_sprite], (0, 0))
                    special.blit(sprites.sprites[genotype.extraeyetype + "/" +
                                 cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    gensprite.blit(special, (0, 0))
                    if sprite_age == 1:
                        special.blit(
                            sprites.sprites[genotype.extraeye + cat_sprite], (0, 0))
                        special.blit(sprites.sprites[genotype.extraeyetype.split(' ; ')[
                                     0] + ' ; blue' + "/" + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                        special.set_alpha(150)
                        gensprite.blit(special, (0, 0))

                if (genotype.pinkdilute[0] == 'dp'):
                    pupils = pygame.Surface(
                        (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    pupils.blit(
                        sprites.sprites['redpupils' + cat_sprite], (0, 0))
                    pupils.set_alpha(100)
                    gensprite.blit(pupils, (0, 0))

            return gensprite

        gensprite.blit(
            GenSprite(cat.genotype, cat.phenotype, cat.moons), (0, 0))

        if (cat.genotype.chimera):
            chimerapatches = pygame.Surface(
                (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
            chimerapatches.blit(
                sprites.sprites[cat.genotype.chimerapattern + cat_sprite], (0, 0))
            chimerapheno = Phenotype(cat.genotype.chimerageno)
            chimerapheno.SpriteInfo(cat.moons)
            chimerapatches.blit(GenSprite(cat.genotype.chimerageno, chimerapheno,
                                cat.moons), (0, 0), special_flags=pygame.BLEND_RGB_MULT)
            gensprite.blit(chimerapatches, (0, 0))

        if not scars_hidden:
            for scar in cat_scars:
                if scar in cat.pelt.scars1:
                    gensprite.blit(
                        sprites.sprites['scars' + scar + cat_sprite], (0, 0))
                if scar in cat.pelt.scars3:
                    gensprite.blit(
                        sprites.sprites['scars' + scar + cat_sprite], (0, 0))

        # draw line art
        if cat.shading:
            gensprite.blit(
                sprites.sprites['shaders' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGB_MULT)
            gensprite.blit(sprites.sprites['lighting' + cat_sprite], (0, 0))

        # make sure colours are in the lines
        if (cat.genotype.wirehair[0] == 'Wh'):
            gensprite.blit(
                sprites.sprites['rexbord' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
            gensprite.blit(
                sprites.sprites['rexbord' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        else:
            gensprite.blit(
                sprites.sprites['normbord' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
            gensprite.blit(
                sprites.sprites['normbord' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        if (cat.genotype.fold[0] == 'Fd'):
            gensprite.blit(
                sprites.sprites['foldbord' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
            gensprite.blit(
                sprites.sprites['foldbord' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        elif (cat.genotype.curl[0] == 'Cu'):
            gensprite.blit(
                sprites.sprites['curlbord' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
            gensprite.blit(
                sprites.sprites['curlbord' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        new_sprite.blit(gensprite, (0, 0))

        lineart = pygame.Surface(
            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
        earlines = pygame.Surface(
            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
        bodylines = pygame.Surface(
            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

        if not dead:
            if (cat.genotype.fold[0] != 'Fd'):
                if (cat.genotype.curl[0] == 'Cu'):
                    earlines.blit(
                        sprites.sprites['curllines' + cat_sprite], (0, 0))
                else:
                    earlines.blit(
                        sprites.sprites['lines' + cat_sprite], (0, 0))
            elif (cat.genotype.curl[0] == 'Cu'):
                earlines.blit(
                    sprites.sprites['fold_curllines' + cat_sprite], (0, 0))
            else:
                earlines.blit(
                    sprites.sprites['foldlines' + cat_sprite], (0, 0))
        elif cat.df:
            if (cat.genotype.fold[0] != 'Fd'):
                if (cat.genotype.curl[0] == 'Cu'):
                    earlines.blit(
                        sprites.sprites['curllineartdf' + cat_sprite], (0, 0))
                else:
                    earlines.blit(
                        sprites.sprites['lineartdf' + cat_sprite], (0, 0))
            elif (cat.genotype.curl[0] == 'Cu'):
                earlines.blit(
                    sprites.sprites['fold_curllineartdf' + cat_sprite], (0, 0))
            else:
                earlines.blit(
                    sprites.sprites['foldlineartdf' + cat_sprite], (0, 0))
        elif dead:
            if (cat.genotype.fold[0] != 'Fd'):
                if (cat.genotype.curl[0] == 'Cu'):
                    earlines.blit(
                        sprites.sprites['curllineartdead' + cat_sprite], (0, 0))
                else:
                    earlines.blit(
                        sprites.sprites['lineartdead' + cat_sprite], (0, 0))
            elif (cat.genotype.curl[0] == 'Cu'):
                earlines.blit(
                    sprites.sprites['fold_curllineartdead' + cat_sprite], (0, 0))
            else:
                earlines.blit(
                    sprites.sprites['foldlineartdead' + cat_sprite], (0, 0))

        earlines.blit(sprites.sprites['isolateears' + cat_sprite],
                      (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        lineart.blit(earlines, (0, 0))
        if (cat.genotype.wirehair[0] == 'Wh'):
            if not dead:
                bodylines.blit(
                    sprites.sprites['rexlineart' + cat_sprite], (0, 0))
            elif cat.df:
                bodylines.blit(
                    sprites.sprites['rexlineartdf' + cat_sprite], (0, 0))
            else:
                bodylines.blit(
                    sprites.sprites['rexlineartdead' + cat_sprite], (0, 0))
        else:
            if not dead:
                bodylines.blit(sprites.sprites['lines' + cat_sprite], (0, 0))
            elif cat.df:
                bodylines.blit(
                    sprites.sprites['lineartdf' + cat_sprite], (0, 0))
            else:
                bodylines.blit(
                    sprites.sprites['lineartdead' + cat_sprite], (0, 0))

        bodylines.blit(sprites.sprites['noears' + cat_sprite],
                       (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        lineart.blit(bodylines, (0, 0))
        new_sprite.blit(lineart, (0, 0))

        # draw skin and scars2
        blendmode = pygame.BLEND_RGBA_MIN

        gensprite = new_sprite
        if cat.phenotype.bobtailnr > 0:
            gensprite.blit(
                sprites.sprites['bobtail' + str(cat.phenotype.bobtailnr) + cat_sprite], (0, 0))
        gensprite.set_colorkey((0, 0, 255))
        new_sprite = pygame.Surface(
            (sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
        new_sprite.blit(gensprite, (0, 0))

        if not scars_hidden:
            for scar in cat_scars:
                if scar in cat.pelt.scars2:
                    new_sprite.blit(
                        sprites.sprites['scars' + scar + cat_sprite], (0, 0), special_flags=blendmode)

        # draw accessories
        if not acc_hidden:
            if cat.pelt.accessory in cat.pelt.plant_accessories:
                new_sprite.blit(
                    sprites.sprites['acc_herbs' + cat.pelt.accessory + cat_sprite], (0, 0))
            elif cat.pelt.accessory in cat.pelt.wild_accessories:
                new_sprite.blit(
                    sprites.sprites['acc_wild' + cat.pelt.accessory + cat_sprite], (0, 0))
            elif cat.pelt.accessory in cat.pelt.collars:
                new_sprite.blit(
                    sprites.sprites['collars' + cat.pelt.accessory + cat_sprite], (0, 0))

        # reverse, if assigned so
        if cat.pelt.reverse:
            new_sprite = pygame.transform.flip(new_sprite, True, False)

    except (TypeError, KeyError):
        logger.exception("Failed to load sprite")

        # Placeholder image
        new_sprite = image_cache.load_image(
            f"sprites/error_placeholder.png").convert_alpha()

    return new_sprite

# ---------------------------------------------------------------------------- #
#                                     OTHER                                    #
# ---------------------------------------------------------------------------- #


def is_iterable(y):
    try:
        0 in y
    except TypeError:
        return False


def get_text_box_theme(themename=""):
    """Updates the name of the theme based on dark or light mode"""
    if game.settings['dark mode']:
        if themename == "":
            return "#default_dark"
        else:
            return themename + "_dark"
    else:
        if themename == "":
            return "text_box"
        else:
            return themename
