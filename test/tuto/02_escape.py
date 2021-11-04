import pygame

# Initialisation de la bibliotheque pygame
pygame.init()

# Creation de la fenetre
largeur = 640
hauteur = 480
fenetre=pygame.display.set_mode((largeur,hauteur))

# la boucle dont on veut sortir :
#   - en appuyant sur ESCAPE
#   - en cliquant sur le bouton de fermeture
i=0;
continuer=True
while continuer== True:

    i=i+1;
    print (i)

    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();
    # On récupere les evenements
    events = pygame.event.get()

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] == True :
        continuer=False

    # Si on a clique sur le bouton de fermeture on sortira
    # au debut du prochain tour de boucle
    # Pour cela, on parcours la liste des evenements
    # et on cherche un QUIT...
    for event in events: # parcours de la liste des evenements recus
        if event.type == pygame.QUIT: # Si un de ces evenements est de type QUIT
            continuer = False

# fin du programme principal...
pygame.quit()
