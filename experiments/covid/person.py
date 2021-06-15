import numpy as np
import pygame

from experiments.covid.config import config
from simulation.agent import Agent
from simulation.utils import *


class Person(Agent):
  
    def __init__(
            self, pos, v, population, index: int, image: str = None, color = (0,0,0),type = None
    ) -> None:
        """
        Args:
        ----
            pos:
            v:
            population:
            index (int):
            image (str): Defaults to "experiments/aggregation/images/ant.png"
        """
        super(Person, self).__init__(
            pos,
            v,
            image,
            color,
            max_speed=config["agent"]["max_speed"],
            min_speed=config["agent"]["min_speed"],
            mass=config["agent"]["mass"],
            width=config["agent"]["width"],
            height=config["agent"]["height"],
            dT=config["agent"]["dt"],
            index=index,
            
           
        )
        self.population = population
        self.recovered = (145, 255, 61)
        self.infectious = (255, 61, 61)
        self.susceptible = (255, 181, 61)
        self.type = type
        self.timer = 0
        self.recovery_time = 5000
        self.quarantine_timer = 0
        

    def infected(self):
        if self.population.find_neighbors(self,config["person"]["radius_view"]) and self.type == "S":
            self.type = "I"
         

    def update_actions(self) -> None:
        self.infected()
        self.get_colors()
        self.recover()
        self.cinema_behavior()
        self.quarantine()
        # self.store_agent_types()

        # avoid any obstacles in the environment
        for obstacle in self.population.objects.obstacles:
            collide = pygame.sprite.collide_mask(self, obstacle)
            if bool(collide):
                self.avoid_obstacle()
       
                
    
    def get_colors(self):
        if self.type == "S":
            self.image.fill(self.susceptible)
        elif self.type == "I":
            self.image.fill(self.infectious)
        elif self.type == "R":
            self.image.fill(self.recovered)
    
    def recover(self):
        if self.type == "I":
            self.timer +=1
            if self.timer % 500 == 0:
                self.type = "R"
    
    def cinema_behavior(self):
        if config['population']['cinema']:
            # react to sites in the environment
            for site in self.population.objects.sites:
                collide = pygame.sprite.collide_mask(self, site)
                if bool(collide):
                    n_neighbours = self.get_n_neighbours() 
                    if n_neighbours == 0:
                        self.v = np.array([0,0])
        
    def get_n_neighbours(self):
        # find all the neighbors of a boid based on its radius view
        neighbors = self.population.find_neighbors(self, 20)
        #get the amount of neighbors
        return len(neighbors)

    def quarantine(self):
        if config['population']['quarantine']:
            for site in self.population.objects.sites:
                    collide = pygame.sprite.collide_mask(self, site)
                    if bool(collide) and self.type == "I":
                        self.quarantine_timer += 1
                        if self.quarantine_timer % 20 == 0:
                            self.v = np.array([0,0])
                    elif bool(collide) and self.type == "S":
                            self.avoid_obstacle()
                    elif bool(collide) and self.type == "R":
                            self.v = np.array([2.482585,   9.6869382])
                            self.max_speed = 30.0
                

                            

    # def store_agent_types(self):
    #    for agent in self.population.agents:
    #        if agent.type != None and agent.type != "":

    #            self.population.datapoints.append(agent.type)
