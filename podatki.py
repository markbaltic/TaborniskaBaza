#pridobivanje podatkov
import requests
import json

###prva vrjanta - anglezi -> ta ima več različnih imen :D
r=requests.get('https://randomuser.me/api/?inc=name,loc,email,dob,phone,location,&nat=gb&results=2&noinfo&seed=tabor')


#druga varjana - slovenci
#r = requests.get('http://uinames.com/api/?region=slovenia&ext&amount=100')
podatki = r.json()
#preurejeno = {'osebe':[]}
sez=[]
js=podatki['results']
for oseba in js:
    trenutni = dict()
    trenutni['ime']=oseba['name']['first']
    trenutni['priimek']=oseba['name']['last']
    trenutni['naslov']=oseba['location']['street'] + ', ' + oseba['location']['postcode']
    trenutni['rojstvo']=oseba['dob'][:10]
    trenutni['telefon']=oseba['phone']
    trenutni['email']=oseba['email']
    sez.append(trenutni)


    
print(sez)



with open('data.json', 'w') as f:
    json.dump(sez, f)



