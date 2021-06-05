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

    def update_actions(self) -> None:
        # find all the neighbors of a boid based on its radius view
        neighbors = self.aggregation.find_neighbors(self, config["cockroach"]["radius_view"])
         #get the amount of neighbors
        n_neighbors = len(neighbors)
        #define variables TO DO config.toml
        wander_dist = 100
        wander_radius = 100
        wander_angle = 100
        leave = True
        wander = True
        still = False

         # avoid any obstacles in the environment
        for obstacle in self.aggregation.objects.obstacles:
            collide = pygame.sprite.collide_mask(self, obstacle)
            if bool(collide):
                self.avoid_obstacle()


        #change between states
        #define wandering state, not sure if it is correct
        for site in self.aggregation.objects.sites:
            collide = pygame.sprite.collide_mask(self, site)
            #if not in the site or not in the leave state then wander
            if not bool(collide) and leave == True:
                pass
                # self.wander(wander_dist, wander_radius, wander_angle)
            #if in the site and not in the leave state then join
            elif bool(collide) and leave == True: 
                pass
                # join()
            

        #     if bool(collide):
        #         self.join(n_neighbors)
        #         print("site")
        #     else:
        #         self.wander(wander_dist, wander_radius, wander_angle)
        #         print('wander')
    # Joining (decided to join an aggregation)

    def join(self,n_neighbours): 
        global still
        #the probaility of joining is queal to the amount of neighbours divided by the total population
        prob = n_neighbours/config['base']['n_agents']
        sample = random.uniform(0,1)
        if sample < prob:
            #wait T join
            still = True
            # return True 
    # Still (stop in the aggregate location)

    def still(self, n_neighbours):
        global still
        prob = n_neighbours/config['base']['n_agents']
        sample = random.uniform(0,1)
        if sample < prob:
            still = False
    # Leaving (where the agent decided to start Wandering

    def leave(self):
        #start walking
        #wait T leaves
        return True