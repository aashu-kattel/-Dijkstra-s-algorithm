import heapq

def dijkstra(graph, start):
    # Initialize distances to all vertices as infinity except for the start vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Use a priority queue to keep track of the vertices with the smallest distances
    pq = [(0, start)]

    while len(pq) > 0:
        # Pop the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(pq)

        # If the distance to the current vertex is already larger than the stored distance, skip
        if current_distance > distances[current_vertex]:
            continue

        # Iterate over the neighbours of the current vertex and update their distances if needed
        for neighbour, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))

    return distances
