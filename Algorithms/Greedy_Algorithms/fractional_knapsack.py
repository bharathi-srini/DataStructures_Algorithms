# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.0
    value_per_unit = [v / float(w) for w, v in zip(weights, values)]
    
    #uvw = zip(value_per_unit,values,weights)
    sort_index = reversed( [i[0] for i in sorted(enumerate(value_per_unit), key=lambda x:x[1])] )
    weights = [ weights[i] for i in sort_index ]
    sort_index = reversed( [i[0] for i in sorted(enumerate(value_per_unit), key=lambda x:x[1])] )
    values = [ values[i] for i in sort_index ]
    sort_index = reversed( [i[0] for i in sorted(enumerate(value_per_unit), key=lambda x:x[1])] )
    value_per_unit = [ value_per_unit[i] for i in sort_index ]
    
    for i in range(0,len(value_per_unit)):
        a = min( weights[i], capacity )
        capacity -= a
        value += a*value_per_unit[i]
        values[i] -= a

        if capacity == 0:
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
