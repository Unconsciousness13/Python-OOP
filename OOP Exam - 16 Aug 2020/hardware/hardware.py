class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if software.capacity_consumption <= self.capacity_available \
                and software.memory_consumption <= self.memory_available:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def used_memory(self):
        return sum(s.memory_consumption for s in self.software_components)

    @property
    def memory_available(self):
        return self.memory - self.used_memory

    @property
    def used_capacity(self):
        return sum(c.capacity_consumption for c in self.software_components)

    @property
    def capacity_available(self):
        return self.capacity - self.used_capacity
