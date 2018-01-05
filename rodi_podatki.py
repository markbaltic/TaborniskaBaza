import json

rod1 = {"imeRod":"rkj", "sedez":"sezana"}
rod2 = {"imeRod":"ror", "sedez":"komen"}
rod3 = {"imeRod":"rcb", "sedez":"divaca"}


# sez_vodov = [vod1, vod2, vod3, vod4, vod5, vod6, vod7, vod8, vod9, vod9, vod10,  vod10, vod11, vod12]
# i = 1
# for el in sez_vodov:
#     while True:
#
#         el["clani"].append(i)
#         if i<=10 or (i%10 != 0):
#             i += 1
#             continue
#         else:
#             i += 1
#             break


polni_rodi = [rod1, rod2, rod3]

st=1000
sez = []
for rod in polni_rodi:
    trenutni = dict()
    trenutni['model'] = "taborniki.Rod"
    trenutni['pk']=st
    trenutni['fields']=rod

    sez.append(trenutni)
    st += 1

with open('rodi.json', 'w') as f:
    json.dump(sez, f)