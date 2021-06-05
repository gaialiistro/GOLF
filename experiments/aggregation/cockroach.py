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

        # react to the sites in the environment
        for site in self.aggregation.objects.sites:
            collide = pygame.sprite.collide_mask(self, site)
            if bool(collide):
                self.site_behavior()
            #if not in the site or not in the leave state then wander
            # if not bool(collide) and leave == True:
            #     pass
            #     # self.wander(wander_dist, wander_radius, wander_angle)
            # #if in the site and not in the leave state then join
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
        n_neighbours = self.get_n_neighbours()
        #the probaility of joining is equeal to the amount of neighbours divided by the total population
        prob = n_neighbours/config['base']['n_agents']
        sample = random.uniform(0,1)
        if sample < prob:
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
    # Leaving (where the agent decided to start Wandering)

    def leave(self):
        #start walking
        #wait T leaves
        return True
    
    def get_n_neighbours(self):
        # find all the neighbors of a boid based on its radius view
        neighbors = self.aggregation.find_neighbors(self, config["cockroach"]["radius_view"])
        #get the amount of neighbors
        return len(neighbors)