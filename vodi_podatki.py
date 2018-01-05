import json

vod1 = {"imeVod":"zajcki", "rod":1000 ,"druzina":"mc"}
vod2 = {"imeVod":"pingvini", "rod":1000 ,"druzina":"mc"}
vod3 = {"imeVod":"cebelice", "rod":1000 ,"druzina":"mc"}
vod4 = {"imeVod":"krokodili", "rod":1000 ,"druzina":"mc"}

vod5 = {"imeVod":"medvedi", "rod":1000 ,"druzina":"gg"}
vod6 = {"imeVod":"svizci", "rod":1000 ,"druzina":"gg"}
vod7 = {"imeVod":"čmrlji", "rod":1000 ,"druzina":"gg"}
vod8 = {"imeVod":"labodi", "rod":1000 ,"druzina":"gg"}

vod9 = {"imeVod":"polhi", "rod":1000 ,"druzina":"pp"}

vod10 = {"imeVod":"meduze", "rod":1000 ,"druzina":"rr"}

vod11 = {"imeVod":"ovce", "rod":1000 ,"druzina":"grce"}

vod12 = {"imeVod":"neuvrsceni", "rod":1000,"druzina":"neuvrsceni"}

#----------------
vodI1 = {"imeVod":"koze", "rod":1001 ,"druzina":"mc"}
vodI2 = {"imeVod":"metulji", "rod":1001 ,"druzina":"mc"}

vodI3 = {"imeVod":"kamele", "rod":1001 ,"druzina":"gg"}
vodI4 = {"imeVod":"konji", "rod":1001 ,"druzina":"gg"}

vodI5 = {"imeVod":"orangutani", "rod":1001 ,"druzina":"pp"}

vodI6 = {"imeVod":"mravlje", "rod":1001 ,"druzina":"grce"}

vodI7 = {"imeVod":"neuvrsceni", "rod":1001,"druzina":"neuvrsceni"}

#-----------------------
vodII1 = {"imeVod":"ribe", "rod":1002 ,"druzina":"mc"}

vodII2 = {"imeVod":"pajki", "rod":1002 ,"druzina":"gg"}

vodII3 = {"imeVod":"hrosci", "rod":1002 ,"druzina":"pp"}

vodII4 = {"imeVod":"kure", "rod":1002 ,"druzina":"grce"}

vodII5 = {"imeVod":"neuvrsceni", "rod":1002,"druzina":"neuvrsceni"}


polni_vodi = [vod1, vod2, vod3, vod4, vod5, vod6, vod7, vod8, vod9, vod10, vod11, vod12, vodI1, vodI2, vodI3, vodI4, vodI5, vodI6, vodI7,
              vodII1, vodII2, vodII3, vodII4, vodII5]

st=5000
sez = []
for vod in polni_vodi:
    trenutni = dict()
    trenutni['model'] = "taborniki.Vod"
    trenutni['pk']=st
    trenutni['fields']=vod

    sez.append(trenutni)
    st += 1



with open('vodi.json', 'w') as f:
    json.dump(sez, f)
