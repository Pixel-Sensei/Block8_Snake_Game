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
