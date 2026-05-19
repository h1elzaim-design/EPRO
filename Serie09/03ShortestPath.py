import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ── Labyrinth ────────────────────────────────────────────────
n = 10
maze = [[0]*n for _ in range(n)]
walls = [(2,8),(0,9),(1,7),(2,2),(2,3),(2,4),(2,5),
         (2,6),(2,7),(3,2),(4,2),(7,2),(6,2),(8,2),
         (4,7),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),
         (5,7),(6,2),(6,6),(7,6),(3,5),(7,4),(8,4),
         (9,4),(8,6),(8,7),(8,8)]
for (x,y) in walls:
    maze[x][y] = 1

start = (9, 1)
goal  = (3, 4)

# ── Meine Funktionen ─────────────────────────────────────────
def update(dist, maze, pos):
    x, y = pos
    n = len(maze)
    for (xp, yp, kosten) in [
        (x-1, y,    1),           (x+1, y,    1),
        (x,   y-1,  1),           (x,   y+1,  1),
        (x-1, y-1,  math.sqrt(2)),(x-1, y+1,  math.sqrt(2)),
        (x+1, y-1,  math.sqrt(2)),(x+1, y+1,  math.sqrt(2)),
    ]:
        tmp = dist[x][y] + kosten
        if 0 <= xp < n and 0 <= yp < n and maze[xp][yp] == 0 and tmp < dist[xp][yp]:
            dist[xp][yp] = tmp
            update(dist, maze, (xp, yp))

def find_shortest_path(dist, path):
    x, y = path[-1]
    if dist[x][y] != 0:
        for (xp, yp) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1),
                         (x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]:
            if 0 <= xp < n and 0 <= yp < n and dist[xp][yp] < dist[x][y]:
                path.append((xp, yp))
                return find_shortest_path(dist, path)
    return path

# ── Berechnen ────────────────────────────────────────────────
dist = [[float('inf')]*n for _ in range(n)]
dist[goal[0]][goal[1]] = 0
update(dist, maze, goal)
path = find_shortest_path(dist, [start])

# ── Visualisierung ───────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 8))

for i in range(n):
    for j in range(n):
        if maze[i][j] == 1:
            # Wand = dunkelblau
            ax.add_patch(plt.Rectangle((i-0.5, j-0.5), 1, 1, color='#1e293b'))
        else:
            # Freies Feld = hellgrau
            ax.add_patch(plt.Rectangle((i-0.5, j-0.5), 1, 1, color='#f1f5f9'))
            # Distanzwert anzeigen
            d = dist[i][j]
            if d < float('inf'):
                ax.text(i, j, f"{d:.1f}", ha='center', va='center',
                        fontsize=6.5, color='#334155')

# Pfad einzeichnen
px = [p[0] for p in path]
py = [p[1] for p in path]
ax.plot(px, py, color='#f59e0b', linewidth=3, zorder=3, label='Pfad')

# Start und Ziel markieren
ax.scatter(*start, color='#6366f1', s=200, zorder=5, label=f'Start {start}')
ax.scatter(*goal,  color='#10b981', s=200, zorder=5, marker='*', label=f'Ziel {goal}')

ax.set_xlim(-1, n)
ax.set_ylim(-1, n)
ax.set_aspect('equal')
ax.set_title(f'Dijkstra mit Diagonalen — Distanz: {dist[start[0]][start[1]]:.2f}', fontsize=13)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('maze.png', dpi=150)
plt.show()
print("Gespeichert als maze.png")
