nb_l = len(tileMap)
nb_c = len(tileMap[0])
sprite = imageBank["all_tiles"]
for i in range(nb_l):
    for j in range(nb_c):
        if tileMap[i][j] == 1:
            mytiles["tileList"].append(
                ElementGraphique(sprite.get_image_name("castleMid.png"), fenetre, x=50 * j,
                                 y=50 * i))
        if tileMap[i][j] == 1111:
            mytiles["affectedByButton"].append(
                button_Platform(sprite.get_image_name("castleMid.png"), fenetre, x=50 * j,
                                y=50 * i))
        if tileMap[i][j] == 112:
            platformCounter += 1
            cropped = pygame.Surface((50, 30), pygame.SRCALPHA)
            cropped.blit(imageBank["all_tiles"].get_image_name("castleHalfMid.png"), (0, 0),
                         (0, 0, 50, 30))
            cropped.set_alpha(150)
            newPlat = disappearing_Platform(cropped, fenetre, x=50 * j,
                                            y=50 * i, lifetime=1500, id=platformCounter)
            mytiles["disapTiles"].append(newPlat)
        if tileMap[i][j] == 111:
            mytiles["tileList"].append(
                ElementGraphique(sprite.get_image_name("castleCenter.png"), fenetre, x=50 * j,
                                 y=(50 * i) - 21))
        if tileMap[i][j] == 2:
            mytiles["tileList"].append(lava(fenetre, x=50 * j, y=50 * i))
        if tileMap[i][j] == 3:
            cropped = pygame.Surface((50, 30), pygame.SRCALPHA)
            cropped.blit(imageBank["all_tiles"].get_image_name("castleHalfMid.png"), (0, 0),
                         (0, 0, 50, 30))
            mytiles["tileList"].append(
                ElementGraphique(cropped, fenetre, x=50 * j, y=50 * i))
        if tileMap[i][j] == 33:
            mytiles["tileList"].append(
                ElementGraphique(sprite.get_image_name("castleHalf.png"), fenetre, x=50 * j,
                                 y=50 * i))
        if tileMap[i][j] == 34:
            mytiles["tileList"].append(
                ElementGraphique(sprite.get_image_name("castleHalf.png"), fenetre, x=50 * j,
                                 y=(50 * i) - 20))
        if tileMap[i][j] == 35:
            platformCounter += 1
            cropped = pygame.Surface((50, 30), pygame.SRCALPHA)
            cropped.blit(imageBank["all_tiles"].get_image_name("castleHalfMid.png"), (0, 0),
                         (0, 0, 50, 30))
            cropped.set_alpha(150)
            newPlat = disappearing_Platform(cropped, fenetre, x=50 * j,
                                            y=(50 * i) + 15, lifetime=1500, id=platformCounter)
            mytiles["disapTiles"].append(newPlat)
        if tileMap[i][j] == 36:
            mytiles["tileList"].append(
                ElementGraphique(sprite.get_image_name("castleHalf.png"), fenetre, x=(50 * j) - 10,
                                 y=(50 * i) + 5))
        if tileMap[i][j] == 4:
            mytiles["tileList"].append(
                ElementGraphique(sprite.get_image_name("castleHalfLeft.png"), fenetre, x=50 * j,
                                 y=50 * i))
        if tileMap[i][j] == 44:
            mytiles["tileList"].append(
                ElementGraphique(sprite.get_image_name("castleHalfRight.png"), fenetre, x=50 * j,
                                 y=50 * i))
        if tileMap[i][j] == 5:
            mytiles["tileList"].append(
                ElementGraphique(sprite.get_image_name("castleCenter.png"), fenetre, x=50 * j,
                                 y=50 * i))
        if tileMap[i][j] == 6:
            mytiles["styleTileList"].append(
                ElementGraphique(sprite.get_image_name("window.png"), fenetre, x=50 * j,
                                 y=50 * i))
        if tileMap[i][j] == 7:
            torchArr = [sprite.get_image_name("tochLit.png"), sprite.get_image_name("tochLit2.png")]
            mytiles["styleTileList"].append(
                ElementAnime(torchArr, fenetre, x=50 * j,
                             y=50 * i))
        if tileMap[i][j] == 8:
            mytiles["tileList"].append(
                ElementGraphique(sprite.get_image_name("castleRight.png"), fenetre, x=50 * j,
                                 y=50 * i))
        if tileMap[i][j] == 9:
            door = Door(fenetre, x=50 * j, y=(50 * i) - 30)
            mytiles["styleTileList"].append(door)
            mytiles["door"] = door
        if tileMap[i][j] == 91:
            mytiles["styleTileList"].append(
                ElementGraphique(sprite.get_image_name("door_openMid.png"), fenetre, x=50 * j,
                                 y=(50 * i)))
        if tileMap[i][j] == 92:
            mytiles["styleTileList"].append(
                ElementGraphique(sprite.get_image_name("door_openTop.png"), fenetre, x=50 * j,
                                 y=(50 * i)))
        if tileMap[i][j] == 10:
            mytiles["styleTileList"].append(
                ElementGraphique(sprite.get_image_name("signRight.png"), fenetre, x=50 * j,
                                 y=50 * i))
        if tileMap[i][j] == 11:
            cropped = pygame.Surface((50, 20), pygame.SRCALPHA)
            cropped.blit(imageBank["all_tiles"].get_image_name("bridgeLogs.png"), (0, 0),
                         (0, 32, 50, 20))
            mytiles["tileList"].append(
                ElementGraphique(cropped, fenetre, x=50 * j,
                                 y=(50 * i) + 50))
        if tileMap[i][j] == 12:
            newSpike = spikes(fenetre, x=50 * j, y=50 * i)
            mytiles["styleTileList"].append(newSpike)
        if tileMap[i][j] == 13:
            newSpike = spikes(fenetre, x=50 * j, y=50 * i)
            mytiles["affectedByButton"].append(newSpike)
        if tileMap[i][j] == 14:
            switchCounter += 1
            passive = pygame.Surface((50, 35), pygame.SRCALPHA)
            passive.blit(imageBank["all_items"].get_image_name("buttonBlue.png"), (0, 0), (0, 15, 50, 35))
            active = pygame.Surface((50, 35), pygame.SRCALPHA)
            active.blit(imageBank["all_items"].get_image_name("buttonBlue_pressed.png"), (0, 0),
                        (0, 15, 50, 35))
            newSwitch = switch(fenetre, 50 * j, (50 * i) + 15, active, passive, switchCounter)
            mytiles["switches"].append(newSwitch)
        if tileMap[i][j] == 141:
            switchCounter += 1
            passive = pygame.Surface((50, 35), pygame.SRCALPHA)
            passive.blit(imageBank["all_items"].get_image_name("buttonBlue.png"), (0, 0), (0, 15, 50, 35))
            active = pygame.Surface((50, 35), pygame.SRCALPHA)
            active.blit(imageBank["all_items"].get_image_name("buttonBlue_pressed.png"), (0, 0),
                        (0, 15, 50, 35))
            newSwitch = switch_display_stuff(fenetre, 50 * j, (50 * i) + 15, active, passive, switchCounter)
            mytiles["switches"].append(newSwitch)
        if tileMap[i][j] == 15:
            cropped = pygame.Surface((50, 30), pygame.SRCALPHA)
            cropped.blit(imageBank["all_tiles"].get_image_name("castleHalfLeft.png"), (0, 0), (0, 0, 50, 30))
            newPlatform = movingPlatform(cropped, fenetre, 50 * j, 50 * j, (50 * i) + 20, (50 * i) - 300, 3)
            mytiles["tileList"].append(newPlatform)
        if tileMap[i][j] == 16:
            cropped = pygame.Surface((100, 20), pygame.SRCALPHA)
            cropped.blit(imageBank["all_tiles"].get_image_name("bridgeLogs.png"), (0, 0), (0, 32, 50, 20))
            cropped.blit(imageBank["all_tiles"].get_image_name("bridgeLogs.png"), (50, 0), (0, 32, 50, 20))
            newPlatform = movingPlatform(cropped, fenetre, (50 * j), (50 * j) + 550, (50 * i) + 45,(50 * i) + 45,3.5)
            mytiles["tileList"].append(newPlatform)
        if tileMap[i][j] == 78:
            mytiles["coins"].append(
                collectable(imageBank["spinning_coin"], soundBank["coin"], fenetre, 50 * j, 50 * i))
        if tileMap[i][j] == 77:
            mytiles["gems"].append(
                collectable(imageBank["blue_gem_animated"], soundBank["gem"], fenetre, 50 * j, 50 * i))

return mytiles

#ennemi
mechant = []
nb_l = len(World.maMap)
nb_c = len(World.maMap[0])
for i in range(nb_l):
    for j in range (nb_c):
        if World.maMap[i][j]==6:
            bad = Badguys(imageBank["flame"], fenetre, x=50 * j, y=50 * i)
            mechant.append(bad)



class Badguys(ElementAnime):

    def __init__(self, img, fen, x, y):

        super().__init__(img,fen,x,y)

        self.dx = random.randint(-5,5)
    #new_badrect=0

    def deplacer(self,world):
        new_badrect= copy.deepcopy(self.rect)
        #new_badrect= self.rect.x
        if world.collide_map(new_badrect):
            self.dx = -self.dx
            new_badrect.x += self.dx
            self.rect.x = new_badrect.x
        else :
            new_badrect.x += self.dx
            self.rect.x = new_badrect.x

    def end(self, fen):
        w, h = self.fenetre.get_size()
        if self.rect.x == perso.rect.x:
            del mechant[self]






for tile in tilelist:
    if tile.rect.colliderect(new_badrect.x, self.rect.y, self.rect.width, self.rect.height):
        new_badrect.x = self.rect.x
        self.dx = -self.dx
        new_badrect.x += self.dx
        self.rect.x = new_badrect.x
    else :
        self.rect.x = new_badrect.x
    if tile.rect.colliderect(new_badrect.y, self.rect.x, self.rect.width, self.rect.height):
        new_badrect.y = self.rect.y
    else :
        new_badrect.x = self.rect.x
        self.dx = -self.dx
        new_badrect.x += self.dx
        self.rect.x = new_badrect.x









if tileMap[i][j] == 69:
    bad = Badguys(fenetre, x=50*j, y=50*i )
    mytiles["enemis"].append(bad)



























 [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],  # 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 9, 0],  # 4
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
    [1, 1, , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0],  # 13
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], ]



    [
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]



       [
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]



           [
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
              [0, 0, 0, 0, 0, 0, 0, 0, 7, 6, 7, 0, 0, 0, 77, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 0, 0],  # 2
              [0, 0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 9],  # 3
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 112, 0, 0, 0, 0, 78, 0, 0, 0, 0, 112, 0, 0, 4, 112, 3, 3],  # 4
              [77, 0, 0, 0, 0, 0, 36, 0, 0, 4, 44, 0, 0, 0, 0, 0, 0, 112, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 77],  # 5
              [0, 0, 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
              [0, 0, 7, 6, 7, 0, 0, 0, 0, 0, 77, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 77, 0, 0, 0, 0, 0, 0, 0],  # 7
              [16, 0, 0, 0, 0, 34, 0, 0, 0, 0, 0, 0, 0, 0, 33, 0, 77, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 0, 0, 112, 0, 0, 0, 112, 0, 0, 112, 7, 6, 7, 0],  # 9
              [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 0],  # 10
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
              [92, 7, 0, 77, 0, 0, 0, 0, 78, 0, 0, 0, 78, 7, 0, 0, 0, 0, 78, 0, 0, 0, 0, 77, 0, 7, 0, 0, 0],  # 12
              [91, 10, 0, 14, 0, 0, 0, 112, 0, 0, 11, 11, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 0, 0, 0, 0, 0, 0, 15],  # 13
              [1, 1, 1, 1, 1, 112, 2, 2, 2, 2, 2, 2, 112, 112, 112, 112, 112, 112, 1, 1, 1, 1, 1, 112, 112, 1, 1, 1, 1], ]  # 14
