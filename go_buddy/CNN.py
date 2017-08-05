import numpy as np
import pickle
from mygrad import Tensor
from mygrad.nnet.layers import *
from mygrad.nnet.activations import *
from mygrad.nnet import losses
from Monte_Carlo3 import Node

import Go


class Go_CNN:
    """
    A class model representing a game utilizing the CNN implementation of the program.
    """
    def __init__(self, root, params=None, stride=(1, 1), p=0.3):
        """
        Initialization of the CNN model: setting class attributes and loading parameters.

        Parameters
        ----------
        root: Node
            A node representing the empty GameState.
        params: Tuple (default=None)
            A tuple of six parameters: W1, W2, W3, b3, W4, b4
            Automatically loaded from text file if None
        stride: Tuple (default=(1, 1))
            The stride distance for the CNN.
            Must match that used to train the CNN.
        p: float
            Dropout probability used to train the CNN.
        """
        if params is None:
            with open("params_52.txt", "rb") as f:
                params = pickle.load(f)
        W1, W2, W3, b3, W4, b4 = params
        self.W1 = W1
        self.W2 = W2
        self.W3 = W3
        self.b3 = b3
        self.W4 = W4
        self.b4 = b4
        self.stride = stride
        self.p = p
        self.root = root
        self.history = [root]

    def update(self, game_move):
        """
        Checks to ensure that a move is valid, before adding it to the game history.

        Parameters
        ----------
        game_move: Tuple
            The move made, in the format (row, col)

        Returns
        -------
        Node
            The new game node
        """
        current_state = self.history[-1]
        if len(current_state.children) < 1:
            current_state.get_children()
        if game_move not in current_state.moves:
            return False
        new_state = current_state.children[current_state.moves.index(game_move)]
        self.history.append(new_state)
        return self.history[-1]

    def convolve(self, x):
        """
        Performs a convolution in order to create a prediction distribution from a board input.

        Parameters
        ----------
        x: np.ndarray, shape=(1, 1, size, size)
            The current board that the move should be predicted for.

        Returns
        -------
        o4: np.ndarray, shape = (1, size, size)
            A distribution of scores for each move on a board.
        """
        stride = self.stride
        p = self.p
        c1 = conv2d(x, self.W1, stride, padding=0)
        c1 *= np.random.binomial(1, (1 - p), c1.shape) / (1 - p)
        # o1 = max_pool(c1, pool, pool)

        c2 = conv2d(c1, self.W2, stride, padding=0)
        c2 *= np.random.binomial(1, (1 - p), c2.shape) / (1 - p)
        o2 = c2.reshape(c2.shape[0], -1)
        # o2 = max_pool(c2, pool, pool).reshape(c2.shape[0], -1)

        o3 = relu(dense(o2, self.W3) + self.b3)
        o3 *= np.random.binomial(1, (1 - p), o3.shape) / (1 - p)
        o4 = dense(o3, self.W4) + self.b4
        return o4

    def get_play(self):
        """
        Given the current game history, attempt determine the best move.
        Use this method to hard code in Go strategies.

        Returns
        -------
        Node
            New game node after move is played
        Tuple or String
            Move made, in the form (row, col) or "P"
        """
        state = self.history[-1]
        scores = state.content.score()
        if state.content.move == "P" and scores[0] > scores[1]:
            # Player passed and computer winning
            move = "P"
        else:
            b = state.content.board
            pred = self.convolve(b.reshape(1, 1, self.root.content.size, self.root.content.size))[0]
            if state.content.moves_played == 0:
                pred[0] = -100
            print(pred)
            move_ind = np.argmax(pred)
            print(move_ind)
            move = (move_ind // self.root.content.size, move_ind % self.root.content.size)
        while self.update(move) is False:
            pred[move_ind] = -100
            move_ind = np.argmax(pred)
            move = (move_ind // self.root.content.size, move_ind % self.root.content.size)
        print(move)
        state = self.history[-1]
        scores = state.content.score()
        if scores[1] - scores[0] > 10:
            move = "P"
            self.history.remove(state)
            self.update(move)
        return self.history[-1], move

    def winner(self):
        """
        Determines if there is a winner at the current state.

        Returns
        -------
        int
            1 or 2, depending on winner
            -1, if tied
            0, if unfinished game
        """
        state = self.history[-1]
        return state.content.winner()


def start_game(param):
    """
    Starts single player game, with computer going first, using python console.

    CNN IMPLEMENTATION

    <<< USED FOR DEBUGGING PURPOSES, MAY NOT BE FULLY FUNCTIONAL >>>

    Parameters
    ----------
    reset: Boolean
        True: Create and train new Monte Carlo
        False: Load Monte Carlo from txt
    size: int
        size of board
    init_time: int
        seconds for which initialization will occur

    Returns
    -------
    int: winner
    """
    print("Computer: I'll start.")
    root = Node(Go.GameState(size=9, komi=0))
    cnn = Go_CNN(root, param)
    state = root.content
    while state.winner() == 0:
        state = cnn.get_play()[0].content
        state.paint(False)
        if state.winner() != 0:
            break
        result = False
        while result is False:
            r = ""
            c = ""
            while not (len(r) > 0 and (r.isdigit() or r.upper() == "P")):
                r = input("Enter row or P to pass: ")
            if r.lower() == "q":
                return
            if r.upper() == "P":
                result = "P"
            else:
                while not (len(c) > 0 and c.isdigit()):
                    c = input("Enter column: ")
                result = (int(r), int(c))
            result = cnn.update(result)
            if result is False:
                continue
            state = result.content
            state.paint(False)

    scores = state.score()
    winner = state.winner()
    if winner < 0:
        print("Tie reached.")
    elif winner == 1:
        print("Computer wins.")
    else:
        print("Player wins.")
    print("The score was " + str(scores[0]) + "-" + str(scores[1]) + ".")
    return winner
