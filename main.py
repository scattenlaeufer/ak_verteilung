__author__ = 'Simon'

import data
import timeslots
NO_SLOTS = 7
NO_ROOMS = 6


class Main(object):
    """Control class to coordinate data loading and start processes"""
    def __init__(self):
        self.data = data.Data()
        self.error = False

    def run(self, type):
        if not self.loaddata(type):
            print("Error in loading data")
            return False
        #self.data.save_data("unis")
        ts = timeslots.TimeSlots(7, 6)
        ts.distribute_rooms(self.data.unis.copy(), self.data.aks)
        ts.print_time_slot_map()
        ts.calculate_collisions(self.data.unis.copy())

    def loaddata(self, type):
        """Call loading processes for either json or txt files
        """
        try:
            if type == "json":
                self.data.read_json("aks", "aks_test.json")
                self.data.read_json("personen", "personen_test.json")
                self.data.read_json("unis", "unis_test.json")
            elif type == "txt":
                self.data.read_txt("aks", "aks.json")
                self.data.read_txt("personen", "personen.json")
                self.data.count_unis()
        except:
            return False
        return True


if __name__ == "__main__":
    run = Main()
    run.run("json")
