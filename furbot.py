import random
import numpy as np
from ..bot_control import Move
from copy import copy
import random


class FurryBot:

    def __init__(self):
        self.target = None
        self.grid_size = None
        self.cross = [[0,1], [-1,0], [0,-1], [1,0]]
        self.cross += [[0,2], [1,1], [2,0], [1,-1], [0,-2], [-1,-1], [-2, 0], [-1,1]]
        self.cross += [[0,3], [1,2], [-2,1], [-3,0], [-2,-1], [-1,-2], [0,-3], [1,-2], [2,-1], [3,0], [2,1], [1,2]]

    def get_name(self):
        return "FurryBot"

    def get_contributor(self):
        return "Ferdinand Schumacher"

    def clamp(self, n, smallest, largest):
        return max(smallest, min(n, largest))

    def get_cell(self, curpos, dir):
        return curpos + dir

    def get_cell_cost(self, grid, coi):
        # Check bounds
        if coi[0] < 0 or coi[0] > self.grid_size - 1 or coi[1] < 0 or coi[1] > self.grid_size - 1:
            return 1e9
        else:
            value = grid[coi[1], coi[0]]
            if value == 0:
                return 0
            else:
                # [floor_colour, 0, bot_colour]
                return [100, 10, 0][(self.id - value) % 3]

    def get_new_target(self, grid):
        min_tile_cost = 1e9
        # Select lowest cost tile in directly connecting tiles
        random.shuffle(self.cross)
        for direction in self.cross:
            # Get cell Of Interest
            coi = self.get_cell(self.position, direction)
            # Get cell cost
            cell_cost = self.get_cell_cost(grid, coi)
            if cell_cost < min_tile_cost:
                min_tile_cost = cell_cost
                self.target = coi
        # If minimum cell cost is not 0, we are surrounded, so take a new random target
        if min_tile_cost > 0:
            self.target[0] = random.randint(0, grid.shape[0] - 1)
            self.target[1] = random.randint(0, grid.shape[1] - 1)

    def determine_next_move(self, grid, enemies, game_info):
        # Store grid size once
        if self.grid_size == None:
            self.grid_size = game_info.grid_size

        # Create a target in storage if doesn't exist
        if  self.target is None:
            self.target = copy(self.position)

        # If reached the target find a new target
        if np.array_equal(self.position, self.target):
            self.get_new_target(grid)

        # Move in direction of target
        if self.target[0] > self.position[0]:
            return Move.RIGHT
        elif self.target[0] < self.position[0]:
            return Move.LEFT
        elif self.target[1] > self.position[1]:
            return Move.UP
        else:
            return Move.DOWN


class Schumi:

    def __init__(self):
        self.previous_position = Move.STAY
        self.grid_size = None
        self.move_scores = {Move.UP: 0, Move.LEFT: 0, Move.DOWN: 0, Move.RIGHT: 0}
        self.move2direction = {Move.UP: [0,1], Move.LEFT: [-1,0], Move.DOWN: [0,-1], Move.RIGHT: [1,0]}
        self.cross2 = [[0,2], [1,1], [2,0], [1,-1], [0,-2], [-1,-1], [-2, 0], [-1,1]]
        self.cross3 = [[0,3], [1,2], [-2,1], [-3,0], [-2,-1], [-1,-2], [0,-3], [1,-2], [2,-1], [3,0], [2,1], [1,2]]

    def get_name(self):
        return "Schumi"

    def get_contributor(self):
        return "Ferdinand Schumacher"

    def reset_move_scores(self):
        for move in self.move_scores:
            self.move_scores[move] = 0

    def get_cell(self, curpos, dir):
        return curpos + dir

    def get_cell_score(self, grid, coi, penalize_boundary):
        # Check bounds
        if coi[0] < 0 or coi[0] > self.grid_size - 1 or coi[1] < 0 or coi[1] > self.grid_size - 1:
            return -10 if penalize_boundary else 0
        # Try to avoid getting stuck by penalizing going back to previous cell
        elif np.array_equal(coi, self.previous_position):
            return -1
        else:
            value = grid[coi[1], coi[0]]
            if value == 0:
                return 1
            elif value == self.id:
                return 0
            else:
                # [floor_colour, 0, bot_colour]
                return [-1, 1, 2][(self.id - value) % 3]

    def update_move_scores(self, direction, score):
        if direction[0] < 0:
            self.move_scores[Move.LEFT] += score
        if direction[0] > 0:
            self.move_scores[Move.RIGHT] += score
        if direction[1] > 0:
            self.move_scores[Move.UP] += score
        if direction[1] > 0:
            self.move_scores[Move.DOWN] += score

    def get_new_move(self, grid):
        self.reset_move_scores()
        # First get scores for first ring of neighbouring cells
        for move in self.move_scores:
            # Get cell Of Interest
            coi = self.get_cell(self.position, self.move2direction[move])
            # Store move score
            self.move_scores[move] = 3.0*self.get_cell_score(grid, coi, True)
        # Then add scores for next ring of neighbouring cells
        for direction in self.cross2:
            # Get cell Of Interest
            coi = self.get_cell(self.position, direction)
            # Add score
            self.update_move_scores(direction, 1.0*self.get_cell_score(grid, coi, False))
        # Lastly add scores for last ring of neighbouring cells
        for direction in self.cross3:
            # Get cell Of Interest
            coi = self.get_cell(self.position, direction)
            # Add score
            self.update_move_scores(direction, 0.5*self.get_cell_score(grid, coi, False))
        # Select highest score tile in directly connecting tiles
        best_score = -10
        best_move = Move.STAY
        moves = list(self.move_scores.keys())
        random.shuffle(moves)
        for move in moves:
            score = self.move_scores[move]
            if score > best_score:
                best_score = score
                best_move = move
        # Save current position for next iteration
        self.previous_position = self.position
        return best_move

    def determine_next_move(self, grid, enemies, game_info):
        # Store grid size once
        if self.grid_size == None:
            self.grid_size = game_info.grid_size
            self.previous_position = self.position
            return Move.STAY

        return self.get_new_move(grid)
