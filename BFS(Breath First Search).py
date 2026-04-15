#Plant life Layout

from collections import deque

def bfs(graph, start):
    done = set()  # Set to keep track of visited nodes
    q = deque([start])  # Initialize the queue with the starting node
    
    done.add(start)
    
    while q:
        node = q.popleft()  # Dequeue a node
        print(node, end=" ")  # Process the node (here, we just print it)
        
        # Explore all the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in done:
                done.add(neighbor)  # Mark the neighbor as visited
                q.append(neighbor)  # Enqueue the neighbor


# Example usage:
graph = {
    'Seed': ['Roots', 'Shoots'],
    'Roots': ['Seed', 'Main_Root', 'Hair_Root'],
    'Shoots': ['Seed', 'Branches'],
    'Main_Root': ['Roots'],
    'Hair_Root': ['Roots'],
    'Branches': ['Shoots']
}

start_node = 'Seed'
print("BFS Traversal starting from node", start_node, ":")
bfs(graph, start_node)

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Graph data
graph = {
    'Seed': ['Roots', 'Shoots'],
    'Roots': ['Seed', 'Main_Root', 'Hair_Root'],
    'Shoots': ['Seed', 'Branches'],
    'Main_Root': ['Roots'],
    'Hair_Root': ['Roots'],
    'Branches': ['Shoots']
}

# Positions – Seed on top, two groups side by side below
positions = {
    'Seed':       (0.00, 1.50),
    'Roots':      (-0.80, 0.60),
    'Main_Root':  (-1.30, 0.05),
    'Hair_Root':  (-0.30, 0.05),
    'Shoots':     ( 0.80, 0.60),
    'Branches':   ( 1.30, 0.05)
}

# ─── Create figure ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12 , 10), facecolor='black')
ax.set_facecolor('black')

# ─── Draw circular grouping boxes ──────────────────────────────────
# Root System circle (left)
ax.add_patch(Circle(
    (-0.80, 0.35), radius=1.0,
    fill=True, facecolor='#3c2f2f', alpha=0.30,
    edgecolor='#8b5a2b', linewidth=3,
    zorder=0
))

# Shoot System circle (right)
ax.add_patch(Circle(
    ( 0.80, 0.35), radius=1.0,
    fill=True, facecolor='#1e3a1e', alpha=0.30,
    edgecolor='#4caf50', linewidth=3,
    zorder=0
))

# Box labels
ax.text(-0.80, 1.10, "Root System", 
        ha='center', fontsize=15, color='#d2a679', fontweight='bold', alpha=0.95)
ax.text( 0.80, 1.10, "Shoot System", 
        ha='center', fontsize=15, color='#a8e6a8', fontweight='bold', alpha=0.95)

# ─── Draw edges ────────────────────────────────────────────────────
drawn = set()
for node, neighbors in graph.items():
    x1, y1 = positions[node]
    for neigh in neighbors:
        edge = tuple(sorted([node, neigh]))
        if edge in drawn:
            continue
        drawn.add(edge)
        
        x2, y2 = positions[neigh]
        ax.plot([x1, x2], [y1, y2],
                color='#bbbbbb', linewidth=2.2, alpha=0.8, zorder=1)

# ─── Draw nodes ────────────────────────────────────────────────────
for node, (x, y) in positions.items():
    if node == 'Seed':
        color = '#e0b070'      # golden seed
        size = 2200
    elif 'Root' in node:
        color = '#8b5a2b'      # brown roots
        size = 1500
    else:  # Shoots, Branches
        color = '#4caf50'      # green shoots
        size = 1500
    
    ax.scatter(x, y,
               s=size,
               c=color,
               edgecolors='white',
               linewidth=2.2,
               zorder=3)
    
    ax.text(x, y, node,
            fontsize=13,
            fontweight='bold',
            ha='center',
            va='center',
            color='white',
            zorder=4)

# ─── Titles ────────────────────────────────────────────────────────
ax.set_title("Plant Structure\nSeed → Root System & Shoot System",
             fontsize=18, color='white', pad=45)

fig.suptitle("After Seed: Two Separate Systems", 
             fontsize=13, color='#dddddd', y=0.94)

# ─── Clean layout ──────────────────────────────────────────────────
ax.axis('off')
plt.subplots_adjust(left=0.02, right=0.98, top=0.90, bottom=0.02)

plt.show()