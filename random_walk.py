from random import choice


class RandomWalk:
    # class for generate random
    def __init__(self, number_points=5000):
        # init attribute walk
        self.number_points = number_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        self.get_steps()
        self.get_steps()

    def get_steps(self):
        """scale = walkers_points"""
        while len(self.x_values) < self.number_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
