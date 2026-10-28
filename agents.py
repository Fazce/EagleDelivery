from collections import deque
import heapq
from itertools import count


class SearchResult:
    def __init__(self, path, expanded):
        self.path = path
        self.expanded = expanded


def reconstruct_path(parents, goal):
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parents[state]
    path.reverse()
    return path


def bfs(campus, start, goal):
    frontier = deque([start])
    parents = {start: None}
    expanded = 0
    while frontier:
        state = frontier.popleft()
        if state == goal:
            return SearchResult(reconstruct_path(parents, goal), expanded)
        expanded += 1
        for action, successor in campus.neighbors(state):
            if successor not in parents:
                parents[successor] = state
                frontier.append(successor)
    return SearchResult(None, expanded)


def manhattan(state, goal):
    """TODO 1: Return Manhattan distance between two (row, column) tuples."""
    # Add the absolute row difference and the absolute column difference.
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def astar(campus, start, goal):
    """TODO 2: Return SearchResult(path, expanded) for A* graph search."""
    # Use heapq as a priority queue and manhattan() as the heuristic.
    # Track best known g-costs and parent states in dictionaries.
    if start == goal:
        return SearchResult([start], 0)
    
    frontier = []
    tie_breaker = count()

    g_costs = {start: 0}
    parents = {start: None}

    start_h = manhattan(start, goal)
    heapq.heappush(frontier, (start_h, next(tie_breaker), 0, start))

    expanded = 0

    while frontier:
        f, _, g, state = heapq.heappop(frontier)

        # Skipping stale entries in the priority queue
        if g != g_costs[state]:
            continue

        # Goal test when removing from the priority queue
        if state == goal:
            return SearchResult(reconstruct_path(parents, goal), expanded)

        expanded += 1

        for action, successor in campus.neighbors(state):
            # Calculate the g-cost for the successor
            new_g = g + 1

            # If cheaper path is found
            if successor not in g_costs or new_g < g_costs[successor]: 
                g_costs[successor] = new_g
                parents[successor] = state

                new_f = new_g + manhattan(successor, goal)
                heapq.heappush(frontier, (new_f, next(tie_breaker), new_g, successor))

    return SearchResult(None, expanded)

def epsilon_greedy(q_values, state, actions, epsilon, rng):
    """TODO 3: Choose an action with epsilon-greedy exploration."""
    # q_values is a dictionary. Its keys are (state, action) pairs.
    # Example key: ((1, 1), "RIGHT"). Unseen entries have value 0.0.

    # Exploration
    if rng.random() < epsilon:
        return rng.choice(actions)

    # Find the highest Q-value for the current state
    best_value = max(q_values.get((state, action), 0.0) for action in actions)

    # Collect all actions that have the best Q-value
    best_actions = [
        action 
        for action in actions 
        if q_values.get((state, action), 0.0) == best_value
    ]

    # Break ties randomly among the best actions
    return rng.choice(best_actions)


def q_learning_update(q_values, state, action, reward, next_state,
                      actions, alpha, gamma, terminal):
    """TODO 4: Update exactly one Q-table entry in place; return nothing."""
    # Get Q(state, action), defaulting to 0.0.
    # If terminal is True, the target is reward with no continuation term.
    # Otherwise target = reward + gamma * max Q(next_state, next_action).
    # Consider every action, including unseen entries with value 0.0.
    # Apply Q <- Q + alpha * (target - Q).
    
    current_q = q_values.get((state, action), 0.0)

    if terminal:
        target = reward
    else:
        max_next_q = max(q_values.get((next_state, next_action), 0.0) for next_action in actions)
        target = reward + gamma * max_next_q    

    q_values[(state, action)] = current_q + alpha * (target - current_q)
