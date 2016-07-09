import os

from flaskapp.config import LAVERNA_PATH
from parser.note import Note
from parser.notebook import Notebook
from parser.notebooktree import NotebookTree


def build_tree(path=None):
    currpath = os.getcwd()
    
    if path is None:
        path = LAVERNA_PATH

    os.chdir(path)
    os.chdir('notebooks')
    mytree = NotebookTree()
    
    notebook_list = [Notebook(x) for x in os.listdir()]

    while(notebook_list != []):
        valid = mytree.add_child_notebook(notebook_list[0])
        if valid == -1:
            notebook_list.append(notebook_list.pop(0))
        else:
            del notebook_list[0]

    os.chdir('../notes')
    note_list = [Note(x) for x in os.listdir()]

    while(note_list != []):
        valid = mytree.add_note(note_list[0])
        if valid == -1:
            note_list.append(note_list.pop(0))
        else:
            del note_list[0]

    os.chdir(currpath)
    return mytree
