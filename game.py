import numpy as np

class Game:
    def __init__(self):
        self.fields = ["id",
                    "type",
                    "team",
                    "hp",
                    "x pos",
                    "y pos",
                    "x velocity",
                    "y velocity",
                    "shoot x",
                    "shoot y"]

    # Initialize state of the world to be empty
    def initialize_world(self):
        self.entities_total = 0
        self.entities_alive = 0
        self.world_state = np.zeros((10, len(self.fields)))

        # print self.world_state

    def add_entity(self, type, team, hp, x_pos, y_pos, x_vel, y_vel, x_sh, y_sh):
        assert hp > 0
        slot = self.find_slot()
        eid = self.entities_total + 1
        self.world_state[slot] = [eid, type, team, hp, x_pos, y_pos, x_vel, y_vel, x_sh, y_sh]

        self.entities_total += 1
        self.entities_alive += 1

    # Get first slot with empty/dead entity
    def find_slot(self):
        slot = 0
        for x in range(self.world_state.shape[0]):
            if self.world_state[x][3] <= 0:
                return x
        return slot


    def step_time(self):
        pass
        # Move entities by velocity

        # Calculate pairwise distances

        # Check for collisions

        # Check for world border collisions

        # Apply hp modifiers




def main():
    game = Game()
    game.initialize_world()
    game.add_entity(0, 0, 1, 0, 0, 0, 0, 0, 0)
    game.add_entity(0, 0, 1, 0, 0, 0, 0, 0, 0)
    game.add_entity(0, 0, 1, 0, 0, 0, 0, 0, 0)

    print game.world_state

    time = 0
    while True:
        game.step_time()
        time += 1
        break

if __name__ == '__main__':
    main()

