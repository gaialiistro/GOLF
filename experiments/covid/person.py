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
        

    def infected(self):
        if self.population.find_neighbors(self,config["person"]["radius_view"]) and self.type == "S":
            self.type = "I"
         

    def update_actions(self) -> None:
        self.infected()
        self.get_colors()
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
        else:
            self.image.fill(self.recovered)