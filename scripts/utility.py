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

    new_sprite = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

    vitiligo = ['PHANTOM', 'POWDER', 'BLEACHED', 'VITILIGO', 'VITILIGOTWO', 'SMOKEY']

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
        solidcolours = {
            'black' : 0,
            'chocolate' : 1,
            'cinnamon' : 2,
            'lowred' : 3,
            'mediumred' : 4,
            'rufousedred' : 5,
            'blue' : 6,
            'lilac' : 7,
            'fawn' : 8,
            'lowcream' : 9,
            'mediumcream' : 10,
            'rufousedcream' : 11,
            'dove' : 12,
            'champagne' : 13,
            'buff' : 14,
            'lowhoney' : 15,
            'mediumhoney' : 16,
            'rufousedhoney' : 17,
            'platinum' : 18,
            'lavender' : 19,
            'beige' : 20,
            'lowivory' : 21,
            'mediumivory' : 22,
            'rufousedivory' : 23
        }

        stripecolourdict = {
                'rufousedapricot' : 'lowred',
                'mediumapricot' : 'rufousedcream',
                'lowapricot' : 'mediumcream',

                'rufousedhoney-apricot' : 'lowred',
                'mediumhoney-apricot' : 'rufousedhoney',
                'lowhoney-apricot' : 'mediumhoney',

                'rufousedivory-apricot' : 'lowhoney',
                'mediumivory-apricot' : 'rufousedivory',
                'lowivory-apricot' : 'mediumivory'
            }
        gensprite = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                
        def GenSprite(genotype, phenotype):
            phenotype.SpriteInfo(cat.moons)

            def CreateStripes(stripecolour, whichbase, coloursurface=None, pattern=None, special=None):
                stripebase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                
                if not pattern and not special and 'solid' not in whichbase:
                    if('chinchilla' in whichbase):
                        stripebase.blit(sprites.sprites['chinchillashading' + cat_sprite], (0, 0))   
                    elif('shaded' in whichbase):
                        stripebase.blit(sprites.sprites['shadedshading' + cat_sprite], (0, 0))       
                    else:           
                        stripebase.blit(sprites.sprites[genotype.wbtype + 'shading' + cat_sprite], (0, 0))      

                if pattern:
                    stripebase.blit(sprites.sprites[pattern + cat_sprite], (0, 0))
                else:    
                    stripebase.blit(sprites.sprites[phenotype.GetTabbySprite() + cat_sprite], (0, 0))

                charc = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                if(genotype.agouti[0] == "Apb" and ('red' not in stripecolour and 'cream' not in stripecolour and 'honey' not in stripecolour and 'ivory' not in stripecolour and 'apricot' not in stripecolour)):
                    charc.blit(sprites.sprites['charcoal' + cat_sprite], (0, 0))
                
                if(genotype.agouti == ["Apb", "Apb"]):
                    charc.set_alpha(125)
                stripebase.blit(charc, (0, 0))

                if coloursurface:
                    stripebase.blit(coloursurface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                elif 'basecolours' in stripecolour:
                    stripebase.blit(sprites.sprites[stripecolour], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                else:
                    surf = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    surf.blit(sprites.sprites['basecolours'+ str(solidcolours.get(stripecolourdict.get(stripecolour, stripecolour)))], (0, 0))
                    if phenotype.caramel == 'caramel' and not ('red' in stripecolour or 'cream' in stripecolour or 'honey' in stripecolour or 'ivory' in stripecolour or 'apricot' in stripecolour):    
                        surf.blit(sprites.sprites['caramel0'], (0, 0))

                    stripebase.blit(surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                
                middle = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                if(genotype.soktype == "full sokoke" and not pattern):
                    middle.blit(stripebase, (0, 0))
                    stripebase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    middle.set_alpha(150)
                    stripebase.blit(middle, (0, 0))
                    middle = CreateStripes(stripecolour, whichbase, coloursurface, pattern=phenotype.GetTabbySprite(special='redbar'), special=special)
                    stripebase.blit(middle, (0, 0))
                elif(genotype.soktype == "mild fading" and not pattern):
                    middle.blit(stripebase, (0, 0))
                    stripebase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    middle.set_alpha(204)
                    stripebase.blit(middle, (0, 0))
                    middle = CreateStripes(stripecolour, whichbase, coloursurface, pattern=phenotype.GetTabbySprite(special='redbar'), special=special)
                    stripebase.blit(middle, (0, 0))
                return stripebase

            def TabbyBase(whichcolour, whichbase, cat_unders, special = None):
                whichmain = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                whichmain.blit(sprites.sprites[whichbase], (0, 0))
                if special !='copper' and cat.moons > 12 and (genotype.silver[0] == 'I' and genotype.corin[0] == 'fg' and (cat.season == 'Leaf-fall' or cat.season == 'Leaf-bare')):
                    sunshine = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    
                    colours = phenotype.FindRed(genotype, cat.moons, special='low')
                    sunshine = MakeCat(sunshine, colours[0], colours[1], [colours[2], colours[3]], special='copper')

                    sunshine.set_alpha(150)
                    whichmain.blit(sunshine, (0, 0))

                unders = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                unders.blit(sprites.sprites["Tabby_unders" + cat_sprite], (0, 0))
                unders.blit(sprites.sprites[cat_unders[0]], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                unders.set_alpha(int(cat_unders[1] * 2.55))
                whichmain.blit(unders, (0, 0))

                if phenotype.caramel == 'caramel' and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):    
                    whichmain.blit(sprites.sprites['caramel0'], (0, 0))

                return whichmain
        
            def AddStripes(whichmain, whichcolour, whichbase, coloursurface=None):
                stripebase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                if((genotype.corin[0] != 'N' and genotype.wbtype == 'shaded') or genotype.wbtype == 'chinchilla'):
                    if not ("rufoused" in whichcolour or 'medium' in whichcolour or 'low' in whichcolour or genotype.wbtype == 'chinchilla'):
                        stripebase.blit(CreateStripes(phenotype.FindRed(genotype, cat.moons, special='red')[0], phenotype.FindRed(genotype, cat.moons, special='red')[1], coloursurface=coloursurface, special="gold"), (0, 0))
                        whichmain.blit(stripebase, (0, 0))
                    stripebase = CreateStripes(whichcolour, whichbase, coloursurface=coloursurface)
                    stripebase.set_alpha(120)
                    whichmain.blit(stripebase, (0, 0))
                    stripebase = CreateStripes(whichcolour, whichbase, coloursurface=coloursurface, pattern='agouti')
                elif(genotype.wbtype == 'shaded' or genotype.corin[0] != 'N'):
                    if not ("rufoused" in whichcolour or 'medium' in whichcolour or 'low' in whichcolour):
                        stripebase.blit(CreateStripes(phenotype.FindRed(genotype, cat.moons, special='red')[0], phenotype.FindRed(genotype, cat.moons, special='red')[1], coloursurface=coloursurface, special="gold"), (0, 0))
                        whichmain.blit(stripebase, (0, 0))
                    stripebase = CreateStripes(whichcolour, whichbase, coloursurface=coloursurface)
                    stripebase.set_alpha(200)
                    whichmain.blit(stripebase, (0, 0))
                    stripebase = CreateStripes(whichcolour, whichbase, coloursurface=coloursurface, pattern='agouti')
                elif('ec' in genotype.ext and 'Eg' not in genotype.ext):
                    stripebase = CreateStripes(whichcolour, whichbase, coloursurface=coloursurface)
                    stripebase.set_alpha(200)
                    whichmain.blit(stripebase, (0, 0))
                    stripebase = CreateStripes(whichcolour, whichbase, coloursurface=coloursurface, pattern='agouti')
                else:
                    stripebase.blit(CreateStripes(whichcolour, whichbase, coloursurface=coloursurface), (0, 0))

                
                whichmain.blit(stripebase, (0, 0))

                return whichmain

            def ApplySmokeEffects(whichmain):
                if(genotype.ext[0] == 'Eg' and genotype.agouti[0] != 'a'):
                    whichmain.blit(sprites.sprites['grizzle' + cat_sprite], (0, 0))
                if genotype.ghosting[0] == 'Gh' or (genotype.silver[0] == 'I' and cat.pelt.length == 'long'):
                    ghostingbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    ghostingbase.blit(sprites.sprites['ghost' + cat_sprite], (0, 0))
                    if(cat.moons < 4):
                        ghostingbase.set_alpha(150)
                    
                    whichmain.blit(ghostingbase, (0, 0))
                if (genotype.silver[0] == 'I' and cat.pelt.length != 'long'):
                    whichmain.blit(sprites.sprites['smoke' + cat_sprite], (0, 0))
                    if(phenotype.silvergold == ' light smoke '):
                        whichmain.blit(sprites.sprites['smoke' + cat_sprite], (0, 0))
                
                return whichmain

            def MakeCat(whichmain, whichcolour, whichbase, cat_unders, special=None):
                if (genotype.white[0] == 'W' or genotype.pointgene[0] == 'c' or whichcolour == 'white' or genotype.white_pattern == ['full white']):
                    whichmain.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                    if(genotype.pointgene[0] == "c"):
                        whichmain.blit(sprites.sprites['albino' + cat_sprite], (0, 0))
                elif(whichcolour != whichbase and special != 'masked silver'):
                    if(genotype.pointgene[0] == "C"):
                        whichmain = TabbyBase(whichcolour, whichbase, cat_unders, special)

                        whichmain = AddStripes(whichmain, whichcolour, whichbase)
                    else:
                        #create base
                        colourbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        if(whichcolour == "black" and genotype.pointgene[0] == "cm"):
                            colourbase.blit(sprites.sprites[whichbase.replace("black", "cinnamon")], (0, 0))
                        else:
                            colourbase = TabbyBase(whichcolour, whichbase, cat_unders, special)

                            if((genotype.pointgene == ["cb", "cb"] and cat_sprite != "20") or (((("cb" in genotype.pointgene or genotype.pointgene[0] == "cm") and cat_sprite != "20") or genotype.pointgene == ["cb", "cb"]) and cat.season == 'Leaf-bare')):
                                colourbase.set_alpha(100)
                            elif((("cb" in genotype.pointgene or genotype.pointgene[0] == "cm") and cat_sprite != "20") or genotype.pointgene == ["cb", "cb"] or ((cat_sprite != "20" or ("cb" in genotype.pointgene or genotype.pointgene[0] == "cm")) and cat.season == 'Leaf-bare')):
                                colourbase.set_alpha(50)
                            elif(cat_sprite != "20" or ("cb" in genotype.pointgene or genotype.pointgene[0] == "cm")):
                                colourbase.set_alpha(15)
                            else:
                                colourbase.set_alpha(0)
                        
                        whichmain.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                        whichmain.blit(colourbase, (0, 0))

                        #add base stripes
                        if("cm" in genotype.pointgene):
                            if(whichcolour == "black" and genotype.pointgene[0] == "cm"):
                                whichmain = AddStripes(whichmain, 'lightbasecolours2', whichbase)
                            else:
                                if("cb" in genotype.pointgene or genotype.pointgene[0] == "cm"):
                                    if(whichcolour == "black" and cat_sprite != "20"):
                                        whichmain = AddStripes(whichmain, 'lightbasecolours2', whichbase)
                                    elif((whichcolour == "chocolate" and cat_sprite != "20") or whichcolour == "black"):
                                        whichmain = AddStripes(whichmain, 'lightbasecolours1', whichbase)
                                    elif(whichcolour == "cinnamon" or whichcolour == "chocolate"):
                                        whichmain = AddStripes(whichmain, 'lightbasecolours0', whichbase)
                                    else:
                                        pointbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                        pointbase.blit(sprites.sprites['basecolours'+ str(solidcolours.get(stripecolourdict.get(whichcolour, whichcolour)))], (0, 0))
                                        if phenotype.caramel == 'caramel' and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):    
                                            pointbase.blit(sprites.sprites['caramel0'], (0, 0))
                                        pointbase.set_alpha(204)
                                        pointbase2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                        pointbase2.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                                        pointbase2.blit(pointbase, (0, 0))
                                        whichmain = AddStripes(whichmain, whichcolour, whichbase, coloursurface=pointbase2)
                                else:
                                    if(whichcolour == "black" and cat_sprite != "20"):
                                        whichmain = AddStripes(whichmain, 'lightbasecolours1', whichbase)
                                    else:
                                        whichmain = AddStripes(whichmain, 'lightbasecolours0', whichbase)
                        
                        else:
                            if(whichcolour == "black" and genotype.pointgene == ["cb", "cb"] and cat_sprite != "20"):
                                whichmain = AddStripes(whichmain, 'lightbasecolours3', whichbase)
                            elif(((whichcolour == "chocolate" and genotype.pointgene == ["cb", "cb"]) or (whichcolour == "black" and "cb" in genotype.pointgene)) and cat_sprite != "20" or (whichcolour == "black" and genotype.pointgene == ["cb", "cb"])):
                                whichmain = AddStripes(whichmain, 'lightbasecolours2', whichbase)
                            elif(((whichcolour == "cinnamon" and genotype.pointgene == ["cb", "cb"]) or (whichcolour == "chocolate" and "cb" in genotype.pointgene) or (whichcolour == "black" and genotype.pointgene == ["cs", "cs"])) and cat_sprite != "20" or ((whichcolour == "chocolate" and genotype.pointgene == ["cb", "cb"]) or (whichcolour == "black" and "cb" in genotype.pointgene))):
                                whichmain = AddStripes(whichmain, 'lightbasecolours1', whichbase)

                            elif(genotype.pointgene == ["cb", "cb"]):
                                pointbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                pointbase.blit(sprites.sprites['basecolours'+ str(solidcolours.get(stripecolourdict.get(whichcolour, whichcolour)))], (0, 0))
                                if phenotype.caramel == 'caramel' and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):    
                                    pointbase.blit(sprites.sprites['caramel0'], (0, 0))
                                pointbase.set_alpha(204)
                                pointbase2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                pointbase2.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                                pointbase2.blit(pointbase, (0, 0))
                                whichmain = AddStripes(whichmain, whichcolour, whichbase, coloursurface=pointbase2)
                            elif("cb" in genotype.pointgene):
                                pointbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                pointbase.blit(sprites.sprites['basecolours'+ str(solidcolours.get(stripecolourdict.get(whichcolour, whichcolour)))], (0, 0))
                                if phenotype.caramel == 'caramel' and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):    
                                    pointbase.blit(sprites.sprites['caramel0'], (0, 0))
                                if(genotype.eumelanin[0] == "bl"):
                                    pointbase.set_alpha(25)
                                else:
                                    pointbase.set_alpha(102)
                                pointbase2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                pointbase2.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                                pointbase2.blit(pointbase, (0, 0))
                                whichmain = AddStripes(whichmain, whichcolour, whichbase, coloursurface=pointbase2)
                            else:
                                whichmain = AddStripes(whichmain, 'lightbasecolours0', whichbase)

                        #mask base
                        colourbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        if(whichcolour == "black" and genotype.pointgene[0] == "cm"):
                            colourbase2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            colourbase.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                            colourbase2.blit(sprites.sprites[whichbase.replace("black", "cinnamon")], (0, 0))
                            colourbase2.set_alpha(150)
                            colourbase.blit(colourbase2, (0, 0))
                        else:
                            colourbase = TabbyBase(whichcolour, whichbase, cat_unders, special)
                        pointbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        pointbase2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        pointbase2.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                        if("cm" in genotype.pointgene):
                            if(whichcolour == "black" and genotype.pointgene[0] == "cm"):
                                pointbase.blit(colourbase, (0, 0))
                            else:
                                if((("cb" in genotype.pointgene or genotype.pointgene[0] == "cm") and cat_sprite != "20") or ((cat_sprite != "20" or ("cb" in genotype.pointgene or genotype.pointgene[0] == "cm")) and cat.season == "Leaf-bare")):
                                    colourbase.set_alpha(204)
                                elif(cat_sprite != "20" or ("cb" in genotype.pointgene or genotype.pointgene[0] == "cm")):
                                    colourbase.set_alpha(125)
                                else:
                                    colourbase.set_alpha(0)

                                pointbase2.blit(colourbase, (0, 0))

                                if(cat.season == "Greenleaf"):
                                    pointbase.blit(sprites.sprites['mochal' + cat_sprite], (0, 0))
                                    pointbase.blit(pointbase2, (0, 0), 
                                                special_flags=pygame.BLEND_RGBA_MULT)
                                elif(cat.season == "Leaf-bare"):
                                    pointbase.blit(sprites.sprites['mochad' + cat_sprite], (0, 0))
                                    pointbase.blit(pointbase2, (0, 0), 
                                                special_flags=pygame.BLEND_RGBA_MULT)
                                else:
                                    pointbase.blit(sprites.sprites['mocham' + cat_sprite], (0, 0))
                                    pointbase.blit(pointbase2, (0, 0), 
                                                special_flags=pygame.BLEND_RGBA_MULT)
                            
                                
                        else:
                            if((genotype.pointgene == ["cb", "cb"] and cat_sprite != "20") or ("cb" in genotype.pointgene and cat_sprite != "20" and cat.season == 'Leaf-bare')):
                                colourbase.set_alpha(180)
                            elif(("cb" in genotype.pointgene and cat_sprite != "20") or genotype.pointgene == ["cb", "cb"] or ((cat_sprite != "20" or "cb" in genotype.pointgene) and cat.season == 'Leaf-bare')):
                                colourbase.set_alpha(120)
                            elif(cat_sprite != "20" or "cb" in genotype.pointgene):
                                colourbase.set_alpha(50)
                            else:
                                colourbase.set_alpha(15)
                            
                            pointbase2.blit(colourbase, (0, 0))

                            if(cat.season == "Greenleaf"):
                                pointbase.blit(sprites.sprites['pointsl' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0), 
                                            special_flags=pygame.BLEND_RGBA_MULT)
                            elif(cat.season == "Leaf-bare"):
                                pointbase.blit(sprites.sprites['pointsd' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0), 
                                            special_flags=pygame.BLEND_RGBA_MULT)
                            else:
                                pointbase.blit(sprites.sprites['pointsm' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0), 
                                            special_flags=pygame.BLEND_RGBA_MULT)
                        
                            
                        #add mask stripes
                    
                        stripebase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        stripebase2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

                        if(whichcolour == "black" and genotype.pointgene[0] == "cm"):
                            colour = 'cinnamon'
                        else:
                            colour = whichcolour
                
                        stripebase.blit(CreateStripes(colour, whichbase), (0, 0))

                        
                        if(cat.season == "Greenleaf"):
                            stripebase2.blit(sprites.sprites['mochal' + cat_sprite], (0, 0))
                            stripebase2.blit(stripebase, (0, 0), 
                                        special_flags=pygame.BLEND_RGBA_MULT)
                        elif(cat.season == "Leaf-bare"):
                            stripebase2.blit(sprites.sprites['mochad' + cat_sprite], (0, 0))
                            stripebase2.blit(stripebase, (0, 0), 
                                        special_flags=pygame.BLEND_RGBA_MULT)
                        else:
                            stripebase2.blit(sprites.sprites['mocham' + cat_sprite], (0, 0))
                            stripebase2.blit(stripebase, (0, 0), 
                                        special_flags=pygame.BLEND_RGBA_MULT)

                        pointbase.blit(stripebase2, (0, 0))

                        whichmain.blit(pointbase, (0, 0))

                else:
                    if(genotype.pointgene[0] == "C"):
                        whichmain.blit(sprites.sprites['basecolours'+ str(solidcolours.get(stripecolourdict.get(whichcolour, whichcolour)))], (0, 0))
                        if phenotype.caramel == 'caramel' and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):    
                            whichmain.blit(sprites.sprites['caramel0'], (0, 0))
                            
                        whichmain = ApplySmokeEffects(whichmain)

                        stripebase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    
                        stripebase.blit(CreateStripes(whichcolour, "solid"), (0, 0))
                        
                        whichmain.blit(stripebase, (0, 0))
                    elif("cm" in genotype.pointgene):
                        colour = None
                        coloursurface = None
                        if(whichcolour == "black" and genotype.pointgene[0] == "cm"):
                            whichmain.blit(sprites.sprites['lightbasecolours2'], (0, 0)) 
                            whichmain = ApplySmokeEffects(whichmain)

                            stripebase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        
                            stripebase.blit(CreateStripes('cinnamon', 'solid', pattern="fullbar"), (0, 0))
                            stripebase.set_alpha(150)

                            whichmain.blit(stripebase, (0, 0))
                        else:
                            stripebase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                
                            if("cb" in genotype.pointgene or genotype.pointgene[0] == "cm"):
                                if(whichcolour == "black" and cat_sprite != "20"):
                                    whichmain.blit(sprites.sprites['lightbasecolours2'], (0, 0))
                                    colour = 'lightbasecolours2'
                                    whichmain = ApplySmokeEffects(whichmain)

                                elif((whichcolour == "chocolate" and cat_sprite != "20") or whichcolour == "black"):
                                    whichmain.blit(sprites.sprites['lightbasecolours1'], (0, 0))
                                    colour = 'lightbasecolours1'
                                    whichmain = ApplySmokeEffects(whichmain)
                                elif(whichcolour == "cinnamon" or whichcolour == "chocolate"):
                                    whichmain.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                                    colour = 'lightbasecolours0'
                                else:
                                    pointbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                                    pointbase.blit(sprites.sprites['basecolours'+ str(solidcolours.get(whichcolour))], (0, 0))
                                    if phenotype.caramel == 'caramel' and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):    
                                        pointbase.blit(sprites.sprites['caramel0'], (0, 0))
                        
                                    pointbase.set_alpha(204)
                                    whichmain.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                                    whichmain.blit(pointbase, (0, 0))
                                    pointbase.blit(whichmain, (0, 0))
                                    coloursurface = pointbase
                                    colour = whichcolour
                                    
                                    whichmain = ApplySmokeEffects(whichmain)
                            else:
                                if(whichcolour == "black" and cat_sprite != "20"):
                                    whichmain.blit(sprites.sprites['lightbasecolours1'], (0, 0))
                                    colour = 'lightbasecolours1'
                                    whichmain = ApplySmokeEffects(whichmain)
                                else:
                                    whichmain.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                                    colour = 'lightbasecolours0'
                            
                            stripebase = CreateStripes(colour, 'solid', coloursurface=coloursurface)
                            whichmain.blit(stripebase, (0, 0))

                            pointbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            pointbase2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            
                            pointbase2.blit(sprites.sprites['basecolours'+ str(solidcolours.get(whichcolour))], (0, 0))
                            if phenotype.caramel == 'caramel' and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):    
                                pointbase2.blit(sprites.sprites['caramel0'], (0, 0))
                        
                            whichmain = ApplySmokeEffects(whichmain)


                            stripebase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            stripebase.blit(CreateStripes(whichcolour, 'solid'), (0, 0))

                            pointbase2.blit(stripebase, (0, 0))

                            if(cat.season == "Greenleaf"):
                                pointbase.blit(sprites.sprites['mochal' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0), 
                                            special_flags=pygame.BLEND_RGBA_MULT)
                            elif(cat.season == "Leaf-bare"):
                                pointbase.blit(sprites.sprites['mochad' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0), 
                                            special_flags=pygame.BLEND_RGBA_MULT)
                            else:
                                pointbase.blit(sprites.sprites['mocham' + cat_sprite], (0, 0))
                                pointbase.blit(pointbase2, (0, 0), 
                                            special_flags=pygame.BLEND_RGBA_MULT)
                        
                            whichmain.blit(pointbase, (0, 0))        
                            
                    else:
                        colour = whichcolour
                        coloursurface = None
                        stripebase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        if(whichcolour == "black" and genotype.pointgene == ["cb", "cb"] and cat_sprite != "20"):
                            whichmain.blit(sprites.sprites['lightbasecolours3'], (0, 0)) 
                            colour = 'lightbasecolours3'
                            whichmain = ApplySmokeEffects(whichmain)
                        elif(((whichcolour == "chocolate" and genotype.pointgene == ["cb", "cb"]) or (whichcolour == "black" and "cb" in genotype.pointgene)) and cat_sprite != "20" or (whichcolour == "black" and genotype.pointgene == ["cb", "cb"])):
                            whichmain.blit(sprites.sprites['lightbasecolours2'], (0, 0)) 
                            colour = 'lightbasecolours2'
                            whichmain = ApplySmokeEffects(whichmain)
                        elif(((whichcolour == "cinnamon" and genotype.pointgene == ["cb", "cb"]) or (whichcolour == "chocolate" and "cb" in genotype.pointgene) or (whichcolour == "black" and genotype.pointgene == ["cs", "cs"])) and cat_sprite != "20" or ((whichcolour == "chocolate" and genotype.pointgene == ["cb", "cb"]) or (whichcolour == "black" and "cb" in genotype.pointgene))):
                            whichmain.blit(sprites.sprites['lightbasecolours1'], (0, 0))  
                            colour = 'lightbasecolours1'
                            whichmain = ApplySmokeEffects(whichmain)
                        elif(genotype.pointgene == ["cb", "cb"]):
                            pointbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            pointbase.blit(sprites.sprites['basecolours'+ str(solidcolours.get(whichcolour))], (0, 0))
                            if phenotype.caramel == 'caramel' and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):    
                                pointbase.blit(sprites.sprites['caramel0'], (0, 0))
                        
                            pointbase.set_alpha(204)
                            whichmain.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                            whichmain.blit(pointbase, (0, 0))
                            pointbase.blit(whichmain, (0, 0)) 
                            coloursurface = pointbase
                            whichmain = ApplySmokeEffects(whichmain)
                        elif("cb" in genotype.pointgene):
                            pointbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            pointbase.blit(sprites.sprites['basecolours'+ str(solidcolours.get(whichcolour))], (0, 0))
                            if phenotype.caramel == 'caramel' and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):    
                                pointbase.blit(sprites.sprites['caramel0'], (0, 0))
                        
                            if(genotype.eumelanin[0] == "bl"):
                                pointbase.set_alpha(25)
                            else:
                                pointbase.set_alpha(102)
                            whichmain.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                            whichmain.blit(pointbase, (0, 0))
                            coloursurface = whichmain
                            whichmain = ApplySmokeEffects(whichmain)

                        else:
                            whichmain.blit(sprites.sprites['lightbasecolours0'], (0, 0))
                            colour = 'lightbasecolours0'

                        stripebase = CreateStripes(colour, 'solid', coloursurface=coloursurface)

                        whichmain.blit(stripebase, (0, 0))

                        pointbase = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        pointbase2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                            
                        pointbase2.blit(sprites.sprites['basecolours'+ str(solidcolours.get(whichcolour))], (0, 0))
                        if phenotype.caramel == 'caramel' and not ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):    
                                pointbase2.blit(sprites.sprites['caramel0'], (0, 0))
                        whichmain = ApplySmokeEffects(whichmain)

                        stripebase = CreateStripes(whichcolour, "solid")
                        
                        pointbase2.blit(stripebase, (0, 0))
                        if(cat.season == "Greenleaf"):
                            pointbase.blit(sprites.sprites['pointsl' + cat_sprite], (0, 0))
                            pointbase.blit(pointbase2, (0, 0), 
                                        special_flags=pygame.BLEND_RGBA_MULT)
                        elif(cat.season == "Leaf-bare"):
                            pointbase.blit(sprites.sprites['pointsd' + cat_sprite], (0, 0))
                            pointbase.blit(pointbase2, (0, 0), 
                                        special_flags=pygame.BLEND_RGBA_MULT)
                        else:
                            pointbase.blit(sprites.sprites['pointsm' + cat_sprite], (0, 0))
                            pointbase.blit(pointbase2, (0, 0), 
                                        special_flags=pygame.BLEND_RGBA_MULT)
                    
                        whichmain.blit(pointbase, (0, 0))


                seasondict = {
                    'Greenleaf': 'summer',
                    'Leaf-bare': 'winter'
                }

                if(genotype.karp[0] == 'K'):
                    if(genotype.karp[1] == 'K'):
                        whichmain.blit(sprites.sprites['homokarpati'+ seasondict.get(cat.season, "spring") + cat_sprite], (0, 0))
                    else:
                        whichmain.blit(sprites.sprites['hetkarpati'+ seasondict.get(cat.season, "spring") + cat_sprite], (0, 0))
                if(genotype.white[0] == 'wsal'):
                    whichmain.blit(sprites.sprites['salmiak' + cat_sprite], (0, 0))



                pads = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                pads.blit(sprites.sprites['pads' + cat_sprite], (0, 0))

                pad_dict = {
                    'red' : 0,
                    'white' : 1,
                    'tabby' : 2,
                    'black' : 3,
                    'chocolate' : 4,
                    'cinnamon' : 5,
                    'blue' : 6,
                    'lilac' : 7,
                    'fawn' : 8,
                    'dove' : 9,
                    'champagne' : 10,
                    'buff' : 11,
                    'platinum' : 12,
                    'lavender' : 13,
                    'beige' : 14
                }

                if(genotype.white[0] == 'W' or genotype.pointgene[0] == 'c' or genotype.white_pattern == ['full white']):
                    pads.blit(sprites.sprites['nosecolours1'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                elif ('red' in whichcolour or 'cream' in whichcolour or 'honey' in whichcolour or 'ivory' in whichcolour or 'apricot' in whichcolour):
                    pads.blit(sprites.sprites['nosecolours0'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                else:
                    pads.blit(sprites.sprites['nosecolours' + str(pad_dict.get(whichcolour))], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                whichmain.blit(pads, (0, 0))
                
                return whichmain

            gensprite = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
            gensprite = MakeCat(gensprite, phenotype.maincolour, phenotype.spritecolour, phenotype.mainunders)

            if('masked' in phenotype.silvergold):
                masked = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                masked = MakeCat(masked, phenotype.maincolour, phenotype.spritecolour, phenotype.mainunders, special="masked silver")
                masked2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                masked2.blit(sprites.sprites["tortiemaskBLUE-TIPPED" + cat_sprite], (0, 0))
                masked2.blit(masked, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                masked2.set_alpha(120)
                gensprite.blit(masked2, (0, 0))
                
            
            def ApplyPatchEffects(sprite):
                if (genotype.ext[0] == 'Eg' and genotype.agouti[0] != 'a') and genotype.satin[0] != "st" and genotype.tenn[0] != 'tr' and not ('red' in phenotype.maincolour or 'cream' in phenotype.maincolour or 'honey' in phenotype.maincolour or 'ivory' in phenotype.maincolour or 'apricot' in phenotype.maincolour):    
                    sprite.blit(sprites.sprites['satin0'], (0, 0))
                elif (genotype.glitter[0] == 'gl' or genotype.ghosting[0] == 'Gh') and (genotype.agouti[0] != 'a' or ('red' in phenotype.maincolour or 'cream' in phenotype.maincolour or 'honey' in phenotype.maincolour or 'ivory' in phenotype.maincolour or 'apricot' in phenotype.maincolour)):    
                    if genotype.satin[0] != "st" and genotype.tenn[0] != 'tr':    
                        sprite.blit(sprites.sprites['satin0'], (0, 0))
                    if(genotype.ghosting[0] == 'Gh'):
                        fading = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                        fading.blit(sprites.sprites['tabbyghost'+cat_sprite], (0, 0))
                        fading.set_alpha(50)
                        sprite.blit(fading, (0, 0))
                        sprite.blit(sprites.sprites['satin0'], (0, 0))
                if not genotype.brindledbi and not ('red' in phenotype.maincolour or 'cream' in phenotype.maincolour or 'honey' in phenotype.maincolour or 'ivory' in phenotype.maincolour or 'apricot' in phenotype.maincolour) and (genotype.ext[0] != "Eg" and genotype.agouti[0] !='a' and (genotype.corin[0] == 'sg' or genotype.corin[0] == 'sh' or ('ec' in genotype.ext and genotype.ext[0] != "Eg") or (genotype.ext[0] == 'ea' and cat.moons > 6) or (genotype.silver[0] == 'i' and genotype.corin[0] == 'fg'))):
                    sunshine = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    sunshine.blit(sprites.sprites['bimetal' + cat_sprite], (0, 0))

                    colours = phenotype.FindRed(genotype, cat.moons, special='nosilver')
                    underbelly = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    underbelly = MakeCat(underbelly, colours[0], colours[1], [colours[2], colours[3]], special='nounders')
                    sunshine.blit(underbelly, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

                    sunshine.set_alpha(75)
                    sprite.blit(sunshine, (0, 0))
                return sprite
            gensprite = ApplyPatchEffects(gensprite)
            

            if(phenotype.patchmain != ""):
                tortpatches = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                tortpatches = MakeCat(tortpatches, phenotype.patchmain, phenotype.patchcolour, phenotype.patchunders)
                if('masked' in phenotype.silvergold):
                    masked = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    masked = MakeCat(masked, phenotype.patchmain, phenotype.patchcolour, phenotype.patchunders, special="masked silver")
                    masked2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                    masked2.blit(sprites.sprites["tortiemaskBLUE-TIPPED" + cat_sprite], (0, 0))
                    masked2.blit(masked, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    masked2.set_alpha(120)
                    tortpatches.blit(masked2, (0, 0))
                    
                
                if phenotype.caramel == 'caramel' and not ('red' in phenotype.patchmain or 'cream' in phenotype.patchmain or 'honey' in phenotype.patchmain or 'ivory' in phenotype.patchmain or 'apricot' in phenotype.patchmain): 
                    tortpatches.blit(sprites.sprites['caramel0'], (0, 0))
                tortpatches = ApplyPatchEffects(tortpatches)
                
                tortpatches2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                tortpatches2.blit(sprites.sprites['tortiemask' + phenotype.tortpattern.replace('rev', "") + cat_sprite], (0, 0))
                tortpatches2.blit(tortpatches, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                gensprite.blit(tortpatches2, (0, 0))    

            if genotype.satin[0] == "st" or genotype.tenn[0] == 'tr':
                gensprite.blit(sprites.sprites['satin0'], (0, 0))

            if (genotype.bleach[0] == "lb" and cat.moons > 3) or 'masked' in phenotype.silvergold:
                gensprite.blit(sprites.sprites['bleach' + cat_sprite], (0, 0))
            
            
            nose = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
            nose.blit(sprites.sprites['nose' + cat_sprite], (0, 0))

            nose_dict = {
                'red' : 0,
                'white' : 1,
                'tabby' : 2,
                'black' : 3,
                'chocolate' : 4,
                'cinnamon' : 5,
                'blue' : 6,
                'lilac' : 7,
                'fawn' : 8,
                'dove' : 9,
                'champagne' : 10,
                'buff' : 11,
                'platinum' : 12,
                'lavender' : 13,
                'beige' : 14
            }

            if(genotype.white[0] == 'W' or genotype.pointgene[0] == 'c'):
                nose.blit(sprites.sprites['nosecolours1'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            elif ((genotype.ext[0] == 'ea' and genotype.agouti[0] != 'a') or 'red' in phenotype.maincolour or 'cream' in phenotype.maincolour or 'honey' in phenotype.maincolour or 'ivory' in phenotype.maincolour or 'apricot' in phenotype.maincolour):
                nose.blit(sprites.sprites['nosecolours0'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            elif (phenotype.maincolour != phenotype.spritecolour and genotype.ext[0] != 'ea'):
                nose.blit(sprites.sprites['nosecolours2'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            else:
                nose.blit(sprites.sprites['nosecolours' + str(nose_dict.get(phenotype.maincolour))], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

            gensprite.blit(nose, (0, 0))

            whitesprite = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

            if(genotype.white_pattern != 'No' and genotype.white_pattern and genotype.white[0] != 'wsal'):
                for x in genotype.white_pattern:
                    if(x and 'dorsal' not in x and x not in vitiligo and 'break/' not in x):
                        whitesprite.blit(sprites.sprites[x + cat_sprite], (0, 0))
            if(genotype.white_pattern != 'No' and genotype.white_pattern):
                for x in genotype.white_pattern:
                    if(x and 'dorsal' not in x and x not in vitiligo and 'break/' in x):
                        whitesprite.blit(sprites.sprites[x + cat_sprite], (0, 0))

            whitesprite.set_colorkey((0, 0, 255))
            nose.blit(sprites.sprites['pads' + cat_sprite], (0, 0))
            nose.blit(sprites.sprites['nose' + cat_sprite], (0, 0))
            nose.blit(sprites.sprites['nosecolours1'], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            nose2 = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
            nose2.blit(whitesprite, (0, 0))

            if(genotype.white_pattern[0]):
                for x in vitiligo:
                    if x in genotype.white_pattern:
                        nose2.blit(sprites.sprites[x + cat_sprite], (0, 0))
            nose2.blit(nose, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

            gensprite.blit(whitesprite, (0, 0))
            if(genotype.white_pattern[0]):
                for x in vitiligo:
                    if x in genotype.white_pattern:
                        gensprite.blit(sprites.sprites[x + cat_sprite], (0, 0))
            if genotype.white_pattern:
                if 'dorsal1' in genotype.white_pattern:
                    gensprite.blit(sprites.sprites['dorsal1' + cat_sprite], (0, 0))
                elif 'dorsal2' in genotype.white_pattern:
                    gensprite.blit(sprites.sprites['dorsal2' + cat_sprite], (0, 0))


            if cat.genotype.sedesp == ['hr', 're'] or (cat.genotype.sedesp[0] == 're' and cat.moons < 12) or (cat.genotype.laperm[0] == 'Lp' and cat.moons < 4):
                gensprite.blit(sprites.sprites['furpoint' + cat_sprite], (0, 0))
                gensprite.blit(sprites.sprites['furpoint' + cat_sprite], (0, 0))
            elif(cat.pelt.length == 'hairless'):
                gensprite.blit(sprites.sprites['hairless' + cat_sprite], (0, 0))
                gensprite.blit(sprites.sprites['furpoint' + cat_sprite], (0, 0))
            elif('patchy ' in cat.phenotype.furtype):
                gensprite.blit(sprites.sprites['donskoy' + cat_sprite], (0, 0))
            
            if('sparse' in cat.phenotype.furtype) and not (cat.genotype.sedesp == ['hr', 're'] or (cat.genotype.sedesp[0] == 're' and cat.moons < 12) or (cat.genotype.laperm[0] == 'Lp' and cat.moons < 4) or cat.pelt.length == 'hairless'):
                gensprite.blit(sprites.sprites['satin0'], (0, 0))
                gensprite.blit(sprites.sprites['satin0'], (0, 0))
                gensprite.blit(sprites.sprites['lykoi' + cat_sprite], (0, 0))
            if('sparse' in cat.phenotype.furtype) and (cat.genotype.sedesp == ['hr', 're'] or (cat.genotype.sedesp[0] == 're' and cat.moons < 12) or (cat.genotype.laperm[0] == 'Lp' and cat.moons < 4)):
                gensprite.blit(sprites.sprites['lykoi' + cat_sprite], (0, 0))

            gensprite.blit(nose2, (0, 0))
            

            if(genotype.fold[0] != 'Fd' or genotype.curl[0] == 'Cu'):
                gensprite.blit(sprites.sprites['ears' + cat_sprite], (0, 0))

            if(int(cat_sprite) < 18):
                lefteye = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                righteye = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
                special = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

                lefteye.blit(sprites.sprites['left' + cat_sprite], (0, 0))
                righteye.blit(sprites.sprites['right' + cat_sprite], (0, 0))

                lefteye.blit(sprites.sprites[genotype.lefteyetype + "/" + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                righteye.blit(sprites.sprites[genotype.righteyetype + "/" + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                gensprite.blit(lefteye, (0, 0))
                gensprite.blit(righteye, (0, 0))

                if(genotype.extraeye):
                    special.blit(sprites.sprites[genotype.extraeye + cat_sprite], (0, 0))
                    special.blit(sprites.sprites[genotype.extraeyetype + "/" + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                    gensprite.blit(special, (0, 0))

                if(genotype.pinkdilute[0] == 'dp'):
                    gensprite.blit(sprites.sprites['redpupils' + cat_sprite], (0, 0))
            
            return gensprite

        gensprite.blit(GenSprite(cat.genotype, cat.phenotype), (0, 0))

        if(cat.genotype.chimera):
            chimerapatches = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
            chimerapatches.blit(sprites.sprites['tortiemask' + cat.genotype.chimerapattern + cat_sprite], (0, 0))
            chimerapheno = Phenotype(cat.genotype.chimerageno)
            chimerapatches.blit(GenSprite(cat.genotype.chimerageno, chimerapheno), (0, 0), special_flags=pygame.BLEND_RGB_MULT)
            gensprite.blit(chimerapatches, (0, 0))

        if not scars_hidden:
            for scar in cat_scars:
                if scar in cat.pelt.scars1:
                    gensprite.blit(sprites.sprites['scars' + scar + cat_sprite], (0, 0))
                if scar in cat.pelt.scars3:
                    gensprite.blit(sprites.sprites['scars' + scar + cat_sprite], (0, 0))

        # draw line art
        if cat.shading:
            gensprite.blit(sprites.sprites['shaders' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGB_MULT)
            gensprite.blit(sprites.sprites['lighting' + cat_sprite], (0, 0))

        # make sure colours are in the lines
        if(cat.genotype.wirehair[0] == 'Wh'):
            gensprite.blit(sprites.sprites['rexbord'+ cat_sprite], (0, 0))
            gensprite.blit(sprites.sprites['rexbord'+ cat_sprite], (0, 0))
        else:
            gensprite.blit(sprites.sprites['normbord'+ cat_sprite], (0, 0))
            gensprite.blit(sprites.sprites['normbord'+ cat_sprite], (0, 0))
        if(cat.genotype.fold[0] == 'Fd'):
            gensprite.blit(sprites.sprites['foldbord'+ cat_sprite], (0, 0))
            gensprite.blit(sprites.sprites['foldbord'+ cat_sprite], (0, 0))
        elif(cat.genotype.curl[0] == 'Cu'):
            gensprite.blit(sprites.sprites['curlbord'+ cat_sprite], (0, 0))
            gensprite.blit(sprites.sprites['curlbord'+ cat_sprite], (0, 0))
        
        gensprite.set_colorkey((0, 0, 255))

        new_sprite.blit(gensprite, (0, 0))

        lineart = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
        earlines = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
        bodylines = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

        if not dead:
            if(cat.genotype.fold[0] != 'Fd'):
                if(cat.genotype.curl[0] == 'Cu'):
                    earlines.blit(sprites.sprites['curllines' + cat_sprite], (0, 0))
                else:
                    earlines.blit(sprites.sprites['lines' + cat_sprite], (0, 0))
            elif(cat.genotype.curl[0] == 'Cu'):
                earlines.blit(sprites.sprites['fold_curllines' + cat_sprite], (0, 0))
            else:
                earlines.blit(sprites.sprites['foldlines' + cat_sprite], (0, 0))
        elif cat.df:
            if(cat.genotype.fold[0] != 'Fd'):
                if(cat.genotype.curl[0] == 'Cu'):
                    earlines.blit(sprites.sprites['curllineartdf' + cat_sprite], (0, 0))
                else:
                    earlines.blit(sprites.sprites['lineartdf' + cat_sprite], (0, 0))
            elif(cat.genotype.curl[0] == 'Cu'):
                earlines.blit(sprites.sprites['fold_curllineartdf' + cat_sprite], (0, 0))
            else:
                earlines.blit(sprites.sprites['foldlineartdf' + cat_sprite], (0, 0))
        elif dead:
            if(cat.genotype.fold[0] != 'Fd'):
                if(cat.genotype.curl[0] == 'Cu'):
                    earlines.blit(sprites.sprites['curllineartdead' + cat_sprite], (0, 0))
                else:
                    earlines.blit(sprites.sprites['lineartdead' + cat_sprite], (0, 0))
            elif(cat.genotype.curl[0] == 'Cu'):
                earlines.blit(sprites.sprites['fold_curllineartdead' + cat_sprite], (0, 0))
            else:
                earlines.blit(sprites.sprites['foldlineartdead' + cat_sprite], (0, 0))

        earlines.blit(sprites.sprites['isolateears' + cat_sprite], (0, 0))
        earlines.set_colorkey((0, 0, 255))

        lineart.blit(earlines, (0, 0))
        if(cat.genotype.wirehair[0] == 'Wh'):
            if not dead:
                bodylines.blit(sprites.sprites['rexlineart' + cat_sprite], (0, 0))
            elif cat.df:
                bodylines.blit(sprites.sprites['rexlineartdf' + cat_sprite], (0, 0))
            else:
                bodylines.blit(sprites.sprites['rexlineartdead' + cat_sprite], (0, 0))
        else:
            if not dead:
                bodylines.blit(sprites.sprites['lines' + cat_sprite], (0, 0))
            elif cat.df:
                bodylines.blit(sprites.sprites['lineartdf' + cat_sprite], (0, 0))
            else:
                bodylines.blit(sprites.sprites['lineartdead' + cat_sprite], (0, 0))
            
        bodylines.blit(sprites.sprites['noears' + cat_sprite], (0, 0))
        bodylines.set_colorkey((0, 0, 255))
        lineart.blit(bodylines, (0, 0))
        new_sprite.blit(lineart, (0, 0))

        # draw skin and scars2
        blendmode = pygame.BLEND_RGBA_MIN

        gensprite = new_sprite
        if cat.phenotype.bobtailnr > 0:
            gensprite.blit(sprites.sprites['bobtail' + str(cat.phenotype.bobtailnr) + cat_sprite], (0, 0))
        gensprite.set_colorkey((0, 0, 255))
        new_sprite = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)
        new_sprite.blit(gensprite, (0, 0))

        if not scars_hidden:
            for scar in cat_scars:
                if scar in cat.pelt.scars2:
                    new_sprite.blit(sprites.sprites['scars' + scar + cat_sprite], (0, 0), special_flags=blendmode)

        # draw accessories
        if not acc_hidden:        
            if cat.pelt.accessory in cat.pelt.plant_accessories:
                new_sprite.blit(sprites.sprites['acc_herbs' + cat.pelt.accessory + cat_sprite], (0, 0))
            elif cat.pelt.accessory in cat.pelt.wild_accessories:
                new_sprite.blit(sprites.sprites['acc_wild' + cat.pelt.accessory + cat_sprite], (0, 0))
            elif cat.pelt.accessory in cat.pelt.collars:
                new_sprite.blit(sprites.sprites['collars' + cat.pelt.accessory + cat_sprite], (0, 0))

        # reverse, if assigned so
        if cat.pelt.reverse:
            new_sprite = pygame.transform.flip(new_sprite, True, False)

    except (TypeError, KeyError):
        logger.exception("Failed to load sprite")

        # Placeholder image
        new_sprite = image_cache.load_image(f"sprites/error_placeholder.png").convert_alpha()

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





