def merge_intervals(intervals):
    interval_dict = {x[0]:[] for x in intervals if x[1]>x[0]}

    for x in intervals:
        if x[1]>x[0]:
            interval_dict[x[0]].append(x[1])
        
    
    for k,v in interval_dict.items():
        interval_dict[k] = max(interval_dict[k])
    
    keys = sorted(interval_dict.keys(), reverse=False)

    j = 0
    for i in range(len(keys)):
        i = i - j
        x1 = keys[i]
        y1 = interval_dict[x1]
        if i<len(keys)-1:
            x2 = keys[i+1]
            y2 = interval_dict[x2]

            if x2 <= y1:
                interval_dict[x1] = max(y1, y2)
                del interval_dict[x2]
                keys.remove(x2)
                j+=1
        else:
            break


    result = [ (k,v) for k,v in interval_dict.items() ]



    return result




intervals = [(1, 1), 
            (-1, -1), 
            (0, 0), 
            (-2, 5), 
            (-5,-4), 
            (-3, 1), 
            (-2, 5), 
            (2, 6), 
            (-2, 0), 
            (-0.25, -0.25), 
            (-0.25, -0.25), 
            (0, 5), 
            (0, 5), 
            (1, 0)]

result = merge_intervals(intervals)
print(result)
# [(-5,-4), (-3, 6)]

