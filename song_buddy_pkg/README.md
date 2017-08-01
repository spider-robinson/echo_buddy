# Song Buddy Python package

## Installation:

Clone or download this folder.
Navigate to the resulting directory.

Run:

    python setup.py develop

## Usage:

To import this module in Python, use 

    import Song_Buddy
    
The primary methods intended for users are
    
       Song_Buddy.identify()
 which records a seven-second clip and returns the top song related to it 
 
       Song_Buddy.train()
 which adds all songs in a specified folder to the database. This may take up to four or so minutes per song.
 See the documentation for information on supported file formats and suggested file organization
 
 <br> <br> <br>
 The documentation for these and all other methods is available in the `__init__.py` file in this folder.
