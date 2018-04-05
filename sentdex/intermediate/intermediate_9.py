CORRECTE_COMBO = (4, 7, 9)
combo_gevonden = False
# 
# for c1 in range(10):
#     if combo_gevonden:
#         break
#     for c2 in range(10):
#         if combo_gevonden:
#             break
#         for c3 in range(10):
#             if combo_gevonden:
#                 break
#             if (c1, c2, c3) == CORRECTE_COMBO:
#                 print('Combo gevonden: {}'.format((c1,c2,c3)))
#                 combo_gevonden = True
#             print(c1,c2,c3)
from l import CORRECTE_COMBO
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
              yield (c1, c2 , c3)
for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECTE_COMBO:
        print('Combi gevonden: {}'.format((c1,c2,c3)))
        break