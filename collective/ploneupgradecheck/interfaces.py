from zope.interface import Attribute
from zope.interface import Interface



class IFileRegistry(Interface):
    """The ``IFileRegistry`` utility handles searching files by extension recursively.
    """

    def find_files(extensions=None):
        """Returns a list of file paths with one of the passed ``extensions``.
        """

    def load(path=None):
        """Loads the file registry.
        """

    def get_basedir():
        """Returns the base directory with which the registry was loaded or ``None`` if it
        was not loaded yet.
        """

    def grep(regexp, extensions=None):
        """Greps all files with the passed ``extensions`` for a ``regexp`` (compiled) per
        line.
        """


class IImportRegistry(Interface):
    """An import manager utility.
    """

    loaded = Attribute('True if the registry is loaded')

    def get_imports(dottedname):
        """Returns all imports starting with ``dottedname``.
        Returned is a list with a dict per import, containing the file and the full
        import.
        """

    def load():
        """Loads the import registry.
        """

    def clear():
        """Clears the import registry.
        """
