def reconstruct_path(path, start, goal):
    current = goal
    result_path = []
    while current is not None:
        result_path.append(current)
        current = path[current]
    result_path.reverse()
    return result_path


def rec_path(path,current_node):
    reconstructed_path = []
    while current_node:
        reconstructed_path.append(current_node.position)
        current_node = path[current_node.position]
    return reconstructed_path[::-1]