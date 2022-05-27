class Student:
    school = "AkiraChix"
    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth
    
    def full_name(self):
        return f"Hello {self.name}."

    def greeting(self):
        return f"Hello {self.name} you were born in {self.year_of_birth}."

    def get_initials(self):
        initials = ""
        full_name = self.name.split()
        for name in full_name:
            initials += name[0].upper()
        return initials    