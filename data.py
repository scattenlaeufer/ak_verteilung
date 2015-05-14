__author__ = 'Simon'

import json
import random


class Data(object):
    """Class data holds information about persons and working groups

    aks is a dictionary with ID(key) and dict(value)
        dict is dictionary Name|Leiter|Halbleiter and str|int|[int]
    personen is a dictionary with name(key) and dict(value)
        dict is dictionary Person-ID|Uni(key) and int|str(value)
    unis is a dictionary with name of university(key) and dict(value)
        dict is dictionary Anzahl|Wünsche(key) int|[int](value)
    """
    def __init__(self):
        self.personen = dict()
        self.aks = dict()
        self.unis = dict()

    def read_json(self, dictionary, filename):
        """Reads JSON files into dict

         dictionary can either be "personen" or "aks" or "unis"
         filename to read
         """
        f = open(filename, "r", encoding="utf-8")
        if dictionary == "personen":
            self.personen = json.load(f)
        elif dictionary == "aks":
            self.aks = json.load(f)
        elif dictionary == "unis":
            self.unis = json.load(f)
        else:
            print("Dictionary %s not found" % dictionary)

    def read_txt(self, dictionary, filename):
        """Reads tab delimited text files into dict

         dictionary can either be "personen" or "aks"
         filename to read
         """
        f = open(filename, "r", encoding="utf-8")
        if dictionary == "personen":
            for line in f.readlines():
                line = line.rstrip("\n")
                line_ar = line.split("\t")
                uni, key, ID = line_ar[0], line_ar[1], line_ar[2]
                if key == "Name":
                    pass
                else:
                    self.personen[key] = {"Person-ID": ID, "Uni": uni}
        elif dictionary == "aks":
            for line in f.readlines():
                line = line.rstrip("\n")
                key, value = line.split("\t")
                if value == "ID":
                    pass
                else:
                    self.aks[int(value)] = {"Name": key, "Leiter": -1, "Halbleiter": []}
        elif dictionary == "uni":
            pass
        else:
            print("Dictionary %s not found" % dictionary)

    def save_data(self, dictionary):
        """Save data into JSON file "personen.json" or "aks.json" or "unis.json" """
        if dictionary == "personen" and len(self.personen) > 0:
            f = open("personen.json", "w", encoding="utf-8")
            f.write(json.dumps(self.personen, sort_keys=True, indent=4, separators=(',', ':')))
        elif dictionary == "aks" and len(self.aks) > 0:
            f = open("aks.json", "w", encoding="utf-8")
            f.write(json.dumps(self.aks, sort_keys=True, indent=4, separators=(',', ':')))
        elif dictionary == "unis" and len(self.unis) > 0:
            f = open("unis.json", "w", encoding="utf-8")
            f.write(json.dumps(self.unis, sort_keys=True, indent=4, separators=(',', ':')))
        else:
            print("Fehler")

    def count_unis(self):
        """Count participants grouped by university/fachschaft"""
        uni = dict()
        for key in self.personen:
            if self.personen[key]["Uni"] in uni:
                uni[self.personen[key]["Uni"]]["Anzahl"] += 1
            else:
                uni[self.personen[key]["Uni"]] = {"Anzahl": 1}
            #uni[self.personen[key]["Uni"]]["Wünsche"] = list()
            randomlist = []
            for index in range(0, 10 + int(random.random()*10)):
                randomlist.append(random.randint(1, len(self.aks)))
            uni[self.personen[key]["Uni"]]["Wünsche"] = randomlist
        self.unis = uni


if __name__ == "__main__":
    md = Data()
    md.read_txt("aks", "planung.csv")
    md.save_data("aks")
    md.read_txt("personen", "personen.csv")
    md.save_data("personen")
    md.count_unis()
    md.save_data("unis")
    print(md.unis)
