from experiments.covid.config import config
from experiments.covid.person import Person
from simulation.swarm import Swarm
from simulation.utils import *
import random


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

        #add lockdown
        if config['population']['lockdown']:
            object_loc=config['population']['lockdown_location']
            scale = config['population']['lockdown_scale']
            filename = ("experiments/covid/images/LockdownSquare.png")
            self.objects.add_object(
                file=filename, pos=object_loc, scale=config['population']['lockdown_scale'], obj_type="obstacle")
            self.objects.add_object(
                file=filename, pos=object_loc, scale=scale, obj_type="obstacle"
            )
            min_x, max_x = area(object_loc[0], scale[0])
            min_y, max_y = area(object_loc[1], scale[1])


        #lockdown program
        if config['population']['lockdown']:
            for index, agent in enumerate(range(5)): #number of agents in lockdown
                coordinates = generate_coordinates(self.screen)
                while (
                        coordinates[0] >= max_x
                        or coordinates[0] <= min_x 
                        or coordinates[1] >= max_y
                        or coordinates[1] <= min_y
                    ):
                        coordinates = generate_coordinates(self.screen)
                self.add_agent(Person(pos=object_loc, v=None, population=self, index=index, type = "S"))

            for index, agent in enumerate(range(num_agents)):#num_agents
                coordinates = generate_coordinates(self.screen)
                while (
                        coordinates[0] <= max_x
                        and coordinates[0] >= min_x
                        and coordinates[1] <= max_y
                        and coordinates[1] >= min_y
                    ):
                        coordinates = generate_coordinates(self.screen)
                self.add_agent(Person(pos=np.array(coordinates), v=None, population=self, index=index, type = "S"))

            for index, agent in enumerate(range(int(num_agents/10))):
                coordinates = generate_coordinates(self.screen)
                while (
                        coordinates[0] <= max_x
                        and coordinates[0] >= min_x
                        and coordinates[1] <= max_y
                        and coordinates[1] >= min_y
                    ):
                        coordinates = generate_coordinates(self.screen)
                self.add_agent(Person(pos=np.array(coordinates), v=None, population=self, index=index, type = "I"))


        #movie theatre configuration
        if config['population']['cinema']:
            object_loc=[500,500]
            scale=[1500,1500]
            filename1 = ("experiments/covid/images/seats.png")
            filename2 = ("experiments/covid/images/cinema.png")
            self.objects.add_object(
                file=filename1, pos=object_loc, scale=scale, obj_type="site")
            self.objects.add_object(
                file=filename2, pos=object_loc, scale=[1000,1000], obj_type="obstacle")
            for index, agent in enumerate(range(num_agents)):#num_agents
                coordinates = generate_coordinates(self.screen)
                self.add_agent(Person(pos=np.array(coordinates), v=None, population=self, index=index, type = "S"))

            for index, agent in enumerate(range(int(num_agents/10))):
                coordinates = generate_coordinates(self.screen)
                self.add_agent(Person(pos=np.array(coordinates), v=None, population=self, index=index, type = "I"))





                
        
          #school configuration
        if config['population']['school']:
            object_loc=[500,600]
            scale=[1000,1000]
            filename1 = ("experiments/covid/images/room.png")
            filename2 = ("experiments/covid/images/structure.png")
            self.objects.add_object(
                file=filename2, pos=object_loc, scale=scale, obj_type="obstacle")
            self.objects.add_object(
                file=filename1, pos=object_loc, scale=scale, obj_type="site")
            min_x, max_x = area(object_loc[0], scale[0])
            min_y, max_y = area(object_loc[1], scale[1])


            for index, agent in enumerate(range(int(num_agents))): #agents in school
                coordinates = generate_coordinates(self.screen)
                while (
                        coordinates[0] >= max_x
                        or coordinates[0] <= min_x 
                        or coordinates[1] >= max_y
                        or coordinates[1] <= min_y
                    ):
                        coordinates = generate_coordinates(self.screen)
                self.add_agent(Person(pos=[500,500], v=None, population=self, index=index, type = "S"))
            for index, agent in enumerate(range(int(num_agents/10))):
                coordinates = generate_coordinates(self.screen)
                while (
                            coordinates[0] >= max_x
                        or coordinates[0] <= min_x 
                        or coordinates[1] >= max_y
                        or coordinates[1] <= min_y
                    ):
                        coordinates = generate_coordinates(self.screen)
                self.add_agent(Person(pos=[500,500], v=None, population=self, index=index, type = "I"))
        
            
            
            
 


        #non-lockdown program
        if  config['population']['outside']:
            for index, agent in enumerate(range(num_agents)):#num_agents
                coordinates = generate_coordinates(self.screen)
                self.add_agent(Person(pos=np.array(coordinates), v=None, population=self, index=index, type = "S"))

            for index, agent in enumerate(range(int(num_agents/10))):
                coordinates = generate_coordinates(self.screen)
                self.add_agent(Person(pos=np.array(coordinates), v=None, population=self, index=index, type = "I"))








