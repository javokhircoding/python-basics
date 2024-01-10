class Shaxs:
    odamlar_soni = 0 
    def __init__(self,ism,familiya,id):
        self.ism = ism
        self.familiya = familiya
        self.id = id
        Shaxs.odamlar_soni += 1

    def get_name(self):
        return f"Ismi: {self.ism}"


    def get_lastname(self):
        return f"Familiyasi: {self.familiya}"

    def get_id(self):
        return f"Id raqami: {self.id}"

    @classmethod
    def get_num(cls):
        return cls.odamlar_soni




class Talaba(Shaxs):
    talabalar_soni = 0 
    def __init__(self,ism,familiya,id,talaba_id):
        super().__init__(ism,familiya,id)
        self.talaba_id = talaba_id
        Talaba.talabalar_soni += 1



    def get_t_id(self):
        return f"Talaba ID'si: {self.talaba_id}"
        Talaba.talabalar_soni += 1




    def get_info(self):
        return f"Ismi: {self.ism}, Familiyasi: {self.familiya}, Passport Raqami: {self.id}, Talaba ID'si: {self.talaba_id}"


    @classmethod 
    def get_num_talaba(cls):
        return f"Talabalar soni: {cls.talabalar_soni}"


talaba1 = Talaba("javohir", "shermatov", "aafuckoff", "aafuckoff2")
print(talaba1.get_info())