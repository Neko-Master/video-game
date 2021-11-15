import os.path

import pygame
import random
import copy
import spritesheet


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
        "Images/Animations/platformerGraphics_otherStyle/HUD/hud_x.png").convert_alpha(), (18, 16.8))
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
    imageBank["blue_gem_animated"] = []
    img1 = pygame.image.load("Images/Animations/gemAnimation/blue_gem_anim.png").convert_alpha()
    for i in range(8):
        cropped = pygame.Surface((32, 32), pygame.SRCALPHA)
        cropped.blit(img1, (0, 0), (i * 32, 0, 32, 32))
        imageBank["blue_gem_animated"].append(cropped)
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
                                                                     (image.get_width() * 0.65,
                                                                      image.get_height() * 0.65))
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
    playerWidth = 36.664
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
        tilesDictionary = spritesheet.SpriteSheet(
            "Images/Animations/platformerGraphics_otherStyle/Tiles/tiles_spritesheet.png",
            "Images/Animations/platformerGraphics_otherStyle/Tiles/tiles_spritesheet.xml")
        imageBank["all_tiles"] = tilesDictionary
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
    soundBank["lava_splash"] = pygame.mixer.Sound("Sounds/lava.flac")
    soundBank["lava_splash"].set_volume(0.1)
    return soundBank


def afficher_map(maMap, imageBank):
    # Afficher tous les murs
    nb_l = len(maMap)
    nb_c = len(maMap[0])
    for i in range(nb_l):
        for j in range(nb_c):
            if maMap[i][j] == 1:
                mur = ElementGraphique(imageBank["mur"], fenetre, x=50 * j, y=50 * i)
                mur.afficher()
        for j in range(nb_c):
            if maMap[i][j] == 2:
                mur = ElementGraphique(imageBank["solleft"], fenetre, x=50 * j, y=50 * i)
                mur.afficher()
        for j in range(nb_c):
            if maMap[i][j] == 3:
                mur = ElementGraphique(imageBank["sol"], fenetre, x=50 * j, y=50 * i)
                mur.afficher()
        for j in range(nb_c):
            if maMap[i][j] == 4:
                mur = ElementGraphique(imageBank["solright"], fenetre, x=50 * j, y=50 * i)
                mur.afficher()
        for j in range(nb_c):
            if maMap[i][j] == 5:
                mur = ElementGraphique(imageBank["dirt"], fenetre, x=50 * j, y=50 * i)
                mur.afficher()


def collide_map(maMap, un_rect):
    # haut
    irect = un_rect.y // 50
    jrect = int(un_rect.x / 50)

    if (maMap[irect][jrect] != 0):
        return True

    # bas
    irect = (un_rect.y + un_rect.h) // 50
    jrect = int(un_rect.x / 64)

    if (maMap[irect][jrect] != 0):
        return True

    return False


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
        return self


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
        self.lives = 3
        self.vitesse = 5
        self.jumpspeed = 0
        self.jump = False

    def deplacer(self, tilelist=[]):
        # on recupere l'etat du clavier
        touches = pygame.key.get_pressed()
        new_rect = copy.deepcopy(self.rect)
        if touches[pygame.K_RIGHT]:
            self.direction = "droite"
            new_rect.x += self.vitesse
        if touches[pygame.K_LEFT]:
            self.direction = "gauche"
            new_rect.x += -self.vitesse
        if (touches[pygame.K_SPACE] or touches[
            pygame.K_UP]) and self.jump == False and self.jumpspeed == 10:  # the last condition prevents doublejumps
            self.direction = "haut"
            self.jumpspeed = -10
            self.jump = True
        if (touches[pygame.K_SPACE] or touches[pygame.K_UP]) == False:
            self.jump = False

        # gravity
        self.jumpspeed += 1  # this controls how fast the plyer falls down
        if self.jumpspeed > 10:
            self.jumpspeed = 10
        new_rect.y += self.jumpspeed
        if not (new_rect.x == self.rect.x and new_rect.y == self.rect.y):
            # collision with tiles
            for tile in tilelist:
                    # x-axis
                if tile.rect.colliderect(new_rect.x, self.rect.y, self.rect.width, self.rect.height):
                    new_rect.x = self.rect.x
                    if type(tile).__name__ == "lava":
                        soundBank["lava_splash"].play()
                        self.lives = 0
                # y-axis
                elif tile.rect.colliderect(self.rect.x, new_rect.y, self.rect.width, self.rect.height):
                    if type(tile).__name__ == "lava":
                        soundBank["lava_splash"].play()
                        self.lives = 0
                    # jumping
                    elif self.jumpspeed < 0:
                        new_rect.y = tile.rect.bottom
                    # falling
                    elif self.jumpspeed >= 0:
                        new_rect.y = tile.rect.top - self.rect.height
        self.rect = new_rect
        # keep player onscreen
        # bottom
        if self.rect.bottom > fenetre.get_height():
            self.rect.bottom = fenetre.get_height()
        # right
        if self.rect.right > fenetre.get_width():
            self.rect.right = fenetre.get_width()
        # left
        if self.rect.left < 0:
            self.rect.left = 0


class Balle(ElementAnime):
    def __init__(self, img, fen):

        w, h = fen.get_size()

        x = random.randint(0, w)
        y = random.randint(0, h)

        super().__init__(img, fen, x, y)

        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)

    def deplacer(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        w, h = self.fenetre.get_size()

        # a gauche ou droite
        if self.rect.x < 0 or self.rect.x + self.rect.w > w:
            self.dx = -self.dx

        # en haut ou bas
        if self.rect.y < 0 or self.rect.y + self.rect.h > h:
            self.dy = -self.dy


def display_hud(fenetre, gem_count, coin_count, time):
    a = 10
    for d in str(time):
        ElementGraphique(imageBank["number_" + d], fenetre, a, 5).afficher()
        a = a + imageBank["number_" + d].get_width() + 2
    a = fenetre.get_rect().centerx - (1.5 * imageBank["heart_full"].get_width())
    # display lives i have
    for i in range(perso.lives):
        ElementGraphique(imageBank["heart_full"], fenetre, a, 5).afficher()
        a = a + imageBank["heart_full"].get_width() + 2
    # display empty hearts ive lost
    for i in range(3 - perso.lives):
        ElementGraphique(imageBank["heart_empty"], fenetre, a, 5).afficher()
        a = a + imageBank["heart_full"].get_width() + 2
    # display inventory
    # gems
    ElementGraphique(imageBank["blue_gem_animated"][0], fenetre, 10, 53).afficher()
    ElementGraphique(imageBank["x_sign"], fenetre, 12 + imageBank["blue_gem_animated"][0].get_width(), 57).afficher()
    # startpos of the numbers
    a = 14 + imageBank["blue_gem_animated"][0].get_width() + imageBank["x_sign"].get_width()
    for d in str(gem_count):
        ElementGraphique(imageBank["small_number_" + d], fenetre, a, 53).afficher()
        a = a + imageBank["small_number_" + d].get_width() + 1
    # coins
    ElementGraphique(imageBank["coin_hud"], fenetre, 11, 55 + imageBank["blue_gem_animated"][0].get_height()).afficher()
    ElementGraphique(imageBank["x_sign"], fenetre, 12 + imageBank["blue_gem_animated"][0].get_width(),
                     57 + imageBank["blue_gem_animated"][0].get_height()).afficher()
    # startpos of the numbers
    a = 20 + imageBank["coin_hud"].get_width() + imageBank["x_sign"].get_width()
    for d in str(coin_count):
        ElementGraphique(imageBank["small_number_" + d], fenetre, a,
                         55 + imageBank["blue_gem_animated"][0].get_height()).afficher()
        a = a + imageBank["small_number_" + d].get_width() + 1


def maxiLvl():
    tileMap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0],  # 2
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0],  # 3
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 3, 0],  # 4
               [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
               [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
               [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
               [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
               [0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
               [0, 0, 0, 0, 3, 3, 4, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 4, 0, 0, 0],  # 11
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0],  # 12
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
               [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]  # 14

    def createMap():
        tileList = []
        nb_l = len(tileMap)
        nb_c = len(tileMap[0])
        sprite = imageBank["all_tiles"]
        for i in range(nb_l):
            for j in range(nb_c):
                if tileMap[i][j] == 1:
                    tileList.append(ElementGraphique(sprite.get_image_name("castleMid.png"), fenetre, x=50 * j,
                                                     y=50 * i))
                if tileMap[i][j] == 2:
                    tileList.append(lava(fenetre, x=50 * j, y=50 * i))
                if tileMap[i][j] == 3:
                    tileList.append(ElementGraphique(sprite.get_image_name("castleHalfMid.png"), fenetre, x=50 * j,
                                                     y=50 * i))
                if tileMap[i][j] == 4:
                    tileList.append(ElementGraphique(sprite.get_image_name("castleHalfLeft.png"), fenetre, x=50 * j,
                                                     y=50 * i))
                if tileMap[i][j] == 5:
                    tileList.append(ElementGraphique(sprite.get_image_name("castleCenter.png"), fenetre, x=50 * j,
                                                     y=50 * i))
                if tileMap[i][j] == 8:
                    tileList.append(ElementGraphique(sprite.get_image_name("door_closedTop.png"), fenetre, x=50 * j,
                                                     y=50 * i))
                if tileMap[i][j] == 9:
                    tileList.append(ElementGraphique(sprite.get_image_name("door_closedMid.png"), fenetre, x=50 * j,
                                                     y=50 * i))
        return tileList

    tiles = createMap()
    continuer = True
    horologeMaxi = pygame.time.Clock()
    while continuer:
        horologeMaxi.tick(30)
        secondsPassed = int(
            timerBuffer + (pygame.time.get_ticks() - start_ticks) / 1000)  # calculate how many seconds played
        if secondsPassed >= timeConst or ingameExitButton.clicked == 1 or perso.lives <= 0:  # you have 300s to reach the end of the lvl
            continuer = 0
        playtimePerLvl = timeConst - secondsPassed
        for fonds in fondarr:
            fonds.afficher()
        for tile in tiles:
            tile.afficher()
        perso.afficher()
        perso.deplacer(tiles)
        ingameExitButton.afficher()
        display_hud(fenetre, player_gems, coins_collected, playtimePerLvl)
        pygame.display.flip()
        pygame.event.pump()


pygame.init()  # Initialisation de la bibliotheque pygame
pygame.mixer.init()  # initialize for sound
# creation de la fenetre
largeur = 1450
hauteur = 700
fenetre = pygame.display.set_mode((largeur, hauteur), pygame.NOFRAME)

imageBank = lire_images()
soundBank = lire_sounds()

# lecture de l'image du perso

perso = Joueur(imageBank["player_2"], fenetre, 55, 600)


# class is declared at this point bc Joueur object is needed
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


class lava(ElementGraphique):
    def __init__(self, fen, x=0, y=0):
        cropped = pygame.Surface((70, 55),pygame.SRCALPHA)
        cropped.blit(imageBank["all_tiles"].get_image_name("liquidLavaTop_mid.png"), (0, 0), (0, 15, 70, 55))
        super().__init__(cropped, fen, x, y+15)

    def afficher(self):
        super().afficher()
        return self


mes_balles = []
for i in range(3):
    balle = Balle(imageBank["flame"], fenetre)
    mes_balles.append(balle)

# lecture de l'image du fond
fondarr = []
for j in range(6):
    for i in range(3):
        fondarr.append(ElementGraphique(imageBank["fond"], fenetre, j * 256, 256 * i))
# Create the buttons for the game
playerButtons = []
for i in range(4):
    playerButtons.append(
        Button(imageBank["player_" + str(i + 1)]["droite"][0], fenetre, fenetre.get_rect().centerx - 175 + (100 * (i)),
               fenetre.get_rect().centery - 100))
ingameExitButton = Button(imageBank["exit_button"], fenetre,
                          fenetre.get_width() - imageBank["exit_button"].get_width() - 3, 5)
menuStartButton = Button(imageBank["start_button"], fenetre, fenetre.get_rect().centerx - 150,
                         fenetre.get_rect().centery - 100)
menuQuitButton = Button(imageBank["quit_button"], fenetre, fenetre.get_rect().centerx + 50,
                        fenetre.get_rect().centery - 100)
endScreenStartButton = Button(imageBank["start_button"], fenetre, fenetre.get_rect().centerx - 150,
                              fenetre.get_rect().centery - 100)
endScreenQuitButton = Button(imageBank["quit_button"], fenetre, fenetre.get_rect().centerx + 50,
                             fenetre.get_rect().centery - 100)
# Choix de la police pour le texte
font = pygame.font.Font(None, 34)
# Text to display
texte = ElementGraphique(font.render('The platformer of Maximilian Amougou and Tony Mardivirin', True, (3, 45, 49)),
                         fenetre, x=fenetre.get_rect().centerx - 300, y=fenetre.get_rect().centery - 200)
textePlayerMenu = ElementGraphique(font.render('Choose Player by clicking on him:', True, (3, 45, 49)), fenetre,
                                   x=fenetre.get_rect().centerx - 200, y=fenetre.get_rect().centery - 200)
pauseText = ElementGraphique(
    font.render("Quit game? Press 'Y'es to end it all or 'N'o to resume the fun", True, (3, 45, 49)), fenetre,
    x=fenetre.get_rect().centerx - 300,
    y=fenetre.get_rect().centery)
endScreenMessage = ElementGraphique(font.render("Try again?", True, (3, 45, 49)), fenetre, x=256, y=256)

# draw this over screen to make it blurry
blurryScreenImg = pygame.Surface((fenetre.get_size()))
blurryScreenImg.fill((77, 77, 77))
blurryScreenImg.set_alpha(111)
blurrScreen = ElementGraphique(blurryScreenImg, fenetre)
# 1 2 3 4 5 6 7 8 9 1*1 2 3 4 5 6 7 8 9 2*1 2 3 4 5 6 7 8 9 3*
maMap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
         [0, 0, 0, 2, 3, 3, 4, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 4, 0, 0, 0, 0],  # 11
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0],  # 12
         [2, 3, 4, 0, 0, 0, 0, 2, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 3, 3, 3, 4],  # 13
         [5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], ]  # 14

# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()
# hella variables for the game xD
i = 1
continuer = 1
# the menus
main_menu = True
player_selection_menu = False
game_paused = False
end_screen = False
display_blurryScreen = False
defaultPlayer = 1
# Ingame variables
player_lives = 3
player_gems = 0
coins_collected = 0
coinArr = []
gemArr = []
for i in range(10):
    posX = random.randint(20, 750)
    posY = random.randint(20, 750)
    coinArr.append(collectable(imageBank["spinning_coin"], soundBank["coin"], fenetre, posX, posY))
for i in range(10):
    posX = random.randint(20, 750)
    posY = random.randint(20, 750)
    gemArr.append(collectable(imageBank["blue_gem_animated"], soundBank["gem"], fenetre, posX, posY))
# timer stuff
playtimePerLvl = 300  # time in seconds
timeConst = playtimePerLvl
secondsPassed = 0
timerBuffer = 0
# music stuff
soundBank["menu_music"].play(10)
lvlMusicPlaying = False
pygame.mixer.music.load("Sounds/Backgroundmusic.ogg")  # has to be done like this so you can pause/unpause
pygame.mixer.music.set_volume(0.25)
# lvlChoice
lvlMaxi = False
# start point of timer
start_ticks = pygame.time.get_ticks()
while continuer:
    # fixons le nombre max de frames / secondes
    horloge.tick(30)
    i = i + 1
    if main_menu:
        for fonds in fondarr:
            fonds.afficher()
        if menuQuitButton.clicked:
            continuer = 0
        if menuStartButton.clicked:
            main_menu = False
            player_selection_menu = True
            fenetre.fill((0, 0, 0))
            pygame.display.flip()
        # Affichage du Texte
        texte.afficher()
        menuStartButton.afficher()
        menuQuitButton.afficher()
        pygame.display.flip()

    elif player_selection_menu:
        for fonds in fondarr:
            fonds.afficher()
        textePlayerMenu.afficher()
        ingameExitButton.afficher()
        if ingameExitButton.clicked:
            continuer = 0
        # generate the clickable players
        for i in range(4):
            playerButtons[i].afficher()
            if playerButtons[i].clicked:
                defaultPlayer = i + 1
                perso = Joueur(imageBank["player_" + str(defaultPlayer)], fenetre, 70, 500)  # 55,600 for maxi Lvl
                player_selection_menu = False
                lvlMaxi = True
                fenetre.fill((0, 0, 0))
                start_ticks = pygame.time.get_ticks()
                pygame.display.flip()
        pygame.display.flip()

    elif game_paused:
        # stop the timer while game is paused
        timerBuffer = secondsPassed
        if not display_blurryScreen:
            blurrScreen.afficher()
            display_blurryScreen = True
        pygame.mixer.music.pause()
        pauseText.afficher()
        pygame.display.flip()
        # another cool way to use buttons
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    continuer = 0
                    break
                if event.key == pygame.K_n:
                    pygame.mixer.music.unpause()
                    game_paused = False
                    display_blurryScreen = False
                    start_ticks = pygame.time.get_ticks()

    elif end_screen:
        pygame.mixer.music.stop()
        touches = pygame.key.get_pressed()
        if touches[pygame.K_ESCAPE]:
            continuer = 0
        for fonds in fondarr:
            fonds.afficher()
        if endScreenQuitButton.clicked:
            continuer = 0
        # reset time and stats here to restart the game
        if endScreenStartButton.clicked:
            end_screen = False
            playtimePerLvl = timeConst
            start_ticks = pygame.time.get_ticks()
            secondsPassed = 0
            timerBuffer = 0
            lvlMusicPlaying = False
        endScreenMessage.rect.centerx=fenetre.get_rect().centerx
        endScreenMessage.afficher()
        endScreenStartButton.afficher()
        endScreenQuitButton.afficher()
        pygame.display.flip()
    # TODO create methods for the levels and call them instaed of everything in this loop
    elif lvlMaxi:
        maxiLvl()
        lvlMaxi = False
    else:
        soundBank["menu_music"].stop()
        if not lvlMusicPlaying:
            lvlMusicPlaying = True
            pygame.mixer.music.play(10)
        touches = pygame.key.get_pressed()
        if touches[pygame.K_ESCAPE]:
            game_paused = True
        for fonds in fondarr:
            fonds.afficher()
        if ingameExitButton.clicked == 1:
            game_paused = True
        secondsPassed = int(
            timerBuffer + (pygame.time.get_ticks() - start_ticks) / 1000)  # calculate how many seconds played
        if secondsPassed >= timeConst:  # you have 300s to reach the end of the lvl
            end_screen = True
            endScreenMessage = ElementGraphique(font.render("Time is up! Retry?", True, (3, 45, 49)), fenetre, x=300,
                                                y=200)
        playtimePerLvl = timeConst - secondsPassed
        if perso.lives <= 0:
            end_screen = True
            endScreenMessage = ElementGraphique(font.render("You just died! Retry?", True, (3, 45, 49)), fenetre, x=300,
                                                y=200)
        perso.deplacer()

        '''
        if collide_map(maMap,perso.rect):
            print("Touché")
        else :
            print("libre")
        '''

        for e in mes_balles:
            e.deplacer()

        # collisions avec les balles
        '''
        for b in mes_balles:
            if perso.contact(b) :
                continuer = 0
        '''
        '''
        for b in mes_balles:
            for bb in mes_balles:
                if b != bb and b.contact(bb) :
                    b.dx = -b.dx
                    b.dy = -b.dy
        '''

        # Affichage du fond
        for fonds in fondarr:
            fonds.afficher()

        afficher_map(maMap, imageBank)

        # Affichage Perso
        perso.afficher()

        for e in mes_balles:
            e.afficher()
        for coin in coinArr:
            if not coin.collected:
                coin.afficher()
            else:
                coins_collected = coins_collected + 1
                coinArr.remove(coin)
        for gem in gemArr:
            if not gem.collected:
                gem.afficher()
            else:
                player_gems = player_gems + 1
                gemArr.remove(gem)
        ingameExitButton.afficher()
        display_hud(fenetre, player_gems, coins_collected, playtimePerLvl)
        # rafraichissement
        pygame.display.flip()

    # if we don't need to handle the events we use pump instead of the for-loop
    pygame.event.pump()
    # for event in pygame.event.get():  # parcours de la liste des evenements recus
    # do stuff with events
# fin du programme principal...
pygame.quit()
