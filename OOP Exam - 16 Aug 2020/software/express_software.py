from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, type, capacity_consumption, memory_consumption):
        super().__init__(type, "Express", capacity_consumption, int(memory_consumption * 2))
