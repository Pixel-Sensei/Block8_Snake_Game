import pygame  # Pygame-Bibliothek importieren für das Spiel-Framework
import random  # Zufallsmodul importieren

pygame.init()  # Pygame initialisieren

# Definition von Farbkonstanten
weiß = (255, 255, 255)
gelb = (255, 255, 102)
schwarz = (0, 0, 0)
rot = (213, 50, 80)
grün = (0, 255, 0)
blau = (50, 153, 213)

# Größe des Spielfensters
dis_breite = 1000
dis_höhe = 400

# Spielfenster initialisieren
dis = pygame.display.set_mode((dis_breite, dis_höhe))
pygame.display.set_caption('Snake')  # Fenstertitel setzen

uhr = pygame.time.Clock()  # Pygame-Uhr erstellen für die Framerate

# Größe eines Schlangenblocks und Geschwindigkeit der Schlange festlegen
schlangenblock = 10
schlangengeschwindigkeit = 15
