# echo_buddy
Final project for Cogworks 2017 (Team Fantastic Four)

## Contains Flask-Ask apps for:

* song buddy:

    an application that maintains a database of songs and uses them to identify snippets

* photo buddy:

an application that maintains a database of facial features and uses them to identify people

* friend buddy:

    an application that automatically recognizes users and maintains lists and information for them 
    
* news buddy:

    a search engine for news articles that relates topics, named entities, and articles
    
* analogy buddy:

    an application that solves analogies using word embeddings
    
 
* game buddy:

    contains three games:
    * word association
    * hangman
    * ghost
    
* go buddy:
    
    an application that plays Go using probablities and a Monte-Carlo Tree Search


    
 To run an Alexa skill, run the Flask-ask app in the correct folder and create an ngrok tunnel to the proper localhost. Use the generated secure-url as the endpoint on the configuration tab of the Alexa Skill Builder. For more detailed instructions and individual intent schema, see the README files for each individual app.
        
 ## Contains Python packages for:
 
 * song buddy:

    an application that maintains a database of songs and uses them to identify snippets
    
* photo buddy:

    an application that maintains a database of facial features and uses them to identify people
    
* news buddy:

    a search engine for news articles that relates topics, named entities, and articles
    
    
 These packages can be installe by cloning the individual folders and calling `python setup.py develop` from the correct directory in the terminal. For more detailed and individualized instructions, see the README files in each folder.
    
For more information on installing Python packages or running Flask-Ask apps on Alexa, see individual README files in each folder.
