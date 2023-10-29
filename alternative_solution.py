sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_solution():
    for g in sayilar[1:]:
        for e in [x for x in sayilar if x != g]:
            for r in [x for x in sayilar if x not in [g, e, 0]]:
                for a in [x for x in sayilar if x not in [g, e, r]]:
                    for l in [x for x in sayilar if x not in [g, e, r, a]]:
                        for d in [x for x in sayilar if x not in [g, e, r, a, l, 0]]:
                            for o in [x for x in sayilar if x not in [g, e, r, a, l, d]]:
                                for n in [x for x in sayilar if x not in [g, e, r, a, l, d, o]]:
                                    for b in [x for x in sayilar if x not in [g, e, r, a, l, d, o, n]]:
                                        for t in [x for x in sayilar if x not in [g, e, r, a, l, d, o, n, b]]:
                                            gerald = (100000 * g) + (10000 * e) + (1000 * r) + (100 * a) + (10 * l) + d
                                            donald = (100000 * d) + (10000 * o) + (1000 * n) + (100 * a) + (10 * l) + d
                                            robert = (100000 * r) + (10000 * o) + (1000 * b) + (100 * e) + (10 * r) + t
                                            if len(set([g, e, r, a, l, d, o, n, b, t])) == 10 and gerald + donald == robert:
                                                return gerald, donald, robert
    return None, None, None

gerald, donald, robert = find_solution()
if gerald is not None:
    print("Gerald:", gerald)
    print("Donald:", donald)
    print("Robert:", robert)
