from experiments.covid.config import config
from experiments.covid.person import Person
from simulation.swarm import Swarm
from simulation.utils import *


class Population(Swarm):
    """Class that represents the Population for the Covid experiment. TODO"""

    def __init__(self, screen_size) -> None:
        super(Population, self).__init__(screen_size)
        # To do

    def initialize(self, num_agents: int) -> None:
        """
        Args:
            num_agents (int):

        """

        # To Do
        # code snipet (not complete) to avoid initializing agents on obstacles
        # given some coordinates and obstacles in the environment, this repositions the agent
        coordinates = generate_coordinates(self.screen)

        if config["population"]["obstacles"]:  # you need to define this variable
            for obj in self.objects.obstacles:
                rel_coordinate = relative(
                    coordinates, (obj.rect[0], obj.rect[1])
                )
                try:
                    while obj.mask.get_at(rel_coordinate):
                        coordinates = generate_coordinates(self.screen)
                        rel_coordinate = relative(
                            coordinates, (obj.rect[0], obj.rect[1])
                        )
                except IndexError:
                    pass
