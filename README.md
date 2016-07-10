# Laverna-Viewer
Flask webapp that converts Lavera Notebook to HTML viewer.

## Installation

* Clone the repo
* `pip install -r requirements.txt`
* Create a `config.py` in the top level (`/Laverna-Viewer/config.py`) and add the path to your Laverna DB location
    * `LAVERNA_PATH = /home/<usr>/Dropbox/Apps/Laverna/notes-db`

## TODO

* Add password protection to certain notebooks
* Add media lookup
* Add pdf support?
* Add details pane
* Add refresh button