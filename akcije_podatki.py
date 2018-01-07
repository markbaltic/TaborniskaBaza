import json
from datetime import datetime
import random

def make_dates():
    year = random.randint(2000,2017)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    start = str(year)+'-'+ str(month)+'-'+str(day)
    end = str(year)+'-'+ str(month)+'-'+str(day+1)
    return(start,end)

datum1 = make_dates()
a1 = {"imeAkcija" : "Izlet v Ljubljano",
    "porocilo" : "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa." \
                 " Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu",
    "zacetek" : datum1[0],
    "konec" : datum1[1],
      "organizator" : 101}

datum2 = make_dates()
a2 = {"imeAkcija" : "Izlet v Maribor",
    "porocilo" : "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam" \
                 " rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta.",
    "zacetek" : datum2[0],
    "konec" : datum2[1],
      "organizator" : 102}

datum3 = make_dates()
a3 = {"imeAkcija" : "Izlet v London",
    "porocilo" : "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born" \
                 " and I will give you a complete account of the system, and expound the actual teachings of the gre",
    "zacetek" : datum3[0],
    "konec" : datum3[1],
      "organizator" : 103}

datum4 = make_dates()
a4 = {"imeAkcija" : "Izlet v Moskvo",
    "porocilo" : "Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica," \
                 " sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pro",
    "zacetek" : datum4[0],
    "konec" : datum4[1],
      "organizator" : 104}

datum5 = make_dates()
a5 = {"imeAkcija" : "Izlet v Divačo",
    "porocilo" : "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the" \
                 " blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large.",
    "zacetek" : datum5[0],
    "konec" : datum5[1],
      "organizator" : 105}

datum6 = make_dates()
a6 = {"imeAkcija" : "Izlet v Komen",
    "porocilo" : "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which" \
                 " I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was.",
    "zacetek" : datum6[0],
    "konec" : datum6[1],
      "organizator" : 106}

datum7 = make_dates()
a7 = {"imeAkcija" : "Izlet v Honolulu",
    "porocilo" : "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into" \
                 " a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could se",
    "zacetek" : datum7[0],
    "konec" : datum7[1],
      "organizator" : 107}

polne_akcije = [a1,a2,a3,a4,a5,a6,a7]

st=1
sez = []
for akcija in polne_akcije:
    trenutni = dict()
    trenutni['model'] = "taborniki.Akcije"
    trenutni['pk']=st
    trenutni['fields']=akcija

    sez.append(trenutni)
    st += 1



with open('akcije.json', 'w') as f:
    json.dump(sez, f)





