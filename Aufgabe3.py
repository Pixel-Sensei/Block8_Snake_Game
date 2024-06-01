# Funktion zum Zeichnen der Schlange definieren
def unsere_schlange(schlangenblock, schlangenliste):
    for x in schlangenliste:
        pygame.draw.rect(dis, schwarz, [x[0], x[1], schlangenblock, schlangenblock])

# Funktion zum Anzeigen von Nachrichten definieren
def nachricht(msg, farbe):
    text = schrift_stil.render(msg, True, farbe)
    dis.blit(text, [dis_breite / 6, dis_höhe / 3])
