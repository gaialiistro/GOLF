from numpy.lib.utils import get_include
from experiments.aggregation.config import config
from simulation.agent import Agent
from simulation.utils import *
import random


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

        self.aggregation = aggregation
        # self.still = None us it like thsi 
    def change_state(self):
        pass
    def site_behavior(self):
        pass

    def update_actions(self) -> None:

         # avoid any obstacles in the environment
        for obstacle in self.aggregation.objects.obstacles:
            collide = pygame.sprite.collide_mask(self, obstacle)
            if bool(collide):
                self.avoid_obstacle()


        #change between states
        #define wandering state, not sure if it is correct
        for site in self.aggregation.objects.sites:
            collide = pygame.sprite.collide_mask(self, site)
            if bool(collide):
                self.site_behavior()
            #if not in the site or not in the leave state then wander
            # if not bool(collide) and leave == True:
            #     pass
            #     # self.wander(wander_dist, wander_radius, wander_angle)


            # #if in the site (TODO: and not in the leave state) then join
                self.join()
    

            # elif bool(collide) and leave == True: 
            #     passs
                # join()
            
        #     if bool(collide):
        #         self.join(n_neighbors)
        #         print("site")
        #     else:
        #         self.wander(wander_dist, wander_radius, wander_angle)
        #         print('wander')



    # Joining (decided to join an aggregation)

    def join(self): 

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


        # if cockroach in site 1
        if self.pos[0] > site1_min_x and self.pos[0] < site1_max_x and self.pos[1] > site1_min_y and self.pos[1] < site1_max_y:
            n_neighbours = self.get_n_neighbours() #check number of neigbors
            Pjoin = n_neighbours/config['base']['n_agents'] #check local density
            join_density = 0.07 #threshold for transitioning to Join state
            if Pjoin > join_density:
                self.pos[0], self.pos[1] = 300, 500 #join site 1

        # if cockroach in site 2
        if self.pos[0] > site2_min_x and self.pos[0] < site2_max_x and self.pos[1] > site2_min_y and self.pos[1] < site2_max_y:
            n_neighbours = self.get_n_neighbours() #check number of neigbors
            Pjoin = n_neighbours/config['base']['n_agents'] #check local density
            join_density = 0.07 #threshold for transitioning to Join state
            if Pjoin > join_density:
                self.pos[0], self.pos[1] = 700, 500 #join site 2
        
        pass
            #wait T join
            # still = True
            # return True 

    # Still (stop in the aggregate location)

    def still(self):
        n_neighbours = self.get_n_neighbours()
        #the probaility of joining is equeal to the amount of neighbours divided by the total population
        prob = 1 - n_neighbours/config['base']['n_agents']
        sample = random.uniform(0,1)
        if sample < prob:
            pass
            # still = False
    # Leaving (where the agent decided to start Wandering

    def leave(self):
        #start walking
        #wait T leaves
        return True
    
    def get_n_neighbours(self):
        # find all the neighbors of a boid based on its radius view
        neighbors = self.aggregation.find_neighbors(self, config["cockroach"]["radius_view"])
        #get the amount of neighbors
        return len(neighbors)