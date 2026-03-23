class UnitConversion:
    def __init__(self, x):
        self.x = x

    def f_c(self) -> float:
        return (self.x - 32) / (9/5)

    def c_f(self) -> float:
        return (self.x * (9/5)) + 32

    def lbs_kg(self) -> float:
        return self.x * 0.453592

    def kg_lbs(self) -> float:
        return self.x / 0.453592

val = UnitConversion(50)
print(format(val.f_c(), '.3f'))
print(format(val.c_f(), '.3f'))
print(format(val.lbs_kg(), '.3f'))
print(format(val.kg_lbs(), '.3f'))
