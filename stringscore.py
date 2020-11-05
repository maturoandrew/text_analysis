def clean_strings(a):
    punc = ["'", ",", ".", "!", "?", "<", ">", "[", "]", "-", "_", "=", "+"]
    for q in punc:
        a = a.replace(q, '')
    a = a.lower().split(' ')
    return a

def set_avg_similarity(a, b):
    a = set(a)
    b = set(b)
    x = len(a.intersection(b))*1.0 / len(a)
    y = len(b.intersection(a))*1.0 / len(b)
    z = (x + y)/2
    return z

def len_comp(a, b):
    # should probably use a norm instead but would need more testing
    x = abs(len(a) - len(b)) * 1.0 / (len(a) + len(b))
    return 1-x

def conv_dict(a, keys=None):
    if keys == None:
        x = {i : a[i] for i in range(len(a))}
    else:
        x = {keys[i]: a[i] for i in range(len(keys))}
    return x

def getkeys(dict, search_val):
    keys = list()
    items = dict.items()
    for item in items:
        if item[1] == search_val:
            keys.append(item[0])
    return keys

def dual_dict_pop(dicta, dictb, tup):
    for i in range(tup[0], tup[0]+tup[2]):
        dicta.pop(i)
    for i in range(tup[1], tup[1]+tup[2]):
        dictb.pop(i)
    return dicta, dictb

def subset_comp(a, b, a_keys=None, b_keys=None):
    biggest_overlap = 0
    final_tup = (-1,-1,-1)
    overlap = set(a).intersection(set(b))
    a = conv_dict(a, a_keys)
    b = conv_dict(b, b_keys)

    for x in overlap:
        overlap_a = getkeys(a, x)
        overlap_b = getkeys(b, x)
        for i in overlap_a:
            for j in overlap_b:
                if a[i] == b[j]:
                    for k in range(1, max(len(a), len(b))):
                        try:
                           if a[i+k] == b[j+k]:
                                if k >= biggest_overlap:
                                    biggest_overlap = k + 1
                                    final_tup = (i,j,k+1)
                           else:
                                break
                        except:
                            break
    a, b = dual_dict_pop(a,b,final_tup)
    a_keys = list(a.keys())
    a = list(a.values())
    b_keys = list(b.keys())
    b = list(b.values())
    return a, a_keys, b, b_keys, final_tup, biggest_overlap

def cycle_subset(a,b,final_tuple=(0,0,0), a_keys=None, b_keys=None):
    running_total = 0
    while final_tuple != (-1,-1,-1):
        a,a_keys, b, b_keys, final_tuple,biggest_overlap = subset_comp(a,b, a_keys, b_keys)
        running_total += biggest_overlap
    return running_total

def compare(a, b):
    a = clean_strings(a)
    b = clean_strings(b)
    avg_length = (len(a) + len(b)) *1.0 /2
    set_sim = set_avg_similarity(a, b)
    #print('set sim is: ' + str(set_sim))

    len_sim = len_comp(a, b)
    #print('len sim is: ' + str(len_sim))

    if len(a) == 1 and len(b) == 1 and a == b:
        subset_sim = 1
        #print('subset sim is: ' + str(subset_sim))
    elif (len(a) == 1 and a[0] in b) or (len(b) == 1 and b[0] in a):
        subset_sim = cycle_subset(a, b)
        subset_sim = (subset_sim + 1)/avg_length
        #print('subset sim is: ' + str(subset_sim))
    else:
        subset_sim = cycle_subset(a, b)
        subset_sim = subset_sim/avg_length
        #print('subset sim is: ' + str(subset_sim))

    set_weight = .3
    len_weight = .0
    subset_weight = .7
    cum_score = set_weight * set_sim + len_weight * len_sim + subset_weight * subset_sim
    #print(cum_score)
    return cum_score


# in this scenario a typo constitutes a different word
# wanted all metrics to be symmetric.
