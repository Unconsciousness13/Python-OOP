class Bunker:
    def __init__(self, ):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supplies = [x for x in self.supplies if x == "FoodSupplies"]
        if food_supplies:
            return food_supplies
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        water_supplies = [w for w in self.supplies if w == "WaterSupplies"]
        if water_supplies:
            return water_supplies
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        painkillers_meds = [p for p in self.medicine if p == "Painkillers"]
        if painkillers_meds:
            return painkillers_meds
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        salves_meds = [s for s in self.medicine if s == "Salves"]
        if salves_meds:
            return salves_meds
        raise IndexError("There are no salves left!")

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError("Survivor with name {name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        med_for_rem = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
        if survivor.needs_healing:
            self.medicine.remove(med_for_rem)
            med_for_rem.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        supply_for_rem = [m for m in self.supplies if m.__class__.__name__ == sustenance_type][-1]
        if survivor.needs_sustenance:
            self.supplies.remove(supply_for_rem)
            supply_for_rem.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
