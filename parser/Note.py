import json
import datetime

class Note():
	"""The Note Class is the core class. It represents a single Laverna Note file.
	"""
	def __init__(self, file=None):
		# initialize the important keys used elsewhere
		self.file_name = ''
		self.content = ''
		self.tags = ''
		self.title = ''
		self.notebookId = ''
		self.created = datetime.datetime.now()
		self.updated = datetime.datetime.now()

		if file is not None:
			self.__add_attrs(file)

	def __load_note(self, file):
		"""Load file to JSON"""
		with open(file, 'r') as file_hdr:
			note_json = json.load(file_hdr)

		return note_json

	def __add_attrs(self, file):
		"""Adds all the JSON keys as Note attributes"""
		note_json = self.__load_note(file)
		for key in note_json:
			setattr(self, key, note_json[key])

	def __repr__(self):
		return "<Note: {0}>".format(self.title)
