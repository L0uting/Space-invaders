TAILLE = 16
import pygame

ennemis = []
for x in range(1, 50, 10):
    for y in range(10, 40, 10):
        ennemis.append(
            pygame.Rect(x * TAILLE, y * TAILLE, TAILLE, TAILLE))
print(ennemis)