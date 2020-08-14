def staircase(n):
    for i in range(n):
        level = i+1
        print(' '*(n-level) + '#'*(level))

n = int(input())
staircase(n)
