from collections import deque
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def move_population(union_list):
    for union in union_list:
        total = 0
        for country in union:
            x, y = country
            total += board[x][y]

        population = total // len(union)

        for country in union:
            x, y = country
            board[x][y] = population


def find_union(x, y):
    q = deque()
    q.append((x, y))
    union = []
    union.append((x, y))
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                if L <= abs(board[cx][cy] - board[nx][ny]) <= R:
                    union.append((nx, ny))
                    visited.add((nx, ny))
                    q.append((nx, ny))
    if len(union) > 1:
        union_list.append(union)


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]



answer = 0

while True:
    union_list = []
    visited = set()
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited:
                visited.add((i, j))
                find_union(i, j)
    if union_list:
        move_population(union_list)
        answer += 1
    else:
        break

print(answer)