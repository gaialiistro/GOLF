from numpy.lib.utils import get_include
from experiments.aggregation.config import config
from simulation.agent import Agent
from simulation.utils import *
import random
import time


class Cockroach(Agent):
    """ """
    def __init__(
            self, pos, v, aggregation, index: int, image: str = "experiments/aggregation/images/ant.png"
    ) -> None:
        """
        Args:
        ----
            pos:
            v:
            flock:
            index (int):
            image (str): Defaults to "experiments/aggregation/images/ant.png"
        """
        super(Cockroach, self).__init__(
            pos,
            v,
            image,
            max_speed=config["agent"]["max_speed"],
            min_speed=config["agent"]["min_speed"],
            mass=config["agent"]["mass"],
            width=config["agent"]["width"],
            height=config["agent"]["height"],
            dT=config["agent"]["dt"],
            index=index
            
        )
        self.state = 'wander'
        self.aggregation = aggregation
        self.start_time = pygame.time.get_ticks()
        self.wait = 3
        self.list_fun = []
        self.counter = 0 
        self.speed = np.array([12.12914438 ,-14.01726499])


    def out_of_site(self):
        # print('c')
                # ----- Site locations -----
        #Site 1 location and scale
        site1_loc = config["aggregation"]["location"]
        site1_scale = config["aggregation"]["scale"]

        #Site 2 location and scale
        site2_loc = config["aggregation"]["location2"]
        site2_scale = config["aggregation"]["scale2"]
        
        #Site 1 coordinates
        site1_min_x, site1_max_x = area(site1_loc[0], site1_scale[0])
        site1_min_y, site1_max_y = area(site1_loc[1], site1_scale[1])

        #Site 2 coordinates
        site2_min_x, site2_max_x = area(site2_loc[0], site2_scale[0])
        site2_min_y, site2_max_y = area(site2_loc[1], site2_scale[1])
        
        if not ((self.pos[0] > site1_min_x + 10 and self.pos[0] < site1_max_x - 10 and self.pos[1] > site1_min_y + 10 and self.pos[1] < site1_max_y - 10) or ( self.pos[0] > site2_min_x + 10 and self.pos[0] < site2_max_x - 10 and self.pos[1] > site2_min_y + 10 and self.pos[1] < site2_max_y - 10)):
            self.start_time = pygame.time.get_ticks()
        return self.start_time

    def site_behavior(self):
        if self.state == 'wander':
            # self.counter = 0
            n_neighbours = self.get_n_neighbours() #check number of neigbors
            Pjoin = n_neighbours*0.05 #check local density
            join_density = random.uniform(0,1) 
            if Pjoin > join_density and pygame.time.get_ticks()-self.start_time > 200:
                self.max_speed = 0.0
                self.state = 'join'

        if self.state == 'join':
            n_neighbours = self.get_n_neighbours() #check number of neigbors
            Pleave = 1-n_neighbours*0.01  #check local density
            leave_density = random.uniform(0,1)
            if self.counter%5000 == 0:
                if Pleave > leave_density:
                    self.state = 'leave'
                    self.max_speed = 30.0
                    self.counter = 0
                    self.v = self.speed

                   
        if self.state == 'leave':
            if self.counter == 1000:
                self.state = 'wander'


    def update_actions(self) -> None:
        self.counter +=1 

         # avoid any obstacles in the environment
        for obstacle in self.aggregation.objects.obstacles:
            collide = pygame.sprite.collide_mask(self, obstacle)
            if bool(collide):
                self.avoid_obstacle()
      
        
        # react to sites in the environment
        for site in self.aggregation.objects.sites:
            collide = pygame.sprite.collide_mask(self, site)
            if bool(collide):
                self.site_behavior()
            else:
                self.out_of_site()
                
    
    def get_n_neighbours(self):
        # find all the neighbors of a boid based on its radius view
        neighbors = self.aggregation.find_neighbors(self, config["cockroach"]["radius_view"])
        #get the amount of neighbors
        return len(neighbors)