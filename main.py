sayilar = [0,1,2,3,4,5,6,7,8,9]
process= True
for g in [value for value in sayilar if value not in [0]]:
    if process:
      for e in [value for value in sayilar if value not in [g]]:
          for r in [value for value in sayilar if value not in [g,e,0]]:
              for a in [value for value in sayilar if value not in [g,e,r]]:
                  for l in [value for value in sayilar if value not in [g,e,r,a]]:
                      for d in [value for value in sayilar if value not in [g,e,r,a,l,0]]:
                          for o in [value for value in sayilar if value not in [g,e,r,a,l,d]]:
                              for n in [value for value in sayilar if value not in [g,e,r,a,l,d,o]]:
                                  for b in [value for value in sayilar if value not in [g,e,r,a,l,d,o,n]]:
                                      for t in [value for value in sayilar if value not in [g,e,r,a,l,d,o,n]]:
                                          gerald = (100000 * g) + (10000 * e) + (1000 * r) + (100 * a) + (10 * l) + d
                                          donald = (100000 * d) + (10000 * o) + (1000 * n) + (100 * a) + (10 * l) + d
                                          robert = (100000 * r) + (10000 * o) + (1000 * b) + (100 * e) + (10 * r) + t
                                          if (gerald + donald == robert and len(set([g,e,r,a,l,d,o,n,b,t])) == 10):
                                              print("Gerald:", gerald)
                                              print("Donald:", donald)
                                              print("Robert:", robert)
                                              process = False
