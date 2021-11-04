import pygame
import random
import copy

def lire_images():
    imageBank = {}
    imageBank["perso"]=pygame.image.load("perso.png").convert_alpha()
    imageBank["perso"]= pygame.transform.scale(imageBank["perso"], (48, 48))
    imageBank["balle"]=pygame.image.load("balle.png").convert_alpha()
    imageBank["fond"]=pygame.image.load("background.jpg").convert_alpha()
    imageBank["mur"]=pygame.image.load("mur.jpg").convert_alpha()
    imageBank["mur"]= pygame.transform.scale(imageBank["mur"], (64, 64))

    return imageBank


def afficher_map(maMap, imageBank):
    # Afficher tous les murs
    nb_l = len(maMap)
    nb_c = len(maMap[0])
    for i in range(nb_l):
        for j in range (nb_c):
            if maMap[i][j]==1:
                mur = ElementGraphique(imageBank["mur"], fenetre, x=64*j, y=64*i)
                mur.afficher()

def collide_map(maMap, un_rect):
    # haut
    irect = un_rect.y//64
    jrect = int(un_rect.x/64)

    if (maMap[irect][jrect] != 0) :
        return True

    # bas
    irect = (un_rect.y+ un_rect.h)//64
    jrect = int(un_rect.x/64)

    if (maMap[irect][jrect] != 0) :
        return True


    return False


class ElementGraphique():
    def __init__(self, img, fen, x=0, y=0):
        self.image = img
        self.rect= self.image.get_rect()
        self.fenetre = fen

        # creation d'un rectangle pour positioner l'image du personnage
        self.rect.x = x
        self.rect.y = y

    def afficher(self):
        self.fenetre.blit(self.image, self.rect)

    def contact(self,autre):
        if self.rect.colliderect(autre.rect):
            return True
        return False


class Joueur(ElementGraphique):
    def __init__(self, img, fen, x=0, y=0):
        super().__init__(img,fen,x,y)

        self.vitesse = 5

    def deplacer(self):
        # on recupere l'etat du clavier
        touches = pygame.key.get_pressed();

        new_rect = copy.deepcopy(self.rect)

        if touches[pygame.K_RIGHT] :
            new_rect.x += self.vitesse

        if touches[pygame.K_LEFT] :
            new_rect.x += -self.vitesse

        if touches[pygame.K_UP] :
            new_rect.y += -self.vitesse

        if touches[pygame.K_DOWN] :
            new_rect.y += self.vitesse

        if collide_map(maMap,new_rect):
            print("Deplacement refusé")
        else :
            print("Deplacement accepté")
            self.rect = new_rect


class Balle(ElementGraphique):
    def __init__(self, img, fen):

        w , h = fen.get_size()

        x = random.randint(0,w)
        y = random.randint(0,h)

        super().__init__(img,fen,x,y)

        self.dx = random.randint(-5,5)
        self.dy = random.randint(-5,5)


    def deplacer(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        w , h = self.fenetre.get_size()

        # a gauche ou droite
        if self.rect.x < 0 or self.rect.x + self.rect.w > w:
            self.dx = -self.dx

        # en haut ou bas
        if self.rect.y < 0 or self.rect.y + self.rect.h > h:
            self.dy = -self.dy

class Bidon(ElementGraphique):

    def faire_un_truc(self):
        print("je fais un truc")

# Initialisation de la bibliotheque pygame
pygame.init()

#creation de la fenetre
largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))

imageBank = lire_images()

# lecture de l'image du perso

perso = Joueur(imageBank["perso"], fenetre, x=60, y=80)


mes_balles = []
for i in range(3):
    balle = Balle(imageBank["balle"], fenetre)
    mes_balles.append(balle)

# lecture de l'image du fond
fond = ElementGraphique(imageBank["fond"],fenetre)


bidon = Bidon(imageBank["balle"], fenetre, x=10, y=10)

## Ajoutons un texte fixe dans la fenetre :
# Choix de la police pour le texte
font = pygame.font.Font(None, 34)

# Creation de l'image correspondant au texte
texte = ElementGraphique(font.render('dot biten', True, (3, 45, 49)), fenetre, x=10, y=10)

maMap = [[1,1,1,1,1],
         [1,0,0,0,0],
         [0,0,1,1,0],
         [0,0,1,1,0]
         ]

# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()

# la boucle dont on veut sortir :
#   - en appuyant sur ESCAPE
#   - en cliquant sur le bouton de fermeture
i=1;
continuer=1
while continuer:

    # fixons le nombre max de frames / secondes
    horloge.tick(30)

    i=i+1
    #print (i)

    '''
    if i > 100:
        perso.vitesse = 15
    '''

    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] :
        continuer=0

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
    fond.afficher()


    afficher_map(maMap, imageBank)

    # Affichage Perso
    perso.afficher()


    for e in mes_balles:
        e.afficher()

    # Affichage du Texte
    texte.afficher()

    # rafraichissement
    pygame.display.flip()

    # Si on a clique sur le bouton de fermeture on sortira
    # au debut du prochain tour de boucle
    # Pour cela, on parcours la liste des evenements
    # et on cherche un QUIT...
    for event in pygame.event.get():   # parcours de la liste des evenements recus
        if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
            continuer = 0	   # On arrete la boucle

# fin du programme principal...
pygame.quit()
