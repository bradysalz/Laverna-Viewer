from parser.notebook import Notebook


class NotebookTree():
    """A NotebookTree represents our Laverna notebook structure.
    Each node in tree is a Notebook. We initialize it as a strucutre
    containing a root node with a blank Notebook and a no parentId."""

    def __init__(self, notebook_list=None):
        self._root = Notebook()
        self._root.id = '0'

        if notebook_list is not None:
            for notebook in notebook_list:
                self.add_notebook(notebook)

    def add_child_notebook(self, new_notebook):
        """Adds a notebook to the tree.

        Recurses through the tree to find parent. Returns -1 if parent
        not found OR if notebook is marked as 'trashed'."""
        if new_notebook.trash != 0:
            return

        parent = self._find_parent_nb(self._root, new_notebook.parentId)
        if parent is not None:
            parent.add_child(new_notebook)
        else:
            return -1

    def add_note(self, new_note):
        """Recursively searches the tree to find the notebook to add the
        note to. Returns -1 if no parent notebook is found or note
        is marked as 'trashed'."""
        if new_note.trash != 0:
            return

        par_id = new_note.notebookId
        parent_notebook = self._find_parent_nb(self._root, par_id)
        if parent_notebook is not None:
            parent_notebook.notes.append(new_note)
        else:
            return -1

    def print_tree(self):
        return self._build_tree_string(self._root, 0)

    def _build_tree_string(self, curr_nb, depth):
        """Prints out the NotebokTree.

        Recurses over all notebooks (NB:) and notes. Should only be used for
        debugging."""
        spacing = depth * '  '
        print(spacing + '|-- ' + curr_nb.name)

        for nt in curr_nb.notes:
            spacing = (depth + 1) * '  '
            print(spacing + '> ' + nt.title)

        if curr_nb.children == []:
            pass
        else:
            for nb in curr_nb.children:
                self._build_tree_string(nb, depth + 1)

    def get_root_nb(self):
        return self._root

    def _find_parent_nb(self, curr_notebook, new_notebook_id):
        """Recurses through the NotebookTree to find the parent
        notebook, else returns None."""
        if curr_notebook.id == new_notebook_id:
            return curr_notebook
        elif curr_notebook.children == []:
            return None
        else:
            for child in curr_notebook.children:
                recurse = self._find_parent_nb(child, new_notebook_id)
                if recurse is not None:
                    return recurse

    def __repr__(self):
        return "<NotebookTree: {0}>".format(self.parentId)
