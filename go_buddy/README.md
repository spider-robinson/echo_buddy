# Go Buddy Alexa Skill

Go Buddy is an Alexa skill that plays Go.

## Required modules:

Install these modules before attempting to run FriendBuddy:

 * pickle
 * numpy
 * flask
 * [Flask-ask](https://flask-ask.readthedocs.io/en/latest/ "Flask-ask information and download page")

## Setup

Enter the [Alexa Skills Kit](https://developer.amazon.com/edw/home.html#/skills "Amazon's Alexa Skills Kit"), which requires an Amazon developer account.

Add a new skill using the button in the upper right corner.

Enter "GoBuddy" as the name and "go" as the invocation name. Click the next button in the bottom right corner to proceed to the Interaction Model.

Paste the following into the Code Editor of the Skill Builder (you may want to enter the Skill Builder interface):
    
  ```
{
  "intents": [
    {
      "name": "AMAZON.CancelIntent",
      "samples": []
    },
    {
      "name": "AMAZON.HelpIntent",
      "samples": []
    },
    {
      "name": "AMAZON.StopIntent",
      "samples": []
    },
    {
      "name": "MoveIntent",
      "samples": [
        "{l_coord} {n_coord}"
      ],
      "slots": [
        {
          "name": "l_coord",
          "type": "letter",
          "samples": []
        },
        {
          "name": "n_coord",
          "type": "AMAZON.NUMBER",
          "samples": []
        }
      ]
    },
    {
      "name": "PassIntent",
      "samples": [
        "pass",
        "I'll pass"
      ],
      "slots": []
    },
    {
      "name": "YesIntent",
      "samples": [
        "yes",
        "okay",
        "ready",
        "sure",
        "ok",
        "yeah",
        "yep"
      ],
      "slots": []
    }
  ],
  "types": [
    {
      "name": "letter",
      "values": [
        {
          "id": null,
          "name": {
            "value": "a",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "b",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "c",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "d",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "e",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "f",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "g",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "h",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "i",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "j",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "k",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "l",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "m",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "n",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "o",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "p",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "q",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "r",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "s",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "t",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "u",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "v",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "w",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "x",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "y",
            "synonyms": []
          }
        },
        {
          "id": null,
          "name": {
            "value": "z",
            "synonyms": []
          }
        }
      ]
    }
  ]
}
```
  
  Save and build the Interaction Model.
  
  Clone or download this folder. Navigate to the resulting directory.
  
  There are two different implementations that you can run, the AI based on a Convolutional Neural Network or a Monte Carlo Tree Search.
  
  Run one of these using:
  
  ```
  python GoBuddy_MCTS.py
  ```
  
  or
  
  ```
  python GoBuddy_CNN.py
  ```
  
  This will start a local host at port 5000.
  
  Use [ngrok](https://ngrok.com/ "ngrok information and download page") to create a tunnel to your local host by running
  
  ```
  .\ngrok http 5000
  ```
  
  In the Alexa Skills Kit, proceed to the Configuration tab.
  
  Select HTTPS as the Endpoint, then your location as the region closest to your target customer.
  
  Copy and paste the secure-url generated by ngrok into the box under Endpoint in the Configuration tab.
  
  Save the Configuration using the save button at the bottom of the page.
  
  Your Alexa skill is now ready to run.

  
## Usage

Say "[play] go" to trigger this skill.

Say "yes" or "ready" when prompted.

Say "stop" to end a game.

Say a move coordinate in the form of {letter} {number}, such as "A 4", to play a move when prompted.

For reference, a Go board will be displayed in the Alexa app.
