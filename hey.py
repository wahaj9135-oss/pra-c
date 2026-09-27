class family:
    def __init__(self, caste):
        self.caste = caste

class wahaj(family):
    def __init__(self, name, age, family_caste):
        self.name = name
        self.age = age
        super().__init__(family_caste)

f = wahaj("wahaj", 18, "syed")
print(f.name)
print(f.age)
print(f.caste)  
