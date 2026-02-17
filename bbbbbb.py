class Salomlashish:
    def __init__(self, ism, fam):
        self.__ism = ism
        self.__fam = fam

    def get_ism(self):
        return self.__ism

    def get_fam(self):
        return self.__fam

    def salom(self):
        print(f"Assalomu alaykum hurmatli {self.__ism} {self.__fam} jamoamizga xush kelibsiz")

salom1 = Salomlashish("Ali", "Valliev")
salom2 = Salomlashish("G'anijon", "Norimov")
salom3 = Salomlashish("Bobur", "Jovliyev")

print(salom1.get_ism())
print(salom2.get_fam())