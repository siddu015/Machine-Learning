import heapq


def A_star_search(start, goal, heuristic, get_neighbors, distance):
    open_set, came_from, g_score = [(heuristic(start, goal), start)], {}, {start: 0}
    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return [start] + path[::-1]

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + distance(current, neighbor)

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (tentative_g_score + heuristic(neighbor, goal), neighbor))
                came_from[neighbor] = current

    return None


start_node, goal_node = (0, 0), (5, 5)
heuristic = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
get_neighbors = lambda node: [(node[0] + 1, node[1]), (node[0] - 1, node[1]), (node[0], node[1] + 1), (node[0], node[1] - 1)]
distance = lambda x, y: 1

result = A_star_search(start_node, goal_node, heuristic, get_neighbors, distance)
print("Path:", result)
