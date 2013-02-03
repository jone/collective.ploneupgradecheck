from collective.ploneupgradecheck.interfaces import IFileRegistry
from zope.interface import implements
import os


IGNRORE_DIRS = [
    '.svn',
    '.git',
    'parts',
    ]


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
            if self._is_ignored(dirname):
                continue

            for name in filenames:
                path = os.path.join(dirname, name)
                self._add(path)

    def clear(self):
        self._files_by_extension = {}
        self._basedir = None

    def get_basedir(self):
        return self._basedir

    def grep(self, regexp, extensions=None):
        matches = []

        for path in self.find_files(extensions=extensions):
            with open(path) as file_:
                contents = file_.read()

            for groups in regexp.findall(contents):
                matches.append({'path': path,
                                'groups': groups})

        return matches

    def _add(self, path):
        _name, ext = os.path.splitext(path)
        ext = ext[1:]

        if ext not in self._files_by_extension:
            self._files_by_extension[ext] = []

        self._files_by_extension[ext].append(path)

    def _is_ignored(self, path):
        for name in IGNRORE_DIRS:
            if path.endswith('/%s' % name) or '/%s/' % name in path:
                return True
        return False

def create_file_registry():
    return FileRegistry()
