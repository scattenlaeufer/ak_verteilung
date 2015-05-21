#!/usr/bin/python

import json

###################
###             ###
###   utils 1   ###
###             ###
###################

def person(name,pid,uni):
    pid = '{0:0>3}'.format(pid)
    for n,p in persons.items():
        #print(p)
        if pid == p['Person-ID']:
            print('du bist zu doof eine eindeutige ID für {} zu erstellen!'.format(name))
            exit()
    person = {'Person-ID':pid,'Uni':uni}
    persons[name] = person

persons = {}

def uni(name,anzahl,wuensche):
    uni = {'Anzahl':anzahl,'Wünsche':wuensche}
    unis[name] = uni

unis = {}

def ak(halbleiter=[],leiter=-1,name=''):
    ak = {"Halbleiter":halbleiter, "Leiter":leiter, "Name":name}
    aks[n] = ak
    return n +1

aks = {}
n = 1

##########################
###                    ###
###   create persons   ###
###                    ###
##########################

# Beispiel:
# person(name,id,uni)

person('Guth, Björn',1,'RWTH Aachen')
person('Behrmann, Jörg',2,'FU Berlin')
person('Philipp',3,'TU Kaiserslautern')
person('Marcus',4,'Uni Frankfurt')
person('Niklas',5,'Uni Konstanz')
person('Jannis',6,'Uni Bremen')
person('Thomi',7,'Uni Heidelberg')
person('Adriana',8,'WWU Münster')
person('Margret',9,'LMU München')
person('Daniela',10,'Uni Frankfurt')
person('Zafer',11,'Uni Potsdam')
person('Opa',12,'FU Berlin')
person('Falck, Timo',13,'RWTH Aachen')
person('Mascha',14,'TU Berlin')

#######################
###                 ###
###   create unis   ###
###                 ###
#######################

# Beispiel:
# uni(uni,anzahl,wünsche)

uni('RWTH Aachen',300,[1,3,6,17])
uni('FU Berlin',3,[2,4,7,15])

######################
###                ###
###   create ake   ###
###                ###
######################

# Beispiel:
# n = ak(halbleiter,leiter,name)

n = ak(['003','004'],-1,'Ak Großveranstaltungen')
n = ak([],-1,'Ak Austausch')
n = ak(['005','006'],-1,'AK Studienführer')
n = ak(['005'],-1,'AK Vernetzung und Austausch der Orgas')
n = ak(['007'],-1,'Bachelor-Master Lehramt in Baden-Württemberg (produktiv!)')
n = ak(['008'],-1,'AK Frauenquote in der Physik')
n = ak([],-1,'Mitgliederversammlung ZaPF e.V.')
n = ak(['009','010','011'],-1,'AK Bachelor-/Masterumfrage')
n = ak([],-1,'AK Lehramt')
n = ak(['001','002'],-1,'AK GO- und Satzungsänderung')
n = ak(['002'],-1,'AK Weiterentwicklung des Gremienworkshops')
n = ak([],-1,'Gremienworkshop')
n = ak([],-1,'Fokus auf mathematische Vorkenntnisse bzgl. Vorkurse')
n = ak(['009','010'],-1,'Workshop Kompetenzorientierung')
n = ak(['005'],-1,'AK CHE und Rankings allgemein')
n = ak(['012'],-1,'AK Opa erzählt vom Krieg')
n = ak(['002','012'],-1,'AK Promovierende')
n = ak(['010','012','013'],-1,'AK Transparenz bei Drittmitteln')
n = ak(['012','013'],-1,'AK Veröffentlichungspflicht')
n = ak(['012','013'],-1,'AK Ethik in der Physik')
n = ak(['012','014'],-1,'AK Gläserne Decke')

###################
###             ###
###   utils 2   ###
###             ###
###################

def create_json(dictionary,file_name):
    json_out = json.dumps(dictionary,sort_keys=True,ensure_ascii=False,indent=4)
    print('writing {}'.format(file_name))
    with open(file_name,'w') as json_file:
        json_file.write(json_out)

create_json(persons,'personen_test.json')
create_json(unis,'unis_test.json')
create_json(aks,'aks_test.json')