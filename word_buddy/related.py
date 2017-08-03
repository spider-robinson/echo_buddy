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
    return "Launching related"

@ask.launch
def start_skill():
    msg = "What word do you want related words about?"
    return question(msg)

@ask.intent("WordIntent")
def tell_related(word):
    answer = ", ".join(np.array(glove.wv.similar_by_word(word))[:,0])
    msg = "The words most similar to, {}, are {}".format(word, answer)
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)