import matplotlib.pyplot as plt

def cantor(interval, depth):
    a, b = interval
    left = (a, 2/3 * a + 1/3 * b)
    right = (1/3 * a + 2/3 * b, b)
    if depth == 1:
        return [left, right]
    else:
        return cantor(left, depth-1) + cantor(right, depth-1)

#############################
#       Visualization       #
#############################
interval = (0, 1)
max_depth = 4

plt.plot([interval[0], interval[1]], [max_depth, max_depth], linewidth=3, color='k')

for depth in range(1, max_depth+1):
    intervals = cantor(interval, depth)
    y = max_depth - depth
    for a, b in intervals:
        plt.plot([a, b], [y, y], linewidth=3, color='k')

labels = [""] + [f"depth {d}" for d in range(1, max_depth+1)]
plt.yticks(range(max_depth), labels[:0:-1])
plt.ylim(-1, max_depth+1)
plt.show()