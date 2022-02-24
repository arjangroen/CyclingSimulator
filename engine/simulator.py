from engine.racer import Racer
from engine.environment import Physics, Segment, Route
phys = Physics()

class Simulation(object):

    def __init__(self, racer, route, air_density=1.225):
        self.racer = racer
        self.route = route
        self.air_density = air_density
        self.state = 0

    def get_terminal_velocity(self, velocity=.1):
        acceleration_force = 2
        eps = 1e-6
        while acceleration_force > eps:
            required_power = self.step(velocity=velocity)
            input_power = self.racer.ftp
            acceleration_force = input_power - required_power
            accelaration = acceleration_force / (self.racer.weight * 9.8067)
            velocity += accelaration
        return velocity


    def step(self, velocity=12):
        weight = self.racer.weight
        grade = self.route.segments[self.state].grade
        crr = self.racer.Crr
        drag_coef = self.racer.drag_coef
        area = self.racer.area
        air_density = self.air_density
        resistance = phys.f_resistance(weight, grade, crr, drag_coef, area, air_density, velocity)
        wheel_power = resistance * (velocity/3.6)
        leg_power = wheel_power / (1-self.racer.Loss_dt)
        return leg_power


def test():
    arjan = Racer()
    route = Route()
    route.add_segment(Segment(grade=10))
    sim = Simulation(arjan, route)
    power = sim.step()
    terminal_velocity = sim.get_terminal_velocity()

if __name__ == '__main__':
    test()



