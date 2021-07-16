from project.dvd import DVD
from project.custоmer import Customer


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer.id == customer_id]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id]

        dvd = dvd[0]
        customer = customer[0]
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return f"DVD is already rented"
        elif dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [customer for customer in self.customers if customer.id == customer_id]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id]

        customer = customer[0]
        dvd = dvd[0]
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for i in range(len(self.customers)):
            result += f"{self.customers[i]}\n"
        for i in range(len(self.dvds)):
            result += f"{self.dvds[i]}\n"
        return result
