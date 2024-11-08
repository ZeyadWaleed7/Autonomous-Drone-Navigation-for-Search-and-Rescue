from collections import deque

def breadth_first_search(start_node):
    search_queue = deque([(start_node, [start_node.position])])
    visited_nodes = set()

    while search_queue:
        current_node, current_path = search_queue.popleft()

        if current_node in visited_nodes:
            continue
        visited_nodes.add(current_node)

        for child_node in current_node.children:
            if not child_node.passable:
                continue

            path_to_child = current_path + [child_node.position]

            if child_node.goal:
                return path_to_child, visited_nodes

            search_queue.append((child_node, path_to_child))

    return None
