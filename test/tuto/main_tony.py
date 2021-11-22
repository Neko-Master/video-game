import os.path
import pygame
import random
import copy

def lire_images():
    imageBank = {}
    imageBank["perso"] = pygame.image.load("Images/perso.png").convert_alpha()
    imageBank["perso"] = pygame.transform.scale(imageBank["perso"], (48, 48))
    imageBank["exit_button"] = pygame.image.load("Images/Animations/platformerGraphics_otherStyle/Tiles/signExit.png")
    imageBank["exit_button"] = pygame.transform.scale(imageBank["exit_button"], (50, 50))
    imageBank["start_button"] = pygame.image.load("Images/start_button.png")
    imageBank["quit_button"] = pygame.image.load("Images/quit_button.png")
    imageBank["balle"] = pygame.image.load("Images/balle.png").convert_alpha()
    imageBank["blue_gem"] = pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/Items/gemBlue.png").convert_alpha()
    imageBank["heart_full"] = pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/HUD/hud_heartFull.png").convert_alpha()
    imageBank["heart_empty"] = pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/HUD/hud_heartEmpty.png").convert_alpha()
    imageBank["hud_gem_green"] = pygame.transform.scale(pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/HUD/hud_gem_green.png").convert_alpha(), (30, 23))
    imageBank["hud_gem_blue"] = pygame.transform.scale(pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/HUD/hud_gem_blue.png").convert_alpha(), (30, 23))
    imageBank["x_sign"] = pygame.transform.scale(pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/HUD/hud_x.png").convert_alpha(), (18, 17))
    imageBank["sol"] = pygame.image.load("Images/Animations/platformerGraphics_otherStyle/Tiles/grassHalfMid.png")
    imageBank["sol"] = pygame.transform.scale(imageBank["sol"], (50, 50))
    imageBank["solleft"] = pygame.image.load("Images/Animations/platformerGraphics_otherStyle/Tiles/grassHalfLeft.png")
    imageBank["solleft"] = pygame.transform.scale(imageBank["solleft"], (50, 50))
    imageBank["solright"] = pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/Tiles/grassHalfRight.png")
    imageBank["solright"] = pygame.transform.scale(imageBank["solright"], (50, 50))
    imageBank["dirt"] = pygame.image.load("Images/Animations/platformerGraphics_otherStyle/Tiles/grassCenter.png")
    imageBank["dirt"] = pygame.transform.scale(imageBank["dirt"], (50, 50))

    imageBank["sol"] = pygame.image.load("Images/Animations/platformerGraphics_otherStyle/Tiles/grassHalfMid.png")
    imageBank["sol"] = pygame.transform.scale(imageBank["sol"], (50, 50))
    imageBank["solleft"] = pygame.image.load("Images/Animations/platformerGraphics_otherStyle/Tiles/grassHalfLeft.png")
    imageBank["solleft"] = pygame.transform.scale(imageBank["solleft"], (50, 50))
    imageBank["solright"] = pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/Tiles/grassHalfRight.png")
    imageBank["solright"] = pygame.transform.scale(imageBank["solright"], (50, 50))
    imageBank["dirt"] = pygame.image.load("Images/Animations/platformerGraphics_otherStyle/Tiles/grassCenter.png")
    imageBank["dirt"] = pygame.transform.scale(imageBank["dirt"], (50, 50))

    imageBank["fond"] = pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/bg_castle.png").convert_alpha()
    imageBank["mur"] = pygame.image.load("Images/mur.png").convert_alpha()
    imageBank["mur"] = pygame.transform.scale(imageBank["mur"], (64, 64))
    imageBank["coin_hud"] = pygame.transform.scale(
        pygame.image.load("Images/Animations/coinAnimation/coin_1.png").convert_alpha(), (25, 25))
    imageBank["spinning_coin"] = []
    for i in range(6):
        imageBank["spinning_coin"].append(
            pygame.image.load("Images/Animations/coinAnimation/coin_" + str(i + 1) + ".png").convert_alpha())
    imageBank["flame"] = []
    for i in range(4):
        imageBank["flame"].append(pygame.image.load("Images/Animations/flameBall_" + str(i) + ".png").convert_alpha())
    for i in range(10):
        imageBank["number_" + str(i)] = pygame.image.load(
            "Images/Animations/platformerGraphics_otherStyle/HUD/hud_" + str(i) + ".png").convert_alpha()
    # smaller numbers
    for i in range(10):
        image = pygame.image.load(
            "Images/Animations/platformerGraphics_otherStyle/HUD/hud_" + str(i) + ".png")
        imageBank["small_number_" + str(i)] = pygame.transform.scale(image.convert_alpha(),
                                                                     (image.get_width() * 1,
                                                                      image.get_height() * 1))
    playerWidth = 48
    playerHeight = 48
    imageBank["player_4"] = {}
    imageBank["player_4"]["droite"] = []
    for i in range(3):
        image = pygame.image.load("Images/Animations/mc-right-" + str(i) + ".png").convert_alpha()
        image = pygame.transform.scale(image, (playerWidth, playerHeight))
        imageBank["player_4"]["droite"].append(image)

    imageBank["player_4"]["gauche"] = []
    for i in range(3):
        image = pygame.image.load("Images/Animations/mc-left-" + str(i) + ".png").convert_alpha()
        image = pygame.transform.scale(image, (playerWidth, playerHeight))
        imageBank["player_4"]["gauche"].append(image)

    imageBank["player_4"]["haut"] = []
    for i in range(3):
        image = pygame.image.load("Images/Animations/mc-up-" + str(i) + ".png").convert_alpha()
        image = pygame.transform.scale(image, (playerWidth, playerHeight))
        imageBank["player_4"]["haut"].append(image)

    imageBank["player_4"]["bas"] = []
    for i in range(3):
        image = pygame.image.load("Images/Animations/mc-down-" + str(i) + ".png").convert_alpha()
        image = pygame.transform.scale(image, (playerWidth, playerHeight))
        imageBank["player_4"]["bas"].append(image)

    # create 3 players you can choose from
    playerWidth = 37
    for i in range(3):
        imageBank["player_" + str(i + 1)] = {}
        # right
        imageBank["player_" + str(i + 1)]["droite"] = []
        for j in range(11):
            if int(j) < 9:
                imageBank["player_" + str(i + 1)]["droite"].append(pygame.transform.scale(pygame.image.load(
                    "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(i + 1) + "_walk/PNG/p" + str(
                        i + 1) + "_walk0" + str(j + 1) + ".png").convert_alpha(), (playerWidth, playerHeight)))
            else:
                imageBank["player_" + str(i + 1)]["droite"].append(pygame.transform.scale(pygame.image.load(
                    "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(i + 1) + "_walk/PNG/p" + str(
                        i + 1) + "_walk" + str(j + 1) + ".png").convert_alpha(), (playerWidth, playerHeight)))
        # left
        imageBank["player_" + str(i + 1)]["gauche"] = []
        for j in range(11):
            if int(j) < 9:
                imageBank["player_" + str(i + 1)]["gauche"].append(pygame.transform.scale(pygame.transform.flip(
                    pygame.image.load(
                        "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(
                            i + 1) + "_walk/PNG/p" + str(
                            i + 1) + "_walk0" + str(j + 1) + ".png").convert_alpha(), True, False),
                    (playerWidth, playerHeight)))
            else:
                imageBank["player_" + str(i + 1)]["gauche"].append(pygame.transform.scale(pygame.transform.flip(
                    pygame.image.load(
                        "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(
                            i + 1) + "_walk/PNG/p" + str(
                            i + 1) + "_walk" + str(j + 1) + ".png"), True, False).convert_alpha(),
                                                                                          (playerWidth, playerHeight)))
        # up
        imageBank["player_" + str(i + 1)]["haut"] = []
        imageBank["player_" + str(i + 1)]["haut"].append(pygame.transform.scale(pygame.image.load(
            "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(i + 1) + "_jump.png").convert_alpha(),
                                                                                (playerWidth, playerHeight)))
        # down
        imageBank["player_" + str(i + 1)]["bas"] = []
        imageBank["player_" + str(i + 1)]["bas"].append(pygame.transform.scale(pygame.image.load(
            "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(i + 1) + "_duck.png").convert_alpha(),
                                                                               (playerWidth, playerHeight)))

    return imageBank


def lire_sounds():
    soundBank = {}
    soundBank["menu_music"] = pygame.mixer.Sound("Sounds/Menumusic.wav")
    soundBank["menu_music"].set_volume(0.25)
    soundBank["button_click"] = pygame.mixer.Sound("Sounds/buttonClick.flac")
    soundBank["button_click"].set_volume(0.3)
    soundBank["coin"] = pygame.mixer.Sound("Sounds/coin.wav")
    soundBank["coin"].set_volume(0.1)
    soundBank["gem"] = pygame.mixer.Sound("Sounds/gem.wav")
    soundBank["gem"].set_volume(0.1)
    return soundBank


class ElementGraphique():
    def __init__(self, img, fen, x=0, y=0):
        self.image = img
        self.rect = self.image.get_rect()
        self.fenetre = fen

        # creation d'un rectangle pour positioner l'image du personnage
        self.rect.x = x
        self.rect.y = y

    def afficher(self):
        self.fenetre.blit(self.image, self.rect)

    def contact(self, autre):
        if self.rect.colliderect(autre.rect):
            return True
        return False


class Button(ElementGraphique):
    def __init__(self, img, fen, x, y):
        super().__init__(img, fen, x, y)
        self.clicked = False

    def afficher(self):
        # mouseposition
        pos = pygame.mouse.get_pos()
        # Clicked on our button?
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                soundBank["button_click"].play()  # everytime a button is clicked this is the sound you will hear
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        super().afficher()


class ElementAnime(ElementGraphique):
    # images est un tableau des images de l'animation
    def __init__(self, images, fen, x=0, y=0, delai=1):
        super().__init__(images[0], fen, x, y)
        self.images = images
        self.delai = delai
        self.num_image = 0
        self.timer = 0

    def afficher(self):
        self.timer += 1

        if self.timer > self.delai:
            self.num_image += 1
            if self.num_image >= len(self.images):
                self.num_image = 0
            self.timer = 0

            self.image = self.images[self.num_image]

        super().afficher()


class ElementAnimeDir(ElementAnime):
    # dico_images est le dictionnaire contenant toutes les animations par direction
    def __init__(self, dico_images, fen, x=0, y=0):
        self.dico_images = dico_images
        self.direction = "droite"
        self.old_dir = "droite"

        super().__init__(self.dico_images[self.direction], fen, x, y)

    def afficher(self):
        if self.direction != self.old_dir:
            self.images = self.dico_images[self.direction]
            self.num_image = 0
            self.old_dir = self.direction

        super().afficher()


class Joueur(ElementAnimeDir):
    def __init__(self, img, fen, x=0, y=0):
        super().__init__(img, fen, x, y)

        self.vitesse = 5

    def deplacer(self,world):
        # on recupere l'etat du clavier
        touches = pygame.key.get_pressed();

        new_rect = copy.deepcopy(self.rect)

        if touches[pygame.K_RIGHT]:
            self.direction = "droite"
            new_rect.x += self.vitesse

        if touches[pygame.K_LEFT]:
            self.direction = "gauche"
            new_rect.x += -self.vitesse

        if touches[pygame.K_UP]:
            self.direction = "haut"
            new_rect.y += -self.vitesse

        if touches[pygame.K_DOWN]:
            self.direction = "bas"
            new_rect.y += self.vitesse

        if world.collide_map(new_rect):
            print("Deplacement refusé")
        else :
            print("Deplacement accepté")
            self.rect = new_rect


class Badguys(ElementAnime):
    def __init__(self, img, fen, maMap):

        x = []
        y = []
        z = 0

        nb_l = len(maMap)
        nb_c = len(maMap[0])
        for i in range(nb_l):
            for j in range (nb_c):


                if maMap[i][j]==6:
                    x.append(i*50)
                    y.append(j*50)


        super().__init__(img,fen,x[z],y[z])

        self.dx = random.randint(-5,5)



class world():
    def __init__(self, fen):
        self.fen = fen
        self.maMap =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],  # 1
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0],  # 9
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
                 [0, 0, 0, 2, 3, 3, 4, 0, 6, 0, 5, 5, 5, 5, 0, 6, 0, 0, 6, 0, 0, 2, 3, 3, 3, 4, 0, 0, 0, 0],  # 11
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0],  # 12
                 [2, 3, 4, 0, 0, 0, 0, 2, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 3, 3, 3, 4],  # 13
                 [5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # 14
                 ]

    def afficher(self):
        # Afficher tous les murs
        nb_l = len(self.maMap)
        nb_c = len(self.maMap[0])
        for i in range(nb_l):
            for j in range(nb_c):
                if self.maMap[i][j] == 1:
                    mur = ElementGraphique(imageBank["mur"], fenetre, x=50 * j, y=50 * i)
                    mur.afficher()
            for j in range(nb_c):
                if self.maMap[i][j] == 2:
                    mur = ElementGraphique(imageBank["solleft"], fenetre, x=50 * j, y=50 * i)
                    mur.afficher()
            for j in range(nb_c):
                if self.maMap[i][j] == 3:
                    mur = ElementGraphique(imageBank["sol"], fenetre, x=50 * j, y=50 * i)
                    mur.afficher()
            for j in range(nb_c):
                if self.maMap[i][j] == 4:
                    mur = ElementGraphique(imageBank["solright"], fenetre, x=50 * j, y=50 * i)
                    mur.afficher()
            for j in range(nb_c):
                if self.maMap[i][j] == 5:
                    mur = ElementGraphique(imageBank["dirt"], fenetre, x=50 * j, y=50 * i)
                    mur.afficher()
            mechant = []
            for j in range(nb_c):
                if self.maMap[i][j] == 6:
                    bad = Badguys(imageBank["flame"], fenetre, x=50 * j, y=50 * i)
                    mechant.append(bad)




    def collide_map(self, un_rect):
        # haut
        irect = un_rect.y // 50
        jrect = int(un_rect.x / 50)

        if (self.maMap[irect][jrect] != 0):
            return True

        # bas
        irect = (un_rect.y + un_rect.h) // 50
        jrect = int(un_rect.x / 64)

        if (self.maMap[irect][jrect] != 0):
            return True

        return False
    super(world,._
    _init__()
    self.arg = arg

class Badguys(ElementAnime):
    def __init__(self, img, fen, x, y):


        super().__init__(img,fen,x,y)

        self.dx = random.randint(-5,5)

     def deplacer(self):


        if world.collide_map():
            print("Deplacement refusé")
            self.dx = -self.dx
            self.rect.x += self.dx
        else :
            print("Deplacement accepté")
            self.rect.x += self.dx












def display_hud(fenetre, lives, gem_count, coin_count, time):
    a = 10
    for d in str(time):
        ElementGraphique(imageBank["number_" + d], fenetre, a, 10).afficher()
        a = a + imageBank["number_" + d].get_width() + 2
    a = 300
    # display lives i have
    for i in range(lives):
        ElementGraphique(imageBank["heart_full"], fenetre, a, 10).afficher()
        a = a + imageBank["heart_full"].get_width() + 2
    # display empty hearts ive lost
    for i in range(3 - lives):
        ElementGraphique(imageBank["heart_empty"], fenetre, a, 10).afficher()
        a = a + imageBank["heart_full"].get_width() + 2
    # display inventory
    # gems
    ElementGraphique(imageBank["hud_gem_blue"], fenetre, 10, 53).afficher()
    ElementGraphique(imageBank["x_sign"], fenetre, 12 + imageBank["hud_gem_blue"].get_width(), 57).afficher()
    # startpos of the numbers
    a = 14 + imageBank["hud_gem_blue"].get_width() + imageBank["x_sign"].get_width()
    for d in str(gem_count):
        ElementGraphique(imageBank["small_number_" + d], fenetre, a, 53).afficher()
        a = a + imageBank["small_number_" + d].get_width() + 1
    # coins
    ElementGraphique(imageBank["coin_hud"], fenetre, 11, 55 + imageBank["hud_gem_blue"].get_height()).afficher()
    ElementGraphique(imageBank["x_sign"], fenetre, 12 + imageBank["hud_gem_blue"].get_width(),
                     57 + imageBank["hud_gem_blue"].get_height()).afficher()
    # startpos of the numbers
    a = 20 + imageBank["coin_hud"].get_width() + imageBank["x_sign"].get_width()
    for d in str(coin_count):
        ElementGraphique(imageBank["small_number_" + d], fenetre, a,
                         55 + imageBank["hud_gem_blue"].get_height()).afficher()
        a = a + imageBank["small_number_" + d].get_width() + 1


pygame.init()  # Initialisation de la bibliotheque pygame
pygame.mixer.init()  # initialize for sound
# creation de la fenetre
largeur = 700
hauteur = 700
fenetre = pygame.display.set_mode((largeur, hauteur), pygame.NOFRAME)

imageBank = lire_images()
soundBank = lire_sounds()



# lecture de l'image du perso

perso = Joueur(imageBank["player_2"], fenetre, 80, 70)


class collectable(ElementAnime):
    def __init__(self, images, collect_sound, fen, x=0, y=0, delai=3):
        super().__init__(images, fen, x, y, delai)
        self.collected = False
        self.collect_sound = collect_sound

    def afficher(self):
        playerpos = perso.rect  # playerpos
        # collisioncheck with player
        if self.rect.colliderect(playerpos) and not self.collected:
            self.collected = True
            self.collect_sound.play()  # everytime a coin is collected
        super().afficher()




# lecture de l'image du fond
fondarr = []
for j in range(3):
    for i in range(3):
        fondarr.append(ElementGraphique(imageBank["fond"], fenetre, j * 256, 256 * i))
# Create the buttons for the game
playerButtons = []
for i in range(4):
    playerButtons.append(Button(imageBank["player_"+str(i+1)]["droite"][0], fenetre, 100 * (i + 1), 256 / 2))
ingameExitButton = Button(imageBank["exit_button"], fenetre, (256 * 3) - 53, 3)
menuStartButton = Button(imageBank["start_button"], fenetre, 256 / 2, 256)
menuQuitButton = Button(imageBank["quit_button"], fenetre, 256 * 2, 256)
endScreenStartButton = Button(imageBank["start_button"], fenetre, 256 / 2, 256)
endScreenQuitButton = Button(imageBank["quit_button"], fenetre, 256 * 2, 256)
# Choix de la police pour le texte
font = pygame.font.Font(None, 34)
# Text to display
texte = ElementGraphique(font.render('The platformer of Maximilian Amougou and Tony Mardivirin', True, (3, 45, 49)),
                         fenetre, x=50, y=200)
textePlayerMenu = ElementGraphique(font.render('Choose Player by clicking on him:', True, (3, 45, 49)), fenetre, x=100,
                                   y=100)
pauseText = ElementGraphique(
    font.render("Quit game? Press 'Y'es to end it all or 'N'o to resume the fun", True, (3, 45, 49)), fenetre, x=75,
    y=100)
endScreenMessage = ElementGraphique(font.render("Try again?", True, (3, 45, 49)), fenetre, x=256, y=256)

# draw this over screen to make it blurry
blurryScreenImg = pygame.Surface((fenetre.get_size()))
blurryScreenImg.fill((77, 77, 77))
blurryScreenImg.set_alpha(111)
blurrScreen = ElementGraphique(blurryScreenImg, fenetre)
