from collective.ploneupgradecheck.interfaces import IFileRegistry
from collective.ploneupgradecheck.interfaces import IImportRegistry
from zope.component import getUtility
from zope.interface import implements
import re


PY_IMPORT_PATTERN = re.compile(r"""
\s*          # Whitespace.
from         #
\s+          # Whitespace.
(\S*?)       # Non-whitespace string.
\s+          # Whitespace.
import       #
\s+          # Whitespace.
(\S*)        # Non-whitespace string.
""", re.VERBOSE)


ZCML_FOR_PATTERN = re.compile(r"""
\s           # Whitespace.
for=         #
['\"]        # Single or double quote.
(            # Start of imports
[^\'^"]+     # Non-whitespace string.
)            # End of 'import' variable.
['\"]        # Single or double quote.
""", re.VERBOSE)


ZCML_SINGLE_LINE = re.compile(r"""
\s           # Whitespace.
(package|component|factory|class|layer)=     #  attribute
['\"]        # Single or double quote.
(            # Start of import
\S+          # Non-whitespace string.
)            # End of 'import' variable.
['\"]        # Single or double quote.
""", re.VERBOSE)


class ImportRegistry(object):
    implements(IImportRegistry)

    def __init__(self):
        self.loaded = False
        self._dottedname_to_paths = None

    def get_imports(self, dottedname):
        self.load()

        for key in self._dottedname_to_paths:
            if key == dottedname or key.startswith(dottedname):
                for path in self._dottedname_to_paths[key]:
                    yield path, key
    def load(self):
        if self.loaded:
            return False

        self._dottedname_to_paths = {}

        self._load_py_imports()
        self._load_zcml_for()
        self._load_zcml_single_line()

        self.loaded = True
        return True

    def clear(self):
        self.loaded = False
        self._dottedname_to_paths = None

    def _load_py_imports(self):
        registry = getUtility(IFileRegistry)

        for item in registry.grep(PY_IMPORT_PATTERN, ['py']):
            dottedname = '.'.join(item.get('groups'))
            path = item.get('path')
            self._register(dottedname, path)

    def _load_zcml_for(self):
        registry = getUtility(IFileRegistry)

        for item in registry.grep(ZCML_FOR_PATTERN, ['zcml']):
            dottednames = re.split(r'\s*', item.get('groups'))
            path = item.get('path')

            for name in dottednames:
                self._register(name, path)

    def _load_zcml_single_line(self):
        registry = getUtility(IFileRegistry)

        for item in registry.grep(ZCML_SINGLE_LINE, ['zcml']):
            _attr, dottedname = item.get('groups')
            self._register(dottedname.strip(), item.get('path'))

    def _register(self, dottedname, path):
        if dottedname not in self._dottedname_to_paths:
            self._dottedname_to_paths[dottedname] = []

        self._dottedname_to_paths[dottedname].append(path)


def create_import_registry():
    return ImportRegistry()
