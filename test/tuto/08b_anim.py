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
    imageBank["fond"] = pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/bg_castle.png").convert_alpha()
    imageBank["mur"] = pygame.image.load("Images/mur.png").convert_alpha()
    imageBank["mur"] = pygame.transform.scale(imageBank["mur"], (64, 64))
    imageBank["flame"] = []
    for i in range(4):
        imageBank["flame"].append(pygame.image.load("Images/Animations/flameBall_" + str(i) + ".png").convert_alpha())
    for i in range(10):
        imageBank["number_" + str(i)] = pygame.image.load(
            "Images/Animations/platformerGraphics_otherStyle/HUD/hud_" + str(i) + ".png").convert_alpha()
    playerSize = 48
    playerHeight = 64.59
    imageBank["player_4"] = {}
    imageBank["player_4"]["droite"] = []
    for i in range(3):
        image = pygame.image.load("Images/Animations/mc-right-" + str(i) + ".png").convert_alpha()
        image = pygame.transform.scale(image, (playerSize, playerSize))
        imageBank["player_4"]["droite"].append(image)

    imageBank["player_4"]["gauche"] = []
    for i in range(3):
        image = pygame.image.load("Images/Animations/mc-left-" + str(i) + ".png").convert_alpha()
        image = pygame.transform.scale(image, (playerSize, playerSize))
        imageBank["player_4"]["gauche"].append(image)

    imageBank["player_4"]["haut"] = []
    for i in range(3):
        image = pygame.image.load("Images/Animations/mc-up-" + str(i) + ".png").convert_alpha()
        image = pygame.transform.scale(image, (playerSize, playerSize))
        imageBank["player_4"]["haut"].append(image)

    imageBank["player_4"]["bas"] = []
    for i in range(3):
        image = pygame.image.load("Images/Animations/mc-down-" + str(i) + ".png").convert_alpha()
        image = pygame.transform.scale(image, (playerSize, playerSize))
        imageBank["player_4"]["bas"].append(image)

        # create 3 players you can choose from
        for i in range(3):
            imageBank["player_" + str(i + 1)] = {}
            # right
            imageBank["player_" + str(i + 1)]["droite"] = []
            for j in range(11):
                if int(j) < 9:
                    imageBank["player_" + str(i + 1)]["droite"].append(pygame.transform.scale(pygame.image.load(
                        "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(i + 1) + "_walk/PNG/p" + str(
                            i + 1) + "_walk0" + str(j + 1) + ".png").convert_alpha(), (playerSize, playerHeight)))
                else:
                    imageBank["player_" + str(i + 1)]["droite"].append(pygame.transform.scale(pygame.image.load(
                        "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(i + 1) + "_walk/PNG/p" + str(
                            i + 1) + "_walk" + str(j + 1) + ".png").convert_alpha(), (playerSize, playerHeight)))
            # left
            imageBank["player_" + str(i + 1)]["gauche"] = []
            for j in range(11):
                if int(j) < 9:
                    imageBank["player_" + str(i + 1)]["gauche"].append(pygame.transform.scale(pygame.transform.flip(
                        pygame.image.load(
                            "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(
                                i + 1) + "_walk/PNG/p" + str(
                                i + 1) + "_walk0" + str(j + 1) + ".png").convert_alpha(), True, False),
                        (playerSize, playerHeight)))
                else:
                    imageBank["player_" + str(i + 1)]["gauche"].append(pygame.transform.scale(pygame.transform.flip(
                        pygame.image.load(
                            "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(
                                i + 1) + "_walk/PNG/p" + str(
                                i + 1) + "_walk" + str(j + 1) + ".png"), True, False).convert_alpha(),
                                                                                              (playerSize,
                                                                                               playerHeight)))
            # up
            imageBank["player_" + str(i + 1)]["haut"] = []
            imageBank["player_" + str(i + 1)]["haut"].append(pygame.transform.scale(pygame.image.load(
                "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(i + 1) + "_jump.png").convert_alpha(),
                                                                                    (playerSize, playerHeight)))
            # down
            imageBank["player_" + str(i + 1)]["bas"] = []
            imageBank["player_" + str(i + 1)]["bas"].append(pygame.transform.scale(pygame.image.load(
                "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(i + 1) + "_duck.png").convert_alpha(),
                                                                                   (playerSize, playerHeight)))

    return imageBank


def lire_sounds():
    soundBank = {}
    soundBank["menu_music"] = pygame.mixer.Sound("Sounds/Menumusic.wav")
    soundBank["menu_music"].set_volume(0.25)

    return soundBank


def afficher_map(maMap, imageBank):
    # Afficher tous les murs
    nb_l = len(maMap)
    nb_c = len(maMap[0])
    for i in range(nb_l):
        for j in range(nb_c):
            if maMap[i][j] == 1:
                mur = ElementGraphique(imageBank["mur"], fenetre, x=64 * j, y=64 * i)
                mur.afficher()


def collide_map(maMap, un_rect):
    # haut
    irect = un_rect.y // 64
    jrect = int(un_rect.x / 64)

    if (maMap[irect][jrect] != 0):
        return True

    # bas
    irect = (un_rect.y + un_rect.h) // 64
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
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        super().afficher()


class ElementAnime(ElementGraphique):
    # images est un tableau des images de l'animation
    def __init__(self, images, fen, x=0, y=0):
        super().__init__(images[0], fen, x, y)
        self.images = images
        self.delai = 10
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

    def deplacer(self):
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

        if collide_map(maMap, new_rect):
            print("Deplacement refusé")
        else:
            print("Deplacement accepté")
            self.rect = new_rect


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


def createTimerElements(fenetre, time):
    a = 10
    for d in str(time):
        ElementGraphique(imageBank["number_" + d], fenetre, a, 10).afficher()
        a = a + 33


pygame.init() # Initialisation de la bibliotheque pygame
pygame.mixer.init() # initialize for sound
# creation de la fenetre
largeur = 256 * 3
hauteur = 256 * 3
fenetre = pygame.display.set_mode((largeur, hauteur), pygame.NOFRAME)

imageBank = lire_images()
soundBank = lire_sounds()

# lecture de l'image du perso

perso = Joueur(imageBank["player_2"], fenetre, 80, 70)

mes_balles = []
for i in range(3):
    balle = Balle(imageBank["flame"], fenetre)
    mes_balles.append(balle)

# lecture de l'image du fond
fondarr = []
for j in range(3):
    for i in range(3):
        fondarr.append(ElementGraphique(imageBank["fond"], fenetre, j * 256, 256 * i))
#Create the buttons for the game
playerButtons = []
for i in range(3):
    playerButtons.append(Button(pygame.image.load(
        "Images/Animations/platformerGraphics_otherStyle/Player/p" + str(i + 1) + "_walk/PNG/p" + str(
            i + 1) + "_walk01.png"),
        fenetre, 100 * (i + 1), 256 / 2))
playerButtons.append(Button(pygame.image.load("Images/Animations/mc-right-0.png"), fenetre, 400, 256 / 2))
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

#draw this over screen to make it blurry
blurryScreenImg = pygame.Surface((fenetre.get_size()))
blurryScreenImg.fill((77, 77, 77))
blurryScreenImg.set_alpha(111)
blurrScreen = ElementGraphique(blurryScreenImg, fenetre)

maMap = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
         [1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
         [1, 0, 1, 1, 0, 0, 1, 0, 1, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
         [1, 1, 1, 1, 1, 1, 0, 1, 0, 1], ]

# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()
#hella variables for the game xD
i = 1;
continuer = 1
# the menus
main_menu = True
player_selection_menu = False
game_paused = False
end_screen = False
display_blurryScreen = False
defaultPlayer = 1
#timer stuff
playtimePerLvl = 300  # time in seconds
timeConst = playtimePerLvl
secondsPassed = 0
timerBuffer = 0
#music stuff
soundBank["menu_music"].play(10)
lvlMusicPlaying=False
pygame.mixer.music.load("Sounds/Backgroundmusic.ogg") #has to be done like this so you can pause/unpause
pygame.mixer.music.set_volume(0.25)
#start point of timer
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
            print("button clicked")
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
        #generate the clickable players
        for i in range(4):
            playerButtons[i].afficher()
            if playerButtons[i].clicked:
                defaultPlayer = i + 1
                perso = Joueur(imageBank["player_" + str(defaultPlayer)], fenetre, 80, 70)
                player_selection_menu = False
                fenetre.fill((0, 0, 0))
                start_ticks = pygame.time.get_ticks()
                pygame.display.flip()
        pygame.display.flip()

    elif game_paused:
        #stop the timer while game is paused
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

        endScreenMessage.afficher()
        endScreenStartButton.afficher()
        endScreenQuitButton.afficher()
        pygame.display.flip()

    else:
        soundBank["menu_music"].stop()
        if not lvlMusicPlaying:
            lvlMusicPlaying=True
            pygame.mixer.music.play(10)
        # on recupere l'etat du clavier
        touches = pygame.key.get_pressed()
        # si la touche ESC est enfoncee, on sortira
        # au debut du prochain tour de boucle
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
        createTimerElements(fenetre, playtimePerLvl)
        ingameExitButton.afficher()
        # rafraichissement
        pygame.display.flip()

     #if we don't need to handle the events we use pump instead of the for-loop
    pygame.event.pump()
    #for event in pygame.event.get():  # parcours de la liste des evenements recus
        #do stuff with events
# fin du programme principal...
pygame.quit()
