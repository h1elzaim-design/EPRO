def update(dist, maze, pos):
    i, j = pos                          # Position entpacken
    for di, dj, cost in directions:     # alle 8 Richtungen
        ni, nj = i + di, j + dj        # Nachbar berechnen
        if 0 <= ni < n and 0 <= nj < n:  # im Grid?
            if maze[ni][nj] == 0:         # kein Wall?
                new_dist = dist[i][j] + cost       # neuer Weg
                if new_dist < dist[ni][nj]:        # kürzer?
                    dist[ni][nj] = new_dist        # speichern
                    update(dist, maze, (ni, nj))   # weiterpropagieren