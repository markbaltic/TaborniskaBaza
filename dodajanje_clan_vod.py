from taborniki.models import Oseba, Vod

from random import randint, shuffle

#naredimo seznam - st. clanov v i-tem vodu
clanov_v_vodu = [15]*24

while sum(clanov_v_vodu) != 150:
    i = randint(0,len(clanov_v_vodu)-1)
    if clanov_v_vodu[i] > 3:
        clanov_v_vodu[i] -= 1


osebe = Oseba.objects.all()
osebe = iter(osebe)


for i in range(24):
    for j in range(0,clanov_v_vodu[i]):
        oseba = next(osebe)
        oseba.vod = Vod.objects.get(id=5000+i)
        oseba.save()



