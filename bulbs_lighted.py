import math

def light_bulbs(bulbs, persons):
    on = []
    off = []
    if bulbs == persons or persons > bulbs:
        for num in range(1, bulbs+1):
            sq = num**0.5
            if sq.is_integer():
                on.append(num)
            else:
                off.append(num)
             
    else:
        for num in range(1, bulbs+1):
            sq = num**0.5
            if sq.is_integer():
                if num <= persons:
                    on.append(num)
                else:
                    off.append(num)
            else:
                if num <= persons:
                    off.append(num)
                else:
                    on.append(num)
   
    print(f"Bulbs on are: {len(on)}")
    print(f"Bulbs off are: {len(off)}")   
          
            
light_bulbs(1000,1000)
light_bulbs(1000,100)
