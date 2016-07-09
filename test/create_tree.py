import os

from parser.note import Note
from parser.notebook import Notebook
from parser.notebooktree import NotebookTree

os.chdir('/home/brady/Dropbox/Apps/Laverna/notes-db/notebooks')

notebook_list = [Notebook(x) for x in os.listdir()]
print([nb.name for nb in notebook_list])
mytree = NotebookTree()

cnt = 0
while(notebook_list != []):
    valid = mytree.add_child_notebook(notebook_list[0])
    cnt = cnt + 1
    if valid == -1:
        notebook_list.append(notebook_list.pop(0))
    else:
        del notebook_list[0]
    if cnt < 10:
        print(notebook_list)

print(mytree.get_print_tree())

#########################################
# Test Note Insertion
#########################################

os.chdir('../notes')
note_list = [Note(x) for x in os.listdir()]
print([type(nt.notebookId) for nt in note_list])

cnt = 0
while(note_list != []):
    valid = mytree.add_note(note_list[0])
    cnt = cnt + 1
    if valid == -1:
        note_list.append(note_list.pop(0))
    else:
        del note_list[0]

print(mytree.get_print_tree())
