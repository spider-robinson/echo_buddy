from flask import Flask
from flask_ask import Ask, question, statement

import News_Buddy
import time

app = Flask(__name__)
ask = Ask(app, '/')


@app.route('/')
def homepage():
    return "NewsBuddy"


@ask.launch
def start_skill():
    welcome_msg = "Hi! I'm News Buddy. What would you like me to tell you?"
    return question(welcome_msg)


@ask.intent("GetTopic")
def question_one(topic):
    results = News_Buddy.news_about(topic)
    if results is None:
        return statement("I couldn't find anything.")
    return statement("I found this: " + results)


@ask.intent("GetEntity")
def question_two(entity, k):
    t0 = time.time()
    result = News_Buddy.related_entities(entity, k=k)
    if result is None:
        return statement("I couldn't find anything.")
    top_results = list(list(zip(*result))[0])
    print(time.time() - t0)
    results = ", ".join(top_results)
    msg = "Most associated with " + entity + ": " + results
    return statement(msg)


@ask.intent("ThirdIntent")
def question_three(query, k):
    result = News_Buddy.entities_about(query, k=k)
    if result is None:
        return statement("I couldn't find anything.")
    top_results = [i[0] for i in result]
    results = ", ".join(top_results)
    msg = "Most associated with " + query + ": " + results
    return statement(msg)


if __name__ == '__main__':
    # main.initialize()
    News_Buddy.get_data()
    app.run(port=5007)