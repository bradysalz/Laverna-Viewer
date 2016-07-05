import json

from parser.note import Note


class Notebook():
    """A Notebook represents a Laverna Notebook. It can hold both Notes and Notebooks. Notes are accessed through the Notes attribute. Notebooks are accessed through either the children or parent attribute, which points to the respective Notebook in the tree"""

    def __init__(self, file_name=None):
        # initialize important paramers used elsewhere
        self.id = 0
        self.name = 'None'
        self.parent = None
        self.children = []
        self.notes = []
        self.parentId = None

        if file_name is not None:
            self._load_notebook(file_name)

    def add_note(self, new_note=None, note_file=None):
        if new_note is not None:
            self.notes.append(new_note)

        elif note_file is not None:
            self.notes.append(Note(note_file))

    def get_notes(self):
        return self.notes

    def get_parent(self):
        return self.parent

    def set_parent(self, parent_nb):
        self.parentId = parent_nb.id

    def get_children(self):
        return self.children

    def add_child(self, new_notebook):
        self.children.append(new_notebook)

    def change_child_format(self, new_format):
        """Set the content format of all child Notes. Applies recursively (to child Notebooks) as well."""
        # change all current notes
        for note in self.notes:
            note.change_format(new_format)

        # change all child notebooks
        for book in self.children:
            book.change_child_format(new_format)

    def _json_notebook(self, file_name):
        with open(file_name, 'r') as f:
            nb_json = json.load(f)
        return nb_json

    def _load_notebook(self, file_name):
        # load the notebook into the object
        data = self._json_notebook(file_name)
        for key in data:
            setattr(self, key, data[key])

    def __repr__(self):
        return "<Notebook: {0}>".format(self.name)
