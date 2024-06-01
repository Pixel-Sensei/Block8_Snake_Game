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

# Schriftarten für den Text im Spiel festlegen
schrift_stil = pygame.font.SysFont("Arial", 25)
punkte_schrift = pygame.font.SysFont("Arial", 35)

# Funktion zum Anzeigen des Punktestands definieren
def dein_score(score):
    wert = punkte_schrift.render("Dein Punktestand: " + str(score), True, gelb)
    dis.blit(wert, [0, 0])

# Funktion zum Zeichnen der Schlange definieren
def unsere_schlange(schlangenblock, schlangenliste):
    for x in schlangenliste:
        pygame.draw.rect(dis, schwarz, [x[0], x[1], schlangenblock, schlangenblock])

# Funktion zum Anzeigen von Nachrichten definieren
def nachricht(msg, farbe):
    text = schrift_stil.render(msg, True, farbe)
    dis.blit(text, [dis_breite / 6, dis_höhe / 3])

# Hauptspiel-Funktion definieren
def spiel():
    spiel_ende = False
    spiel_schließen = False

    x1 = dis_breite / 2  # Startposition der Schlange auf der x-Achse
    y1 = dis_höhe / 2    # Startposition der Schlange auf der y-Achse

    x1_veränderung = 0   # Anfangsgeschwindigkeit der Schlange auf der x-Achse
    y1_veränderung = 0   # Anfangsgeschwindigkeit der Schlange auf der y-Achse

    schlangenliste = []  # Liste für die Koordinaten der Schlangenblöcke
    länge_der_schlange = 1  # Startlänge der Schlange

    # Zufällige Position für das Essen festlegen
    essen_x = round(random.randrange(0, dis_breite - schlangenblock) / 10.0) * 10.0
    essen_y = round(random.randrange(0, dis_höhe - schlangenblock) / 10.0) * 10.0

    while not spiel_ende:

        while spiel_schließen:
            dis.fill(blau)
            nachricht("Du hast verloren! Drücke R zum Neustarten oder Q zum Beenden des Spiels", rot)
            dein_score(länge_der_schlange - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        spiel_ende = True
                        spiel_schließen = False
                    if event.key == pygame.K_r:
                        spiel()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spiel_ende = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_veränderung = -schlangenblock
                    y1_veränderung = 0
                elif event.key == pygame.K_RIGHT:
                    x1_veränderung = schlangenblock
                    y1_veränderung = 0
                elif event.key == pygame.K_UP:
                    y1_veränderung = -schlangenblock
                    x1_veränderung = 0
                elif event.key == pygame.K_DOWN:
                    y1_veränderung = schlangenblock
                    x1_veränderung = 0

        if x1 >= dis_breite or x1 < 0 or y1 >= dis_höhe or y1 < 0:
            spiel_schließen = True

            x1 += x1_veränderung
            y1 += y1_veränderung

            dis.fill(blau)
            pygame.draw.rect(dis, grün, [essen_x, essen_y, schlangenblock, schlangenblock])
            schlangenkopf = [x1, y1]
            schlangenliste.append(schlangenkopf)

            if len(schlangenliste) > länge_der_schlange:
                del schlangenliste[0]

            for x in schlangenliste[:-1]:
                if x == schlangenkopf:
                    spiel_schließen = True

            unsere_schlange(schlangenblock, schlangenliste)
            dein_score(länge_der_schlange - 1)

            pygame.display.update()

            if x1 == essen_x and y1 == essen_y:
                essen_x = round(random.randrange(0, dis_breite - schlangenblock) / 10.0) * 10.0
                essen_y = round(random.randrange(0, dis_höhe - schlangenblock) / 10.0) * 10.0
                länge_der_schlange += 1

            uhr.tick(schlangengeschwindigkeit)

    pygame.quit()
    quit()

spiel()
