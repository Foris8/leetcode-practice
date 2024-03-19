class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def bfs(x, y):
            visited = set()
            queue = deque([(0, 0)])
            steps = 0

            while queue:
                curr_level_cnt = len(queue)

                for i in range(curr_level_cnt):
                    curr_x, curr_y = queue.popleft()

                    if (curr_x, curr_y) == (x, y):
                        return steps

                    for off_x, off_y in offsets:
                        next_x, next_y = curr_x + off_x, curr_y + off_y

                        if (next_x, next_y) not in visited:
                            visited.add((next_x, next_y))
                            queue.append((next_x, next_y))

                steps += 1

        return bfs(x, y)