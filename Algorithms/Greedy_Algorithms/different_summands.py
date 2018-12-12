# Uses python3
import sys

def optimal_summands(n):
    summands = [] 
    k = n 
    m = 1

    if n == 2 or n == 1:
        summands.append(n)
    else:
        for i in range(1,k):
            if k <= 2*m:
                summands.append(k)
                break
            else:
                summands.append(m)
                k = k - m
                m = m + 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
