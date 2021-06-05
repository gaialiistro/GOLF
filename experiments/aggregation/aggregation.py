from experiments import aggregation
from experiments.aggregation.cockroach import Cockroach
from experiments.aggregation.config import config
from simulation.utils import *
from simulation.swarm import Swarm


class Aggregations(Swarm):
    """
    This class inherits from the base class Swarm.

    """
    def __init__(self, screen_size) -> None:
        """
        This function is the initializer of the class Aggregation.
        :param screen_size:
        """
        super(Aggregations, self).__init__(screen_size)
        self.object_loc = config["aggregation"]["site"]

    def initialize(self, num_agents: int) -> None:
        """
        Initialize the whole swarm, creating and adding the aggregation areas, and the agent, placing them inside of the
        screen.
        :param num_agents: int:
"""
    #add sites
        if config['aggregation']['site']:
            object_loc=config['aggregation']['location']
            filename = ("experiments/aggregation/images/greyc1.png")
            self.objects.add_object(
                file=filename, pos=object_loc, scale=config['aggregation']['scale'], obj_type="site")
        if config['aggregation']['site2']:
            object_loc=config['aggregation']['location2']
            filename = ("experiments/aggregation/images/greyc1.png")
            self.objects.add_object(
                file=filename, pos=object_loc, scale=config['aggregation']['scale2'], obj_type="site")
    #add outside borders
        if config['aggregation']['outside']:
            scale = [800, 800]
            filename = ("experiments/flocking/images/convex.png")
#("experiments/aggregation/images/greyc2.png")
            object_loc = config["base"]["object_location"]
            self.objects.add_object(
                file=filename, pos=object_loc, scale=scale, obj_type="obstacle"
            )
            min_x, max_x = area(object_loc[0], scale[0])
            min_y, max_y = area(object_loc[1], scale[1])
    #add agents
        for index, agent in enumerate(range(num_agents)):
            coordinates = generate_coordinates(self.screen)
            if config['aggregation']['outside']:
                while (
                        coordinates[0] >= max_x
                        or coordinates[0] <= min_x
                        or coordinates[1] >= max_y
                        or coordinates[1] <= min_y
                    ):
                        coordinates = generate_coordinates(self.screen)


            self.add_agent(Cockroach(pos=np.array(coordinates), v=None, aggregation=self, index=index))


