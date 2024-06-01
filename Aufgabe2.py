# Schriftarten für den Text im Spiel festlegen
schrift_stil = pygame.font.SysFont("Arial", 25)
punkte_schrift = pygame.font.SysFont("Arial", 35)

# Funktion zum Anzeigen des Punktestands definieren
def dein_score(score):
    wert = punkte_schrift.render("Dein Punktestand: " + str(score), True, gelb)
    dis.blit(wert, [0, 0])
