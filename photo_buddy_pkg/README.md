# Photo Buddy Python package

## Installation:

Clone or download this folder.
Navigate to the resulting directory.

Run:

    python setup.py develop

## Usage:

To import this module in Python, use 

    import Photo_Buddy
    
The primary method intended for users is

    Photo_Buddy.go()
which takes a picture and compares it to the database in order to identify a person and displays the image with identification
    
    Photo_Buddy.identify()
which takes a picture and identifies the people in it and, if possible, saves a person to the database with their name
 
 The documentation for this and all other methods is available in the `__init__.py` file in this folder.
 
            
 ###
 ###       
 #### Credits
          
 
 Please note that this code makes extensive use of Davis King's DLib library.
