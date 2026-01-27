class U3D:
    def __init__(self, w, h, l, p, e):
        self.w = w
        self.h = h
        self.l = l
        self.p = p
        self.e = e

    def inertia(self): # I = (W * H^3) / 12
        return (self.w * (self.h ** 3)) / 12
    
    def deflection(self): # D = (P * L^3) / (3 * E * I)
        return (self.p * self.l**3) / (3 * self.e * self.inertia())

    def bending_stress(self): # B = (P * L * H) / (2 * I)
        return self.p * self.l * self.h / (2 * self.inertia())


def main():
    w = float(input("Enter width of the beam (W): "))
    h = float(input("Enter height of the beam (H): "))
    l = float(input("Enter length of the beam (L): "))
    p = float(input("Enter force applied (P): "))
    e = float(input("Enter modulus of elasticity (E): "))

    beam = U3D(w, h, l, p, e)

    print("\n=== BEAM PROPERTIES ===")
    print(f"Moment of Inertia (I): {round(beam.inertia(), 2)}")
    print(f"Deflection (D): {round(beam.deflection(), 2)}")
    print(f"Bending Stress (B): {round(beam.bending_stress(), 2)}")

if __name__ == "__main__":
    main()

    