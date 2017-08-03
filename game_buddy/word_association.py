import numpy as np
import pickle
import gensim
import time
from gensim.models.keyedvectors import KeyedVectors

t0 = time.time()
path = "glove.6B.50d.txt.w2v"
glove = KeyedVectors.load_word2vec_format(path, binary=False)
t1 = time.time()
print("loaded word vectors in ", t1-t0)

class Word_Association:
    """
    Capable of playing a simple word association game using word embeddings
    The computer starts by giving a random word,
    then the user gives a related word.
    This continues until the user gives a word that isn't related or has been used already
    or the computer can't come up with a related word that hasn't been used.
    """
    def __init__(self, seed=None, level=1):
        """
        Creates a game session.

        Parameters
        ----------
        seed: str
            the word on whcih the game will start (random if None)
        level: int
            the difficulty level (1 is recommended, higher is harder)
        """
        t0 = time.time()
        self.glove = glove
        with open('english_words.txt', 'r') as f:
            self.vocab = f.read()
        with open('most_common_words.txt', 'rb') as f:
            self.seed = pickle.load(f)
        self.word = self.seed[np.random.randint(0,len(self.seed))]
        if seed is not None:
            self.word = seed
        self.used = [self.word]
        self.level = level
        t1 = time.time()
        print("Created game with seed ", self.word, " in ", t1-t0)

    def start(self):
        """
        Called at the beginning of the game. Starts the game session.
        
        Returns
        -------
        str
            the message describing the game and the first word
        """
        return "Let's play a word association game! The first word is " + self.word

    def take_turn(self, guess):
        """
        Continues the game session.

        Parameters
        ----------
        guess: str
            the users' given related word

        Returns
        -------
        str
            if the game ended, who won/lost with a reason
            if the game will continue, the next word generated by the computer
        """
        #print("you guessed", guess)
        threshold = .5
        if guess not in self.glove.wv.vocab:
            return "I'm sorry; I don't know the word " + guess + ". Try a different word!"
        else:
            gauge = self.glove.wv.similarity(guess, self.word)
            #print(gauge)
        if gauge < threshold:
            return guess + " isn't closely related to " + self.word + ". You lost!"
        elif guess in self.used:
            return "We already used " + guess + ". You lost!"
        else:
            self.used.append(guess)
            N = self.level + 2
            my_words = np.array(self.glove.wv.most_similar(guess, topn=N))[:,0].tolist()
            #print(my_words)
            for i, word in enumerate(my_words):
                if word in self.used or word not in self.vocab:
                    #print("deleting ", word)
                    del my_words[i]
            self.word = my_words[np.random.randint(0, len(my_words))]
            if self.word in self.used or word not in self.vocab:
                #print("I would have said ", self.word)
                return "I can't think of any more words related to " + guess + ". You win!"
            self.used.append(self.word)
        return self.word

def inline_play():
    game = Word_Association(level=3)
    print(game.start())
    me = input("What's your guess? ").lower()
    msg = game.take_turn(me)
    turn = 0
    while msg[-1] is not '!':
        print(msg)
        me = input("What's your guess? ").lower()
        msg = game.take_turn(me)
        turn += 1
        #print(turn)
    print(msg)

