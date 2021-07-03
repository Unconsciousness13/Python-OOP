class Smartphone:
    
    def __init__(self, memory: int, apps=[], is_on=False) -> None:
        self.apps = apps
        self.is_on = is_on
        self.memory = memory
        self.total_apps_count = 0

    def power(self):
        self.is_on = True
        return self.is_on

    def install(self, app, app_memory):
        if self.memory >= app_memory:
            if self.is_on == True:
                self.memory -= app_memory
                self.total_apps_count += 1
                return f"Installing {app}"
            return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {self.total_apps_count}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
