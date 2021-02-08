# project1-gnn3
This is an Application that gets information about three artists on sotify and randomly display 1 artist best track, a preview if it exists, the artist's name and a picture related to the track. The App was made with Flask module, requests module was also used in order to send and receive request from Spotify API, JSON was also used to read the reponse received. dotenv module was alo used in order to hide personal key
## Requirements
1. pip install slack
2. pip install python-dotenv
3. pip install requests
## Setup
1. Create `.env` file in your main directory
2. Add your SPOTIFY key from https://developer.spotify.com/dashboard/ with the line: `export clientsecret='your KEY'`

## Run Application
1. Run command in terminal `python app.py`

## Questions Answer
### What are at least 3 technical issues you encountered with your project? How did you fix them?
  - flask module was not working although it was already installed i kept getting error "No module names flask"
  i googled and end up on a solution : i deleted  the virtualenv i created with command like "virtualenv flask"
  the cd to flask, then activate a new virtualenv with command line "source bin/activate" then installed flask and it worked;
  - My API request url did not have the country parameter had to concatenate '?market=US' with the url
  - could not get if statement working tried everything 
### What are known problems, if any, with your project? 
  -There is no problem
### What would you do to improve your project in the future? 
  - Code Styling and Organization
