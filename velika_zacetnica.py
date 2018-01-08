from taborniki.models import Oseba, Vod, Rod

osebe = Oseba.objects.all()
vodi = Vod.objects.all()
rodi = Rod.objects.all()



for oseba in osebe:
    oseba.ime = oseba.ime.title()
    oseba.priimek = oseba.priimek.title()
    oseba.save()

for vod in vodi:
    vod.imeVod = vod.imeVod.title()
    vod.save()

for rod in rodi:
    rod.imeRod = rod.imeRod.upper()
    rod.sedez = rod.sedez.title()
    rod.save()





