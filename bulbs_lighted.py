def light_bulbs(bulbs, persons):
    on = []
    off = []
    
    for num in range(1, bulbs+1):
            lst = []
            for x in range(1, num+1):
                if num%x == 0 and x<=persons:
                    lst.append(x)
            if (len(lst)) % 2 == 0:
                off.append(num)
            else:
                on.append(num)
                
    print(f"Bulbs on are: {len(on)}")
    print(f"Bulbs off are: {len(off)}")   

light_bulbs(1000,100)
