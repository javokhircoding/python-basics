from uuid import uuid4


class Avto:
    __num_avto = 0 
    def __init__(self, make, model, turi, rangi, narhi = None, km=0):
        self.make = make
        self.model = model
        self.turi = turi
        self.rangi = rangi
        self.__narhi = narhi
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1


    @classmethod
    def get_num_avto(cls):
        return f"Jami avtomobillar soni: {cls.__num_avto}"

    def get_info(self):
        return f"Ishlab chiqaruvchi: {self.make},Turi: {self.turi},Modeli: {self.model},Rangi: {self.rangi}"

    def get_km(self):
        return f"Avtomobil yurgani: {self.__km}"


    def get_id(self):
        return f"ID raqami: {self.__id}"


    def add_km(self, kml):
        if kml>0:
            self.__km += kml
        else:
            print("Yurgan masofani kamaytirib bo'lmaydi!")


car1 = Avto("Nissan", "r-34", "Sedan", "Ko'k", 200000, 1000)

info = car1.get_info()
print(info)

print(car1.get_id())
print(Avto.get_num_avto())