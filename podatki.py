#pridobivanje podatkov
import requests
import json

###prva vrjanta - anglezi -> ta ima več različnih imen :D
r=requests.get('https://randomuser.me/api/?inc=name,loc,email,dob,phone,location,picture,&nat=gb&results=2&noinfo&seed=tabor')


#druga varjana - slovenci
#r = requests.get('http://uinames.com/api/?region=slovenia&ext&amount=100')
podatki = r.json()
#preurejeno = {'osebe':[]}
sez=[]
js=podatki['results']
st = 1
for oseba in js:
    trenutni = dict()
    trenutni['model'] = "taborniki.Oseba"
    trenutni['pk']=st
    trenutni['fields']=dict()
    trenutni['fields']['ime']=oseba['name']['first']
    trenutni['fields']['priimek']=oseba['name']['last']
    trenutni['fields']['naslov']=oseba['location']['street'] + ', ' + oseba['location']['postcode']
    trenutni['fields']['rojstvo']=oseba['dob'][:10]
    trenutni['fields']['telefon']=oseba['phone']
    trenutni['fields']['email']=oseba['email']
    trenutni['fields']['slika'] = oseba['picture']['large']
    sez.append(trenutni)
    st += 1


    
print(sez)



with open('data.json', 'w') as f:
    json.dump(sez, f)

# Vsi podatki morajo biti zapakirani na zgornji način. Shranimo jih v json file v mapi fixtures. Potem ji poženemo z
#python3 manage.py loaddata imefila  --settings=TaborniskaBaza.settings_local


