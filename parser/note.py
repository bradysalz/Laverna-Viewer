import json
import datetime
import pypandoc


class Note():
    """The Note Class is the core class. It represents a single Laverna Note
    file. While it primarily just reads in the JSON file to a class, we also
    can change the content format (using pandoc)."""

    def __init__(self, file=None):
        # initialize the important keys used elsewhere
        self.file_name = ''
        self.content = ''
        self.tags = ''
        self.title = ''
        self.notebookId = ''
        self.content_format = ''
        self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()

        if file is not None:
            self._add_attrs(file)
            self.notebookId = str(self.notebookId)

    def change_format(self, new_format):
        """Change content format using pypandoc. Initializes as Markdown"""
        self.content = pypandoc.convert_text(
            self.content,
            new_format,
            format=self.content_format,
            extra_args=['--mathjax'])

    def _load_note(self, file):
        """Load file to JSON"""
        with open(file, 'r') as file_hdr:
            note_json = json.load(file_hdr)

        return note_json

    def _add_attrs(self, file):
        """Adds all the JSON keys as Note attributes"""
        note_json = self._load_note(file)
        for key in note_json:
            setattr(self, key, note_json[key])

        self.content_format = 'md'

    def __repr__(self):
        return "<Note: {0}>".format(self.title)
