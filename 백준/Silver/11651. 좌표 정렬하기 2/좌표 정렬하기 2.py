N = int(input())
plots = [list(map(int, input().split() )) for i in range(N)]
sorted_plots = sorted(plots, key = lambda x: (x[1], x[0]))
for i in sorted_plots:
    print(*i)