import math

class U6D:

    @staticmethod
    def projectile_motion(velocity:float, angle:float):
        gravity = 9.80665

        rad = math.radians(angle)
        v_xo = velocity * math.cos(math.radians(angle))
        v_yo = velocity * math.sin(math.radians(angle))
        flight_time = 2*velocity*math.sin(rad)/gravity

        return rad, v_xo, v_yo, flight_time, gravity
    
    @staticmethod
    def dt(v_xo:float, v_yo:float, gravity:float, time:float):
        h_v = v_xo
        h_d = h_v * time

        v_d = v_yo * time - 1/2 * gravity * time**2
        v_v = v_yo - gravity * time

        return h_d, v_v, v_d
        

def main():
    import time
    velocity = float(input("Please enter a value for the initial velocity Vo: "))
    angle = float(input("Please enter a value for the Angle in degrees: "))
    
    rad, v_xo, v_yo, flight_time, gravity = U6D.projectile_motion(velocity, angle)

    time.sleep(0.5)
    print("-----------------------------------------")
    print("Given inputs:")
    time.sleep(1.5)
    print(f"- Initial Velocity (Vo) = {velocity} m/s")
    print(f"- Angle in degrees = {angle} Deg")
    print(f"Given value of g = {gravity} m/s^2")

    time.sleep(0.5)
    print("-----------------------------------------")
    print("Converting angle to radians:")
    time.sleep(1.5)
    print(f"- Angle in radians = {rad:.2f} rad")

    time.sleep(0.5)
    print("-----------------------------------------")
    print("Calculating values of initial Vertical, Horizontal Velocity, and Time of flight:")
    time.sleep(1.5)
    print(f"- Initial Horizontal Velocity Vxo = {v_xo:.2f} m/s")
    print(f"- Initial Vertical Velocity Vyo = {v_yo:.2f} m/s")
    print(f"- The time of flight = {flight_time:.2f} s")

    time.sleep(0.5)
    print("-----------------------------------------")
    timed = float(input("Enter a given time for which both the distances and vertical velocity are calculated, t: "))
    h_d, v_v, v_d = U6D.dt(v_xo, v_yo, gravity, timed)

    time.sleep(0.5)
    print(f"The horizontal distance is = {h_d:.2f} m")
    print(f"The vertical distance is = {v_d:.2f} m")
    print(f"The vertical velocity is = {v_v:.2f} m/s")

if __name__ == "__main__":
    main()