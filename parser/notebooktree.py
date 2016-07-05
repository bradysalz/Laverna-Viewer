from parser.notebook import Notebook


class NotebookTree():
    """A NotebookTree represents our Laverna notebook structure. Each node in tree is a Notebook. We initialize it as a strucutre containing a root node with a blank Notebook and a no parentId."""

    def __init__(self, notebook_list=None):
        self._root = Notebook()
        self._root.id = '0'

        if notebook_list is not None:
            for notebook in notebook_list:
                self.add_notebook(notebook)

    def add_child_notebook(self, new_notebook):
        parent = self._find_parent_nb(self._root, new_notebook)
        if parent is not None:
            parent.add_child(new_notebook)
            return 'yes'
        else:
            # wrong parent - raise error
            # raise WrongParentId
            return 'nope'

    def get_print_tree(self):
        curr_str = '\n'
        return self._build_tree_string(self._root, curr_str, 1)

    def _build_tree_string(self, curr_nb, tree_str, depth):
        """please fix this recursively! currently prints out whole tree which is dumb."""
        for i in range(depth):
            tree_str += '  '
        tree_str += '|-- ' + curr_nb.name + '\n'

        if curr_nb.children == []:
            return tree_str
        else:
            for nb in curr_nb.children:
                tree_str += self._build_tree_string(nb, tree_str, depth + 1)
            return tree_str

    def get_root_nb(self):
        return self._root

    def _find_parent_nb(self, curr_notebook, new_notebook):
        """jesus christ why is my girlfriend so smart. jk i fixed the recursion bug, take that"""
        if curr_notebook.id == new_notebook.parentId:
            return curr_notebook
        elif curr_notebook.children == []:
            return None
        else:
            for child in curr_notebook.children:
                recurse = self._find_parent_nb(child, new_notebook)
                if recurse is not None:
                    return recurse

    def __repr__(self):
        return "<NotebookTree: {0}>".format(self.parentId)
