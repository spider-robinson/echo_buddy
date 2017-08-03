# Song Buddy Python package

### Install these modules before attempting to run SongBuddy:

 * pickle
 * numpy
 * scipy
 * [librosa](https://github.com/LLCogWorks2017/Week1/issues/6 "librosa installation instructions")
 * MatPlotLib
 * [microphone](https://github.com/LLCogWorks2017/Microphone "Ryan Soklaski's Microphone module")

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
