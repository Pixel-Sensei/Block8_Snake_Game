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
