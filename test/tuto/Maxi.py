def afficher_bad(self,W):
    nb_l = len(W.maMap)
    nb_c = len(W.maMap[0])
    self = []
    for j in range(nb_c):
        if W.maMap[i][j] == 6:
            bad = Badguys(imageBank["flame"], fenetre, x=50 * j, y=50 * i)
            self.append(bad)
