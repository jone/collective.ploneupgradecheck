from collective.ploneupgradecheck.interfaces import IFileRegistry
from zope.interface import implements
import os


class FileRegistry(object):
    implements(IFileRegistry)

    def __init__(self):
        self._files_by_extension = {}
        self._basedir = None

    def find_files(self, extensions=None):
        if extensions is None:
            extensions = self._files_by_extension.keys()

        files = []
        for ext in extensions:
            files.extend(self._files_by_extension.get(ext, []))

        return files

    def load(self, path=None):
        self.clear()

        if path is None:
            path = os.getcwd()
        self._basedir = path

        for dirname, dirnames, filenames in os.walk(path):
            for name in filenames:
                path = os.path.join(dirname, name)
                self._add(path)

    def clear(self):
        self._files_by_extension = {}
        self._basedir = None

    def get_basedir(self):
        return self._basedir

    def _add(self, path):
        _name, ext = os.path.splitext(path)
        ext = ext[1:]

        if ext not in self._files_by_extension:
            self._files_by_extension[ext] = []

        self._files_by_extension[ext].append(path)

def create_file_registry():
    return FileRegistry()
