# Laverna-Viewer
Flask webapp that converts Lavera Notebook to HTML viewer.

## Installation

* Clone the repo
* `pip install -r requirements.txt`
* Create a `config.py` in the top level (`/Laverna-Viewer/config.py`) 
    * Add the path to your Laverna profile: `LAVERNA_PATH = /home/<usr>/Dropbox/Apps/Laverna/notes-db`
    * Add basic authentication: `AUTH_UN = my_name` and `AUTH_PW = my_password`
    * Optional, add a `MEDIA_PATH = <path>` to have a way to display images
* `python run.py` to start the server on localhost

## TODO
* Add more static file support
