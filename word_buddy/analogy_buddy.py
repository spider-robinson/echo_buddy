from flask import Flask
from flask_ask import Ask, statement, question
import requests
import time
import unidecode
import json
import numpy as np
import gensim
from gensim.models.keyedvectors import KeyedVectors

app = Flask(__name__)
ask = Ask(app, '/')

global glove
path = "glove.6B.50d.txt.w2v"
glove = KeyedVectors.load_word2vec_format(path, binary=False)


@app.route('/')
def homepage():
    return "Launching analogies"

@ask.launch
def start_skill():
    msg = "What analogy would you like me to solve?"
    return question(msg)

def analogythis(thatone, thistwo, thattwo, k=3):
    """
    Solves an analogy of the form this is to that as what is to that
    or what is to that as this is to that (which are mathematically equivalent)

    Parameters:
    -----------
    thatone: str
    thistwo: str
    thattwo: str
    k: int (Optional)
        the number of matches to return

    Returns:
    --------
    thisone: list(str)
        the top k solutions to the given analogy

    Example:
    --------
    analogythis(man, queen, woman, k=1)
        returns ["king"]
    """
    query = glove.wv[thistwo] - glove.wv[thattwo] + glove.wv[thatone]
    thisone = np.array(glove.wv.similar_by_vector(query))[:k,0].tolist()
    print(thatone)
    return thisone

@ask.intent("ThisIntent")
def solvethis(thatone, thistwo, thattwo):
    thisone = ", or ".join(analogythis(thatone, thistwo, thattwo))
    answer_msg = "{}, is to {}, as {}, is to, {}".format(thisone, thatone, thistwo, thattwo)
    return statement(answer_msg)

def analogythat(thisone, thistwo, thattwo, k=3):
    """
    Solves an analogy of the form this is to that as this is to what
    or this is to what as this is to that (which are mathematically equivalent)

    Parameters:
    -----------
    thisone: str
    thistwo: str
    thattwo: str
    k: int (Optional)
        the number of matches to return

    Returns:
    --------
    thatone: list(str)
        the top k solutions to the given analogy

    Example:
    --------
    analogythis(king, queen, woman, k=1)
        returns ["man"]
    """
    query = glove.wv[thisone] + glove.wv[thattwo] - glove.wv[thistwo]
    thatone = np.array(glove.wv.similar_by_vector(query))[:k,0].tolist()
    print(thatone)
    return thatone

@ask.intent("ThatIntent")
def solvethis(thisone, thistwo, thattwo):
    thatone = ", or ".join(analogythat(thisone, thistwo, thattwo))
    answer_msg = "{}, is to {}, as {}, is to, {}".format(thisone, thatone, thistwo, thattwo)
    return statement(answer_msg)

if __name__ == '__main__':
    app.run(debug=True)
