def Cost(H, condition, weight=1):
    cost = {}

    if 'AND' in condition:
        cost[' AND '.join(condition['AND'])] = sum(H[node] + weight for node in condition['AND'])

    if 'OR' in condition:
        cost[' OR '.join(condition['OR'])] = min(H[node] + weight for node in condition['OR'])

    return cost


def update_cost(H, conditions, weight=1):
    least_cost = {}

    for key in reversed(conditions):
        c = Cost(H, conditions[key], weight)
        H[key] = min(c.values())
        least_cost[key] = c
        print(f"{key} : {conditions[key]} >>> {c}")

    return least_cost


def shortest_path(Start, Updated_cost):
    if Start not in Updated_cost:
        return Start

    key = min(Updated_cost[Start], key=Updated_cost[Start].get)
    Next = key.split()

    if len(Next) == 1:
        return Start + '<--' + shortest_path(Next[0], Updated_cost)

    return Start + '<--(' + key + ') [' + \
        shortest_path(Next[0], Updated_cost) + ' + ' + \
        shortest_path(Next[-1], Updated_cost) + ']'


H = {'A': -1, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 0, 'I': 0, 'J': 0}
Conditions = {
    'A': {'OR': ['B'], 'AND': ['C', 'D']},
    'B': {'OR': ['E', 'F']},
    'C': {'OR': ['G'], 'AND': ['H', 'I']},
    'D': {'OR': ['J']}
}
weight = 1

print('Updated Cost:')
Updated_cost = update_cost(H, Conditions, weight)
print('*' * 75)
print('Shortest Path:\n', shortest_path('A', Updated_cost))
