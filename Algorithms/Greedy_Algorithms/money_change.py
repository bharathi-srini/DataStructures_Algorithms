# Uses python3
import sys

def safe_div(x,y):
    if y == 0:
        return 0
    return int(x / y)

def get_change(m):
    c10 = safe_div(m,10)
    if c10 == 0:
        c5 = safe_div(m,5)
    else:
        c5 = safe_div(m - (c10*10),5)
    c1 = m - (c10*10) - (c5*5)
    return c10 +c5 +c1

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(int(m)))
