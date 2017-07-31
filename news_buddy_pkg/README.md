# News Buddy Python package

# Installation:

Clone or download this folder.
Navigate to the resulting directory.

Run:

    python setup.py develop

# Usage:

To import this module in Python, use 

    import News_Buddy
    
The primary methods intended for users are
    
       News_Buddy.news_about(topic)
 which gives the first sentence of the article most related to the given topic
 
       News_Buddy.entities_related(entity)
 which gives the entities most frequently associated with the given entities
 
       News_Buddy.entities_about(topic)
 which gives the entities most mentioned in articles related to the given topic
 
 
 The documentation for these and all other methods is available in the `__init__.py` file in this folder.
