from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.hardware.hardware import Hardware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory = sum(h.memory for h in System._hardware)
        total_used_memory = sum([h.used_memory for h in System._hardware])

        total_capacity = sum(h.capacity for h in System._hardware)
        total_used_capacity = sum([h.used_capacity for h in System._hardware])

        return f"System Analysis\nHardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {total_used_capacity} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ""
        for har in System._hardware:
            result += f"Hardware Component - {har.name}\n"
            express_soft_c = [s for s in har.software_components if s.__class__.__name__ == "ExpressSoftware"]
            result += f"Express Software Components: {len(express_soft_c)}\n"
            light_soft_c = [li for li in har.software_components if li.__class__.__name__ == "LightSoftware"]
            result += f"Light Software Components: {len(light_soft_c)}\n"
            result += f"Memory Usage: {sum(s.memory_consumption for s in har.software_components)} / {har.memory}\n"
            result += f"Capacity Usage: {sum(s.capacity_consumption for s in har.software_components)} / {har.capacity}\n"
            result += f"Type: {har.type}\n"
            soft_names = ', '.join(s.name for s in har.software_components)
            result += f"Software Components: {soft_names if soft_names else None}"

        return result
