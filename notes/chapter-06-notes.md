# Graphs

A graph is a data structure used to represent relationships between objects.

A graph is made of:

- Vertices (nodes) → the objects
- Edges → the connections between them

## Example:

Alice → Bob
Alice → Claire
Bob → Anuj
Bob → Peggy

This structure is useful for representing networks such as:
- Social networks
- Maps and routes
- Internet connections
- Recommendations

## Graph Representation

Graphs are commonly stored using an adjacency list.
Example:
graph = {
  "you": ["alice", "bob", "claire"],
  "bob": ["anuj", "peggy"],
  "alice": ["peggy"],
  "claire": ["thom"],
  "anuj": [],
  "peggy": [],
  "thom": []
}
Each node points to the list of its neighbors.


# Breadth-First Search (BFS)

Breadth-First Search (BFS) is an algorithm used to search through a graph.

It explores the graph level by level, checking all neighbors before moving deeper.

BFS is useful for:
- Finding the shortest path between two nodes
- Searching for a node that satisfies a condition

## How BFS Works

BFS uses a queue data structure.
Steps:

- Add the starting node's neighbors to a queue.
- Take the first person from the queue.
- Check if they match the search condition.
- If not, add their neighbors to the queue.
- Repeat until the target is found or the queue is empty.

## Example:

Searching for a mango seller in a network:
you → alice, bob, claire
bob → anuj, peggy
claire → thom, jonny

Search order:
alice → bob → claire → anuj → peggy → thom
The algorithm checks people closest to you first.

➡️ [View BFS implementation ](../code/bfs.py)

## Time Complexity
BFS runs in:
O(V + E)
Where:
V = number of vertices (nodes)
E = number of edges (connections)

## Key Properties
- Uses a queue
- Explores nodes level by level
- Finds the shortest path in an unweighted graph