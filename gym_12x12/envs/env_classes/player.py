from abc import ABC, ABCMeta, abstractmethod

# Games need players. But we should only be able to instantiate a HumanPlayer or an AIPlayer
# The Class 'Player' is abstract


class Player (ABC):
    __metaclass__ = ABCMeta

    # Private instance variable
    _p_piece_color = None

    @property
    def piece_color(self):
        return self._p_piece_color

    @piece_color.setter
    def piece_color(self, value):
        self._p_piece_color = value


class HumanPlayer (Player):
    def __init__(self, arg_piece_color):
        self.piece_color = arg_piece_color


class AIPlayer (Player):
    def __init__(self, arg_piece_color):
        self.piece_color = arg_piece_color


class Strategy:
    """" Strategies are objects that contain info on possible moves the AI can make. When the game board state is 
    scanned / evaluated by the AI, the AI will store-up some possible strategies and then determine 'possible_plays',
    which are simply x,y of where to place the next move
    """""
    priority_level = 0  # holds the strategy priority level
    center = ()  # a strategy centers around a center tile of which we get the surrounding tiles, it will be a tuple
    possible_plays = []  # this should be a list of x,y for possible plays in this strategy
    surrounding_tiles = []  # this should be a list of x,y co-ordinates (max 4, min 2) of tiles that surround the center

    def __init__(self):
        pass

