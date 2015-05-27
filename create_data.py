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
person('Adriana',8,'Uni Münster')
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

uni('RWTH Aachen',100,[1,3,6,17])
uni('Uni Konstanz',17,[])
uni('Uni Düsseldorf',14,[])
uni('Uni Frankfurt',13,[])
uni('TU Dresden',11,[])
uni('FU Berlin',11,[])
uni('Uni Bonn',8,[])
uni('HU Berlin',8,[])
uni('CAU Kiel',7,[])
uni('Uni Würzburg',7,[])
uni('Uni Bochum',6,[])
uni('Uni Potsdam',6,[])
uni('TU Berlin',6,[])
uni('TU Ilmenau',5,[])
uni('Uni Münster',5,[])
uni('TU Dortmund',5,[])
uni('Uni Göttingen',4,[])
uni('Uni Siegen',4,[])
uni('TU Chemnitz',4,[])
uni('Uni Wuppertal',4,[])
uni('Uni Bremen',4,[])
uni('LMU München',4,[])
uni('Uni Regensburg',3,[])
uni('TU Braunschweig',3,[])
uni('Uni Freiburg',3,[])
uni('Uni Duisburg-Essen',3,[])
uni('Uni Jena',3,[])
uni('Uni Kassel',3,[])
uni('TU Darmstadt',3,[])
uni('Universität Bielefeld',3,[])
uni('KIT Karlsruhe',3,[])
uni('TU Kaiserslautern',3,[])
uni('Uni Heidelberg',3,[])
uni('Uni Rostock',2,[])
uni('Uni Wien',2,[])
uni('TU Freiberg',1,[])
uni('FAU Erlangen',1,[])
uni('Uni Oldenburg',1,[])
uni('TU München',1,[])

######################
###                ###
###   create ake   ###
###                ###
######################

# Beispiel:
# n = ak(halbleiter,leiter,name)

n = ak([3,4],3,'Ak Großveranstaltungen')
n = ak([],-1,'Ak Austausch')
n = ak([5,6],5,'AK Studienführer')
n = ak([5],5,'AK Vernetzung und Austausch der Orgas')
n = ak([7],7,'Bachelor-Master Lehramt in Baden-Württemberg (produktiv!)')
n = ak([8],8,'AK Frauenquote in der Physik')
n = ak([],-1,'Mitgliederversammlung ZaPF e.V.')
n = ak([9,10,11],9,'AK Bachelor-/Masterumfrage')
n = ak([],-1,'AK Lehramt')
n = ak([1,2],2,'AK GO- und Satzungsänderung')
n = ak([2],2,'AK Weiterentwicklung des Gremienworkshops')
n = ak([],-1,'Gremienworkshop')
n = ak([],-1,'Fokus auf mathematische Vorkenntnisse bzgl. Vorkurse')
n = ak([9,10],9,'Workshop Kompetenzorientierung')
n = ak([5],5,'AK CHE und Rankings allgemein')
n = ak([12],12,'AK Opa erzählt vom Krieg')
n = ak([2,12],2,'AK Promovierende')
n = ak([10,12,13],10,'AK Transparenz bei Drittmitteln')
n = ak([12,13],12,'AK Veröffentlichungspflicht')
n = ak([12,13],12,'AK Ethik in der Physik')
n = ak([12,14],14,'AK Gläserne Decke')

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
