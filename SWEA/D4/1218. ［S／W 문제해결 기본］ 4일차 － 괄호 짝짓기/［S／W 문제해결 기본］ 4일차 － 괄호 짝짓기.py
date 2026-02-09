# import sys

# sys.stdin = open("input.txt" , 'r')

T = 10

for tc in range (1, T+1):
    str_len = int(input())
    str = input()
    stack = []
    answer = 1
    pair = {"(" : ")", "{" : "}", "[" : "]", "<" : ">"}

    for c in str:
        if c in "({[<":
            stack.append(c)
        
        if c in ")}]>":
            if not stack:
                answer = 0
                break

            left = stack.pop()
            if pair[left] != c:
                answer = 0
                break

    print(f'#{tc} {answer}')
