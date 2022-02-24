import numpy as np

class Physics(object):

    def f_gravity(self, weight, grade):
        return 9.8067 * (np.sin(np.arctan(grade / 100)) * weight)

    def f_rolling(self, weight, grade, Crr):
        return 9.8067 * (np.cos(np.arctan(grade / 100)) * weight) * Crr

    def f_drag(self, drag_coefficient, area, air_density, velocity, headwind=0.):
        return 0.5 * drag_coefficient * area * air_density * ((velocity+headwind)/3.6) ** 2

    def f_resistance(self, weight, grade, Crr, drag_coefficient, area, air_density, velocity):
        gravity = self.f_gravity(weight, grade)
        rolling = self.f_rolling(weight, grade, Crr)
        air = self.f_drag(drag_coefficient, area, air_density, velocity)
        return gravity + rolling + air

    def f_power(self, resistance, speed):
        return resistance * speed

    def f_speed(self, power, resistance):
        return power / resistance


class Segment(object):

    def __init__(self, grade=0, length: int = 1):
        """

        :param gradient: gradient
        :param length: x100 meter
        """
        self.grade = grade
        self.length = length

class Route(object):

    def __init__(self):
        self.segments = []

    def add_segment(self, segment):
        self.segments.append(segment)

    @property
    def profile(self):
        profile = []
        for segment in self.segments:
            for i in range(segment.length):
                profile.append(segment.grade)
        return np.array(profile)






