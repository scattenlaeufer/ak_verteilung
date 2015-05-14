__author__ = 'Simon'


class TimeSlots(object):
    def __init__(self, slots, rooms):
        self.slots = list()
        for s in range(0, slots):
            self.slots.append(list())
            for r in range(0, rooms):
                self.slots[s].append("s%ir%i" % (s+1, r+1))
        self.akpunkte = dict()
        self.aks = dict()
        self.no_rooms = rooms
        self.no_slots = slots
        self.ak_wishes = dict()

    def distribute_rooms(self, unis, aks):
        self.aks = aks.copy()
        for k in aks.keys():
            self.ak_wishes[str(k)] = list()
        room = 0
        slot = 0
        self.akpunkte = dict()
        for uni in unis:
            index = 0
            for wish in unis[uni]["Wünsche"]:
                ak_id = wish  #0 is top wish left
                punkte = self.no_slots - unis[uni]["Anzahl"] - (index - 1)
                self.ak_wishes[str(ak_id)].append((uni, punkte))
                self.akpunkte[ak_id] = int(self.akpunkte.get(ak_id, 0) + punkte)
                index += 1
        while len(self.akpunkte) > 0:
            top_score_akid = keywithmaxval(self.akpunkte)
            self.slots[slot][room] = str(top_score_akid)
            self.akpunkte.pop(top_score_akid)
            slot += 1
            if slot >= self.no_slots:
                slot %= self.no_slots
                room += 1
            if room >= self.no_rooms:
                write_to_file("rooms_full.log", "All rooms full")
                write_to_file("rooms_full.log", "%i left groups:" % len(self.akpunkte))
                write_to_file("rooms_full.log", "%s" % self.akpunkte)
                return

    def print_time_slot_map(self):
        print("",end="\t")
        for i in range(1, self.no_rooms+1):
            print("Room%i" % i, end="\t")
        print()
        for index, slot in enumerate(self.slots):
            print("Slot%i" % (index+1), end="\t")
            for room in slot:
                print(room, end="\t")
            print()

    def calculate_collisions(self, unis):
        for slot in self.slots:
            uni_in_slot = dict()
            collisions = 0
            for ak in slot:
                uni_in_ak = set()
                if ak.startswith("s"):
                    write_to_file("debug.log", "empty room %s" % ak)
                else:
                    for uni in self.ak_wishes[str(ak)]:
                        if uni[0] in uni_in_ak:
                            continue
                        if uni[0] in uni_in_slot and uni[0] not in uni_in_ak:
                            uni_in_slot[uni[0]] += 1
                            if uni_in_slot[uni[0]] > unis[uni[0]]["Anzahl"]:
                                collisions += 1
                                write_to_file("problems.txt", "%s can't participate in ak %s" % (uni[0], ak))
                            uni_in_ak.add(uni[0])
                            write_to_file("participation.log", "%s participates in\t%s" % (uni[0], ak))

                        else:
                            uni_in_ak.add(uni[0])
                            uni_in_slot[uni[0]] = 1
                            write_to_file("participation.log", "%s participates in\t%s" % (uni[0], ak))
            write_to_file("participation.log", "##########NEXT SLOT#############")
            write_to_file("collisions.log", "%i collisions in slot %s" % (collisions, slot))
        return


def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
    b) return the key with the max value"""
    k = list(d.keys())
    v = list(d.values())
    return k[v.index(max(v))]


def write_to_file(filename, string):
    f = open(filename, "a")
    string = string.rstrip("\n")
    f.write(string + "\n")
    f.close()