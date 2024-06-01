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
