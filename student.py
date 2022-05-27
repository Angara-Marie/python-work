class Student:
    school = "AkiraChix"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def full_name(self):
        return f"Hello {self.name}."

    def year_of_birth(self):
        year = 2022 - self.age
        return f"Hello {self.name} you were born in {year}."

    def get_initials(self):
        initials = ""
        full_name = self.name.split()
        for name in full_name:
            initials += name[0].upper()
        return initials    