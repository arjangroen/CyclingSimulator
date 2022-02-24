from faker import Faker
fake = Faker('nl_NL')


class Racer(object):

    def __init__(self, ftp: int = 250, body_weight: int = 72, name='', drag_coef: float = 0.65):
        """
        :param ftp: Functional Treshhold power in watts
        :param weight: weight in kg
        :param name: rider name
        """
        self.name = fake.name() if not name else name
        self.ftp = ftp
        self.body_weight = body_weight
        self.drag_coef = drag_coef
        self.Crr = 0.005
        self.Loss_dt = 0.02

    @property
    def ftp_per_kg(self):
        return self.ftp / self.body_weight

    @property
    def relative_fitness(self):
        return self.ftp / self.body_weight**(2/3)

    @property
    def area(self):
        return 0.1 * self.body_weight**(1/3)

    @property
    def weight(self):
        return self.body_weight + self.body_weight*0.12 + 3






