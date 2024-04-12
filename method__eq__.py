class Building:
    def __init__(self, number_of_floors = 10, building_type = ""):
        self.number_of_floors = number_of_floors
        self.building_type = building_type

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and self.building_type == other.building_type



building_1 = Building(5, "castle")
building_2 = Building(5, "castle")

print(building_1 == building_2)
print()



castle = Building(5, "castle")
flat = Building("flat", 6)
app = Building(6, "flat")

print(castle == flat)
print(app == flat)




