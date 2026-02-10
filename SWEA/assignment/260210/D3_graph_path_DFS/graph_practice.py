#import sys

#sys.stdin = open("sample_input.txt", "r")

T = int(input())

def dfs(current, goal):
    if current == goal:
        return 1
    stack[current] = True
    for next in graph.get(current, []):
        if not stack[next]:
            if dfs(next, goal):
                return 1
    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}

    for _ in range(E):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

    # print(graph)
    S, G = map(int, input().split())
    stack = [0] * (V + 1)
    answer = dfs(S,G)
    # print(answer)

    print(f'#{tc} {answer}')