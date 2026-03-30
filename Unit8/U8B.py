# CEET252 - Python U8A template
import math

class Projectile:

    def __init__(self, Velocity:float, Angle:float, t:float = 0, g:float = 9.80665):
        # i use type hints here for enhanced definition
        # otherwise t would return an int error.

        # define first 3 __init__ attributes here ...
        self.velocity = Velocity
        self.angle_deg = Angle
        self.time = t
        self.g = g
        self.rad = math.radians(Angle)

        # all calculations are done here
        self.v_xo = Velocity * math.cos(self.rad)
        self.v_yo = Velocity * math.sin(self.rad)
        self.flight_time = (2 * Velocity * math.sin(self.rad)) / g

    def destination(self):

        global ihv, ivv # global variables to store inithv and initvv for use in at_t method

        ihv = self.v_xo
        ivv = self.v_yo
        flight_time = (2 * ivv) / self.g

        print("----------------------------------------------------------------")
        print("Converting Angle to Radians:")
        print(f"- The Angle in Radians is = {self.rad:.2f} Rad")

        print("-----------------------------------------------------------------")
        print("Calculating values of initial Vertical, Horizontal Velocity, and Time of flight:")
        print(f"- Initial Horizontal Velocity Vxo = {ihv:.2f} m/s")
        print(f"- Initial Vertical Velocity Vyo = {ivv:.2f} m/s")
        print(f"- The Time of Flight = {flight_time:.2f} seconds")
        print(f"- Given value of g = {self.g} m/s^2")
        print("-----------------------------------------------------------------")
        return self

    def at_t(self):

        print(f"- @ Time of t = {self.time:.2f} seconds")
        h_d = ihv * self.time
        v_d = ivv * self.time - 0.5 * self.g * self.time**2
        v_v = ivv - self.g * self.time

        print(f"- The Horizontal Distance is = {h_d:.2f} m")
        print(f"- The Vertical Distance is = {v_d:.2f} m")
        print(f"- The Vertical Velocity is = {v_v:.2f} m/s")
        print("-----------------------------------------------------------------")
        return self

# pass the attributes, initial velocity, angle in degree, time-of-interest, and
# gravitation constant (default is given as g = 9.80665)
def main():
    p1 = Projectile(40, 60, 0.5).destination()
    p2 = Projectile(40, 60, 0.5).at_t()

if __name__ == "__main__":
    main()