from abc import ABC, ABCMeta, abstractmethod

# Games need players. But we should only be able to instantiate a HumanPlayer or an AIPlayer
# The Class 'Player' is abstract


class Player (ABC):
    """
    The player class represents participants in our game. They can be human players or AI players.
    This is an abstract class and cannot be instantiated.
    """
    __metaclass__ = ABCMeta

    # Private instance variable
    _p_piece_color = None
    _p_name = None  # holds the name or label/identifier

    @property
    def piece_color(self):
        return self._p_piece_color

    @piece_color.setter
    def piece_color(self, value):
        self._p_piece_color = value

    @property
    def name(self):
        return self._p_name

    @name.setter
    def name(self, value):
        self._p_name = value


class HumanPlayer (Player):
    """
    A human player will be prompted to make its move via the keyboard input
    """
    def __init__(self):
        pass


class AIPlayer (Player):
    """
    An AI Player
    """
    def __init__(self):
        pass

    def get_all_possible_strategies(self, gamedata):
        """
        :param gamedata: the current game board
        :return: should return [row, col] indicating where to play next
        """

        list_of_strategies = [] # Blank List

        for rows in range(0, len(gamedata.Board.Grid)):
            for cols in range(0, gamedata.Board.COL_COUNT):
                print("cols=", cols)
                s = Strategy(gamedata, [rows, cols])
                list_of_strategies.append(s)  # Add

        print ("Total number of list_of_strategies", len(list_of_strategies))
        return list_of_strategies # Return a List

    def do_ai_move(self):
        # Essentially returns a [row, col] causing the AI to make a move after analyzing its logic
        pass


class Strategy:
    """" Strategies are objects that contain info on possible moves the AI can make. When the game board state is
    scanned / evaluated by the AI, the AI will store-up some possible strategies and then determine 'possible_plays',
    which are simply [row, col] of where to place the next move

    priority_level = 0  # holds the strategy priority level
    center = ()  # a strategy centers around a center tile of which we get the surrounding tiles, it will be a tuple
    possible_plays = []  # this should be a list of x,y for possible plays in this strategy
    surrounding_tiles = []  # this should be a list of x,y co-ordinates (max 4, min 2) of tiles that surround the center
    """

    def __init__(self, arg_game_reference, arg_center):
        # self.Game = arg_game_reference  # This basically holds a reference to the current gameboard
        self.center = arg_center
        self.priority_level = 0
        self.possible_plays = []

        row, cols = arg_center
        self.surrounding_tiles = arg_game_reference.get_surrounding_pieces(row, cols)

        # Calculate possible plays
        print("strategy centered on", self.center)
        print("length of surrounding tiles =", len(self.surrounding_tiles))
        print("surrounding tiles index 0 is", self.surrounding_tiles[0])
        for piece in range(0, len(self.surrounding_tiles)):
            r, c = self.surrounding_tiles[piece]
            if arg_game_reference.Board.Grid[r, c] == 0:  # Only add a possible play if the [r,c] is empty (0)
                self.possible_plays.append([r, c])
                print("Tally possible plays =", len(self.possible_plays))
